---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "大模型的参数量及其计算访存开销的理论分析"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2023-11-01T13:09:34+08:00
lastmod: 2023-11-01T13:09:34+08:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

toc: true
---

推理服务系统的根本目标在于降低时延和提高吞吐量，LLM 推理的优化也是如此。首字时延（Time To First Token, TTFT）和吐字时延（Time Per Output Token, TPOT）就是两个非常重要的指标。如何优化 LLM 推理的这两个指标成为近年来学术界热议的问题。在研究这个问题之前，有必要深入理解 LLM 架构，分析其参数量和计算访存开销。

<!--more-->

------

Transformer[^1] 是一种 Encoder-Decoder 结构的模型，它被认为是 LLM 的基础模型。此后，诸如 Encoder only 模型（BERT[^2]）、Decoder only 模型（GPT[^3]）、Encoder-Decoder 模型都是在 Transformer 基础之上的变体。但不论是何种结构的 LLM，其内部都主要包含如下 block：

- Multi-Head Self-Attention：多头自注意力
- Feed-Forward：前馈网络
- Add & LayerNorm：层归一化

此外，还包括如下一些 block：

- Token Embedding：词嵌入
- Position Embedding：位置嵌入
- Linear：输出的线性层
- Softmax：激活函数

{{< figure src="b942cec77fa0bc17ef4016894aae2f2e.png" title="Transformer Architecture." numbered="true" >}}

LLM 超参数定义如下：

|          超参数          | 符号表示 | Transformer 中的大小 |
| :----------------------: | :------: | :------------------: |
|   $d_{\textrm{model}}$   |    M     |         512          |
| $d_k$, $d_v$ ($d_{qkv}$) |    D     |          64          |
|           Head           |    H     |          8           |
|         $d_{ff}$         |    F     |         2048         |

根据论文中的定义，其中 $M = HD$，$F = 4M$。

## 参数量理论计算

### MHA

多头自注意力模块的每个 head 都需要 2 次 Self-Attention 的计算，即

$$
\text{Attention}(Q, K, V) = \text{Softmax}(\frac{QK^T}{\sqrt{d_k}})V
$$

在那之前，需要将每个 token 从 $d_{\textrm{model}}$ 维映射到 $d_k$ 或 $d_v$ 维。（在 Transformer 模型中，$d_{\textrm{model}} = 512$，而 $d_k = d_v = \frac{d_{\textrm{model}}}{h} = 64$，这里 $h = 8$。）所以，输入的 $Q, K, V$ 向量都需要进行投影操作，共需 3 个线性变换矩阵 $W_K, W_Q, W_V$，维度均为 `(M, D)`。

{{< figure src="9b71910d735ee7b15951fdc350cc411d.png" title="Multi-Head Self-Attention Block." numbered="true" >}}

最终将每个 head 拼接起来，得到 $d_v \times h = d_{\textrm{model}}$ 维。这个结果再投影到 $d_{\textrm{model}}$ 维，需 1 个线性变换矩阵 $W_O$，维度为 `(M, M)`。即

{{< math >}}
$$
\begin{align}
    \text{MultiHead}(Q, K, V) &= \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O \\
    \text{where } \text{head}_i &= \text{Attention}(QW^Q_i, KW^K_i, VW^V_i)
\end{align}
$$
{{< /math >}}

因此，多头自注意力模块的总参数量为

{{< math >}}
$$
\begin{align}
    & (d_{\textrm{model}} \times d_{qkv} + d_{qkv}) \times 3 \times h + (d_{\textrm{model}} \times d_{\textrm{model}} + d_{\textrm{model}}) \\
    =\ & 4 (d_{\textrm{model}}^2 + d_{\textrm{model}})
\end{align}
$$
{{< /math >}}

在 $d_{ff}$ 很大的情况下，可以近似认为参数量为 $4d_{\textrm{model}}^2$。

### FFN

前馈网络模块由 2 个全连接层，即

{{< math >}}
$$
\begin{align}
    \text{FFN}(x) = \text{ReLU}(xW_1 + b_1)W_2 + b_2
\end{align}
$$
{{< /math >}}

其中隐藏层 $d_{ff}$ 的维度一般是 $d_{\textrm{model}}$ 的 4 倍。所以参数矩阵 $W_{in}, W_{out}$ 的维度分别为 `(M, F)` 和 `(F, M)`。因此，前馈网络模块的总参数量为

{{< math >}}
$$
\begin{align}
    & (d_{\textrm{model}} \times d_{ff} + d_{ff}) + (d_{ff} \times d_{\textrm{model}} + d_{\textrm{model}}) \\
    =\ & 2 d_{\textrm{model}} d_{ff} + d_{\textrm{model}} + d_{ff}
\end{align}
$$
{{< /math >}}

### Add & LayerNorm

这一模块包含两个操作，一是 Add，即残差连接；二是 Layer Normalization，即

{{< math >}}
$$
\begin{align}
    y = \frac{x - \mu}{\sigma + \epsilon} \times \gamma + \beta
\end{align}
$$
{{< /math >}}

其中，$\mu$ 为均值，$\sigma$ 为标准差，$\epsilon$ 为定值，$\gamma$ 为缩放因子，$\beta$ 为偏移因子。$\gamma, \beta$ 是需要学习的参数，是 `(1, M)` 维的向量。因此，这部分参数量为

{{< math >}}
$$
2 \times d_{\textrm{model}}
$$
{{< /math >}}

### Embedding

Token Embedding 过程包含参数，参数量取决于训练数据 token 的数量 `vocab_size`。参数矩阵的维度为 `(vocab_size, M)`。

而 Positional Embedding 采用三角函数计算，即

{{< math >}}
$$
\begin{align}
    PE_{(pos, 2i)} &= \sin (pos / 10000^{2i / d_{\textrm{model}}}) \\
    PE_{(pos, 2i+1)} &= \cos (pos / 10000^{2i / d_{\textrm{model}}})
\end{align}
$$
{{< /math >}}

此过程不需要学习，因此没有参数。

### Linear & Softmax

从最后一个编码器输出的结果需要经过一个线性层，通过 Softmax 化为概率分布后，选择最大概率的 token 输出。因此，线性层的参数矩阵具有 `(M, vocab_size)` 维。这部分的参数量为

{{< math >}}
$$
d_{\textrm{model}} \times \text{vocab_size}
$$
{{< /math >}}

## 参数量估算

LLM 总参数量为上述各部分参数量之和。不考虑输入和输出，按照 GPT 的架构，即 Decoder only，每个 Decoder 共 1 个 MHA、1 个 FFN 和 2 个 Add & LayerNorm。这样我们可以得到参数量为

{{< math >}}
$$
\begin{align}
    & 4 (d_{\textrm{model}}^2 + d_{\textrm{model}}) + \\ 
    & 2 d_{\textrm{model}} d_{ff} + d_{\textrm{model}} + d_{ff} + \\
    & 2 \times d_{\textrm{model}} \times 2 \\
\end{align}
$$
{{< /math >}}

这里我们继续简化，令 $d_{ff} = 4d_{\textrm{model}} = 4d$，得到

{{< math >}}
$$
\begin{align}
    & 4 (d^2 + d) + 2d \times 4d + d + 4d +2d \times 2 \\
    =\ & 12d^2 + 13d
\end{align}
$$
{{< /math >}}

当 $d_{\textrm{model}}$ 较大时，Encoder 和 Decoder 部分的参数量和其他部分相比远远更大。因此，要快速估计 LLM 的参数量，一般可以采用 $12d_{\textrm{model}}^2$ 作为估计值。

## 验证参数量

### Transformer

按照上述计算方法，我们首先验证 Transformer 的参数量。

首先，计算一个 Encoder 的参数量。一个 Encoder 包含 1 个 MHA block、1 个 FFN block 和 2 个 Add & LayerNorm，即

{{< math >}}
$$
\begin{align}
    & 4 (d_{\textrm{model}}^2 + d_{\textrm{model}}) + \\ 
    & 2 d_{\textrm{model}} d_{ff} + d_{\textrm{model}} + d_{ff} + \\
    & 2 \times d_{\textrm{model}} \times 2 \\
    =\ & 4 \times 512 \times (512+1) + \\
    & 2 \times 512 \times 2048 + 512 + 2048 + \\
    & 2 \times 512 \times 2 \\
    =\ & 3,152,384
\end{align}
$$
{{< /math >}}

接下来，计算一个 Decoder 的参数量。一个 Decoder 包含 2 个 MHA block、1 个 FFN block 和 3 个 Add & LayerNorm，即

{{< math >}}
$$
\begin{align}
    & 4 (d_{\textrm{model}}^2 + d_{\textrm{model}}) \times 2 + \\ 
    & 2 d_{\textrm{model}} d_{ff} + d_{\textrm{model}} + d_{ff} + \\
    & 2 \times d_{\textrm{model}} \times 3 \\
    =\ & 4 \times 512 \times (512+1) \times 2 + \\
    & 2 \times 512 \times 2048 + 512 + 2048 + \\
    & 2 \times 512 \times 3 \\
    =\ & 4,204,032
\end{align}
$$
{{< /math >}}

上面计算的只是一个 Encoder 或 Decoder 的参数量。Transformer 的 Encoder-Decoder 的数量均为 6 个。

除此之外，从最后一个编码器输出的结果需要经过一个线性层，通过 Softmax 化为概率分布后，选择最大概率的 token 输出。因此，线性层的参数矩阵具有 `(M, vocab_size)` 维。在 Transformer 论文中，训练所用的英语和德语对照表的 token 数量为 37,000 个。

因此，不考虑 Embedding，Transformer 的参数量为

{{< math >}}
$$
\begin{align}
    & (3,152,384 + 4,204,032) \times 6 + 37,000 \times 512 \\
    =\ & 63,082,496
\end{align}
$$
{{< /math >}}

这和论文中给出的 65M 的参数量在同一个量级上。只不过，这里没有考虑输入和输出部分的参数量。如果模型足够大，那么参数量主要取决于 Encoder 和 Decoder 部分。

### LLaMA

LLaMA[^4] 是基于 Transformer 的 Decoder only 模型。考虑到 LLaMA 是参数量远大于 Transformer 的 LLM，所以我们采用估算法，可以得到下表：

|   Model   | $d_{\textrm{model}}$ | Layer | 采用 $12d_{\textrm{model}}^2$ 估算 | 采用 $12d_{\textrm{model}}^2 + 13d_{\textrm{model}}$ 估算 |
| :-------: | :------------------: | :---: | :--------------------------------: | :-------------------------------------------------------: |
| LLaMA-7B  |         4096         |  32   |           6,442,450,944            |                       6,444,154,880                       |
| LLaMA-13B |         5120         |  40   |           12,582,912,000           |                      12,585,574,400                       |
| LLaMA-30B |         6656         |  60   |           31,897,681,920           |                      31,902,873,600                       |
| LLaMA-65B |         8192         |  80   |           64,424,509,440           |                      64,433,029,120                       |

可见，估算值和论文给定的参数量相差无几。同时也说明，LLM 参数量越大，Encoder 和 Decoder 部分的参数量占比也就越大。可以基本上忽略输入输出部分的参数。

## 计算访存开销

首先需要给出如下两个定义：

- FLOPS (Floating Point Operations Per Second): 每秒浮点运算次数，用于衡量模型计算开销。
- MOPS (Memory Operations Per Second): 每秒内存访问次数，用于衡量模型访存（I/O）开销。

一般地，如果一个系统在单位时间内访存次数越小而计算次数越多，那么该系统的吞吐量就越大。定义算术强度（Arithmetic Intensity[^5]）为

{{< math >}}
$$
\begin{align}
    \text{Arithmetic Intensity} = \frac{\text{FLOPS}}{\text{MOPS}}
\end{align}
$$
{{< /math >}}

显然，算术强度越大，系统的吞吐量越高。

计算和访存与 sequence length 和 batch size 直接相关，下面分别用 `S` 和 `B` 来表示其大小。在全量推理和增量推理阶段，FLOPS、MOPS 和算术强度的复杂度如下表所示：

|             Stage             |  Output Shape  |    FLOPS    |      MOPS       | Arithmetic Intensity |
| :---------------------------: | :------------: | :---------: | :-------------: | :------------------: |
|      $QW_Q, KW_K, VW_V$       | `(B, S, H, D)` | $O(BSM^2)$  |  $O(2BSM+M^2)$  |  $O(1/(1/M+1/BS))$   |
|         $Q \times K$          | `(B, S, H, D)` | $O(BS^2M)$  | $O(2BSM+BS^2H)$ |   $O(1/(1/D+1/S))$   |
|   $\text{Score} \times V $    | `(B, S, H, D)` | $O(BS^2M)$  | $O(2BSM+BS^2H)$ |   $O(1/(1/D+1/S))$   |
| $\text{Attention} \times W_O$ |  `(B, S, M)`   | $O(BSM^2)$  |  $O(2BSM+M^2)$  |  $O(1/(1/M+1/BS))$   |
|       $Y \times W_{in}$       |  `(B, S, F)`   | $O(8BSM^2)$ |  $O(BSM+4M^2)$  |  $O(1/(1/M+1/BS))$   |
| $\text{ReLU} \times W_{out}$  |  `(B, S, M)`   | $O(8BSM^2)$ |  $O(BSM+4M^2)$  |  $O(1/(1/M+1/BS))$   |

> 注：本表根据[剖析 GPT 推断中的批处理效应](https://abcdabcd987.com/2023/05/13/transformer-batching/)一文进行整理。

上表给出了 LLM 主要的 8 个线性算子的 FLOPS、MOPS 和算术强度，这些开销在 LLM 推理过程中占主导地位。通过上表，我们可以得出如下几点结论：

1. 序列长度和批量大小对计算和访存开销的影响是直接的。
2. 8 个线性算子可以分为如下两类：
   - `projection`：即 `activation * weight`，包括 MHA block 的 $QW_Q, KW_K, VW_V$ 和 $\text{Attention} \times W_O$ 以及 FFN block 的两个 MLP 层。
   - `act-to-act`：即 MHA block 的 2 次自注意力计算 $Q \times K$ 和 $\text{Score} \times V$。
3. $d_{\textrm{model}}$ 对 `projection` 算子的 FLOPS 和 MOPS 都具有二次的影响，序列长度对 `act-to-act` 算子的 FLOPS 和 MOPS 都具有二次的影响。在序列长度较小时，`act-to-act` 算子的计算量较小；但在序列长度较大时，`act-to-act` 算子的计算量较大。
4. 增大序列长度、批量大小、$d_{\textrm{model}}$，以及减少 head 的数量，都有助于提高算术强度。不过，序列长度和批量大小受显存限制不可能无限增加，$d_{\textrm{model}}$ 和 head 是超参数，可以看作是定值。所以，吞吐量提升的瓶颈在于显存。
5. 对于增量推理的单个 token 生成阶段，$S \equiv 1$。所以，增量推理阶段和全量推理阶段的 FLOPS、MOPS 以及算术强度有很大不同，编码器模型和解码器模型的瓶颈也有所不同。譬如，增量推理阶段的算术强度要明显低于全量推理，这和我们的直观感受是一致的。

[^1]: [Vaswani, Ashish, et al. “Attention Is All You Need.” Proceedings of the 31st International Conference on Neural Information Processing Systems, Curran Associates Inc., 2017, pp. 6000–10.](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
[^2]: [Devlin, Jacob, et al. “BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding.” arXiv:1810.04805 [Cs], May 2019.](http://arxiv.org/abs/1810.04805)
[^3]: [Radford, Alec, and Karthik Narasimhan. Improving Language Understanding by Generative Pre-Training. 2018.](https://www.semanticscholar.org/paper/Improving-Language-Understanding-by-Generative-Radford-Narasimhan/cd18800a0fe0b668a1cc19f2ec95b5003d0a5035)
[^4]: [Touvron, Hugo, et al. LLaMA: Open and Efficient Foundation Language Models. arXiv:2302.13971, arXiv, 27 Feb. 2023.](https://doi.org/10.48550/arXiv.2302.13971)
[^5]: [Kim, Sehoon, et al. Full Stack Optimization of Transformer Inference: A Survey. arXiv:2302.14017, arXiv, 27 Feb. 2023.](https://doi.org/10.48550/arXiv.2302.14017)
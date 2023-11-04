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
draft: true

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

<!--more-->

------

## 参数量估算

Transformer[^1] 是一种 Encoder-Decoder 结构的模型，它被认为是 LLM 的基础模型。此后，诸如 Encoder only 模型（BERT[^2]）、Decoder only 模型（GPT[^3]）、Encoder-Decoder 模型都是在 Transformer 基础之上的变体。但不论是何种结构的模型，其内部都主要包含如下 block：

- Multi-Head Self-Attention：多头自注意力
- Feed-Forward：前馈网络
- Add & LayerNorm：层归一化

此外，还包括如下一些 block：

- Token Embedding：词嵌入
- Position Embedding：位置嵌入
- Linear：输出的线性层
- Softmax：激活函数

|          超参数          | 符号表示 | Transformer 中的大小 |
| :----------------------: | :------: | :------------------: |
|   $d_{\textrm{model}}$   |    M     |         512          |
| $d_k$, $d_v$ ($d_{qkv}$) |    D     |          64          |
|           $h$            |    H     |          8           |
|         $d_{ff}$         |    F     |         2048         |

### MHA

多头自注意力模块的每个 head 都需要 2 次 Self-Attention 的计算，即

$$
\text{Attention}(Q, K, V) = \text{Softmax}(\frac{QK^T}{\sqrt{d_k}})V
$$

在那之前，需要将每个 token 从 $d_{\textrm{model}}$ 维映射到 $d_k$ 或 $d_v$ 维。（在 Transformer 模型中，$d_{\textrm{model}} = 512$，而 $d_k = d_v = \frac{d_{\textrm{model}}}{h} = 64$，这里 $h = 8$。）所以，输入的 $Q, K, V$ 向量都需要进行投影操作，共需 3 个线性变换矩阵 $W_K, W_Q, W_V$，维度均为 `(M, D)`。

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

其次，计算一个 Decoder 的参数量。一个 Decoder 包含 2 个 MHA block、1 个 FFN block 和 3 个 Add & LayerNorm，即

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

Transformer 的 Encoder-Decoder 的数量均为 6 个。因此，不考虑 Embedding，Transformer 的参数量为

{{< math >}}
$$
(3,152,384 + 4,204,032) \times 6 = 44,138,496
$$
{{< /math >}}

这些参数是最主要的，也是最占显存的。现在考虑输入输出。关于输入 Embedding，论文中指出训练所用的英语和德语对照表的 token 数量为 37,000 个。关于输出，主要是一个 `(M, vocab_size)` 维的线性层。因此，最终 Transformer 的参数量为

{{< math >}}
$$
\begin{align}
    & (3,152,384 + 4,204,032) \times 6 + 37,000 \times 512 + 512 \times 512 \\
    =\ & 63,082,496
\end{align}
$$
{{< /math >}}

这和论文中给出的 65M 的参数量在同一个量级上。只不过，这里没有考虑输入和输出部分的参数量。如果模型足够大，那么参数量主要取决于 Encoder 和 Decoder 部分。

### LLaMa[^4]



[^1]: [Vaswani, Ashish, et al. “Attention Is All You Need.” Proceedings of the 31st International Conference on Neural Information Processing Systems, Curran Associates Inc., 2017, pp. 6000–10.](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
[^2]: [Devlin, Jacob, et al. “BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding.” arXiv:1810.04805 [Cs], May 2019.](http://arxiv.org/abs/1810.04805)
[^3]: [Radford, Alec, and Karthik Narasimhan. Improving Language Understanding by Generative Pre-Training. 2018.](https://www.semanticscholar.org/paper/Improving-Language-Understanding-by-Generative-Radford-Narasimhan/cd18800a0fe0b668a1cc19f2ec95b5003d0a5035)
[^4]: [Touvron, Hugo, et al. LLaMA: Open and Efficient Foundation Language Models. arXiv:2302.13971, arXiv, 27 Feb. 2023.](https://doi.org/10.48550/arXiv.2302.13971)

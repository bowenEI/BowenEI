---
# Documentation: https://hugoblox.com/docs/managing-content/

title: "挑战 2024 年考研数学（一）"
subtitle: ""
summary: ""
authors: []
tags: [考研, 数学]
categories: []
date: 2023-12-24T22:20:59+08:00
lastmod: 2023-12-26T22:20:59+08:00
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

2024 年考研已落下帷幕。据报道，今年考研的人数比去年减少了 36 万（共 438 万人报考），引发社会广泛关注。在刚刚结束的数学科目考试中，不少考生哀叹今年的数学试题难如登天，特别是 301 数学（一）。

本篇博客将持续更新今年数学（一）每道题目的详细作答过程，体会莘莘学子们在考场上的不易。

<!--more-->

------

## 选择题

### 1

已知函数 $f(x)=\int_{0}^{x} e^{\cos t} \mathrm{d} t$，$g(x)=\int_{0}^{\sin x} e^{t^{2}} \mathrm{d} t$，则 $(\qquad)$

A. $f(x)$ 是奇函数，$g(x)$ 是偶函数

B. $f(x)$ 是偶函数，$g(x)$ 是奇函数

C. $f(x)$ 与 $g(x)$ 均为奇函数

D. $f(x)$ 与 $g(x)$ 均为周期函数

【解】

本题考察变限函数的定义和积分的性质。若一个函数具有奇偶性，则其求导和积分结果的奇偶性正好相反。题干中的被积函数都是偶函数，且变限积分的上限是奇函数。因此，其导函数都是偶函数，所以原函数都是奇函数。

### 2

设 $P=P(x, y, z), Q=Q(x, y, z)$ 均为连续函数，$\Sigma$ 为曲面 $z=\sqrt{1-x^{2}-y^{2}} \ (x \leqslant 0, y \geqslant 0)$ 的上侧，则 $\iint_{\Sigma} P \mathrm{d}y \mathrm{d}z + Q \mathrm{d}z \mathrm{d}x = (\qquad)$

A. $\iint_{\Sigma}\left(\frac{x}{z} P+\frac{y}{z} Q\right) \mathrm{d}x \mathrm{d}y$

B. $\iint_{\Sigma}\left(-\frac{x}{z} P+\frac{y}{z} Q\right) \mathrm{d}x \mathrm{d}y$

C. $\iint_{\Sigma}\left(\frac{x}{z} P-\frac{y}{z} Q\right) \mathrm{d}x \mathrm{d}y$

D. $\iint_{\Sigma}\left(-\frac{x}{z} P-\frac{y}{z} Q\right) \mathrm{d}x \mathrm{d}y$

【解】

本题考察第二类曲面积分的转换投影法。通过四个选项可以判断是往 $xOy$ 平面上投影，因此分别计算 $z$ 对 $x, y$ 的偏导数

{{< math >}}
$$
\begin{align*}
    z^2 &= 1 - x^2 - y^2 \\
    2z \cdot \frac{\partial z}{\partial x} &= -2x \\
    \Longrightarrow \frac{\partial z}{\partial x} &= - \frac{x}{z} \\
    2z \cdot \frac{\partial z}{\partial y} &= -2y \\
    \Longrightarrow \frac{\partial z}{\partial y} &= - \frac{y}{z}
\end{align*}
$$
{{< /math >}}

所以

{{< math >}}
$$
\begin{align*}
    &\ \iint_{\Sigma} P \mathrm{d}y \mathrm{d}z + Q \mathrm{d}z \mathrm{d}x \\
    =&\ \iint_{\Sigma} \left( P \cdot \left(-\frac{\partial z}{\partial x}\right) + Q \cdot \left(-\frac{\partial z}{\partial y}\right) \right) \mathrm{d}y \mathrm{d}z \\
    =&\ \iint_{\Sigma} \left( \frac{x}{z} + \frac{y}{z} \right) \mathrm{d}x \mathrm{d}y
\end{align*}
$$
{{< /math >}}

### 3

已知幂级数 $\sum_{n = 0}^{\infty} a_n x^n$ 的和函数为 $\ln(2 + x)$，则 $\sum_{n = 0}^{\infty} n a_{2n} = (\qquad)$

A. $-\frac{1}{6}$

B. $-\frac{1}{3}$

C. $\frac{1}{6}$

D. $\frac{1}{3}$

【解】

本题考察幂级数和泰勒公式。首先我们将和函数 $\ln(2 + x)$ 泰勒展开

{{< math >}}
$$
\begin{align*}
    \ln{(2 + x)} &= \ln{2} + \ln{(1 + \frac{x}{2})} \\
    &= \ln{2} + \sum_{n = 1}^{\infty} \frac{(-1)^{n-1}}{n} \left( \frac{x}{2} \right)^{n} \\
\end{align*}
$$
{{< /math >}}

易知，$a_0 = \ln{2}$。利用待定系数法，当 $n \geqslant 1$ 时，数列 $\{a_n\}$ 的通项公式为

{{< math >}}
$$
\begin{align*}
    a_n = \frac{(-1)^{n-1}}{n \cdot 2^n}
\end{align*}
$$
{{< /math >}}

所以待求的和式为

{{< math >}}
$$
\begin{align*}
    \sum_{n = 0}^{\infty} n a_{2n} &= \sum_{n = 1}^{\infty} n \frac{(-1)^{2n-1}}{2n \cdot 2^{2n}} \\
    &= -\frac{1}{2} \sum_{n = 1}^{\infty} \frac{1}{4^{n}} \\
    &= -\frac{1}{2} \lim_{n \to \infty}  \frac{\frac{1}{4} \left(1 - \frac{1}{4^{n}}\right)}{1 - \frac{1}{4}} \\
    &= -\frac{1}{6}
\end{align*}
$$
{{< /math >}}

### 4

设函数 $f(x)$ 在区间 $(-1,1)$ 上有定义，且 $\lim _{x \to 0} f(x)=0$，则 $(\qquad)$

A. 当 $\lim _{x \to 0} \frac{f(x)}{x}=m$ 时，$f'(0)=m$

B. 当 $f'(0)=m$ 时，$\lim _{x \to 0} \frac{f(x)}{x}=m$

C. 当 $\lim _{x \to 0} f'(x)=m$ 时，$f'(0)=m$

D. 当 $f'(0)=m$ 时，$\lim _{x \to 0} f'(x)=m$

【解】

本题考察导数的定义。函数在某点可导需要满足以下 2 个条件：

1. 左导数等于右导数
2. 函数在该点处连续

对于 B 选项，因为 $f'(0) = m$，暗含了 $f(x)$ 在 $x = 0$ 处连续的条件，从而极限值等于函数值，即

{{< math >}}
$$
\lim_{x \to 0} f(x) = f(0) = m
$$
{{< /math >}}

由导数定义得

{{< math >}}
$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{f(x)}{x} = m
$$
{{< /math >}}

可以证明 B 选项正确。而 A 选项恰好是其逆命题，不一定成立。这是因为 $f(0)$ 不一定等于 $0$，下面给出一个反例

{{< math >}}
$$
f(x) = \begin{cases}
    1 & x = 0 \\
    x^2 \sin{\frac{1}{x}} & x \in (-1, 0) \cup (0, 1)
\end{cases} \tag{1}
$$
{{< /math >}}

$f(x)$ 在 $x = 0$ 处的极限为

{{< math >}}
$$
\lim_{x \to 0} f(x) = \lim_{x \to 0^{+}} x^2 \sin{\frac{1}{x}} = \lim_{x \to 0^{-}} x^2 \sin{\frac{1}{x}} = 0 \neq f(0)
$$
{{< /math >}}

对于 C 选项，是典型的导函数极限存在但不可导的情况。下面给出一个反例

{{< math >}}
$$
\begin{align*}
    f(x) = \begin{cases}
        1 & x = 0 \\
        x^2 & x \in (-1, 0) \cup (0, 1)
    \end{cases}
\end{align*}
$$
{{< /math >}}

其导函数为

{{< math >}}
$$
\begin{align*}
    f'(x) = \begin{cases}
        \nexists & x = 0 \\
        2x & x \in (-1, 0) \cup (0, 1)
    \end{cases}
\end{align*}
$$
{{< /math >}}

导函数的极限

{{< math >}}
$$
\begin{align*}
    \lim_{x \to 0} f'(x) &= \lim_{x \to 0} 2x = 0
\end{align*}
$$
{{< /math >}}

但 $f(x)$ 在 $x = 0$ 处的导数却不存在，因为不连续。

而 D 选项刚好相反，是典型的可导但导函数极限不存在的情况。可以采用类似 (1) 式的反例，说明如下

{{< math >}}
$$
\begin{align*}
    f(x) = \begin{cases}
        0 & x = 0 \\
        x^2 \sin{\frac{1}{x}} & x \in (-1, 0) \cup (0, 1)
    \end{cases}
\end{align*}
$$
{{< /math >}}

易知

{{< math >}}
$$
\begin{align*}
    \lim_{x \to 0^{+}} f(x) = \lim_{x \to 0^{-}} f(x) = f(0) = 0
\end{align*}
$$
{{< /math >}}

这说明 $f(x)$ 在 $(-1, 1)$ 上连续。由导数的定义，计算 $f(x)$ 在 $x = 0$ 处的导数

{{< math >}}
$$
\begin{align*}
    f'(0) &= \lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} \\
    &= \lim_{x \to 0} \frac{x^2 \sin{\frac{1}{x}}}{x} \\
    &= 0
\end{align*}
$$
{{< /math >}}

但是导函数的极限

{{< math >}}
$$
\begin{align*}
    \lim_{x \to 0} f'(x) &= \lim_{x \to 0} 2x \sin{\frac{1}{x}} - \cos{\frac{1}{x}} \\
    &= \nexists
\end{align*}
$$
{{< /math >}}

### 5

在空间直角坐标系 $O-xyz$ 中，三张平面 $\pi_i: a_ix+b_iy+c_i = d_i$ 的位置关系如图所示。记 $\alpha_i = (a_i, b_i, c_i)，\beta_i = (a_i, b_i, c_i, d_i)$。若

{{< math >}}
$$
r \begin{pmatrix}
    \alpha_1 \\
    \alpha_2 \\
    \alpha_3
\end{pmatrix} = m, r \begin{pmatrix}
    \beta_1 \\
    \beta_2 \\
    \beta_3 \\
\end{pmatrix} = n
$$
{{< /math >}}

则 $(\qquad)$

A. $m=1, n=2$

B. $m=n=2$

C. $m=2, n=3$

D. $m=n=3$

{{< figure src="049564e9d0f8acd85f6b48a462a59e89.png" >}}

【解】

本题考查线性方程组解的性质。本题通过给出三维空间中平面的位置关系，考察考生对线性方程组的直观理解，颇有新意。

由图可知，平面 $\pi_1 \cap \pi_2 \cap \pi_3 = l$，交于一条直线。这说明，三个平面所对应的平面方程组成的三元线性方程组有无穷多解，且位于同一条直线上。所以，其基础解系只有一个向量作基。

那么，相应的齐次线性方程组的系数矩阵的秩 $r = 3 - 1 = 2$，相应的非齐次线性方程组的增广矩阵的秩应该和前者相同。

### 6

设向量

{{< math >}}
$$
\alpha_1 = \begin{bmatrix}
    a \\
    1 \\
    -1 \\
    1
\end{bmatrix}, \alpha_2 = \begin{bmatrix}
    1 \\
    b \\
    a
\end{bmatrix}, \alpha_3 = \begin{bmatrix}
    1 \\
    a \\
    -1 \\
    1
\end{bmatrix}
$$
{{< /math >}}

若 $\alpha_1, \alpha_2, \alpha_3$ 线性相关，且其中任意两个向量线性无关，则 $(\qquad)$

A. $a=1, b \neq -1$

B. $a=1, b=-1$

C. $a \neq -2, b=2$

D. $a=-2, b=2$

【解】

本题考查向量组的关系。题目给出了 3 个 4 维向量，将之排列成 $4 \times 3$ 的矩阵。

由题意可知，3 个向量线性相关，意味着该矩阵的任意 3 阶子式的行列式等于零，即

{{< math >}}
$$
\begin{align*}
    \begin{vmatrix}
        a & 1 & 1 \\
        1 & 1 & a \\
        1 & a & 1
    \end{vmatrix} &= a + a + a - 1 - 1 - a^3 \\
    &= -a^3 + 3a - 2 \\
    &= (a - 1)(-a^2 - a + 2) \\
    &= -(a - 1)^2(a + 2) = 0 \\
    \Longrightarrow a &\in \{1, -2\}
\end{align*}
$$
{{< /math >}}

当 $a=1$ 时，$\alpha_1$ 和 $\alpha_3$ 必然线性相关，不合题意，舍去。因此，$a = -2$。再计算含有 $b$ 的 3 阶子式的行列式，以反解出 $b$，即

{{< math >}}
$$
\begin{align*}
    \begin{vmatrix}
        -2 & 1 & 1 \\
        1 & 1 & -2 \\
        -1 & b & -1
    \end{vmatrix} &= \begin{vmatrix}
        1 & 1 & -2 \\
        -1 & b & -1 \\
        -2 & 1 & 1
    \end{vmatrix} \\
    &= \begin{vmatrix}
        1 & 1 & -2 \\
        0 & b+1 & -3 \\
        0 & 3 & -3
    \end{vmatrix} \\
    &= \begin{vmatrix}
        b+1 & -3 \\
        3 & -3
    \end{vmatrix} \\
    &= -3(b+1) + 9 = 0 \\
    \Longrightarrow b &= 2
\end{align*}
$$
{{< /math >}}

### 7

设 $A$ 是秩为 2 的 3 阶矩阵，$\alpha$ 是满足 $A \alpha = 0$ 的非零向量。若对满足 $\beta^{\top} \alpha = 0$ 的 3 维列向量 $\beta$，均有 $A \beta = \beta$，则 $(\qquad)$

A. $A^3$ 的迹为 2

B. $A^3$ 的迹为 5

C. $A^2$ 的迹为 8

D. $A^2$ 的迹为 9

【解】

本题考察矩阵的特征值和特征向量。依题意，$A \alpha = 0$ 且 $\alpha$ 是非零向量，说明矩阵至少有一个特征值 $\lambda = 0$，且它是属于 $\alpha$ 的特征值。

同理，对于任意与 $\alpha$ 正交的向量 $\beta$ 均满足 $A \beta = \beta$，说明 $\lambda = 1$ 也是矩阵 $A$ 的特征值。而且，$\alpha, \beta$ 都是 3 维列向量，说明 $\lambda = 1$ 至少是二重特征值。同时，$A$ 的秩又等于 2，说明 $\lambda = 1$ 恰好是二重特征值。因此

{{< math >}}
$$
A \sim \begin{bmatrix}
    1 & & \\
    & 1 & \\
    & & 0
\end{bmatrix}
$$
{{< /math >}}

故 $\operatorname{tr}(A^3) = 1+1+0 = 2$。

### 8

> TODO

### 9

> TODO

### 10

> TODO

## 填空题

### 11

若

{{< math >}}
$$
\lim_{x \to 0} \frac{(1+ax^2)^{\sin{x}} - 1}{x^3} = 6
$$
{{< /math >}}

则 $a = \underline{\qquad}$

【解】

{{< math >}}
$$
\begin{align*}
    \lim_{x \to 0} \frac{(1+ax^2)^{\sin{x}} - 1}{x^3} &= \lim_{x \to 0} \frac{e^{\sin{x} \ln{(1+ax^2)}} - 1}{x^3}
\end{align*}
$$
{{< /math >}}

由 $e^x - 1 \sim 0 \ (x \to 0)$ 等价无穷小替换，可得

{{< math >}}
$$
\begin{align*}
    \cdots &= \lim_{x \to 0} \frac{\sin{x} \ln{(1+ax^2)}}{x^3}
\end{align*}
$$
{{< /math >}}

由 $\sin{x} \sim x$ 以及 $\ln{(x+1)} \sim x \ (x \to 0)$ 等价无穷小替换，可得

{{< math >}}
$$
\begin{align*}
    \cdots = \lim_{x \to 0} \frac{x \cdot ax^2}{x^3} &= 6 \\
    \Longrightarrow a &= 6
\end{align*}
$$
{{< /math >}}

### 12

设函数 $f(u, v)$ 具有 2 阶连续偏导数，且 {{< math >}}$\left. \mathrm{d} f\right|_{(1,1)} = 3 \mathrm{d} u + 4 \mathrm{d} v${{< /math >}}，令 {{< math >}}$y = f\left(\cos{x}, 1+x^{2}\right)${{< /math >}}，则 {{< math >}}$\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x = 0} = \underline{\qquad}${{< /math >}}

【解】

本题考察偏导数和全微分。易知

{{< math >}}
$$
\begin{align*}
    \left. f'_u \right|_{(1,1)} &= 3 \\
    \left. f'_v \right|_{(1,1)} &= 4
\end{align*}
$$
{{< /math >}}

对 $y$ 求导，可得

{{< math >}}
$$
\begin{align*}
    \frac{\mathrm{d} y}{\mathrm{d} x} =&\ 
 \frac{\mathrm{d} f\left(\cos x, 1+x^{2}\right)}{\mathrm{d} x} \\
    =&\ f'_u \cdot (-\sin{x}) + f'_v \cdot 2x \\
    \frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}} =&\ \frac{\mathrm{d}^{2} f\left(\cos x, 1+x^{2}\right)}{\mathrm{d} x^{2}} \\
    =&\ [f''_{uu} \cdot (-\sin{x}) + f''_{uv} \cdot 2x] (-\sin{x}) + f'_{u} \cdot (-\cos{x}) + \\
    &\ [f''_{vu} \cdot (-\sin{x}) + f''_{vv} \cdot 2x] \cdot 2x + 2 f'_{v}
\end{align*}
$$
{{< /math >}}

于是

{{< math >}}
$$
\begin{align*}
    \frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}} &= \left.\frac{\mathrm{d}^{2} f(\cos x, 1+x^{2})}{\mathrm{d} x^{2}}\right|_{x=0} \\
    &= \left. - f'_u \right|_{(1,1)} + \left. 2 f'_v \right|_{(1,1)} \\
    &= 5
\end{align*}
$$
{{< /math >}}

### 13

已知函数 $f(x) = x+1$，若

{{< math >}}
$$
\begin{align*}
    f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_{n} \cos{nx}, \ x \in [0, \pi]
\end{align*}
$$
{{< /math >}}

则 $\lim_{n \to \infty} n^2 \sin{a_{2n-1}} = \underline{\qquad}$

【解】

本题考察傅里叶级数。由公式得

{{< math >}}
$$
\begin{align*}
    a_n &= \frac{2}{\pi} \int_{0}^{\pi} (x+1) \cos{\frac{n \pi x}{\pi}} \mathrm{d}x \\
    &= \frac{2}{n \pi} \left(
        \left. \sin{nx} \right|_{0}^{\pi} + \int_{0}^{\pi} x \mathrm{d} \sin{nx}
    \right) \\
    &= \frac{2}{n \pi} \left(
        \left. x \sin{nx} \right|_{0}^{\pi} - \int_{0}^{\pi} \sin{nx} \mathrm{d} x
    \right) \\
    &= \frac{2}{n^2 \pi} \left. \cos{nx} \right|_{0}^{\pi} \\
    &= -\frac{4}{n^2 \pi}
\end{align*}
$$
{{< /math >}}

于是

{{< math >}}
$$
\begin{align*}
    \lim_{n \to \infty} n^2 \sin{a_{2n-1}} &= -\lim_{n \to \infty} n^2 \cdot \sin{\frac{4}{(2n-1)^2 \pi}} \\
\end{align*}
$$
{{< /math >}}

原式为 $\infty \cdot 0$ 型未定式，利用倒代换，令

{{< math >}}
$$
\begin{align*}
    t &= \frac{1}{2n - 1} \\
    \Longrightarrow n &= \frac{t+1}{2t}
\end{align*}
$$
{{< /math >}}

于是原式可化为

{{< math >}}
$$
\begin{align*}
    \cdots &= -\lim_{t \to 0} \left( \frac{t+1}{2t} \right)^2 \sin{\frac{4t^2}{\pi}} \\
    &= -\lim_{t \to 0} \left( \frac{t+1}{2t} \right)^2 \cdot \frac{4t^2}{\pi} \\
    &= -\lim_{t \to 0} \frac{(t+1)^2}{\pi} \\
    &= -\frac{1}{\pi}
\end{align*}
$$
{{< /math >}}

### 14

微分方程

{{< math >}}
$$
y' = \frac{1}{(x+y)^2}
$$
{{< /math >}}

满足条件 $y(1) = 0$ 的解为 $\underline{\qquad}$

【解】

令 $x+y = u$，等式两边同时对 $x$ 求导，得到 $u' = 1+y'$。代入原式得

{{< math >}}
$$
\begin{align*}
    u' - 1 &= \frac{1}{u^2} \\
    \frac{\mathrm{d}u}{\mathrm{d}x} &= \frac{1+u^2}{u^2} \\
\end{align*}
$$
{{< /math >}}

采用分离变量法解这个微分方程，得

{{< math >}}
$$
\begin{align*}
    \int \frac{u^2}{1+u^2} \mathrm{d}u &= \int \mathrm{d}x \\
    \Longrightarrow x &= \int \left(1 - \frac{1}{1+u^2}\right) \mathrm{d}u \\
    &= u - \arctan{u} + C \\
\end{align*}
$$
{{< /math >}}

即

{{< math >}}
$$
\begin{align*}
    x &= x + y - \arctan{(x+y)} + C \\
    y &= \arctan{(x+y)} + C
\end{align*}
$$
{{< /math >}}

代入初始条件，可解得

{{< math >}}
$$
\begin{align*}
    0 &= \arctan{1} + C \\
    \Longrightarrow C &= -\frac{\pi}{4}
\end{align*}
$$
{{< /math >}}

故原微分方程的解为

{{< math >}}
$$
x = \tan{(y + \frac{\pi}{4})} - y
$$
{{< /math >}}

### 15

设实矩阵

{{< math >}}
$$
A = \begin{bmatrix}
    a+1 & a \\
    a & a
\end{bmatrix}
$$
{{< /math >}}

若对任意实向量 $\alpha = [x_1, x_2]^{\top}, \beta = [y_1, y_2]^{\top}$，都有

{{< math >}}
$$
(\alpha^{\top} A \beta)^{2} \leqslant \alpha^{\top} A \alpha \cdot \beta^{\top} A \beta
$$
{{< /math >}}

都成立，则 $a$ 的取值范围是 $\underline{\qquad}$

【解】

用作差法，得到

{{< math >}}
$$
\begin{align*}
    (\alpha^{\top} A \beta)^{2} - \alpha^{\top} A \alpha \cdot \beta^{\top} A \beta &= \alpha^{\top} A ( \beta \alpha^{\top} - \alpha \beta^{\top} ) A \beta \\
    &= \alpha^{\top} A \left(
        \begin{bmatrix}
            x_1 y_1 & x_2 y_1 \\
            x_1 y_2 & x_2 y_2
        \end{bmatrix} - \begin{bmatrix}
            x_1 y_1 & x_1 y_2 \\
            x_2 y_1 & x_2 y_2
        \end{bmatrix}
    \right) A \beta \\
    &= \alpha^{\top} A (x_1 y_2 - x_2 y_1) \begin{bmatrix}
        0 & -1 \\
        1 & 0
    \end{bmatrix} A \beta \\
    &= (x_1 y_2 - x_2 y_1) \alpha^{\top} \begin{bmatrix}
        a+1 & a \\
        a & a
    \end{bmatrix} \begin{bmatrix}
        0 & -1 \\
        1 & 0
    \end{bmatrix} \begin{bmatrix}
        a+1 & a \\
        a & a
    \end{bmatrix} \beta \\
    &= (x_1 y_2 - x_2 y_1) \alpha^{\top} \begin{bmatrix}
        a & -(a+1) \\
        a & -a
    \end{bmatrix} \begin{bmatrix}
        a+1 & a \\
        a & a
    \end{bmatrix} \beta \\
    &= (x_1 y_2 - x_2 y_1) \alpha^{\top} \begin{bmatrix}
        0 & -a \\
        a & 0
    \end{bmatrix} \beta \\
    &= a (x_1 y_2 - x_2 y_1) \begin{bmatrix}
        x_1 & x_2
    \end{bmatrix} \begin{bmatrix}
        0 & -1 \\
        1 & 0
    \end{bmatrix} \begin{bmatrix}
        y_1 \\
        y_2
    \end{bmatrix} \\
    &= -a (x_1 y_2 - x_2 y_1)^2 \leqslant 0 \\
    \Longrightarrow a &\geqslant 0
\end{align*}
$$
{{< /math >}}

### 16

设随机试验每次成功的概率为 $p$，现进行 3 次独立重复试验。在至少成功 1 次的情况下，3 次试验全部成功的概率为 $\frac{4}{13}$，则 $p = \underline{\qquad}$

【解】

本题考察二项分布以及条件概率。设随机变量 $X$ 表示 3 次试验中成功的次数，则 $X \sim B(3, p)$。由题意得

{{< math >}}
$$
\begin{align*}
    P(X=3 | X \geqslant 1) &= \frac{P(X=3, X \geqslant 1)}{P(X \geqslant 1)} \\
    &= \frac{C_3^3 p^3}{1 - C_3^0 (1 - p)^3} = \frac{4}{13}
\end{align*}
$$
{{< /math >}}

整理并解这个方程

{{< math >}}
$$
\begin{align*}
    13 p^3 + 4 (1 - p)^3 &= 4 \\
    9 p^3 + 12 p^2 - 12 p &= 0 \\
    3 p^2 + 4 p - 4 &= 0 \quad (0 < p < 1) \\
    (3p - 2)(p + 2) &= 0 \\
    \Longrightarrow p &= \frac{2}{3}
\end{align*}
$$
{{< /math >}}

## 解答题

### 17

已知平面区域 {{< math >}}$D = \{(x, y) \mid \sqrt{1-y^2} \leqslant x \leqslant 1, -1 \leqslant y \leqslant 1\}${{< /math >}}，计算

{{< math >}}
$$
\iint_D \frac{x}{\sqrt{x^2+y^2}} \mathrm{d}x \mathrm{d}y
$$
{{< /math >}}

【解】

依题意，积分区域是一个 $y$ 型区域，且关于 $x$ 轴对称。而被积函数关于 $x$ 是奇函数，关于 $y$ 是偶函数。所以原积分式可化为

{{< math >}}
$$
\begin{align*}
    2 \iint_{D_1} \frac{x}{\sqrt{x^2+y^2}} \mathrm{d}x \mathrm{d}y
\end{align*}
$$
{{< /math >}}

其中

{{< math >}}
$$
D_1 = \{(x, y) \mid \sqrt{1-y^2} \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1\}
$$
{{< /math >}}

这仍然是一个 $y$ 型区域。不过注意到，如果先关于 $y$ 积分，会得到反三角函数，不利于计算。所以，应该将这个区域看成 $x$ 型区域。于是

{{< math >}}
$$
\begin{align*}
    \cdots &= 2 \iint_{D_1} \frac{x}{\sqrt{x^2+y^2}} \mathrm{d}x \mathrm{d}y \\
    &= \int_{0}^{1} \mathrm{d}y \int_{\sqrt{1-y^2}}^{1} (x^2+y^2)^{-\frac{1}{2}} \mathrm{d} x^2 \\
    &= \int_{0}^{1} \left. 2(x^2+y^2)^{\frac{1}{2}} \right|_{\sqrt{1-y^2}}^{1} \mathrm{d}y \\
    &= 2 \int_{0}^{1} \left( \sqrt{1+y^2} - 1 \right) \mathrm{d}y
\end{align*}
$$
{{< /math >}}

计算这个定积分，不得不进行三角换元。令

{{< math >}}
$$
\begin{align*}
    y &= \tan{\theta} \\
    y \in [0, 1] & \Rightarrow \theta \in [0, \frac{\pi}{4}] \\
    \mathrm{d}y &= \sec^2{\theta} \mathrm{d}\theta
\end{align*}
$$
{{< /math >}}

所以原式可化为

{{< math >}}
$$
\begin{align*}
    \cdots &= 2 \int_{0}^{\frac{\pi}{4}} (\sec{\theta} - 1) \sec^2{\theta} \mathrm{d}\theta \\
    &= 2 \int_{0}^{\frac{\pi}{4}} \frac{\cos{\theta}}{\cos^4{\theta}} \mathrm{d}\theta - 2 \int_{0}^{\frac{\pi}{4}} \sec^2{\theta} \mathrm{d}\theta \\
    &= 2 \int_{0}^{\frac{\pi}{4}} \left. \frac{\mathrm{d} \sin{\theta}}{(1 - \sin^2{\theta})^2} - 2 \tan{\theta} \right|_{0}^{\frac{\pi}{4}} \\
    &= 2 \int_{0}^{\frac{\sqrt{2}}{2}} \frac{\mathrm{d}t}{(t+1)^2 (t-1)^2} - 2
\end{align*}
$$
{{< /math >}}

计算至此，需要对被积的分式裂项。设

{{< math >}}
$$
\begin{align*}
    \frac{1}{(t+1)^2 (t-1)^2} = \frac{A}{t+1} + \frac{B}{t-1} + \frac{C}{(t+1)^2} + \frac{D}{(t-1)^2} \tag{2}
\end{align*}
$$
{{< /math >}}

由留数法，可以首先解得

{{< math >}}
$$
\begin{align*}
    C &= \left. \frac{1}{(t-1)^2} \right|_{t=-1} = \frac{1}{4} \\
    D &= \left. \frac{1}{(t+1)^2} \right|_{t=1} = \frac{1}{4}
\end{align*}
$$
{{< /math >}}

代入方程 (2)，得到

{{< math >}}
$$
\begin{align*}
    \frac{1}{(t+1)^2 (t-1)^2} &= \frac{A}{t+1} + \frac{B}{t-1} + \frac{t^2+1}{2 (t+1)^2 (t-1)^2} \\
    \frac{1-t^2}{2 (t+1)^2 (t-1)^2} &= \frac{A}{t+1} + \frac{B}{t-1} \\
    -\frac{1}{2 (t+1) (t-1)} &= \frac{A}{t+1} + \frac{B}{t-1} \\
\end{align*}
$$
{{< /math >}}

再一次使用留数法，可以解得

{{< math >}}
$$
\begin{align*}
    A &= \left. -\frac{1}{2} \times \frac{1}{t-1} \right|_{t=-1} = \frac{1}{4} \\
    B &= \left. -\frac{1}{2} \times \frac{1}{t+1} \right|_{t=1} = -\frac{1}{4}
\end{align*}
$$
{{< /math >}}

于是，原式可化为

{{< math >}}
$$
\begin{align*}
    \cdots &= \frac{1}{2} \left[
        \int_{0}^{\frac{\sqrt{2}}{2}} \frac{\mathrm{d}t}{t+1} - \int_{0}^{\frac{\sqrt{2}}{2}} \frac{\mathrm{d}t}{t-1} + \int_{0}^{\frac{\sqrt{2}}{2}} \frac{\mathrm{d}t}{(t+1)^2} + \int_{0}^{\frac{\sqrt{2}}{2}} \frac{\mathrm{d}t}{(t-1)^2}
    \right] - 2 \\
    &= \frac{1}{2} \left[
        \ln{(t+1)} \Big|_{0}^{\frac{\sqrt{2}}{2}} - \ln{(1-t)} \Big|_{0}^{\frac{\sqrt{2}}{2}} - \frac{1}{t+1} \Big|_{0}^{\frac{\sqrt{2}}{2}} - \frac{1}{t-1} \Big|_{0}^{\frac{\sqrt{2}}{2}}
    \right] - 2 \\
    &= \frac{1}{2} \left[
        \ln{\frac{2+\sqrt{2}}{2-\sqrt{2}}} - \left(
            \frac{2}{\sqrt{2}+2} - 1 + \frac{2}{\sqrt{2}-2} + 1
        \right)
    \right] - 2 \\
    &= \frac{1}{2} \left[
        2 \ln{(\sqrt{2}+1)} - \frac{2 \times 2\sqrt{2}}{(\sqrt{2}+2)(\sqrt{2}-2)}
    \right] - 2 \\
    &= \ln{(\sqrt{2}+1)} + \sqrt{2} - 2
\end{align*}
$$
{{< /math >}}

【点评】

本题形为二重积分，实际上难点在于定积分的计算过程。本题涉及到二重积分的对称性、定积分第二换元法（三角换元）、三角函数有理式的积分、分式裂项等诸多知识点，且计算量非常大，计算过程繁琐，极易出错。

### 20

已知有向曲线 $L$ 为球面 $x^2 + y^2 + z^2 = 2x$ 与平面 $2x - z - 1 = 0$ 的交线，且从 $z$ 轴正向往负向看去为逆时针方向。计算曲线积分

{{< math >}}
$$
\oint_{L} (6xyz - yz^2) \mathrm{d}x + 2x^2z \mathrm{d}y +xyz \mathrm{d} z
$$
{{< /math >}}

本题求解的是空间曲线的第二类曲线积分，考察斯托克斯（Stokes）公式的运用。斯托克斯公式将空间曲线的第二类曲线积分转化为空间曲面的第二类曲面积分。

依题意，球面与平面的交线应当是一个圆，是一个封闭曲线。化为第二类曲面积分后，积分区域就是一个有界的平面。

{{< math >}}
$$
\begin{align*}
    I &= \oint_{L} (6xyz - yz^2) \mathrm{d}x + 2x^2z \mathrm{d}y +xyz \mathrm{d} z \\
    &= \iint_{\Sigma} \begin{vmatrix}
        \mathrm{d}y \mathrm{d}z & \mathrm{d}z \mathrm{d}x & \mathrm{d}x \mathrm{d}y \\
        \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
        6xyz - yz^2 & 2x^2z & xyz
    \end{vmatrix} \\
    &= \iint_{\Sigma} (xz - 2x^2) \mathrm{d}y \mathrm{d}z + (6xy - 2yz - yz) \mathrm{d}z \mathrm{d}x + (4xz - 6xz + z^2) \mathrm{d}x \mathrm{d}y \\
    &= \iint_{\Sigma} (xz - 2x^2) \mathrm{d}y \mathrm{d}z + (6xy - 3yz) \mathrm{d}z \mathrm{d}x + (z^2 - 2xz) \mathrm{d}x \mathrm{d}y \\
\end{align*}
$$
{{< /math >}}

其中 $\Sigma$ 表示平面 $z = 2x - 1$ 的上侧。应用转换投影法，将第二类曲面积分转化为 $xOy$ 平面内的二重积分。

{{< math >}}
$$
\begin{align*}
    I &= \iint_{\Sigma} (xz - 2x^2) \mathrm{d}y \mathrm{d}z + (6xy - 3yz) \mathrm{d}z \mathrm{d}x + (z^2 - 2xz) \mathrm{d}x \mathrm{d}y \\
    &= \iint_{\Sigma} (xz - 2x^2) \cdot (-2) + (6xy - 3yz) \cdot 0 + (z^2 - 2xz) \mathrm{d}x \mathrm{d}y \\
    &= \iint_{\Sigma} (4x^2 - 4xz + z^2) \mathrm{d}x \mathrm{d}y \\
    &= \iint_{D} [4x^2 - 4x(2x-1) + (2x-1)^2] \mathrm{d}x \mathrm{d}y \\
    &= \iint_{D} \mathrm{d}x \mathrm{d}y
\end{align*}
$$
{{< /math >}}

联立球面和平面的方程

{{< math >}}
$$
L: \begin{cases}
    x^2 + y^2 + z^2 = 2x \\
    2x - z - 1 = 0
\end{cases}
$$
{{< /math >}}

即为空间曲线 $L$ 的方程。消去 $z$，得到交线在 $xOy$ 平面内的投影

{{< math >}}
$$
\begin{align*}
    x^2 + y^2 + (2x-1)^2 &= 2x \\
    5x^2 + y^2 - 6x + 1 &= 0 \\ 
    5 \left[ \left(x - \frac{3}{5} \right)^2 - \frac{9}{25} \right] + y^2 + 1 &= 0 \\
    5 \left( x - \frac{3}{5} \right)^2 + y^2 &= \frac{4}{5} \\
    \frac{\left( x - \frac{3}{5} \right)^2}{\left( \frac{2}{5} \right)^2} + \frac{y^2}{\left( \frac{2}{\sqrt{5}} \right)^2} &= 1
\end{align*}
$$
{{< /math >}}

这说明了积分区域在 $xOy$ 平面内的投影是一个椭圆区域 $D$。由平面解析几何的相关知识，可以判断椭圆的半长轴和半短轴分别为 $a = \frac{2}{\sqrt{5}}$ 和 $b = \frac{2}{5}$。由椭圆面积公式 $S = \pi ab$ 得

{{< math >}}
$$
\begin{align*}
    I &= \iint_{D} \mathrm{d}x \mathrm{d}y \\
    &= \pi \times \frac{2}{5} \times \frac{2}{\sqrt{5}} \\
    &= \frac{4 \sqrt{5} \pi}{25}
\end{align*}
$$
{{< /math >}}

【点评】

本题题型较为常规，但考察到了很多的知识点，包括斯托克斯公式、转换投影法、二重积分等。同时，由于斯托克斯公式需要计算三阶行列式，无形之中增加了本题的计算量。此外，计算二重积分时，由于倾斜平面截球面所得交线在 $xOy$ 平面内的投影是椭圆，求解这个椭圆方程也需要一些计算量。如稍有不慎，二重积分的被积函数算错，由于积分区域复杂，计算量会更大。这在考场上是十分令人崩溃的。
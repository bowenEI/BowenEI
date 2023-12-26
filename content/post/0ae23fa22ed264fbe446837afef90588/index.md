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

{{< gdocs src="https://docs.google.com/document/d/1GP4QxKlc49zVq3suq2CgQ6ZlIVZt2oEUiUL0xX0vlmQ/edit?usp=sharing" >}}

## 选择题

### 1

本题考察变限函数的定义和积分的性质。若一个函数具有奇偶性，则其求导和积分结果的奇偶性正好相反。题干中的被积函数都是偶函数，且变限积分的上限是奇函数。因此，其导函数都是偶函数，所以原函数都是奇函数。

### 2

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

本题考查线性方程组解的性质。本题通过给出三维空间中平面的位置关系，考察考生对线性方程组的直观理解，颇有新意。

由图可知，平面 $\pi_1 \cap \pi_2 \cap \pi_3 = l$，交于一条直线。这说明，三个平面所对应的平面方程组成的三元线性方程组有无穷多解，且位于同一条直线上。所以，其基础解系只有一个向量作基。

那么，相应的齐次线性方程组的系数矩阵的秩 $r = 3 - 1 = 2$，相应的非齐次线性方程组的增广矩阵的秩应该和前者相同。

### 6

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

## 填空题

## 解答题

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
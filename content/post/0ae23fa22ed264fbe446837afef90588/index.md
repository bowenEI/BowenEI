---
# Documentation: https://hugoblox.com/docs/managing-content/

title: "挑战 2024 年考研数学（一）"
subtitle: ""
summary: ""
authors: []
tags: [考研, 数学]
categories: []
date: 2023-12-24T22:20:59+08:00
lastmod: 2023-12-24T22:20:59+08:00
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
---

2024 年考研已落下帷幕。据报道，今年考研的人数比去年减少了 36 万（共 438 万人报考），引发社会广泛关注。在刚刚结束的数学科目考试中，不少考生哀叹今年的数学试题难如登天，特别是 301 数学（一）。

本篇博客将持续更新今年数学（一）每道题目的详细作答过程，体会莘莘学子们在考场上的不易。

<!--more-->

------

## 选择题

## 填空题

## 解答题

### 20

已知有向曲线 $L$ 为球面 $x^2 + y^2 + z^2 = 2x$ 与平面 $2x - z - 1 = 0$ 的交线，且从 $z$ 轴正向往负向看去为逆时针方向。计算曲线积分

{{< math >}}
$$
\oint_{L} (6xyz - yz^2) \mathrm{d}x + 2x^2z \mathrm{d}y +xyz \mathrm{d} z
$$
{{< /math >}}

【解】

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
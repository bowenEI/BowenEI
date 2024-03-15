---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "动态规划"
linktitle: "动态规划"
date: 2021-10-16T20:55:30+08:00
type: book
summary: ""
weight: 200
---

<!--more-->

## 动态规划的原理

与分治算法类似，动态规划法也是把问题一层一层地分解为规模逐渐减小的同类型的子问题，但是与分治算法有一些区别。

动态规划将当前问题分解为多个相关子问题，而且子问题的解可以被重复使用。每个子问题只求解一次，结果保存在表中，以后用到时直接存取。

## 动态规划的条件

- **最优子结构**：当一个问题的最优解包含了子问题的最优解时，称这个问题具有最优子结构。
- **重叠子问题**：在问题的求解过程中，很多子问题的解将被多次使用。

## 状态转移方程

可以用数学中的递推公式来理解，动态规划的本质是利用子问题的结果递推出当前问题的结果。构造状态转移方程是动态规划算法最核心的步骤，需要针对具体的问题进行构造。

{{< callout note >}}

**动态规划与数学归纳法的区别与联系**

1. 动态规划和数学归纳法都有递推的思想。
2. 动态规划的状态转移方程是根据具体问题人为构造出来的，而数学归纳法的递推关系正是需要证明的。
3. 动态规划的目的是利用递推思想求解复杂的最优解问题，而数学归纳法的目的是证明归纳猜想是否成立。

总而言之，动态规划和数学归纳法可以用下面的形式加以区别：

- 动态规划：一般（状态转移方程）$\rightarrow$ 特殊（目标问题解）
- 数学归纳法：特殊（待证明结论）$\rightarrow$ 一般（递推关系成立）

{{< /callout >}}

## 动态规划的一般步骤

1. 给出问题表示，明确初始问题
2. 分析最优结构，构造递推公式
3. 自底向上计算，注意计算顺序
4. 记录决策过程，回溯最优方案

## 动态规划经典问题

{{< list_children >}}

## 小结

问题一般采用动态规划法，当具有

1. 最优子结构性质时
2. 高度重复性

若问题不是 NP-hard 问题，进一步分析后就有可能获得效率较高的算法。

若问题本身就是 NP-hard 问题，那么与其它的精确算法相比，动态规划法性能一般不算太坏。
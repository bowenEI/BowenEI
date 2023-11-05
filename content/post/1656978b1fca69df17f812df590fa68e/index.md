---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "并行计算集合通信初步"
subtitle: ""
summary: ""
authors: []
tags: []
categories: [Academic, Knowledge]
date: 2023-11-05T14:48:37+08:00
lastmod: 2023-11-05T14:48:37+08:00
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

作为并行计算的一个重要概念，集合通信经常被用来构建高性能的单程序流/多数据流（Single Program-Multiple Data, SPMD）程序，譬如分布式机器学习系统。本文将介绍集合通信中的常见算子，并分析其复杂度。

<!--more-->

------

## 通信模型

假设在一个分布式的集群中，共有 $n$ 个设备。用数组 `device[i]` 表示第 `i` 个设备。设备之间的点对点（Point-to-Point, P2P）通信由全双工传输（Full-Duplex Transmission）实现。那么，该通信模型的基本行为可以定义如下：

- 每次通信有且仅有一个发送者（Sender）和一个接收者（Receiver）。这意味着，在某个特定的时刻，每个设备仅能至多或接收一个消息（Message）。每个设备可以同时发送一个消息和接收一个消息。一个网络中可以同时传输多个来自于不同设备的消息。

- 传输一个长度为 $l$ 个字节（Byte）的消息会花费 $a+bl$ 的时间。
  - $a$ 代表延迟（Latency），即一个字节通过网络从一个设备出发到达另一个设备所需的全部时间。$a$ 的大小取决于两个设备之间的物理距离（如跨设备、跨机器、跨集群等）。
  - $b$ 代表传输延迟（Transmission Delay），即传输一个具有 $l$ 个字节的消息所需的全部时间。$b$ 的大小取决于通信网络的带宽。

需要注意的是，这里简化了传输延迟的定义，并没有考虑在真实网络传输中会出现的丢失的消息（Dropped Message）和损坏的消息（Corrupted Message）的情况。

{{< figure src="2f1ac53ab4bff8e769030ba38a90ac67.png" title="通信模型" numbered="true" >}}

## 常见集合通信算子

{{< figure src="7baab6efbf4f728b2df8d7d1e8f955fe.png" title="常见集合通信算子" numbered="true" >}}

### Broadcast

广播（Broadcast）是最基础的集合通信算子之一。对于第 `i` 个设备，广播意味着将长度为 $l$ 字节的消息发送给其余的 $n-1$ 个设备。由于每个设备在一个时刻只能发送一个消息，一种简单的实现方式循环发送 $n-1$ 次，其通信开销为

{{< math >}}
$$
\begin{align}
    T_{\textrm{broadcast}} = (n-1)(a+bl)
\end{align}
$$
{{< /math >}}

{{< figure src="b4640f7c166969f9b0236bad31effb1c.png" title="Broadcast" numbered="true" >}}

但是很显然，这种通信方式是串行的，没有并行性。我们可以利用分治思想对上述算法进行优化，将这个问题分解为在两个子集群中进行广播，每个子集群有 $n/2$ 个设备。然后对于每个子集群，又可以继续采用分治思想分解问题，直到每个子集群仅有一个设备。此时，只包括两种情况：

1. 子集群的这个设备上包括需要广播的消息。此时什么都不需要做。
2. 子集群的这个设备上没有需要广播的消息。此时，需要将消息发送给之。

每个子集群的通信的通信是独立的，也就是可以并行的。所以把这些通信开销加起来，得到

{{< math >}}
$$
\begin{align}
    T_{\textrm{broadcast}} = (a+bl) \log_2{n}
\end{align}
$$
{{< /math >}}

下图展示了分治算法的过程：

{{< figure src="1f7c2421e5eded92a327f0dd9fc42aeb.png" title="分治算法" numbered="true" >}}

其中，设备数量 $n=8$。第一次分治，设备 `1` 发送消息给设备 `1` 和 `5`（本地就无需发送了，下同）；第二次分治，设备 `1` 发送消息给设备 `1` 和 `3`，设备 `5` 发送消息给设备 `5` 和 `7`；第三次分治，设备 `1` 发送消息给设备 `1` 和 `2`，设备 `3` 发送消息给设备 `3` 和 `4`，设备 `5` 发送消息给设备 `5` 和 `6`，设备 `7` 发送消息给设备 `7` 和 `8`。

### Reduce & All Reduce

在分布式机器学习系统中，另一个常见的操作是将不同设备上的计算结果进行聚合（Aggregation）。例如求和、乘积、最值等，这里我们统一用一个聚合函数 $f$ 来表示。如果最终的结果只存在编号为 `i` 的一个设备上，这就是 Reduce 算子；如果所有的设备都需要存储最终的结果，这就是 All Reduce 算子。

{{< figure src="3a2f6411fb885633c5f1cc74a42101ce.png" title="Reduce & All Reduce" numbered="true" >}}

由于上述分治算法的并行性，Reduce 和 All Reduce 的通信开销均为

{{< math >}}
$$
\begin{align}
    T_{\textrm{reduce}} = (a+bl) \log_2{n} + O(f(l))
\end{align}
$$
{{< /math >}}

其中，$O(f(l))$ 表示聚合函数的时间复杂度，它是 $l$ 的函数。

### Gather & All Gather

收集（Gather）也是一个常见的操作，例如张量的拼接（Concatenate）。Gather 和 All Gather 的通信开销均为

{{< math >}}
$$
\begin{align}
    T_{\textrm{gather}} = a \log_2{n} + (n-1)bl
\end{align}
$$
{{< /math >}}

{{< figure src="914f573b614695fda2b89bcabd5d080c.png" title="Gather & All Gather" numbered="true" >}}

这里要注意，在第 $t$ 次分治中，传输的信息长度都为原来的 $2^t$ 倍。所以，分治算法无法降低传输时延，和串行一样为 $(n-1)bl$。

特别地，对于 All Gather 算子，通信开销可以通过[超立方体](https://link.springer.com/book/10.1007/978-3-030-25209-0)算法降低为和 Gather 一样。由于篇幅问题本文不再赘述，感兴趣的读者可以参考相关链接。

### Scatter

Scatter 算子可以被视为是 Gather 算子的逆运算：把一个存在于编号为 `i` 的设备上，长度为 $n$（信息长度为 $nl$）的链式数据结构 `L` 中的值分散到每个设备上。使得 `device[i]` 的设备会得到 `L[i]` 的结果。

{{< figure src="8a096c5bbeb0d3f6e2d51e62b2f628db.png" title="Scatter" numbered="true" >}}

因此，Scatter 算子的通信开销为

{{< math >}}
$$
\begin{align}
    T_{\textrm{scatter}} = a \log_2{n} + (n-1)bl
\end{align}
$$
{{< /math >}}

### Reduce Scatter

{{< figure src="7ce7e96d1d88971b8823e756c996c30d.png" title="Reduce Scatter" numbered="true" >}}

### All to All

{{< figure src="f4c27c45d1731d1e43c4893bb2a3ddea.png" title="All to All" numbered="true" >}}
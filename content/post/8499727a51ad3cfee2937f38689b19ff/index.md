---
# Documentation: https://hugoblox.com/docs/managing-content/

title: "Towards Efficient Generative Large Language Model Serving: A Survey From Algorithms to Systems"
subtitle: "面向高效生成式大语言模型的服务：从算法到系统的综述"
summary: ""
authors: []
tags: [LLM, Inference, Survey]
categories: [Academic]
date: 2024-01-15T01:07:11+08:00
lastmod: 2024-01-17T01:07:11+08:00
featured: false
draft: false
toc: true

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

<!--more-->

## Abstract 摘要

> In the rapidly evolving landscape of artificial intelligence (AI), generative large language models (LLMs) stand at the forefront, revolutionizing how we interact with our data. However, the computational intensity and memory consumption of deploying these models present substantial challenges in terms of serving efficiency, particularly in scenarios demanding low latency and high throughput. This survey addresses the imperative need for efficient LLM serving methodologies from a machine learning system (MLSys) research perspective, standing at the crux of advanced AI innovations and practical system optimizations. We provide in-depth analysis, covering a spectrum of solutions, ranging from cutting-edge algorithmic modifications to groundbreaking changes in system designs. The survey aims to provide a comprehensive understanding of the current state and future directions in efficient LLM serving, offering valuable insights for researchers and practitioners in overcoming the barriers of effective LLM deployment, thereby reshaping the future of AI.

在快速发展的人工智能 (AI) 领域，生成式大语言模型 (LLM) 处于最前沿，彻底改变了我们与数据交互的方式。然而，部署这些模型所需的计算强度和内存消耗对服务效率提出了巨大的挑战，特别是在需要低延迟和高吞吐量的场景中。这篇综述从机器学习系统（MLSys）研究的角度探讨了对高效 LLM 服务方法的迫切需求，这是先进 AI 创新和实用系统优化的关键所在。我们给出了深入的分析，涵盖了一系列解决方案，从尖端算法的改进到系统设计的突破性优化。该综述旨在全面了解高效 LLM 服务的现状和未来方向，为研究人员和从业者提供宝贵的见解，帮助他们克服有效部署 LLM 的障碍，从而重塑 AI 的未来。

## Taxonomy 分类

{{< figure src="1efdd3bd0e2fa731ee1537e3954c9dca.png" >}}

## Algorithmic Innovations 算法创新

### Decoding Algorithm 译码算法

{{< figure src="e8de4471a5f436349f6ef3de7e905880.png" >}}

### Architecture Design 架构设计

{{< figure src="dfe60d993412dcf33947208291559286.png" >}}

### Model Compression 模型压缩

## System Optimizations 系统优化

### Low-bit Quantization 低比特量化

### Parallel Computation 并行计算

### Memory Management 内存管理

### Request Schedudling 请求调度

### Kernel Optimization 内核优化
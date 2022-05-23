---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Dynamic Path Based DNN Synergistic Inference Acceleration in Edge Computing Environment"
authors:
- Meng Zhou
- Bowen Zhou
- Huitian Wang
- Fang Dong
- Wei Zhao
date: 2022-05-06T14:24:55+08:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-05-06T14:24:55+08:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "2021 IEEE 27th International Conference on Parallel and Distributed Systems (ICPADS)"
publication_short: "ICPADS 2021 (CCF C 类会议)"

abstract: "Deep Neural Networks (DNNs) have achieved excellent performance in intelligent applications. Nevertheless, it is elusive for devices with limited resources to support computationally intensive DNNs, while employing the cloud may lead to prohibitive latency. Better solutions are exploiting edge computing and reducing unnecessary computation. Multi-exit DNN based on the early exit mechanism has an impressive effect in the latter, and in edge computing paradigm, model partition on multi-exit chain DNNs is proved to accelerate inference effectively. However, despite reducing computations to some extent, multiple exits may lead to instability of performance due to variable sample quality, performance inferior to the original model especially in the worst case. Furthermore, nowadays DNNs are universally characterized by a directed acyclic graph (DAG), complicating the partition of multi-exit DNN exceedingly. To solve the issues, in this paper, considering online exit prediction and model execution optimization for multi-exit DNN, we propose a Dynamic Path based DNN Synergistic inference acceleration framework (DPDS), where exit designators are designed to avoid iterative entry for exits; to further promote computational synergy in the edge, the multi-exit DNN is dynamically partitioned according to network environment to achieve fine-grained computing offloading. Experimental results show that DPDS can significantly accelerate DNN inference by 1.87× to 6.78×."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://ieeexplore.ieee.org/document/9763784
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

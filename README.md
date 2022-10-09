# BowenEI

## 仓库简介

该仓库是我的[个人主页](https://bowenei.gitee.io/)在 Gitee Pages 上托管的源码，使用 [Hugo](https://gohugo.io/) 框架和 [Hugo Academic Theme](https://github.com/wowchemy/starter-hugo-academic) 主题。

## 环境依赖

### Hugo

- [Golang](https://golang.org/)
- ~~[Hugo v0.81.0](https://github.com/gohugoio/hugo/releases/tag/v0.81.0)~~
- ~~[Hugo v0.89.4](https://github.com/gohugoio/hugo/releases/tag/v0.89.4)~~
- ~~[Hugo v0.91.2](https://github.com/gohugoio/hugo/releases/tag/v0.91.2)~~
- ~~[Hugo v0.97.3](https://github.com/gohugoio/hugo/releases/tag/v0.97.3)~~
- [Hugo v0.104.3](https://github.com/gohugoio/hugo/releases/tag/v0.104.3)

### Wowchemy

[Wowchemy](https://wowchemy.com/docs/) 是本博客依赖的主题框架。主题版本位于 `go.mod`，更新方法详见[文档](https://wowchemy.com/docs/hugo-tutorials/update/)。

## 使用说明

### 快速上手

1. `content/` 文件夹下是博客的内容，编辑主要都集中在这部分。包括 `learn/` 和 `post/` 两个重要的文件夹，以及 `home/` 文件夹下的各个部分。`content/` 文件夹下的各个文件夹名称不可随意修改！
2. `learn/` 文件夹下是我学习各个课程的笔记，主要是计算机编程方面，还包括马克思主义以及其他方面。
3. `post/` 文件夹下主要是一些博客文章，主要包括文献阅读等方面。
4. `assets/media/` 文件夹下则是按照 `content/` 文件夹下的结构存储需要使用的图片，相当于图床。

### home

`home` 文件夹下的 `md` 文件是组成博客各页面最基本的部分，由 `index.md` 来控制。

- `about.md` 主要是个人的自我介绍。
- `blogs.md` 主要用于显示个人最近发布的博客文章。
- `gallery.md` 是照片墙。
- `publications.md` 主要用于发表的论文。
- `tags.md` 主要用于显示感兴趣的方向和内容，这由博客文章所打的标签数量决定。

### learn

`learn` 文件夹下主要是我个人的学习笔记，包括马克思主义、计算机基本知识、恋爱心理以及数学等各领域的知识。

### post

`post/` 文件夹下主要是一些博客文章，每篇文章都会有类别 `categories` 属性，可能会有标签 `tags` 属性。目前，我的博客文章主要包含如下几种类别：

- `Essay`: 随笔。主要是专业知识、科研之外的一些内容。
- `Academic`: 学术。主要是文献精读后的笔记和理解，以及学术交流中专家学者的一些观点和见解。
- `Technique`: 技术。主要包含计算机编程、人工智能等各类语言和工具的使用。
- `Read`: 阅读。主要包含书籍阅读后的笔记与思维导图。
- `Presentation`：演讲。主要包含专家、学者的演讲原文，以及对这些演讲的整理和归纳。
- `Knowledge`：知识。主要包括各大领域的一些知识和基本概念。

## 注意事项

### Go modules

~~本博客使用的主题被打包为 `Go modules`，它被放在 Github 仓库中，可能会存在访问较慢的问题。~~

~~在从远程同步最新仓库前，应当先执行 `hugo mod tidy` 整理 `module`，然后再 `git pull`，以防止出现 `hugo` 连接不上主题仓库的问题。~~

该问题现已得到解决，只需要在 `config/_default/config.yaml` 中设置代理：

```yaml
module:
  proxy: https://goproxy.cn
```

### svg 渲染

本博客所在的 Gitee 远程仓库存在图片加载性能方面的问题，特别是对于矢量图 `svg` 的渲染。

## Github Actions 自动部署

Github Actions 提供了自动化的部署工具，可以实现 Github Pages 的自动部署。当我们在本地向远程仓库推送更新之后的博客内容时，远程仓库执行一系列操作即可实现自动更新。Github 上有 Hugo 静态页面框架部署的模板，简单几步设置即可完成。

# BowenEI

## 仓库简介

该仓库是我的[个人主页](https://bowenei.gitee.io/)在 Gitee Pages 上托管的源码，使用 [Hugo](https://gohugo.io/) 框架和 [Hugo Academic Theme](https://github.com/wowchemy/starter-hugo-academic) 主题。

## 环境依赖

- [Golang](https://golang.org/)
- ~~[Hugo v0.81.0](https://github.com/gohugoio/hugo/releases/tag/v0.81.0)~~
- ~~[Hugo v0.89.4](https://github.com/gohugoio/hugo/releases/tag/v0.89.4)~~
- ~~[Hugo v0.91.2](https://github.com/gohugoio/hugo/releases/tag/v0.91.2)~~
- [Hugo v0.97.3](https://github.com/gohugoio/hugo/releases/tag/v0.97.3)

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

### 注意事项

~~在从远程同步最新仓库前，应当先执行 `hugo mod tidy` 整理 `module`，然后再 `git pull`，以防止出现 `hugo` 连接不上主题仓库的问题。~~

1. 本博客使用的主题被打包为 `Go modules`，它被放在 Github 仓库中，可能会存在访问较慢的问题。
2. 本博客所在的 Gitee 远程仓库存在图片加载性能方面的问题，特别是对于矢量图 `svg` 的渲染。

## Github Actions 自动部署

Github Actions 提供了自动化的部署工具，可以实现 Github Pages 的自动部署。当我们在本地向远程仓库推送更新之后的博客内容时，远程仓库执行一系列操作即可实现自动更新。

为了实现本博客的自动部署，需要经过如下几个步骤：

### 配置仓库和子仓库

我们将 Hugo 编译生存的静态页面放在 `./docs/` 文件夹下，使用 `hugo -d ./docs/` 即可。我们将博客源码作为主仓库，将 `./docs/` 文件夹作为子仓库。本地编译完成后，需要先提交并推送子仓库，然后再提交并推送主仓库。

本博客的源代码与远程仓库 [](https://github.com/bowenEI/bowenEI) 关联，静态页面与远程仓库 [](https://github.com/bowenEI/bowenEI.github.io) 关联。Github Actions 实现自动部署的原理在于，将源代码远程仓库中的 `./docs/` 部署到静态页面远程仓库。不过，这需要一些必要的权限。

首先，我们在仓库文件夹下生成一对 `ssh` 密钥。要注意不能一路回车确认，要给出生成的路径 `./.ssh/id_rsa` 否则会覆盖之前已经配置好的 `ssh` 密钥。

```sh
ssh-keygen -t rsa -C "$(git config user.email)"
```

接下来，在源代码远程仓库 [](https://github.com/bowenEI/bowenEI) 中设置 Actions secrets，键名称必须为 `ACTIONS_DEPLOY_KEY`，值为刚才生成的 `ssh` **私钥**。

```sh
cat .ssh/id_rsa
```

最后，在静态页面远程仓库 [](https://github.com/bowenEI/bowenEI.github.io) 中设置 Deploy keys，添加一个键，名称随意（最好能够说明用途），值为刚才生成的 `ssh` **公钥**。

```sh
cat .ssh/id_rsa.pub
```

这样配置的原因在于，源代码远程仓库有了私钥，相当于在部署时告诉静态页面远程仓库我拥有和本机一样的权限。而静态页面远程仓库有了公钥，相当于接受源代码远程仓库的 `ssh` 访问。

### 配置 yml 文件

Github Actions 自动部署是通过 `yml` 文件来进行配置的。我们下面先给出本博客的配置文件，然后再来解读其中的一些含义。

```yml
name: Auto Deploy hugo

on: [push]

jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository code
        uses: actions/checkout@v2
        with:
          submodules: recursive
          fetch-depth: 0
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 0.91.2
          extended: true
      - name: Build 
        run: hugo
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          deploy_key: ${{ secrets.ACTIONS_DEPLOY_KEY }}     # secret 中设置好私钥
          external_repository: bowenEI/bowenEI.github.io    # Page 仓库
          publish_branch: master                            # Page 仓库的分支
          publish_dir: ./docs                               # 静态网页路径
          commit_message: ${{ github.event.head_commit.message }}
```

整个配置文件不难理解。`runs-on` 表示在什么样的操作系统或者环境下运行，这里是 Ubuntu 的最新版。`steps` 表示整个 Actions 一共需要执行的步骤，我们可以看到一共分为四步：

1. 检查仓库代码，这一步其实就是在核实 `ssh` 连接以及权限的问题。
2. 安装 Hugo 环境，`with` 参数中给出了 Hugo 的版本以及是否带有扩展。
3. 构建 Hugo 静态页面，这实际上和我们本地运行 `hugo` 命令是同样的作用。
4. 部署 Hugo 静态页面，这相当于在远程仓库开启静态页面服务，`with` 参数中给出了私钥、部署仓库的地址、分支以及静态网页的路径。
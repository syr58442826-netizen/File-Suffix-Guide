# File Suffix Guide CLI 工具

命令行版本的文件后缀查询工具，快速查询 200+ 种文件后缀的详细信息。

## 目录

- [功能特点](#功能特点)
- [环境要求](#环境要求)
- [安装说明](#安装说明)
- [使用方法](#使用方法)
  - [查询后缀](#查询后缀)
  - [模糊搜索](#模糊搜索)
  - [分类浏览](#分类浏览)
  - [随机推荐](#随机推荐)
  - [统计信息](#统计信息)
  - [禁用颜色](#禁用颜色)
  - [查看帮助](#查看帮助)
- [数据说明](#数据说明)
- [常见问题](#常见问题)

## 功能特点

- 200+ 种常见文件后缀详细信息
- 精确查询 + 模糊搜索（名称、分类、标签、描述）
- 16 大分类浏览
- 随机推荐功能
- 统计信息展示（分类排行、热门标签等）
- ANSI 彩色输出，Windows 原生支持
- 纯 Python 标准库，零依赖
- 跨平台：Windows / Mac / Linux

## 环境要求

- Python 3.6 或更高版本
- 无需安装任何第三方库

查看 Python 版本：

```bash
python --version
```

## 安装说明

本工具无需安装，直接运行即可。

1. 确保 `suffix-cli.py` 和 `data.json` 在同一目录下
2. 打开命令行/终端，进入该目录
3. 运行命令：

```bash
python suffix-cli.py -h
```

如果显示帮助信息，说明可以正常使用。

> **提示**：在 Linux/Mac 上可能需要使用 `python3` 代替 `python`。

## 使用方法

### 查询后缀

查询指定后缀的详细信息：

```bash
# 查询 .txt 后缀
python suffix-cli.py txt

# 带点也可以
python suffix-cli.py .txt

# 查询 .pdf
python suffix-cli.py pdf
```

输出内容包含：
- 后缀名和中文名
- 所属分类和标签
- 定义 / 用途说明
- 推荐打开软件
- 常见报错（简要）
- 文档位置

### 模糊搜索

如果不确定具体后缀名，可以使用搜索模式，在名称、分类、标签、描述中进行模糊匹配：

```bash
# 搜索与 python 相关的后缀
python suffix-cli.py -s python

# 搜索图片相关后缀
python suffix-cli.py -s 图片

# 搜索压缩格式
python suffix-cli.py -s 压缩
```

> 直接输入关键词（不加 `-s`）时，如果精确匹配不到后缀，会自动转为模糊搜索。

### 分类浏览

列出所有分类：

```bash
python suffix-cli.py -l
# 或
python suffix-cli.py --list-categories
```

查看某个分类下的所有后缀：

```bash
# 查看编程类后缀
python suffix-cli.py -c 编程

# 查看图片类后缀
python suffix-cli.py -c 图片

# 模糊匹配分类名
python suffix-cli.py -c 办公
```

### 随机推荐

随机推荐一个后缀，发现冷门知识：

```bash
python suffix-cli.py -r
```

随机推荐多个后缀：

```bash
# 随机推荐 5 个
python suffix-cli.py --random 5

# 随机推荐 10 个
python suffix-cli.py --random 10
```

### 统计信息

查看整个知识库的统计信息：

```bash
python suffix-cli.py --stats
```

包含：
- 后缀总数、分类数量
- 数据完整度统计
- 分类数量排行（带柱状图）
- 热门标签 TOP 10

### 禁用颜色

如果终端不支持 ANSI 颜色，或在脚本中使用需要纯文本输出，可以禁用颜色：

```bash
python suffix-cli.py --no-color txt
```

### 查看帮助

查看完整帮助信息：

```bash
python suffix-cli.py -h
# 或
python suffix-cli.py --help
```

## 数据说明

数据存储在 `data.json` 文件中，格式如下：

```json
[
  {
    "suffix": "txt",
    "name": "纯文本文件",
    "category": "日常办公文档类",
    "categoryPath": "01-日常办公文档类",
    "docPath": "docs/01-日常办公文档类/txt.md",
    "tags": ["办公", "文档", "文本"],
    "description": "TXT 是纯文本文件...",
    "software": ["记事本", "Notepad++", "VS Code"],
    "errors": ["打开后显示乱码", "文件太大打不开"]
  }
]
```

字段说明：
- `suffix`：后缀名（小写，不带点）
- `name`：中文名
- `category`：分类名称
- `categoryPath`：分类目录名（带编号前缀）
- `docPath`：对应文档的相对路径
- `tags`：标签数组
- `description`：定义/用途描述
- `software`：推荐打开软件列表
- `errors`：常见报错列表

数据来源为项目 `docs/` 目录下的 Markdown 文档。

## 常见问题

### Q1: 运行时提示 "数据文件不存在" 怎么办？

A: 请确保 `data.json` 和 `suffix-cli.py` 在同一个目录下。两个文件必须配套使用。

### Q2: Windows 下颜色显示异常（显示 `[31m` 等字符）？

A: 这是因为旧版 Windows 命令行不支持 ANSI 颜色。可以：
- 使用 Windows 10 及以上版本的系统（默认支持）
- 使用 Windows Terminal（推荐）
- 加上 `--no-color` 参数禁用颜色输出

### Q3: 中文显示乱码怎么办？

A: 请确保终端使用 UTF-8 编码：
- Windows: 执行 `chcp 65001` 切换编码
- Mac/Linux: 默认就是 UTF-8

### Q4: 可以自己添加后缀数据吗？

A: 可以。直接编辑 `data.json` 文件，按照现有格式添加新条目即可。

### Q5: 如何更新数据？

A: 数据来源于项目 `docs/` 目录下的 Markdown 文档。如果文档有更新，可以使用项目提供的数据提取脚本重新生成 `data.json`。

### Q6: 搜索结果太多，只显示了前 20 条？

A: 为了避免输出过多，模糊搜索最多显示 20 条结果。建议使用更精确的关键词进行搜索。

### Q7: 支持批量查询吗？

A: 目前暂不支持批量查询。如需批量处理，可以直接读取 `data.json` 文件进行操作。

---

*本工具是 [File-Suffix-Guide](https://github.com/your-repo/File-Suffix-Guide) 项目的命令行版本*

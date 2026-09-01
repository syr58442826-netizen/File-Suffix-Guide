# .md 文件后缀详解（Markdown）

## 1. 文件定义 & 用途

MD 是 **Markdown** 文档的后缀名。Markdown 是一种轻量级标记语言，用简单的符号来标记文本格式（标题、列表、加粗等），既能保持纯文本的可读性，又能通过渲染呈现出丰富的排版效果。

- **全称**：Markdown Document
- **类型**：轻量级标记语言文档
- **发明者**：John Gruber（2004年）
- **特点**：易读易写、纯文本格式、可转换为 HTML/PDF/Word 等多种格式

## 2. 适用场景

- 写技术文档、README 文件（GitHub 标配）
- 写博客文章（很多博客平台支持 Markdown）
- 记笔记（Obsidian、Notion、Typora 等笔记软件）
- 写技术书籍和教程
- 聊天/论坛中排版文字（微信公众号、知乎、Discord 等）
- 写邮件（部分邮件客户端支持）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Visual Studio Code、Notepad++（需插件）、Typora（免费版） | Typora 付费版、Obsidian、Sublime Text |
| Mac | Visual Studio Code、MacDown、Typora（免费版）、Obsidian | Typora 付费版、BBEdit、Ulysses |
| Linux | Visual Studio Code、ReText、Remarkable、Obsidian | Sublime Text、Atom |

**新手推荐**：
- 入门首选：**Typora**（所见即所得，不用记语法）
- 程序员首选：**VS Code**（配合 Markdown Preview Enhanced 插件）
- 笔记首选：**Obsidian**（双链笔记，功能强大）

## 4. 如何编辑、如何导出

### 如何编辑
1. 用 Markdown 编辑器打开 .md 文件
2. 使用 Markdown 语法编写内容，常用语法：
   - `# 标题`  → 一级标题
   - `## 标题` → 二级标题
   - `**加粗**` → 加粗文字
   - `- 列表项` → 无序列表
   - `` `代码` `` → 行内代码
   - `[链接文字](网址)` → 超链接

### 如何导出/转换
- **转成 HTML**：VS Code 插件或 Pandoc 命令转换
- **转成 PDF**：Typora → 文件 → 导出 → PDF
- **转成 Word**：Pandoc 命令：`pandoc input.md -o output.docx`
- **转成图片**：用 Markdown 编辑器的导出功能或截图
- **批量转换**：使用 **Pandoc** 命令行工具（支持几乎所有格式互转）

## 5. 常见报错与解决

### 问题1：Markdown 文件双击打不开
**原因**：系统没有安装支持 .md 的编辑器，或者文件关联错误。

**解决方法**：
1. 安装 Typora、VS Code 或 Obsidian 等软件
2. 右键 .md 文件 → 打开方式 → 选择对应软件
3. 勾选"始终使用此应用打开"

---

### 问题2：图片显示不出来
**原因**：图片路径写错了，或者图片文件被移动/删除了。

**解决方法**：
1. 检查图片路径是否正确（相对路径 vs 绝对路径）
2. 推荐使用相对路径，把图片放在和 .md 文件同一个文件夹或子文件夹里
3. 路径中有中文或空格时，用 `<>` 包裹：`![图片](./图片%20名称.png)`
4. 使用图床（如 PicGo + GitHub/SM.MS）存网络图片，用 URL 引用

---

### 问题3：不同软件渲染效果不一样
**原因**：Markdown 有很多扩展语法（GFM、CommonMark 等），不同软件支持程度不同。

**解决方法**：
1. 尽量使用标准 Markdown 语法（标题、列表、加粗、链接等基础语法都是通用的）
2. 表格、任务列表等高级语法，导出前先预览确认
3. 如果要发布到特定平台（如知乎、公众号），先用该平台的编辑器预览
4. 推荐使用 **Pandoc** 作为统一转换工具，兼容性最好

---

### 问题4：表格排版错乱
**原因**：Markdown 表格语法对对齐有严格要求，或者中文全角字符导致宽度计算错误。

**解决方法**：
1. 确保表格分隔线（`---`）数量正确，每列至少有 3 个短横线
2. 对齐冒号要写对：`:---` 左对齐，`:---:` 居中，`---:` 右对齐
3. 使用 VS Code 的 Markdown All in One 插件自动格式化表格
4. 复杂表格建议用 HTML 的 `<table>` 标签写

---
## 💡 小知识

Markdown 的设计哲学是"可读性优先"。即使不用任何渲染工具，直接用记事本打开 .md 文件，你也能看懂大概意思——标题前面有 `#` 号，加粗文字两边有 `**` 号，就像人们在纯文本时代自然而然形成的"暗号"一样。Markdown 把这些"民间约定"整理成了一套正式规范。

## 🔗 相关链接

- [Markdown 官方教程](https://www.markdownguide.org/)
- [Typora 官网](https://typora.io/)
- [Obsidian 官网](https://obsidian.md/)
- [Pandoc 万能文档转换工具](https://pandoc.org/)
- [Markdown 语法速查表](https://github.com/ruanyf/document-style-guide/blob/master/markdown.md)

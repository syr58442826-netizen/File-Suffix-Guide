# .tex 文件后缀详解

## 1. 文件定义 & 用途

TEX 是 **LaTeX 排版源文件**，是一种"用写代码的方式来排版文档"的格式。你不用鼠标拖拽调格式，而是用命令描述"这里是一个公式""这是一段引用"，然后由 LaTeX 引擎编译成漂亮的 PDF。它是学术界，尤其是数学、物理、计算机领域论文排版的绝对主力。

- **全称**：TeX / LaTeX source（.tex 是源代码文件）
- **类型**：标记语言源文件（需编译生成 PDF）
- **开发者**：Donald Knuth（TeX，1978 年）；Leslie Lamport（LaTeX 宏包，1984 年）
- **特点**：公式排版无敌、自动处理参考文献和交叉引用、版本可控（纯文本）、输出质量极高
- **本质**：纯文本文件，里面是 LaTeX 命令，编译后生成 PDF/DVI

写 LaTeX 就像写代码：源文件是 .tex，"运行"它得到的是排版精美的 PDF。它的公式排版质量至今没有软件能超越，所以理工科学术圈离不开它。

## 2. 适用场景

- **学术论文写作**：数学、物理、计算机、工程领域的论文标配
- **书籍/教材排版**：尤其是含大量公式的学术著作
- **简历/报告**：追求极致排版质量的个人简历、技术报告
- **公式/化学方程式**：在网页、PPT 中插入复杂公式（LaTeX 语法已成通用标准）
- **Beamer 演示文稿**：用 LaTeX 做学术风格的幻灯片
- **学位论文**：很多高校研究生论文模板就是 LaTeX 写的

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | TeXstudio、TeXworks、VS Code + LaTeX Workshop 插件 | WinEdt（付费）、Tectonic |
| Mac | TeXShop（MacTeX 自带）、VS Code + 插件、TeXstudio | Texpad（付费） |
| Linux | TeXstudio、Kile、Emacs + AUCTeX、VS Code + 插件 | - |

**新手推荐**：
- 一站式安装：**MacTeX**（Mac）/ **TeX Live**（Windows/Linux），装完自带编辑器和编译器
- 在线零安装：**Overleaf**（网页版 LaTeX，浏览器里写论文，免配置，强烈推荐新手）
- 编辑器选择：**TeXstudio**（专门写 LaTeX，补全好用）或 **VS Code**（配 LaTeX Workshop 插件）

## 4. 如何编辑、如何导出

### 如何编辑
1. **本地编辑**：安装 TeX Live/MacTeX → 用 TeXstudio/VS Code 打开 .tex 文件编辑
2. **在线编辑**：注册 Overleaf，上传 .tex 文件，在线编辑实时预览，零配置
3. **基本结构**：.tex 文件以 `\documentclass{}` 开头，正文在 `\begin{document}` 和 `\end{document}` 之间

### 如何导出/转换
- **编译生成 PDF**：在编辑器中点"编译/Build"，或命令行 `pdflatex main.tex`（公式多的用 `xelatex` 支持中文更好）
- **生成 PDF（含中文）**：用 `xelatex` 命令，配合 `ctex` 宏包
- **转成 Word**：用 `pandoc main.tex -o output.docx`（公式转成 OMML）
- **转成 HTML**：`pandoc main.tex -o output.html` 或用 make4ht
- **实时预览**：Overleaf 自动编译，本地用 LaTeX Workshop 的"实时预览"功能

## 5. 常见报错与解决

### 问题1：编译报错 "Undefined control sequence"（未定义命令）
**原因**：用了某个命令但忘了在开头 `\usepackage{}` 引入对应的宏包，或命令拼写错误。

**解决方法**：
1. 看报错信息里指向的行号，检查那个命令是否拼写正确
2. 确认是否引入了对应宏包（如用 `\includegraphics` 需要 `\usepackage{graphicx}`）
3. 善用编辑器的命令补全功能，减少拼写错误
4. 把报错信息复制到搜索引擎，LaTeX 社区（如 TeX StackExchange）几乎覆盖所有常见错误

### 问题2：中文显示不出来，变成方块或编译报错
**原因**：默认的 pdflatex 引擎对中文支持差，需要用支持 Unicode 的引擎和中文宏包。

**解决方法**：
1. 改用 **xelatex** 引擎编译（命令：`xelatex main.tex`），它原生支持 Unicode
2. 在导言区加入 `\usepackage{ctex}`（ctex 宏包专门处理中文）
3. 或直接用 `\documentclass{ctexart}` 作为文档类
4. 编辑器里把默认编译器从 pdflatex 改成 xelatex
5. 最省心：用 Overleaf，选"XeLaTeX"编译器，勾选中文支持

### 问题3：参考文献编号变成问号 [?]
**原因**：LaTeX 的参考文献需要多次编译，或缺少 .bibtex/.biber 编译步骤。

**解决方法**：
1. 完整编译流程是：`pdflatex → bibtex → pdflatex → pdflatex`（编译两遍才能解析交叉引用）
2. 用 `latexmk` 工具一键完成全流程：`latexmk -pdf main.tex`
3. 现代编辑器（TeXstudio/Overleaf）通常有"一键编译"会自动处理多遍编译
4. 检查 .bib 文件路径和 `\bibliography{}` 引用的文件名是否一致

### 问题4：公式太长溢出页面，或对齐错乱
**原因**：长公式未使用合适的环境换行，或矩阵/分式结构超出版心。

**解决方法**：
1. 长公式用 `align` 或 `multline` 环境换行对齐
2. 过宽公式用 `\resizebox{}{}{}` 或 `\scalebox{}{}` 缩放
3. 矩阵太大用 `smallmatrix` 或调整 `\arraycolsep` 列间距
4. 参考数学模式排版技巧，如 `\displaystyle` 控制分式大小

---
## 💡 小知识

TeX 的发明人 Donald Knuth 是计算机科学界的传奇。他在写巨著《计算机程序设计艺术》时，对出版社的排版质量极其不满——尤其是数学公式排得又丑又乱。一怒之下，他决定自己开发一套排版系统，这就是 TeX（1978 年）。他甚至暂停了写书，专心搞了十年排版。Knuth 为 TeX 设定了版本号趋近于 π（3.14159...），每次更新往后加一位小数。LaTeX 则是 Leslie Lamport 在 TeX 基础上封装的"宏包"，让普通人也能用上 TeX 的强大能力。今天，几乎所有顶刊的数学论文都是 LaTeX 排版的，Knuth 的一时"较真"改变了整个学术界的写作方式。

## 🔗 相关链接

- [Overleaf 在线 LaTeX 编辑器](https://www.overleaf.com/)
- [TeX Live 下载](https://www.tug.org/texlive/)
- [MacTeX 下载](https://www.tug.org/mactex/)
- [TeXstudio 下载](https://www.texstudio.org/)
- [TeX StackExchange 问答社区](https://tex.stackexchange.com/)
- [LearnLaTeX.org 中文教程](https://learnlatex.org/zh/)

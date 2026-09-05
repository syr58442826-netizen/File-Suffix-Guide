# .nb 文件后缀详解

## 1. 文件定义 & 用途

NB（Notebook，笔记本）文件是 Wolfram Mathematica 的交互式笔记本文件格式。Mathematica 是一款强大的科学计算软件，支持符号计算、数值计算、可视化、编程等多种功能。.nb 文件是 Mathematica 的核心文档格式，它把代码、输出结果、图形、文本、公式、交互控件等混合在一起，形成一个"活的"计算文档。

NB 文件的核心特点：
- **交互式笔记本**：代码、结果、文本、图形混合排列
- **即时计算**：输入公式或代码，按 Shift+Enter 立即得到结果
- **符号计算强大**：擅长代数、微积分、方程求解等符号运算
- **可视化丰富**：内置强大的 2D/3D 绘图功能
- **格式美观**：支持排版级别的数学公式显示
- **Wolfram 语言**：使用 Wolfram 语言（一种函数式编程语言）

## 2. 适用场景

- **数学研究**：符号推导、公式验证、定理证明
- **物理/工程计算**：物理建模、工程仿真、数值计算
- **数据分析**：数据处理、统计分析、可视化展示
- **教学与学习**：大学数学/物理课程的交互式教学
- **科研报告**：把计算过程和结果整合到一份文档中
- **编程学习**：学习 Wolfram 语言和函数式编程

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Wolfram Player、Wolfram Engine（开发者免费） | Wolfram Mathematica |
| Mac | Wolfram Player、Wolfram Engine | Wolfram Mathematica |
| Linux | Wolfram Player、Wolfram Engine | Wolfram Mathematica |
| 在线 | Wolfram Cloud、Wolfram Alpha Pro | - |

**新手推荐：**
- **完整功能**：Wolfram Mathematica（付费）
- **免费查看**：Wolfram Player（免费，可查看和交互，但不能编辑）
- **云端使用**：Wolfram Cloud（有免费额度）

## 4. 如何编辑、如何导出

### NB 文件的基本结构

一个 Mathematica 笔记本由多个"单元"（Cell）组成：
- **输入单元**：代码（以 `In[n]:=` 标记）
- **输出单元**：计算结果（以 `Out[n]=` 标记）
- **文本单元**：说明文字、标题等
- **节/小节**：组织结构的标题单元

示例：
```
（标题单元）我的第一个 Mathematica 笔记本

（文本单元）下面计算 1+1：

（输入单元）In[1]:= 1 + 1

（输出单元）Out[1]= 2

（文本单元）再画一个函数图像：

（输入单元）In[2]:= Plot[Sin[x], {x, 0, 2 Pi}]

（输出单元）[显示一个正弦函数图像]
```

### 基本操作

**运行代码：**
- 在输入单元中输入代码（如 `1 + 1`）
- 按 `Shift + Enter` 运行
- 自动生成输出单元

**常用计算示例：**
```mathematica
(* 注释：用 (* 和 *) 包裹 *)

(* 基本算术 *)
2 + 3 * 4
10!                  (* 阶乘 *)

(* 符号计算 *)
Integrate[x^2, x]    (* 积分 ∫x²dx *)
D[Sin[x], x]         (* 求导 d/dx sin(x) *)
Solve[x^2 - 5x + 6 == 0, x]   (* 解方程 *)

(* 矩阵运算 *)
{{1, 2}, {3, 4}} // MatrixForm
Inverse[{{1, 2}, {3, 4}}]     (* 矩阵求逆 *)

(* 绘图 *)
Plot[Sin[x], {x, 0, 10}]      (* 2D 图 *)
Plot3D[Sin[x] Cos[y], {x, 0, Pi}, {y, 0, Pi}]  (* 3D 图 *)

(* 数据分析 *)
data = {1, 4, 9, 16, 25};
Mean[data]
Total[data]
ListPlot[data]
```

### 如何导出为其他格式

**导出为 PDF：**
1. 文件 → 另存为 → PDF
2. 或用代码：`Export["output.pdf", 笔记本对象]`

**导出为 HTML：**
1. 文件 → 另存为 → HTML
2. 适合网页分享

**导出为图片：**
```mathematica
(* 导出单个图形 *)
graph = Plot[Sin[x], {x, 0, 2 Pi}];
Export["sin_plot.png", graph];

(* 导出为 SVG 矢量图 *)
Export["sin_plot.svg", graph];
```

**导出为 Wolfram 脚本（.wls）：**
1. 文件 → 另存为 → Wolfram 语言脚本 (.wls)
2. 只保留代码，不含输出和文本

### Wolfram Player 查看 NB 文件

如果只是想查看和交互，不需要完整的 Mathematica：
1. 下载安装 Wolfram Player（免费）
2. 直接双击 .nb 文件即可打开
3. 可以运行代码、与交互控件互动
4. 但不能编辑和保存修改

## 5. 常见报错与解决

### 问题 1：.nb 文件打不开，提示需要 Mathematica

**原因：** 没有安装 Mathematica 或 Wolfram Player。

**解决方法：**
1. 下载安装 Wolfram Player（免费，可查看和运行）
2. 或使用 Wolfram Cloud（在线版，有免费额度）
3. 如果需要编辑，需要安装完整的 Mathematica
4. 学生和教师通常可以通过学校获得免费或优惠的 Mathematica 许可证

### 问题 2：代码运行很慢或卡住

**原因：** 计算量太大，或代码写得不够高效。

**解决方法：**
1. 简化计算，先用小规模数据测试
2. 用 `N[]` 做数值计算（比符号计算快得多）
3. 避免不必要的符号运算
4. 查看内存使用情况（任务管理器/活动监视器）
5. 对于大型计算，考虑用更专业的数值方法

### 问题 3：输出的公式显示不正常

**原因：** 字体缺失或渲染设置问题。

**解决方法：**
1. 确保安装了 Mathematica 的字体包
2. 在偏好设置中调整字体渲染选项
3. 导出为 PDF 后查看，PDF 的公式渲染通常更准确
4. 在线版本（Wolfram Cloud）的渲染效果更好

### 问题 4：Mathematica 和 MATLAB 选哪个？

**解答：** 两者各有擅长，取决于你的需求：
- **符号计算强**：选 Mathematica（公式推导、符号积分、代数化简是它的强项）
- **数值计算/工程**：选 MATLAB（矩阵运算、信号处理、控制系统更成熟）
- **交互式文档**：Mathematica 的笔记本更漂亮、功能更强
- **行业生态**：工程界 MATLAB 用户多，数学/物理界 Mathematica 用户多
- **价格**：都不便宜，学生都有优惠或免费版
- **很多人两个都用，各取所长**

---

## 💡 小知识

Mathematica 的创始人是 Stephen Wolfram（史蒂芬·沃尔夫勒姆），一位传奇的物理学家和计算机科学家。他 15 岁发表第一篇物理论文，20 岁拿到加州理工学院的博士学位，22 岁就成了物理学教授。

但 Stephen Wolfram 最广为人知的成就，是 1988 年发布的 Mathematica 软件。Mathematica 第一次让人们看到——数学计算也可以是"可视化"和"交互式"的。你输入一个积分公式，它就能给你算出结果；你输入一个函数，它就能画出漂亮的图形。在那个年代，这简直像是魔法。

Mathematica 的笔记本（Notebook）设计更是革命性的。在传统的编程环境里，代码和输出是分开的——你写一段代码，运行后结果出现在另一个窗口里。但 Mathematica 的笔记本把代码、输出、图形、文字混合在一起，就像一本"会计算的笔记本"。你可以在公式旁边写注释，在图形下面写分析，整个文档既是程序又是报告。

这种"计算文档"的理念后来影响了很多产品——Jupyter Notebook（Python 的交互式笔记本）就深受 Mathematica 的启发。不过 Mathematica 的笔记本更强大，因为它不仅能跑代码，还能做符号计算、排版级别的公式显示、交互式控件等等。

有趣的是，Stephen Wolfram 后来还搞了一个更宏大的项目——Wolfram Alpha，一个"计算知识引擎"。你问它任何问题（数学的、物理的、历史的、地理的……），它都能给你计算出答案。而 Wolfram Alpha 的底层，用的就是 Mathematica 的技术。

## 🔗 相关链接

- [Wolfram Mathematica 官方网站](https://www.wolfram.com/mathematica/)
- [Wolfram Player 下载](https://www.wolfram.com/player/)
- [Wolfram Cloud（在线版）](https://www.wolframcloud.com/)
- [Wolfram 语言文档](https://reference.wolfram.com/language/)
- [.m MATLAB 脚本详解](./m.md)
- [.py Python 脚本详解](../06-编程源代码文件/py.md)

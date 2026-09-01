# .r 文件后缀详解

## 1. 文件定义 & 用途

.r 是 **R 语言**的源代码文件后缀。R 是一门专为统计计算和数据可视化设计的编程语言，在学术研究、数据科学、生物信息学等领域广泛使用。

简单来说，.r 文件里写的是统计分析和画图代码，运行后可以处理数据、做统计检验、画出漂亮的图表。R 语言拥有全球最丰富的统计包生态（CRAN 上有近两万个扩展包）。

**主要用途：**
- 统计分析与假设检验
- 数据可视化（ggplot2 是业界标杆）
- 机器学习与数据挖掘
- 生物信息学与基因数据分析
- 金融量化分析与风险建模
- 学术研究报告与可重复性研究

## 2. 适用场景

- 数据分析和统计建模
- 科研论文中的数据分析和图表制作
- 生成可重复的研究报告
- 数据探索与可视化
- 金融和生物医学数据分析

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [RStudio Desktop](https://posit.co/download/rstudio-desktop/)（免费版）、[VS Code](https://code.visualstudio.com/) + R 扩展 | RStudio Pro（付费版）、Sublime Text |
| Mac | [RStudio Desktop](https://posit.co/download/rstudio-desktop/)、[VS Code](https://code.visualstudio.com/) + R 扩展 | RStudio Pro |
| Linux | [RStudio Desktop](https://posit.co/download/rstudio-desktop/)、[VS Code](https://code.visualstudio.com/) + R 扩展、Vim | RStudio Pro |

**新手推荐：** RStudio Desktop（免费版）是 R 语言的标准 IDE，几乎每个 R 用户都用它。安装时先装 R 语言本体，再装 RStudio。

## 4. 如何编辑、如何导出

### 环境准备

**安装 R 语言本体：**
1. 去 [CRAN 官网](https://cran.r-project.org/) 下载对应平台安装包
2. Windows/Mac 直接运行安装程序
3. Linux：`sudo apt install r-base`（Debian/Ubuntu）

验证安装：
```bash
R --version
```

**安装 RStudio（推荐）：**
去 [RStudio 官网](https://posit.co/download/rstudio-desktop/) 下载 Desktop 免费版安装。

### 如何编辑

**一个简单的 R 示例：**
```r
# hello.R
# R 中注释用井号
greet <- function(name) {
  return(paste("你好，", name, "！", sep = ""))
}

print(greet("小明"))

# 数据分析示例
# 创建一个数据框
data <- data.frame(
  name = c("张三", "李四", "王五"),
  score = c(85, 92, 78)
)

# 计算平均分
mean_score <- mean(data$score)
print(paste("平均分：", mean_score))

# 画一个简单的图
plot(data$score, type = "b", col = "blue",
     main = "成绩图", xlab = "学生", ylab = "分数")
```

注意：R 用 `<-` 赋值（也可以用 `=`），函数调用用圆括号，数据框用 `$` 访问列。

### 如何运行

**方法一：RStudio 中运行（最常用）**
1. 打开 .r 文件
2. 选中代码按 Ctrl+Enter（Mac: Cmd+Enter）逐行运行
3. 或点 Source 按钮运行整个文件

**方法二：命令行运行**
```bash
# 在终端直接运行脚本
Rscript hello.R

# 或进入 R 交互环境
R
> source("hello.R")
> q()  # 退出
```

### 如何导出

**导出图表：**
```r
# 导出为 PNG 图片
png("plot.png", width = 800, height = 600)
plot(data$score)
dev.off()

# 导出为 PDF
pdf("plot.pdf")
plot(data$score)
dev.off()
```

**导出分析报告（R Markdown，推荐）：**
```r
# 安装 rmarkdown 包
install.packages("rmarkdown")

# 在 RStudio 中新建 R Markdown 文件
# 可以导出为 HTML、PDF、Word 报告
# 将代码、结果、图表、文字说明整合在一起
```

## 5. 常见报错与解决

### 问题1：报错 "there is no package called 'xxx'"

**原因：** 使用了未安装的 R 包。

**解决方法：**
```r
# 安装缺失的包
install.packages("ggplot2")

# 国内用户建议先设置镜像源加速
options(repos = c(CRAN = "https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
install.packages("ggplot2")

# 安装后加载使用
library(ggplot2)
```

### 问题2：报错 "could not find function 'xxx'"

**原因：** 函数不存在，通常是因为忘了加载包，或函数名拼写错误。

**解决方法：**
1. 检查函数名拼写
2. 确认函数所属的包已用 `library()` 加载
3. 如果是某个包的函数，用 `包名::函数名()` 方式调用：
```r
# 明确指定来自哪个包
dplyr::filter(data, score > 80)
```
4. 如果是自定义函数，确认已 `source()` 加载或已定义

### 问题3：安装包时报错 "installation of package had non-zero exit status"（编译失败）

**原因：** 某些 R 包包含 C/C++ 代码，需要编译器，或缺少系统依赖库。

**解决方法：**
1. Windows：安装 [Rtools](https://cran.r-project.org/bin/windows/Rtools/) 编译工具链
2. Mac：安装 Xcode Command Line Tools：`xcode-select --install`
3. Linux：安装编译工具：`sudo apt install build-essential libcurl4-openssl-dev libssl-dev`
4. 尝试安装预编译版本（binary）：
```r
# 优先安装 binary 版本（不需要编译）
install.packages("xxx", type = "binary")
```

### 问题4：报错 "object 'xxx' not found"

**原因：** 使用了未定义的变量或函数，可能是变量名拼错或没运行定义该变量的代码。

**解决方法：**
1. 检查变量名拼写
2. 在 RStudio 中确认代码已逐行运行（选中代码按 Ctrl+Enter）
3. 用 `ls()` 查看当前环境中有哪些变量
4. 检查是否在函数内部用了局部变量但在外部访问

---

## 💡 小知识

- R 语言由新西兰奥克兰大学的 Ross Ihaka 和 Robert Gentleman 开发，名字来源于两位创始人名字的首字母
- R 是 S 语言的实现，S 语言由贝尔实验室开发
- CRAN（Comprehensive R Archive Network）上有近 2 万个统计相关扩展包
- ggplot2 是 R 最著名的可视化包，基于"图形语法"理论，同一个图表可以用层层叠加的方式构建
- R 在学术界（尤其生物医学和统计学）使用率极高，但工业界更多用 Python

## 🔗 相关链接

- [R 语言官网](https://www.r-project.org/)
- [CRAN 包仓库](https://cran.r-project.org/)
- [RStudio 官网](https://posit.co/)
- [R 语言教程（菜鸟教程）](https://www.runoob.com/r/r-tutorial.html)
- [ggplot2 文档](https://ggplot2.tidyverse.org/)
- [R Markdown 官网](https://rmarkdown.rstudio.com/)

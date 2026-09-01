# .djvu 文件后缀详解

## 1. 文件定义 & 用途

DjVu（发音类似"黛雅-武"）是一种专为**扫描文档和图片密集型内容**设计的高压缩比文档格式。它最大的本事是：能把一整本扫描的图书压到非常小，同时保持文字清晰可读。

- **全称**：DjVu（源自法语 déjà vu，"既视感"）
- **类型**：高压缩比扫描文档格式
- **开发者**：AT&T 实验室（1996 年）
- **特点**：压缩率极高、分图层存储（文字层+背景层）、支持 OCR 文字层、可在网页流式浏览
- **对比 PDF**：扫描图书时，DjVu 的体积通常只有 PDF 的 1/5 到 1/10

DjVu 的核心技术是**分层压缩**：把页面的文字部分和背景/图片部分分开处理——文字用高分辨率保证清晰，背景用低分辨率压缩体积，两者叠加在一起就是一张既清晰又小巧的页面。

## 2. 适用场景

- **图书/古籍数字化**：图书馆、档案馆大批量扫描藏书
- **扫描文档存档**：合同、票据、说明书等纸质文件电子化
- **漫画/绘本电子版**：图片密集但体积要求小
- **学术资料分享**：论文、期刊扫描件网络传播
- **网页在线浏览**：DjVu 支持流式加载，适合网页逐页查看

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | DjView、WinDjView、SumatraPDF、STDU Viewer | Document Express Editor |
| Mac | DjView、MacDjView、Preview（部分版本） | Document Express Editor |
| Linux | DjView4、Evince（部分版本）、Okular | djvulibre 命令行工具 |

**新手推荐**：
- Windows 用户：**WinDjView** 是最经典的轻量阅读器，打开即用
- 跨平台免费首选：**DjView**（基于 djvulibre，三大系统都有）
- 也想看 PDF：**SumatraPDF** 同时支持 DjVu 和 PDF，一个软件搞定

## 4. 如何编辑、如何导出

### 如何编辑
DjVu 本质是版式固定的扫描文档，编辑能力有限，常见操作如下：

1. **添加注释/书签**：用 DjView 或 WinDjView 添加标注、书签
2. **OCR 识别文字**：DjVu 可以内嵌 OCR 文字层，用 DjVuLibre 的 `djvutoch` 命令或 Document Express 添加
3. **页面增删/合并**：用 djvulibre 命令行工具（`djvm` 命令）合并、删除页面
4. **内容修改**：DjVu 不适合直接改文字，建议转成 PDF 或 OCR 后用 Word 编辑

### 如何导出/转换
- **转成 PDF**：用 Document Express、doPDF 或在线工具（如 djvu-pdf.com）转换；命令行可用 `ddjvu -format=pdf input.djvu output.pdf`
- **转成图片**：用 `ddjvu -format=tiff` 或 DjView 导出为 PNG/JPG
- **提取文字**：如果 DjVu 已含 OCR 层，可直接复制；否则需先 OCR 识别
- **扫描生成 DjVu**：用 Document Express Desktop 或 ScanTailor 扫描后导出为 DjVu

## 5. 常见报错与解决

### 问题1：DjVu 文件在 Windows 上双击没反应
**原因**：系统没有关联 .djvu 文件，或未安装任何 DjVu 阅读器。

**解决方法**：
1. 安装 **WinDjView** 或 **SumatraPDF**（免费轻量）
2. 安装后右键 .djvu 文件 → 打开方式 → 选择 WinDjView，并勾选"始终使用此应用"
3. 如果已安装仍打不开，检查文件是否下载完整（正常 DjVu 至少几百 KB 起）

### 问题2：DjVu 打开后文字看不清，发虚模糊
**原因**：扫描分辨率本身偏低，或阅读器缩放后渲染质量差。

**解决方法**：
1. 用 DjView 调整渲染模式，开启"放大后重采样"选项
2. 放大查看（DjVu 的文字层是高分辨率，放大后文字反而更清晰）
3. 如果是低分辨率扫描件，本身清晰度有限，可转成 PDF 后用锐化滤镜处理
4. 文字实在看不清，用 OCR 工具提取纯文字阅读

### 问题3：想把 DjVu 转成 PDF 但格式变乱/体积变大
**原因**：转换工具未正确处理 DjVu 的分层结构，或用了位图方式逐页转换。

**解决方法**：
1. 推荐用 **ddjvu 命令行**转换：`ddjvu -format=pdf -quality=85 input.djvu output.pdf`，能较好保留矢量文字层
2. 用 Document Express Professional 导出 PDF，保留可搜索文字层
3. 在线转换工具（如 AnyConv、Zamzar）适合小文件，注意隐私
4. 如果只转一两页，可以在 DjView 中逐页导出为图片再合成 PDF

---
## 💡 小知识

DjVu 这个名字来自法语"déjà vu"（既视感），意思是"似曾相识"——暗示你在屏幕上看到的扫描页面，就像真书一样熟悉。它在 1996 年由 AT&T 实验室开发，当年号称"能在 56K 拨号上网时代流畅浏览整本扫描图书"。虽然今天 PDF 一统天下，但在图书馆数字化领域，DjVu 仍是体积和清晰度平衡得最好的格式之一。遗憾的是，由于推广不力和浏览器原生支持不足，DjVu 始终没能走进大众视野。

## 🔗 相关链接

- [DjVuLibre 官方网站](http://djvu.sourceforge.net/)
- [WinDjView 下载](https://windjview.sourceforge.io/)
- [SumatraPDF（支持 DjVu）](https://sumatraproject.org/)
- [.pdf 文件后缀详解](../01-日常办公文档类/pdf.md)

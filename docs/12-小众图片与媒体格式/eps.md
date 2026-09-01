# .eps 文件后缀详解

## 1. 文件定义 & 用途

EPS 是 **封装 PostScript**（Encapsulated PostScript）的缩写，是一种**矢量图形格式**，常用于印刷出版领域。它基于 Adobe 的 PostScript 页面描述语言，可以无损放大缩小，是早期专业印刷和矢量设计的标准格式。

- **全称**：Encapsulated PostScript
- **类型**：矢量图形格式（可含位图预览）
- **开发者**：Adobe Systems
- **发布年份**：1980 年代末
- **特点**：矢量无损缩放、支持 CMYK 印刷色彩、含位图预览头、PostScript 描述
- **现状**：在新版 Illustrator 中已被 PDF/AI 逐步取代，但仍被广泛支持

EPS 文件通常包含两部分：一个低分辨率位图预览（用于在软件里快速显示）+ PostScript 矢量描述（用于打印输出高精度）。

## 2. 适用场景

- **印刷出版**：logo、插图等矢量元素送印
- **矢量素材分发**：矢量素材库、品牌 logo 的标准格式
- **跨软件矢量交换**：Illustrator、CorelDRAW、InDesign 之间传矢量图
- **CMYK 印刷工作流**：需要四色印刷的矢量图
- **老项目兼容**：老版设计文件、印刷厂老流程

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Inkscape（免费矢量编辑）、IrfanView（仅预览）、Ghostscript + GSview | Adobe Illustrator、CorelDRAW、Affinity Designer |
| Mac | Inkscape、预览（部分） | Adobe Illustrator、Affinity Designer、CorelDRAW |
| Linux | Inkscape、Ghostscript | - |

**新手推荐**：
- 矢量编辑免费首选：**Inkscape**（开源，可导入 EPS 编辑）
- 行业标准：**Adobe Illustrator**（EPS 的原生支持最好）
- 仅查看：装 **Ghostscript + GSview** 或用 IrfanView（需 Ghostscript 支持）
- 印刷厂对接：Illustrator 是标配

## 4. 如何编辑、如何导出

### 如何编辑
1. **Adobe Illustrator**：原生支持 EPS 完整编辑，打开后可修改矢量路径
2. **CorelDRAW**：可导入编辑 EPS（部分复杂 EPS 可能有兼容问题）
3. **Inkscape**：需装 Ghostscript 才能导入 EPS；导入后可编辑，但部分效果可能丢失
4. **Affinity Designer**：可打开编辑 EPS

### 如何导出/转换
- **Illustrator 导出 EPS**：文件 → 另存为 → EPS，设置版本、预览格式、是否含字体
- **转 SVG**：Inkscape/Illustrator 另存为 SVG（现代矢量通用格式）
- **转 PDF**：Illustrator 另存为 PDF，现代印刷更推荐 PDF
- **转 PNG/JPG**：用 Illustrator/Inkscape 导出位图，设置高分辨率
- **批量转换**：ImageMagick（`magick input.eps output.png`，需 Ghostscript）

## 5. 常见报错与解决

### 问题1：EPS 文件在 Photoshop 里打开变成位图，不能编辑矢量
**原因**：Photoshop 是位图软件，打开 EPS 会栅格化成位图；只有矢量软件（Illustrator/Inkscape）能保持矢量可编辑。

**解决方法**：
1. 要编辑矢量：用 **Illustrator** 或 **Inkscape** 打开
2. Photoshop 里可用"置入"（Place）将 EPS 作为智能对象，缩放不损画质，但仍非矢量编辑
3. 导出位图时设高分辨率（300 DPI 以上）保证印刷清晰度
4. 长期方案：把矢量工作迁移到 SVG 或 AI 格式

### 问题2：EPS 打开后字体变成了默认字体或乱码
**原因**：EPS 文件未嵌入字体，而打开的电脑没装原文件使用的字体。

**解决方法**：
1. 打开 EPS 时选"嵌入字体"选项（Illustrator 导出 EPS 勾选"包含字体"）
2. 在目标电脑安装原字体后再打开
3. 文字转曲：在 Illustrator 中"轮廓化"文字（变矢量路径），不再依赖字体，但失去可编辑性
4. 改用 PDF 格式（PDF 嵌入字体更完善）

### 问题3：Inkscape 打不开 EPS，提示需要 Ghostscript
**原因**：Inkscape 本身不能直接解析 PostScript，依赖 Ghostscript 做转换。

**解决方法**：
1. 安装 **Ghostscript**（免费）：从 ghostscript.com 下载安装
2. 配置 Inkscape 找到 Ghostscript 路径（Inkscape 设置 → 系统 → Ghostscript 路径）
3. 重启 Inkscape 后即可导入 EPS
4. 或先用 Ghostscript 命令行转 PDF：`gswin64c -dEPSCrop -sDEVICE=pdfwrite -o out.pdf in.eps`，再用 Inkscape 打开 PDF

### 问题4：EPS 文件体积很大，发邮件被拒
**原因**：EPS 可能内嵌了高分辨率位图预览或字体，体积膨胀。

**解决方法**：
1. 另存时取消"包含文档缩略图"，用低分辨率预览
2. 改存为 PDF 或 SVG，体积通常更小
3. 用压缩软件（7-Zip）压缩后再发送
4. 文件分享用网盘链接代替邮件附件

---
## 💡 小知识

EPS 是 PostScript 时代的产物。PostScript 是 Adobe 1984 年推出的页面描述语言，当年激光打印机的"通用语言"。EPS 把单页矢量图形封装成可嵌入文档的独立单元，很快成为印刷出版业的矢量交换标准。但 EPS 也有时代局限：它本质是打印指令而非现代文件格式，不支持透明度、渐变网格等现代效果，且文件头里塞位图预览让结构臃肿。Adobe 自己也意识到这点，从 2000 年代起就力推 PDF 和 AI 格式取代 EPS。Illustrator 9 之后甚至默认用 PDF 兼容的 AI 格式。但印刷行业惯性大，至今很多印刷厂仍要 EPS，所以它"死而不僵"。新项目建议用 PDF 或 SVG，但遇到 EPS 也得会处理。

## 🔗 相关链接

- [Inkscape 官网](https://inkscape.org/)
- [Ghostscript 官网](https://www.ghostscript.com/)
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html)
- [.ai 文件后缀详解](../02-图片与设计文件类/ai.md)
- [.pdf 文件后缀详解](../01-日常办公文档类/pdf.md)

# .tif / .tiff 文件后缀详解

## 1. 文件定义 & 用途

TIFF（也写作 TIF）是 **标签图像文件格式**（Tagged Image File Format）的缩写，是一种高质量的位图格式。它支持无损压缩，能保留最多的图像细节，是专业摄影、印刷出版、医学影像等领域的标准格式。

- **全称**：Tagged Image File Format
- **类型**：位图图片（支持多种压缩方式和位深）
- **开发者**：Aldus 公司（后被 Adobe 收购）
- **发布年份**：1986年
- **特点**：高质量、支持无损压缩、支持多页、支持多种位深、印刷行业标准
- **支持**：1位黑白、8位灰度、24位真彩色、32位CMYK、48位深等多种格式

## 2. 适用场景

- 专业摄影（摄影师保存高质量原片）
- 印刷出版（杂志、画册、海报的印刷输出）
- 医学影像（CT、X光片的存储）
- 扫描存档（高质量文档扫描）
- 传真和文档管理
- 多页文档（一个 TIFF 文件可以包含多张图片）
- GIS 地理信息和卫星图像

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 照片（系统自带）、画图、IrfanView、XnView MP | Adobe Photoshop、Lightroom、ACDSee、Corel PaintShop Pro |
| Mac | 预览（系统自带）、照片 App | Adobe Photoshop、Lightroom、Pixelmator Pro、Affinity Photo |
| Linux | GIMP、Gwenview、Shotwell、Eye of GNOME | GIMP、darktable、Krita |

**新手推荐**：
- 日常查看：系统自带的照片/预览 App 就够了
- 专业处理：**Adobe Photoshop** 或 **Lightroom**
- 免费替代：**GIMP**（开源免费，支持 TIFF）
- 摄影后期：**Lightroom Classic**（摄影师首选）
- 看图管理：**XnView MP** 或 **ACDSee**（支持批量查看和管理）

## 4. 如何编辑、如何导出

### 如何编辑
1. 用 Photoshop 或其他专业软件打开 TIFF 文件
2. 进行调色、修图等操作
3. 保存时可选择压缩方式（无压缩、LZW 无损压缩、ZIP 压缩等）

### 如何导出/转换
- **转成 JPG**：
  - Photoshop：文件 → 存储为 → JPEG
  - 批量转换：用 Lightroom 或 XnView MP 批量导出
- **转成 PNG**：另存为 PNG 格式
- **转成 PDF**：
  - 多页 TIFF 可以合并成一个 PDF
  - 用 Photoshop 或 Acrobat 转换
- **JPG 转 TIFF**：打开后另存为 TIFF（但不会增加画质，只是格式变了）
- **RAW 转 TIFF**：用 Lightroom/Capture One 导出为 TIFF（保留最多细节）
- **多页 TIFF**：
  - 制作：用 Photoshop 的"文件 → 自动 → PDF 演示文稿"再转 TIFF
  - 拆分：用 IrfanView 或 XnView 拆分成单张图片
- **压缩 TIFF**：
  - LZW 压缩：无损压缩，体积小 30-50%，兼容性好
  - ZIP 压缩：无损压缩，效果更好但兼容性稍差
  - JPEG 压缩：有损压缩，体积最小但损失画质

## 5. 常见报错与解决

### 问题1：TIFF 文件太大，占用空间多
**原因**：TIFF 通常是无损或无压缩的，一张高质量照片可能有几十 MB 甚至上百 MB。

**解决方法**：
1. 使用 LZW 无损压缩：保存时选择 LZW 压缩，体积减小一半左右，画质完全无损
2. 如果是照片分享，转成 JPG 格式（体积小 10 倍以上）
3. 降低位深：从 16 位/通道降到 8 位/通道（普通使用 8 位足够）
4. 降低分辨率：如果不是印刷用，72-150 dpi 就够了
5. 使用 Lightroom 管理照片，智能预映加快浏览速度

---

### 问题2：TIFF 图片打不开或显示异常
**原因**：TIFF 格式有很多变体（不同压缩方式、不同位深、多页等），有些软件不支持某些变体。

**解决方法**：
1. 换个软件试试（Photoshop 兼容性最好，IrfanView 也很强）
2. 如果是 CMYK 模式的 TIFF，某些看图软件显示颜色会不对
   - 用 Photoshop 打开：图像 → 模式 → RGB 颜色
3. 如果是 LZW 压缩的 TIFF，某些老软件不支持
   - 用 Photoshop 重新保存为"无压缩"TIFF
4. 如果是多页 TIFF，某些软件只显示第一页
   - 用 IrfanView 或 XnView 可以翻页查看

---

### 问题3：TIFF 转 JPG 后颜色变了
**原因**：TIFF 可能是 CMYK 模式（印刷用），转成 JPG 后变成 RGB，颜色会有差异。或者是颜色配置文件的问题。

**解决方法**：
1. 在 Photoshop 中转换：图像 → 模式 → RGB 颜色（先转模式再存 JPG）
2. 编辑 → 转换为配置文件 → 选择 sRGB（网络通用色彩空间）
3. 保存 JPG 时勾选"嵌入颜色配置文件"
4. 印刷用 TIFF 保持 CMYK 模式，网络用 JPG 用 sRGB 模式
5. 专业工作请使用校色过的显示器，减少颜色偏差

---

### 问题4：多页 TIFF 只能看到第一页
**原因**：很多图片查看器只支持单页 TIFF，不支持多页（也叫多帧 TIFF）。

**解决方法**：
1. 用 **IrfanView** 或 **XnView MP** 打开，可以按 PageUp/PageDown 翻页
2. 用 Photoshop 打开：会显示为多个图层或多个文件
3. 拆分成单张图片：用 IrfanView 的"选项 → 提取所有页面"
4. 转成 PDF：多页 TIFF 转 PDF 后查看更方便
5. 传真和扫描出来的文件通常是多页 TIFF

---
## 💡 小知识

TIFF 格式的名字里有个"Tagged"（标签），这是什么意思呢？原来 TIFF 文件是由很多"标签"组成的——每个标签描述图片的一个属性，比如宽度、高度、颜色深度、压缩方式等等。这种设计的好处是扩展性极强——想加新功能？加个新标签就行了，老软件遇到不认识的标签直接跳过就行。所以 TIFF 才能从 1986 年一直用到今天，不断加入新功能（如 CMYK、LZW 压缩、多页、GeoTIFF 地理信息等），而格式本身始终兼容。这种"标签化"的设计思想也影响了后来的很多文件格式。

## 🔗 相关链接

- [Adobe TIFF 规范](https://www.adobe.io/open/standards/TIFF.html)
- [Adobe Photoshop 官网](https://www.adobe.com/cn/products/photoshop.html)
- [Adobe Lightroom 官网](https://www.adobe.com/cn/products/photoshop-lightroom.html)
- [IrfanView 图片查看器](https://www.irfanview.com/)
- [XnView MP 图片管理工具](https://www.xnview.com/en/xnviewmp/)
- [GIMP 免费图像编辑器](https://www.gimp.org/)

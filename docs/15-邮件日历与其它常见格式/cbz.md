# .cbz 文件后缀详解

## 1. 文件定义 & 用途

CBZ 是**漫画书文件**（Comic Book ZIP）的后缀，与 CBR 类似，区别在于 CBZ 本质上是 ZIP 压缩包。它把一组漫画图片（JPEG、PNG、BMP 等）打包成一个 ZIP 文件，改后缀为 `.cbz`，方便漫画阅读软件按页翻阅。

- **全称**：Comic Book ZIP
- **类型**：漫画书文件
- **本质**：ZIP 压缩包（改了后缀名）
- **特点**：按图片文件名排序显示、支持翻页阅读、兼容性比 CBR 更好
- **优势**：ZIP 格式是开放标准，任何系统原生支持，不依赖 RAR 解压工具

CBZ 与 CBR 的唯一区别是压缩格式不同：CBZ 用 ZIP，CBR 用 RAR。在实际使用中，CBZ 的兼容性更好，因为几乎所有操作系统都原生支持 ZIP 解压，而不需要安装额外的 WinRAR。

## 2. 适用场景

- **漫画阅读**：下载和整理漫画资源，用阅读器翻页阅读
- **漫画制作存档**：把漫画图片打包成 CBZ 方便管理分享
- **图像小说/绘本**：图片为主的电子书常用 CBZ 格式
- **跨平台漫画分享**：CBZ 比 CBR 兼容性更好，推荐用于分享

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | CDisplayEX、HoneyView、Sumatra PDF、MangaMeeya | ComicRack |
| Mac | Simple Comic、YACReader、Preview（系统自带，可解压后浏览） | - |
| Linux | YACReader、qComicBook、Evince（部分版本） | - |
| 手机 | CDisplayEX/Tachiyomi（安卓）、ChickensComic/iComics（iOS） | - |

**新手推荐**：
- Windows 用户：**HoneyView** 或 **Sumatra PDF**（都能直接打开 CBZ）
- Mac 用户：**YACReader** 或先解压用 **Preview** 浏览
- Linux 用户：**YACReader**（跨平台，功能全面）
- 手机用户：安卓用 **CDisplayEX**，iOS 用 **ChickensComic**
- 最通用方案：**Sumatra PDF** 跨平台都能用

## 4. 如何编辑、如何导出

### 如何打开 CBZ 文件
1. **漫画阅读器打开**：安装 CDisplayEX / HoneyView / YACReader，双击 CBZ 文件即可阅读
2. **Sumatra PDF 打开**：Sumatra PDF 原生支持 CBZ，翻页浏览
3. **直接解压**：把 .cbz 改为 .zip，双击即可解压得到图片（Windows/Mac 系统自带 ZIP 支持）
4. **浏览器打开**：把 .cbz 改为 .zip，解压后用浏览器按页查看图片

### 如何制作 CBZ 文件
1. 把漫画图片按 001.jpg、002.jpg、003.jpg... 的顺序命名（文件名排序决定阅读顺序）
2. 选中所有图片 → 右键 → 发送到 → 压缩(zipped)文件夹（Windows 自带）
3. 压缩完成后，将 .zip 后缀改为 .cbz
4. 用漫画阅读器打开确认页序正确
5. 也可以用 7-Zip：右键 → 7-Zip → 添加到压缩包 → 格式选 ZIP → 完成后改后缀

### 如何编辑内容
- 添加/删除页面：解压后修改图片，重新打包为 ZIP 改后缀 .cbz
- 调整顺序：解压后重命名图片（补零对齐），重新打包
- 合并/拆分：解压后重新组织图片，分别打包成新的 CBZ

### 格式转换
- **CBZ 转 CBR**：解压 CBZ 得到图片，用 RAR 格式重新打包，改为 .cbr
- **CBZ 转 PDF**：用 ComicRack 或在线工具将 CBZ 转为 PDF；也可解压后用图片转 PDF 工具
- **CBZ 转图片**：解压即可获得原始图片文件
- **PDF 转 CBZ**：将 PDF 每页导出为图片，打包为 ZIP 改后缀 .cbz

## 5. 常见报错与解决

### 问题1：CBZ 文件打不开
**原因**：系统没有关联漫画阅读器，或文件实际不是 ZIP 格式。

**解决方法**：
1. 安装支持 CBZ 的阅读器：CDisplayEX、HoneyView、YACReader、Sumatra PDF
2. 把 .cbz 改为 .zip，双击用系统自带解压功能打开（Windows/Mac 原生支持 ZIP）
3. 如果 .zip 也打不开，用 7-Zip 尝试打开（容错性更强）
4. 检查文件大小是否为 0 字节（下载失败导致）
5. 确认文件头是否为 `PK`（ZIP 文件标志），用 7-Zip 打开查看
6. 如果是从网上下载的，可能下载不完整，重新下载

---

### 问题2：CBZ 打开后页面顺序混乱
**原因**：图片文件名排序不规范，如 1.jpg、10.jpg、2.jpg...（按字符串排序时 10 排在 2 前面）。

**解决方法**：
1. 解压 CBZ，将图片重命名为 001.jpg、002.jpg...003.jpg（补零对齐位数）
2. 使用支持"自然排序"的阅读器（如 CDisplayEX、HoneyView 默认按数字大小排序）
3. 在阅读器设置中检查排序方式：选择"自然排序"或"数字排序"
4. 重新打包：按正确顺序命名图片后重新打包为 CBZ
5. 使用批量重命名工具（如 PowerToys 的 PowerRename）统一补零

---

### 问题3：CBZ 文件体积太大
**原因**：内部图片分辨率过高或格式未优化（如用了 BMP 而非 JPEG）。

**解决方法**：
1. 解压 CBZ，检查内部图片格式和大小
2. 用图片批量压缩工具（如 Caesium、ImageOptim）压缩图片后重新打包
3. 将 BMP/PNG 转为 JPEG（照片类用 JPEG 更省空间）
4. 降低图片分辨率（对于屏幕阅读，1500px 宽通常足够）
5. 重新打包时使用 ZIP 的最大压缩级别
6. 考虑转换为 CB7（7z 格式）以获得更高压缩率

---
## 💡 小知识

CBZ 和 CBR 是漫画爱好者社区的"非官方标准"。它们的巧妙之处在于：不需要发明新的文件格式，只是把现成的 ZIP 和 RAR 压缩包改了个后缀名。这样漫画阅读器就能通过后缀名识别漫画文件，而任何解压软件也都能打开它们。

在 CBR 和 CBZ 之间推荐选 CBZ：因为 ZIP 格式是开放标准，所有操作系统原生支持，不需要安装额外软件就能解压查看。而 RAR 格式需要 WinRAR 或 7-Zip 等第三方工具。如果你只是自己阅读，CBZ 和 CBR 体验一样；但如果要分享给别人，CBZ 更方便。

## 🔗 相关链接

- [CDisplayEX 官网](https://www.cdisplayex.com/)
- [HoneyView 官网](https://www.bandisoft.com/honeyview/)
- [YACReader 官网](https://www.yacreader.com/)
- [7-Zip 官网（可解压 CBZ）](https://www.7-zip.org/)
- [.cbr 漫画书文件后缀详解](./cbr.md)

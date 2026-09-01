# .chm 文件后缀详解

## 1. 文件定义 & 用途

CHM 是**编译的 HTML 帮助文件**（Compiled HTML Help）的后缀，由微软开发。它将一组 HTML 页面、图片、索引和目录编译打包成一个文件，常用于软件的帮助文档、教程手册等。大部分 Windows 软件（特别是老软件）的帮助文档都是 CHM 格式。

- **全称**：Compiled HTML Help
- **类型**：编译帮助文档
- **开发者**：微软（Microsoft）
- **发布年份**：1997年（随 HTML Help Workshop 发布）
- **特点**：体积小、支持全文搜索、支持目录索引、内嵌 HTML 页面和图片
- **前身**：HLP 格式（WinHelp，老版 Windows 帮助格式）

CHM 文件本质上是把 HTML 网页打包并用 LZX 算法压缩，内部结构类似一个压缩包。Windows 自带的"HTML 帮助"程序可以浏览目录、搜索关键词、跳转页面。

## 2. 适用场景

- **软件帮助文档**：大量软件用 CHM 格式发布使用手册
- **技术教程手册**：编程语言、API 文档常以 CHM 形式分发
- **离线百科**：把网页内容打包成 CHM 方便离线查阅
- **电子书**：部分技术电子书以 CHM 格式制作
- **系统/驱动文档**：Windows 驱动和系统组件的帮助文件

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | HTML 帮助程序 hh.exe（系统自带）、Sumatra PDF Reader | HelpNDoc、Help & Manual |
| Mac | Chmox、iCHM、Enolsoft CHM View | - |
| Linux | xCHM、KchmViewer、Okular（部分版本） | - |
| 跨平台 | Calibre（可查看部分 CHM）、浏览器（需先解压） | - |

**新手推荐**：
- Windows 用户：**双击即可**，系统自带的 HTML 帮助程序直接打开
- Mac 用户：安装 **Chmox** 或 **iCHM** 免费查看
- Linux 用户：安装 **KchmViewer**（界面友好，功能全面）

## 4. 如何编辑、如何导出

### 如何打开 CHM 文件
1. **Windows**：双击 CHM 文件，系统自带的 HTML 帮助程序（hh.exe）自动打开
2. **Mac/Linux**：安装第三方工具（Chmox / KchmViewer）
3. **解压查看源码**：用 7-Zip 解压 CHM 文件，可以看到内部的 HTML 页面和图片

### 如何制作 CHM 文件
- **微软 HTML Help Workshop**（免费）：微软官方 CHM 制作工具
  1. 编写 HTML 页面
  2. 用 HTML Help Workshop 创建项目（.hhp 文件）
  3. 添加目录（.hhc）和索引（.hhk）
  4. 编译生成 CHM 文件
- **第三方工具**：
  - HelpNDoc（免费版功能够用）
  - Help & Manual（专业付费）
  - WinCHM（简单易用）
  - Far Manager + HTMLHelp 插件

### 格式转换
- **CHM 转 PDF**：用 CHM 转换工具（如 CHM to PDF Converter），或先解压再用浏览器打开后打印为 PDF
- **CHM 转 HTML**：用 7-Zip 解压，直接得到原始 HTML 文件
- **CHM 转 EPUB**：先解压为 HTML，再用 Calibre 转为 EPUB

## 5. 常见报错与解决

### 问题1：CHM 文件打开后内容空白或显示"无法导航"
**原因**：Windows 安全机制阻止了从网络下载的 CHM 文件（NTFS 安全区域标记），或者 CHM 文件被损坏。

**解决方法**：
1. 右键 CHM 文件 → 属性 → 勾选"解除锁定" → 确定 → 重新打开
2. 把 CHM 文件移动到本地磁盘（如桌面），不要从网络共享或压缩包中直接打开
3. 用 7-Zip 解压 CHM，用浏览器直接打开内部 HTML 文件
4. 如果文件已损坏，重新下载获取完整文件

---

### 问题2：CHM 文件中的中文显示乱码
**原因**：CHM 内部 HTML 页面的编码声明与系统区域设置不匹配。

**解决方法**：
1. 用 7-Zip 解压 CHM 文件，用浏览器打开内部 HTML 页面
2. 在浏览器中切换编码为 GBK 或 UTF-8（右键 → 编码 → 选择对应编码）
3. 尝试在控制面板 → 区域 → 管理标签页 → 更改系统区域设置 → 设置为中文（简体，中国）
4. 使用 KchmViewer 等第三方工具打开（编码兼容性更好）
5. 如果是自己制作 CHM，确保所有 HTML 页面统一使用 UTF-8 或 GBK 编码

---

### 问题3：CHM 文件无法搜索或搜索功能失效
**原因**：CHM 的全文搜索索引损坏，或文件被修改后未重新编译搜索索引。

**解决方法**：
1. 用 7-Zip 解压 CHM，用 Windows 搜索或其它桌面搜索工具代替全文搜索
2. 解压后用浏览器打开 HTML，用浏览器的 Ctrl+F 搜索
3. 如果是自己制作 CHM：在 HTML Help Workshop 编译时勾选"Compile full-text search"
4. 尝试在另一台电脑上打开确认是文件问题还是系统问题
5. 使用 KchmViewer 等工具自带搜索功能

---
## 💡 小知识

CHM 格式虽然已经有些"古老"了（1997年推出），但至今仍然是 Windows 平台上最常见的帮助文档格式之一。它使用的 LZX 压缩算法是微软为压缩 HTML 内容专门设计的，压缩率很高，一个几百页文档的 CHM 可能只有几 MB。

不过微软在 Windows 10 之后逐渐淡化了对 CHM 的支持（新软件更推荐用在线文档或 PDF），但为了兼容老软件和驱动文档，Windows 至今仍然内置了 HTML 帮助查看器。

## 🔗 相关链接

- [HTML Help Workshop 下载](https://www.microsoft.com/en-us/download/details.aspx?id=21138)
- [KchmViewer 官网](https://github.com/ultradisk/kchmviewer)
- [HelpNDoc 官网](https://www.helpndoc.com/)
- [7-Zip 官网（可解压 CHM）](https://www.7-zip.org/)

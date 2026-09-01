# .heif 文件后缀详解

## 1. 文件定义 & 用途

HEIF 是 **高效图像文件格式**（High Efficiency Image File Format）的缩写，是一个基于 HEVC/H.265 编码的**通用图片容器**。简单说：HEIC 是 HEIF 容器的一种具体实现（苹果的命名），而 .heif 是更通用的扩展名。一个 HEIF 文件里可以装单张图片、图片序列（连拍/Live Photo）、动画，甚至带音频的图片。

- **全称**：High Efficiency Image File Format
- **类型**：图片容器格式（可装图片/序列/动画）
- **开发者**：MPEG 组织（ISO/IEC 23008-12 标准）
- **发布年份**：2015 年
- **特点**：容器结构、支持多图序列、支持透明通道和 16 位色深、基于 HEVC 编码
- **对比 HEIC**：HEIC 是苹果对 HEIF 的叫法，二者本质同源；.heif 更通用，.heic 更常见于苹果设备

可以把 HEIF 理解成"图片界的 MP4"——MP4 是个容器能装各种音视频，HEIF 也是个容器能装各种图片内容。

## 2. 适用场景

- **图片序列存储**：连拍、Live Photo、动态壁纸（一个文件装多帧）
- **高效图片分发**：网页和 APP 用 HEIF 替代 JPG 省流量
- **图像衍生/编辑**：HEIF 支持存储编辑指令（非破坏性编辑链）
- **现代系统图片**：安卓 9+、iOS、新版 macOS 都支持
- **专业图片存档**：16 位色深和透明通道，适合高质量图片

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 系统照片（Win10 1809+ 需 HEIF 扩展）、ImageGlass、IrfanView | Adobe Photoshop、Lightroom |
| Mac | 预览（系统自带）、照片 App | Adobe Photoshop、Lightroom、Pixelmator Pro |
| Linux | gThumb、ImageMagick、GIMP（需插件） | Darktable |
| 手机 | iOS 系统相册、Google 相册 | Lightroom Mobile |

**新手推荐**：
- Mac/iOS 用户：系统自带，直接打开
- Windows 用户：装 **HEIF 图像扩展** 后用"照片"打开，或用 **ImageGlass**
- 跨平台查看：**ImageGlass** 或 **IrfanView**

## 4. 如何编辑、如何导出

### 如何编辑
1. **Photoshop/Lightroom**：2019+ 原生支持 HEIF/HEIC
2. **Pixelmator Pro**（Mac）：原生支持，优化好
3. **GIMP**：安装 HEIF 插件
4. **在线编辑**：Photopea 支持打开 HEIF

### 如何导出/转换
- **转 JPG/PNG**：用 ImageGlass、IrfanView、XnConvert 批量转换
- **命令行转换**：ImageMagick `magick input.heif output.jpg`
- **在线转换**：CloudConvert、Convertio
- **Mac 预览**：打开 → 导出 → 选择 JPG/PNG
- **提取序列帧**：HEIF 装的是图片序列时，可用 ffmpeg 或工具拆出每帧

## 5. 常见报错与解决

### 问题1：Windows 打不开 .heif 文件
**原因**：和 HEIC 一样，Windows 默认无 HEVC 解码器。

**解决方法**：
1. 微软商店安装 **"HEIF 图像扩展"**（免费）+ **"HEVC 视频扩展"**
2. 或直接用 **ImageGlass/IrfanView**（自带解码，无需系统扩展）
3. 在线转换工具转成 JPG 后再处理

### 问题2：HEIF 文件里的图片序列（连拍/Live Photo）只显示第一帧
**原因**：部分查看器只读 HEIF 容器里的首图，不解析序列。

**解决方法**：
1. 用支持序列的查看器：iOS 相册、macOS 照片会完整播放
2. 用 **ffmpeg** 拆帧：`ffmpeg -i input.heif frame_%03d.jpg`
3. Windows 上用"照片"App（装好扩展后）可播放 Live Photo
4. 提取所有帧后再单独处理

### 问题3：HEIF 转 JPG 后透明背景变黑色
**原因**：HEIF 支持透明通道（类似 PNG），而 JPG 不支持透明，转换时透明区域默认填黑。

**解决方法**：
1. 需要保留透明背景的，转成 **PNG** 而非 JPG
2. 用 ImageMagick 转换时加白色背景：`magick input.heif -background white -flatten output.jpg`
3. Photoshop 中转换时新建白底图层再合并
4. 检查原 HEIF 是否真的有透明通道，有些只是误判

---
## 💡 小知识

HEIF 是 MPEG 组织的"正牌"标准（ISO/IEC 23008-12），苹果只是最早大规模落地它的厂商，并起了个 .heic 的名字。HEIF 真正的野心不只是"更好的 JPG"，而是"图片界的 MP4"——它是个容器，能装图片序列、衍生图、编辑指令，甚至音频。这意味着未来一张"图片"可能是个完整的图像故事：原始图+编辑历史+多角度连拍，全在一个文件里。不过 HEIF 依赖收费的 HEVC 专利，这也催生了基于免费 AV1 编码的 AVIF 格式来挑战它。格式之争，远未结束。

## 🔗 相关链接

- [HEIF 标准说明（诺基亚）](https://nokiatech.github.io/heif/)
- [ImageGlass 官网](https://imageglass.org/)
- [ImageMagick 官网](https://imagemagick.org/)
- [.heic 文件后缀详解](./heic.md)
- [.jpg 文件后缀详解](../02-图片与设计文件类/jpg.md)

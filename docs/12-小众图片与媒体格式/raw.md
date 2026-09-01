# .raw 文件后缀详解

## 1. 文件定义 & 用途

RAW 是相机拍摄的**原始图像数据**，被称为"数字底片"。当相机拍 JPG 时，其实是相机内部先把原始数据加工（白平衡、锐化、降噪、压缩）再保存；而 RAW 保存的是 sensor 直接捕获的、未经"美化"的原始数据，把后期处理的主动权完全交给你。

- **全称**：RAW Image（原始图像，非缩写，就是"生的"意思）
- **类型**：未处理的相机原始图像数据
- **特点**：信息量最大、宽容度高（可救回过曝/欠曝）、白平衡可无损调整、文件较大
- **注意**：RAW 不是一个统一格式，各厂商有各自格式（见下表），.raw 是较通用的扩展名之一

各厂商常见 RAW 格式：
| 厂商 | 扩展名 |
|------|--------|
| 佳能 Canon | .cr2 / .cr3 |
| 尼康 Nikon | .nef |
| 索尼 Sony | .arw |
| 富士 Fujifilm | .raf |
| 奥林巴斯 Olympus | .orf |
| 松下 Panasonic | .rw2 |
| Adobe 通用 | .dng |

## 2. 适用场景

- **专业摄影后期**：商业摄影、风光、人像，追求极致画质
- **大光比场景**：逆光、日落等明暗反差大的场景，RAW 宽容度高能救回细节
- **白平衡要求严苛**：商品摄影、婚纱摄影，RAW 可无损调白平衡
- **需要大幅后期**：要调曝光、拉阴影、提亮暗部的照片
- **存档数字底片**：保留最大信息量作为原始素材长期保存
- **输出大幅面打印**：RAW 信息量大，放大打印画质更好

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | RawTherapee、darktable、IrfanView（部分）、FastStone Image Viewer | Adobe Lightroom、Capture One、DxO PhotoLab |
| Mac | 预览（部分支持）、RawTherapee、darktable | Adobe Lightroom、Capture One、DxO PhotoLab、Apple Aperture（已停更） |
| Linux | RawTherapee、darktable、digiKam | - |

**新手推荐**：
- 免费后期首选：**darktable** 或 **RawTherapee**（开源免费，功能接近 Lightroom）
- 行业标准：**Adobe Lightroom**（摄影后期主力，订阅制）
- 佳能/尼康/索尼用户：厂商自带软件（Canon Digital Photo Pro、Nikon Capture、Sony Imaging Edge）免费且对自家格式优化最好
- 通用方案：转成 DNG（Adobe 的通用 RAW 格式）长期保存

## 4. 如何编辑、如何导出

### 如何编辑
RAW 不能像 JPG 那样直接用画图改，必须用 RAW 处理软件"显影"：

1. **Lightroom/Capture One**：调曝光、白平衡、色彩、镜头校正、降噪等，非破坏性编辑
2. **darktable/RawTherapee**：免费替代，功能强大
3. **厂商软件**：如佳能 DPP，对自家相机色彩还原最准
4. **编辑流程**：RAW 调整 → 导出 JPG/TIFF → 需要精修再用 Photoshop 处理

### 如何导出/转换
- **导出 JPG**：在 Lightroom/darktable 中"导出" → 选 JPG，设置质量
- **导出 TIFF**：需要无损保留画质给印刷用，导出 TIFF
- **转 DNG**：用 Adobe DNG Converter 转成通用 DNG 格式
- **批量导出**：Lightroom/darktable 支持批量导出，配合预设提高效率
- **不能直接转成可编辑图层**：需先导出 TIFF/JPG 再进 Photoshop

## 5. 常见报错与解决

### 问题1：RAW 文件在 Windows 照片查看器里打不开
**原因**：Windows 系统自带查看器不支持各厂商 RAW 格式，需装扩展或专用软件。

**解决方法**：
1. 微软商店安装 **"Raw 图片扩展"**（Microsoft Raw Image Extension，免费），之后"照片"App 可预览部分 RAW
2. 用 **RawTherapee** 或 **darktable** 直接打开（推荐，功能也强）
3. 用厂商自带软件（如佳能 DPP）打开对应格式
4. 装一个 **FastStone Image Viewer**，能快速预览多种 RAW

### 问题2：换了新相机，旧版 Lightroom 打不开新 RAW
**原因**：每个新相机型号的 RAW 编码有变化，需要新版 RAW 解码库（ACR/Lightroom 版本）支持。

**解决方法**：
1. 升级 Lightroom/ACR 到最新版（可能需要订阅最新版）
2. 用 Adobe DNG Converter 把新 RAW 转成 DNG，旧版软件就能打开
3. 用厂商最新自带软件打开
4. 用 RawTherapee/darktable（开源，更新快，常比商业软件更早支持新机型）

### 问题3：RAW 文件体积很大，硬盘装不下
**原因**：RAW 保留全部原始数据，单张常见 20-80MB（高像素机上百 MB）。

**解决方法**：
1. 精选保留：只保留"值得后期"的 RAW，其余转 JPG 后删除 RAW
2. 用 DNG 压缩：Adobe DNG Converter 转换时勾选"有损压缩"或"嵌入快速加载预览"，体积可减半
3. 外置硬盘/ NAS 冷存储：RAW 存归档盘，日常工作用导出的 JPG
4. 拍摄时用 RAW+JPG 双格式：日常用 JPG，重要照片才动 RAW
5. 云存储：Google Photos、阿里云盘等支持 RAW 原图备份（注意容量）

---
## 💡 小知识

RAW 之所以叫"数字底片"，是因为它和胶片时代的底片扮演同样角色：底片本身不能直接看，要"显影"成照片；RAW 也要经过"显影"软件处理才能变成可视的 JPG/TIFF。RAW 最大的价值在于"宽容度"——一张过曝两档的 JPG 基本是废片（高光死白无细节），但同样过曝的 RAW 往往能拉回大部分高光细节，因为它记录了 12-14 位的亮度信息，而 JPG 只有 8 位。这就是专业摄影师"宁可多拍 RAW 也不拍 JPG"的原因。代价是体积和后期工作量，但对追求画质的人来说绝对值得。各厂商 RAW 不统一是历史包袱，Adobe 推 DNG 想统一却未能成功，所以摄影后期软件都得"会读几十种 RAW"。

## 🔗 相关链接

- [RawTherapee 官网](https://rawtherapee.com/)
- [darktable 官网](https://www.darktable.org/)
- [Adobe DNG Converter 下载](https://helpx.adobe.com/camera-raw/digital-negative.html)
- [Microsoft Raw 图像扩展](https://apps.microsoft.com/detail/9nctmq2jb3bp)
- [.cr2 文件后缀详解](./cr2.md)

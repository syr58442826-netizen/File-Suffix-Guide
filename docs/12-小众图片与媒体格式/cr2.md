# .cr2 文件后缀详解

## 1. 文件定义 & 用途

CR2 是**佳能（Canon）相机的 RAW 格式**，是 RAW 的一种具体厂商实现。它存储佳能相机感光元件捕获的原始图像数据，未经相机内部处理，是佳能摄影师的"数字底片"。

- **全称**：Canon Raw version 2
- **类型**：相机原始图像数据（佳能专属 RAW）
- **开发者**：Canon 佳能
- **使用时期**：2004-2018 年（EOS 5D Mark II、70D、6D 等机型）
- **继任者**：CR3（2018 年起，EOS R 系列等新机型使用）
- **特点**：12/14 位色深、未压缩或轻度压缩、保留完整拍摄元数据（EXIF）

CR2 本质是 TIFF 格式的扩展（基于 TIFF/EP 标准），文件头是 TIFF 结构，但内部是佳能自定义的数据。它是专业摄影领域的常见格式。

## 2. 适用场景

- **佳能单反/微单摄影后期**：用佳能 EOS 系列拍摄的专业/爱好者后期处理
- **商业/风光/人像摄影**：追求最大画质和后期空间的场景
- **白平衡/曝光精修**：CR2 可无损调整白平衡、大幅拉回曝光
- **大幅面打印输出**：信息量大，打印质量好
- **佳能照片存档**：作为原始底片长期保存

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Canon Digital Photo Professional（DPP，佳能官方免费）、RawTherapee、darktable | Adobe Lightroom、Capture One、DxO PhotoLab |
| Mac | Canon DPP、RawTherapee、darktable、预览（部分） | Adobe Lightroom、Capture One、DxO PhotoLab |
| Linux | RawTherapee、darktable、digiKam | - |

**新手推荐**：
- 佳能用户首选：**Canon Digital Photo Professional（DPP）**——佳能官方免费软件，对 CR2 色彩还原最准
- 专业后期：**Adobe Lightroom**（行业主流）或 **Capture One**（佳能色彩支持优秀）
- 免费开源：**RawTherapee** 或 **darktable**，功能接近 Lightroom

## 4. 如何编辑、如何导出

### 如何编辑
1. **Canon DPP**：官方软件，佳能色彩科学还原最准，支持镜头校正、数码镜头优化
2. **Lightroom/Capture One**：专业后期主力，预设丰富，批量处理强
3. **darktable/RawTherapee**：免费替代，调整能力全面
4. **编辑流程**：CR2 显影（曝光/白平衡/色彩）→ 导出 TIFF/JPG → 需精修进 Photoshop

### 如何导出/转换
- **导出 JPG/TIFF**：DPP 或 Lightroom 中"导出/转换并保存"，选格式和质量
- **转 DNG**：用 Adobe DNG Converter 转成通用 DNG
- **转 CR3**：无意义，CR3 是新格式编码，不能从 CR2 转换
- **批量转换**：DPP 支持批量"转换并保存"，Lightroom 支持导出预设批量处理

## 5. 常见报错与解决

### 问题1：CR2 文件在 Windows 上只显示图标，预览不出来
**原因**：Windows 默认不识别 CR2，缺少解码器和缩略图支持。

**解决方法**：
1. 安装佳能官方 **Canon DPP**，会自动关联 CR2 并生成缩略图
2. 微软商店装 **"Raw 图像扩展"**，"照片"App 可预览
3. 用 **FastStone Image Viewer** 或 **XnView MP** 浏览，缩略图速度快
4. 装佳能的 **EOS Utility** 也有助于系统识别 CR2

### 问题2：新版/老版软件打不开某些 CR2
**原因**：不同佳能机型的 CR2 内部编码有差异，软件需要对应版本的支持包；新机型 CR2 常需新版软件。

**解决方法**：
1. 升级 Lightroom/ACR/darktable 到最新版
2. 用 Canon DPP 最新版（佳能官网免费下载，对新机型支持最及时）
3. 用 Adobe DNG Converter 转成 DNG，绕过版本兼容问题
4. 开源 RawTherapee/darktable 更新频繁，常较早支持新机型

### 问题3：CR2 文件体积大，连拍时存储卡很快就满
**原因**：CR2 单张约 20-40MB，连拍几十张就上 GB。

**解决方法**：
1. 日常非关键场合改拍 JPG 或 RAW+JPG（按需用 RAW）
2. 用高速大容量存储卡（128GB/256GB SD 或 CFexpress）
3. 拍摄后及时导出到电脑/硬盘，清空存储卡
4. 长期归档用 DNG 压缩存储，节省空间
5. 重要拍摄备双卡（CFexpress + SD）防万一

### 问题4：CR2 在 Capture One 里颜色和 DPP 不一样
**原因**：不同软件对 CR2 的色彩解码算法不同，DPP 用佳能官方色彩科学，第三方软件是逆向解读。

**解决方法**：
1. 追求佳能官方色彩：用 **Canon DPP** 处理
2. 用 Capture One 时套用佳能相机对应的"相机配置文件"（Camera Profile）校正
3. Lightroom 中切换"相机校准"面板的配置文件，选 Adobe Standard 或 Camera Standard
4. 建立统一的后期预设，保证多软件输出色彩一致

---
## 💡 小知识

CR2 陪伴了佳能数码摄影的黄金时代。从 2004 年的 EOS-1D Mark II 到 2018 年的 EOS 5D Mark IV，无数经典照片的"底片"都是 CR2。它基于 TIFF 结构，是当时最成熟的 RAW 容器之一。2018 年，佳能推出 EOS R 全画幅微单，顺势把 RAW 格式升级为 CR3——CR3 采用新的 CIF 结构，支持压缩更好、还支持 HEIF 直接出图。虽然新机型用 CR3，但海量的 CR2 存档仍需被支持，所以所有主流后期软件至今都同时支持 CR2 和 CR3。对佳能老用户来说，CR2 是十多年拍摄记忆的载体，格式虽"老"，价值不减。

## 🔗 相关链接

- [Canon Digital Photo Professional 下载](https://www.canon.com.cn/support/dpp/)
- [RawTherapee 官网](https://rawtherapee.com/)
- [darktable 官网](https://www.darktable.org/)
- [Adobe DNG Converter](https://helpx.adobe.com/camera-raw/digital-negative.html)
- [.raw 文件后缀详解](./raw.md)

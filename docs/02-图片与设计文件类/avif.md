# .avif 文件后缀详解

## 1. 文件定义 & 用途

AVIF 是 **AV1 Image File Format** 的缩写，是一种基于 AV1 视频编码技术开发的现代图片格式。它由开放媒体联盟（Alliance for Open Media）开发，目标是比 JPG 更小、比 PNG 支持透明、比 WebP 压缩率更高。

简单来说，AVIF 是目前压缩效率最高的图片格式之一——同等画质下，体积比 JPG 小约 50%，比 WebP 还要小。

- **全称**：AV1 Image File Format
- **类型**：光栅图片（有损/无损压缩）
- **开发者**：Alliance for Open Media（开放媒体联盟）
- **发布年份**：2019年
- **特点**：超高压缩率、支持透明通道、支持 HDR、支持动画
- **官网**：https://aomediacodec.github.io/av1-avif/

## 2. 适用场景

- 网页图片优化（大幅减少页面加载时间）
- 移动端 App 中的图片资源（节省带宽和存储）
- 需要透明背景的图片（替代 PNG，体积更小）
- HDR 高动态范围图片展示
- 简单动画（替代 GIF，体积更小质量更好）
- 图片 CDN 和云存储（节省存储成本）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 现代浏览器（Chrome/Edge/Firefox）、ImageGlass、IrfanView（需插件） | Adobe Photoshop（2021+）、Affinity Photo、Paint.NET（需插件） |
| Mac | 预览（macOS 13+）、现代浏览器（Chrome/Firefox） | Adobe Photoshop（2021+）、Pixelmator Pro、Affinity Photo |
| Linux | 现代浏览器、GIMP（2.10.22+）、Eye of GNOME | GIMP、Krita |

**新手推荐**：
- 最简单的查看方式：直接用 **Chrome / Edge / Firefox 浏览器**拖入即可
- 批量查看：**ImageGlass**（Windows 免费，支持 AVIF）
- 编辑处理：**GIMP**（2.10.22 以上版本原生支持）
- 专业编辑：**Adobe Photoshop**（2021 及以上版本支持）

## 4. 如何编辑、如何导出

### 如何编辑
1. 用 Photoshop 2021+ 打开 .avif 文件即可编辑
2. 用 GIMP 2.10.22+ 打开编辑
3. 操作方式与编辑 JPG/PNG 一致

### 如何导出/转换
- **JPG/PNG 转 AVIF**：
  - 在线工具：[Squoosh](https://squoosh.app/)（Google 出品，免费好用）
  - 命令行：用 `cavif` 或 `avifenc` 工具批量转换
  - Photoshop：文件 → 导出 → 另存为 → 选择 AVIF（需较新版本）
- **AVIF 转 JPG/PNG**：用浏览器打开后右键另存，或用 ImageGlass 批量转换
- **AVIF 转 WebP**：用 Squoosh 或 ffmpeg
  ```bash
  ffmpeg -i input.avif output.webp
  ```

## 5. 常见报错与解决

### 问题1：AVIF 图片在旧版软件中打不开
**原因**：AVIF 是较新的格式（2019年发布），很多旧版软件不支持。

**解决方法**：
1. 用现代浏览器（Chrome 85+、Firefox 93+、Edge 92+）打开
2. 升级图片查看软件到最新版本
3. 如果必须用旧软件，先转换为 JPG/PNG 格式
4. 用在线工具 Squoosh 快速转换格式

---

### 问题2：AVIF 图片在网页中不显示
**原因**：旧版浏览器不支持 AVIF 格式，或 Web 服务器未配置正确的 MIME 类型。

**解决方法**：
1. 在 HTML 中使用 `<picture>` 标签提供 fallback：
   ```html
   <picture>
     <source srcset="image.avif" type="image/avif">
     <source srcset="image.webp" type="image/webp">
     <img src="image.jpg" alt="描述">
   </picture>
   ```
2. 服务器配置 MIME 类型：`image/avif`
3. 对不支持 AVIF 的浏览器自动回退到 WebP 或 JPG

---

### 问题3：AVIF 编码速度很慢
**原因**：AVIF 基于 AV1 编码，编码算法复杂度很高，对 CPU 要求较大。

**解决方法**：
1. 使用速度优先的编码参数（如 cavif 的 `--speed` 参数调高）
2. 降低图片分辨率后再编码
3. 用 GPU 加速的编码工具
4. 批量转换时可以并行处理多张图片

---

### 问题4：AVIF 图片在某些社交媒体平台上传失败
**原因**：部分平台的图片处理系统尚未支持 AVIF 格式。

**解决方法**：
1. 上传前先转换为 JPG 格式（最通用）
2. 用 Squoosh 或 ImageGlass 快速转换
3. 关注平台更新公告，越来越多平台正在加入 AVIF 支持

---

## 💡 小知识

AVIF 的核心编码技术 AV1 是由 Google、Mozilla、Cisco、Amazon、Netflix 等公司组成的"开放媒体联盟"共同开发的。它的诞生是为了对抗 HEVC/H.265 格式——后者因为专利费问题让很多公司头疼。AV1 和 AVIF 都是免专利费的开放标准，这也是它能被各大浏览器迅速支持的重要原因。目前 Chrome、Firefox、Edge 已原生支持 AVIF，Safari 从 macOS 13（Safari 16）开始也支持了。可以说 AVIF 正在成为下一代图片格式的事实标准。

## 🔗 相关链接

- [AVIF 官方规范](https://aomediacodec.github.io/av1-avif/)
- [Squoosh 在线图片转换](https://squoosh.app/)
- [Can I Use - AVIF 浏览器支持情况](https://caniuse.com/avif)
- [ImageGlass 免费看图软件](https://imageglass.org/)
- [.webp 格式详解](./webp.md)
- [.jpg 格式详解](./jpg.md)

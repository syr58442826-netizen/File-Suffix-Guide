# .mov 文件后缀详解

## 1. 文件定义 & 用途

MOV 是 Apple 公司开发的 QuickTime 视频格式，全称 QuickTime Movie。它和 MP4 一样使用 MPEG-4 编码标准，两者关系非常密切，可以说是"近亲"。

MOV 格式的核心特点：
- **苹果生态标配**：Mac、iPhone、iPad 的原生视频格式
- **画质出色**：支持高质量视频编码，适合专业剪辑
- **支持多轨道**：可以包含视频、音频、字幕、章节等
- **支持 Alpha 通道**：可以存储带透明背景的视频（常用于特效合成）
- **专业剪辑友好**：Final Cut Pro、Premiere 等剪辑软件优化良好

## 2. 适用场景

- **苹果设备拍摄**：iPhone、iPad 录制的视频默认是 MOV 格式
- **专业视频剪辑**：剪辑软件的常用中间格式和输出格式
- **影视后期制作**：支持 ProRes 编码，影视行业常用
- **特效合成**：带 Alpha 通道的 MOV 视频用于 AE 等合成软件
- **Mac 屏幕录制**：QuickTime Player 录屏保存为 MOV
- **广告/宣传片制作**：高质量内容的常用格式

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | QuickTime Player（Apple 官方）、VLC 媒体播放器、PotPlayer | Adobe Premiere Pro、After Effects |
| Mac | QuickTime Player（系统自带）、VLC、IINA | Final Cut Pro、Adobe Premiere Pro、After Effects |
| Linux | VLC 媒体播放器、MPV | DaVinci Resolve |
| 手机 | iOS 系统自带、VLC、MX Player | - |

## 4. 如何编辑、如何导出

### 如何编辑

**简单剪辑（Mac 用户）：**
- 使用 QuickTime Player（系统自带，支持裁剪、分割、合并）
- 使用剪映 Mac 版（免费，操作简单）

**简单剪辑（Windows 用户）：**
- 使用剪映 Windows 版
- 使用 Shotcut（免费开源）

**专业剪辑：**
- Final Cut Pro（Mac 专属，行业顶级，对 MOV 优化最好）
- Adobe Premiere Pro（跨平台，业界标准）
- DaVinci Resolve（免费版功能强大，支持 ProRes）

### 如何导出

**从 iPhone/iPad 导出 MOV：**
1. 用数据线连接电脑
2. Mac 上用"照片"App 或 AirDrop 导出
3. Windows 上用 iTunes 或直接从磁盘复制

**从剪辑软件导出 MOV：**
1. 选择"文件" → "导出" → "媒体"
2. 格式选择 QuickTime（.mov）
3. 视频编码可选：H.264（通用）、ProRes（专业剪辑，文件大）、HEVC（体积小）
4. 设置分辨率和质量
5. 点击导出

**其他格式转 MOV：**
1. 使用格式工厂、HandBrake 或 FFmpeg
2. 选择输出格式为 MOV
3. 推荐编码：H.264 + AAC
4. 开始转换

## 5. 常见报错与解决

### 问题 1：Windows 电脑播放 MOV 只有声音没画面

**原因：** Windows 缺少 QuickTime 解码器或视频编码不支持。

**解决方法：**
1. 安装 Apple 官方的 QuickTime Player
2. 或者直接使用 VLC 播放器（自带所有解码器）
3. 用格式工厂把 MOV 转成 MP4 格式
4. 安装 K-Lite Codec Pack 解码器包

### 问题 2：MOV 文件导入剪辑软件失败或卡顿

**原因：** 编码格式不兼容，或电脑配置不足。

**解决方法：**
1. 确认剪辑软件是否支持该编码（如 ProRes 在 Windows 上支持有限）
2. 用格式工厂或 FFmpeg 转成 H.264 编码的 MOV 或 MP4
3. 在剪辑软件中创建代理文件（Proxy）进行剪辑
4. 更新显卡驱动，开启硬件加速

### 问题 3：iPhone 录制的 MOV 视频在 Windows 上倒着播放

**原因：** iPhone 拍摄的视频通过旋转元数据记录方向，Windows 播放器不识别。

**解决方法：**
1. 使用 VLC 播放器（会自动识别方向）
2. 用格式工厂转换时，选择"旋转"功能修正方向
3. 用 QuickTime Player 打开后重新导出
4. 使用 FFmpeg 命令旋转：`ffmpeg -i input.mov -c copy -metadata:s:v rotate="0" output.mov`

### 问题 4：MOV 文件损坏无法打开

**原因：** 传输中断、存储空间不足、设备意外关机等。

**解决方法：**
1. 用 VLC 播放器尝试播放（容错性较好）
2. Mac 用户可以用 QuickTime Player 尝试修复
3. 使用专业修复工具，如 Stellar Repair for Video
4. 用 FFmpeg 尝试转码修复：`ffmpeg -err_detect ignore_err -i input.mov -c copy output.mov`
5. 重新从原设备导出文件

---

## 💡 小知识

MOV 和 MP4 其实是"亲兄弟"——它们都基于 MPEG-4 标准，很多时候只改个后缀名就能互相播放。MOV 格式诞生于 1998 年，比 MP4 还早几年，后来 MP4 格式在制定时参考了很多 MOV 的设计。

MOV 格式最厉害的地方是它的 ProRes 编码系列，这是 Apple 专为影视后期制作开发的编码。ProRes 视频画质极高，同时剪辑时对电脑的压力很小，是好莱坞电影后期的常用格式之一。

## 🔗 相关链接

- [Apple QuickTime 官方页面](https://support.apple.com/quicktime)
- [Final Cut Pro 官方网站](https://www.apple.com/final-cut-pro/)
- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [.mp4 格式详解](./mp4.md)
- [.avi 格式详解](./avi.md)

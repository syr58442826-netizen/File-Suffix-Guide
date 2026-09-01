# .wma 文件后缀详解

## 1. 文件定义 & 用途

WMA 是 **Windows Media Audio** 的缩写，微软开发的音频压缩格式，1999 年推出，对标 MP3。它曾是 Windows 生态的主力音频格式，集成在 Windows Media Player 中，主打"同码率音质优于 MP3"和 DRM 版权保护。

- **全称**：Windows Media Audio
- **类型**：有损/无损音频压缩格式（含 WMA Lossless 变体）
- **开发者**：Microsoft
- **发布年份**：1999 年
- **特点**：与 Windows 深度集成、支持 DRM 版权保护、有 WMA Lossless 无损变体
- **现状**：在微软生态外逐渐边缘化，被 AAC/MP3 取代，但老资料库仍有大量 WMA

## 2. 适用场景

- **Windows 老资料库**：早期用 WMP 翻录 CD 存的音乐
- **Windows 系统音频**：系统提示音、老软件音效
- **DRM 保护音频**：早期在线音乐商店的加密音乐
- **语音/有声书**：低码率 WMA 语音清晰
- **老设备兼容**：部分老 MP3 播放器、车载音响支持 WMA

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Windows Media Player（系统自带）、VLC、foobar2000、AIMP | Adobe Audition |
| Mac | VLC、Flip4Mac（QuickTime 组件） | Adobe Audition |
| Linux | VLC、ffplay（ffmpeg） | - |
| 手机 | VLC、Poweramp（Android） | - |

**新手推荐**：
- Windows 用户：**Windows Media Player** 原生支持；**VLC** 跨平台更通用
- Mac 用户：**VLC**（系统不原生支持 WMA）
- 长期方案：把 WMA 转成 MP3/AAC，通用性更好

## 4. 如何编辑、如何导出

### 如何编辑
1. **Windows Media Player**：可翻录 CD 为 WMA，但编辑能力弱
2. **Adobe Audition**：支持 WMA 编辑
3. **Audacity**：需装 FFmpeg 库才能导入 WMA
4. **标签编辑**：Mp3tag 可编辑 WMA 元数据

### 如何导出/转换
- **WMA 转 MP3/AAC**：用 ffmpeg `ffmpeg -i input.wma -c:a libmp3lame -q:a 2 output.mp3`
- **格式工厂/foobar2000**：图形界面批量转换
- **在线转换**：CloudConvert、Convertio
- **CD 翻录为 WMA**：WMP 的"翻录"功能，但建议翻成 MP3 更通用
- **批量转换**：foobar2000 转码器支持批量

## 5. 常见报错与解决

### 问题1：Mac/Linux 上打不开 WMA 文件
**原因**：WMA 是微软格式，Mac 和 Linux 系统默认不支持。

**解决方法**：
1. 装 **VLC** 播放器，跨平台支持 WMA
2. Mac 装 **Flip4Mac** 组件让 QuickTime 支持 WMA
3. 用 ffmpeg 转成 MP3/M4A 后再播放：`ffmpeg -i input.wma output.mp3`
4. 在线转换工具转格式

### 问题2：WMA 文件播放时提示"需要许可证"或无法播放
**原因**：文件带有微软 DRM 版权保护，只能在授权的设备/账号上播放。

**解决方法**：
1. 这类是早期音乐商店购买的加密 WMA，需用原账号授权的电脑播放
2. 微软已停止 DRM 服务支持，老 DRM WMA 基本无法破解（合法购买的也尴尬）
3. 非法破解 DRM 在多数地区违法，不建议尝试
4. 教训：以后购买数字音乐选择无 DRM 的格式（如 MP3/AAC/FLAC）

### 问题3：WMA 转换后音质变差或有杂音
**原因**：有损转有损累积损失，或编码器质量问题。

**解决方法**：
1. 用高码率目标格式（MP3 320kbps）减少损失
2. 用 ffmpeg 的优质编码器，避免劣质转换工具
3. 如有原始 CD，重新翻录成目标格式，不经过 WMA 中转
4. 转换前用 Audacity 检查音量，避免削波杂音

### 问题4：老 WMA 文件打不开，提示损坏
**原因**：WMA 文件结构较老，存储介质损坏或文件系统问题。

**解决方法**：
1. 用 VLC 尝试播放（容错性强）
2. 用 ffmpeg 尝试读取：`ffmpeg -i input.wma -c:a libmp3lame output.mp3`，有时能"抢救"出音频
3. 从备份/原 CD 重新获取
4. 珍贵音频可尝试专业修复工具（如 Stellar Repair）

---
## 💡 小知识

WMA 是微软"想统治数字音乐"的尝试。1999 年 MP3 大热但微软没份，于是推出 WMA，宣称"64kbps WMA 音质等同 128kbps MP3"，并主打 DRM 版权保护吸引唱片公司。当年微软联手多家唱片公司开数字音乐商店，想复制 Windows 的垄断神话。但历史跟微软开了个玩笑：苹果 iPod + iTunes 用 AAC + 公平使用策略横扫市场，微软的 WMA 阵营节节败退。2000 年代末，微软自己的 Zune 音乐播放器都败给 iPod，WMA 生态彻底崩盘。今天 WMA 只剩下"老资料库"的价值，新音乐几乎没人用 WMA 了。它是个典型的"巨头押注却输给更开放方案"的案例。

## 🔗 相关链接

- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [ffmpeg 官网](https://ffmpeg.org/)
- [foobar2000 官网](https://www.foobar2000.org/)
- [.mp3 文件后缀详解](../03-音视频媒体类/mp3.md)
- [.aac 文件后缀详解](./aac.md)

# .aac 文件后缀详解

## 1. 文件定义 & 用途

AAC 是 **高级音频编码**（Advanced Audio Coding）的缩写，是 MP3 的官方"继任者"。它在同等音质下体积比 MP3 小约 25-30%，是苹果生态、YouTube、数字电视的主流音频格式。你听到的绝大多数在线视频和流媒体音频，底层多半是 AAC。

- **全称**：Advanced Audio Coding
- **类型**：有损音频压缩格式
- **开发者**：MPEG 组织（杜比、Fraunhofer、索尼、AT&T 等联合）
- **发布年份**：1997 年
- **特点**：音质优于 MP3、支持多声道（最多 48 通道）、低延迟、广泛兼容
- **常见场景**：MP4 视频里的音轨、m4a 文件、数字广播、iPhone 录音

AAC 通常不单独出现，而是封装在 MP4/M4A 容器里（.m4a 就是 AAC 音频）。纯 .aac 文件多用于流媒体和专业场景。

## 2. 适用场景

- **在线视频音轨**：YouTube、B站等视频的音频部分基本是 AAC
- **苹果生态音频**：iTunes Store 音乐、Apple Music、iPhone 录音
- **流媒体音乐**：多数流媒体平台用 AAC 编码
- **数字电视/广播**：DAB+ 数字广播用 AAC
- **移动设备存储**：体积小音质好，适合手机存音乐
- **游戏/应用音频**：移动端应用的音效

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | VLC、Windows Media Player（系统自带）、foobar2000、QQ音乐 | Adobe Audition、Audacity |
| Mac | QuickTime Player（系统自带）、VLC、iTunes/音乐 App | Adobe Audition、Logic Pro |
| Linux | VLC、Audacious、mpv | Audacity、Ardour |
| 手机 | 系统自带播放器、VLC | - |

**新手推荐**：
- 通用播放：系统自带播放器基本都支持 AAC
- 万能播放：**VLC**
- 免费编辑：**Audacity**（需配 FFmpeg 库支持 AAC）
- Windows 本地听歌：**foobar2000**

## 4. 如何编辑、如何导出

### 如何编辑
1. **Audacity**：需安装 FFmpeg 库后才能导入/导出 AAC；可裁剪、混音
2. **Adobe Audition**：原生支持 AAC 编辑
3. **foobar2000**：可转码、加标签，非波形编辑
4. **标签编辑**：Mp3tag、MusicBrainz Picard 编辑 AAC/m4a 元数据

### 如何导出/转换
- **iTunes/音乐 App 导出 AAC**：导入音频 → 右键 → 转换为 AAC
- **MP3 转 AAC**：用 ffmpeg `ffmpeg -i input.mp3 -c:a aac -b:a 192k output.m4a`
- **AAC 转 MP3**：`ffmpeg -i input.m4a -c:a libmp3lame -q:a 2 output.mp3`
- **从视频提取 AAC**：`ffmpeg -i input.mp4 -c:a copy output.m4a`（无损抽取音轨）
- **批量转换**：foobar2000、格式工厂支持批量

## 5. 常见报错与解决

### 问题1：Audacity 打不开 AAC/m4a 文件
**原因**：Audacity 默认不含 FFmpeg 库，而 AAC 解码依赖 FFmpeg。

**解决方法**：
1. 在 Audacity 中安装 FFmpeg 库：编辑 → 首选项 → 库 → FFmpeg → 下载安装
2. 安装后重启 Audacity，即可导入/导出 AAC/m4a
3. 或先用 ffmpeg 命令行转成 WAV 再用 Audacity 编辑

### 问题2：AAC 文件在某些老设备/老车载音响上放不了
**原因**：老设备只支持 MP3，不支持 AAC 解码。

**解决方法**：
1. 转 MP3：用 ffmpeg 或格式工厂转成 MP3（320kbps 保证音质）
2. 老车载音响可升级固件或换支持 AAC 的播放器
3. 买车载 MP3 播放器/USB 解码器
4. 确认设备规格，新设备基本都支持 AAC

### 问题3：AAC 转换后音质下降或出现爆音
**原因**：码率设置过低，或多次有损转换累积损失；音量过高导致削波爆音。

**解决方法**：
1. 用足够码率：AAC 建议 192-256kbps，低于 128kbps 听感明显下降
2. 避免有损转有损：从无损源（FLAC/WAV）直接转 AAC
3. 转换前检查音量峰值，避免超过 0dB（用 Audacity 的"标准化"控制）
4. 用高质量编码器：苹果的 AAC 编码器公认质量最佳，其次 ffmpeg 的 libfdk_aac

---
## 💡 小知识

AAC 是 MP3 的"官方继任者"——由开发 MP3 的 MPEG 组织亲自操刀，目的就是弥补 MP3 的技术短板（高频损失、立体声处理粗糙）。AAC 1997 年问世，苹果是它最大的推手：2003 年 iTunes Store 上线时，乔布斯坚持用 AAC 而非 MP3，并宣称"128kbps AAC 音质等同 192kbps MP3"。事实证明他没吹牛，AAC 确实更高效。今天你听的几乎所有在线视频、流媒体音乐，底层音频基本都是 AAC（封装在 MP4/m4a 里）。有趣的是，虽然 AAC 是"继任者"，MP3 却因先发优势和"无脑兼容"至今没被完全淘汰——专利过期后的 MP3 反而更自由了。但论技术，AAC 已是事实王者。

## 🔗 相关链接

- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [Audacity 官网](https://www.audacityteam.org/)
- [ffmpeg 官网](https://ffmpeg.org/)
- [foobar2000 官网](https://www.foobar2000.org/)
- [.mp3 文件后缀详解](../03-音视频媒体类/mp3.md)
- [.ogg 文件后缀详解](./ogg.md)

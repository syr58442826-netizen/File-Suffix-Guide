# .aiff 文件后缀详解

## 1. 文件定义 & 用途

AIFF 是 **Audio Interchange File Format** 的缩写，是苹果公司在 1988 年开发的音频文件格式。它和 WAV 类似，都是无压缩的线性 PCM 音频格式，音质很高但文件体积大。AIFF 一直是 Mac 平台上专业音频领域的常用格式。

简单来说，AIFF 就是苹果版的 WAV——无损未压缩音频，音质好，体积大。

- **全称**：Audio Interchange File Format
- **类型**：音频文件（无压缩 PCM / 也可压缩为 AIFF-C）
- **开发者**：Apple（苹果）
- **发布年份**：1988年
- **特点**：无损未压缩、音质高、Mac 平台原生支持、与 WAV 同等音质

## 2. 适用场景

- 专业音乐制作和录音（Mac 平台）
- 音频编辑和后期处理（Logic Pro 等苹果专业软件）
- 高品质音乐收藏（追求无损音质）
- 音频素材库和母带存储
- 苹果生态下的音频文件交换

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | VLC 媒体播放器、Audacity、foobar2000 | Adobe Audition、Ableton Live |
| Mac | QuickTime Player（系统自带）、VLC、iTunes/音乐 | Logic Pro、Adobe Audition、Pro Tools |
| Linux | VLC 媒体播放器、Audacity | Ardour、Reaper |

**新手推荐**：
- Mac 用户：系统自带 **QuickTime Player** 和**音乐 App** 直接支持
- 跨平台播放：**VLC 媒体播放器**（全平台免费）
- 免费编辑：**Audacity**（开源音频编辑器，支持 AIFF）
- 专业制作：**Logic Pro**（Mac 专属，苹果出品的专业音频软件）

## 4. 如何编辑、如何导出

### 如何编辑
1. 用 Audacity 打开 .aiff 文件即可编辑（剪切、混音、效果处理）
2. 用 Logic Pro 打开进行专业编辑
3. 编辑操作与 WAV 文件一致
4. 保存时可以选择 AIFF 或其他格式

### 如何导出/转换
- **AIFF 转 WAV**：用 Audacity 或 ffmpeg 转换（`ffmpeg -i input.aiff output.wav`）
- **AIFF 转 MP3**：用 Audacity 或 iTunes/音乐 导出
- **AIFF 转 FLAC**：用 Audacity 或 ffmpeg（无损压缩，体积更小）
- **AIFF 转 AAC/M4A**：用 iTunes/音乐 App 转换（适合移动设备）
- **从 CD 翻录**：iTunes/音乐 默认可翻录 CD 为 AIFF 格式
- **批量转换**：用 ffmpeg 批量处理或 dBpoweramp

## 5. 常见报错与解决

### 问题1：AIFF 文件太大，占满硬盘和手机存储
**原因**：AIFF 是无压缩格式，一首 4 分钟歌曲约 40-50MB，远大于 MP3 的 3-5MB。

**解决方法**：
1. 转为 FLAC 格式（无损压缩，体积减少约 50%）
2. 转为 AAC/M4A 格式（高质量有损压缩，体积减少 80% 以上）
3. 转为 MP3 格式（兼容性最好，体积小）
4. 只在编辑/存档时用 AIFF，日常收听用压缩格式
5. 用 Audacity 或 ffmpeg 批量转换

---

### 问题2：Windows 上打不开 AIFF 文件
**原因**：Windows 系统默认的媒体播放器可能不原生支持 AIFF 格式。

**解决方法**：
1. 用 VLC 媒体播放器打开（免费，支持 AIFF）
2. 用 foobar2000 打开（免费音频播放器）
3. 安装 K-Lite Codec Pack 解码器包后用 WMP 播放
4. 转为 WAV 或 MP3 格式后在 Windows 上播放

---

### 问题3：AIFF 文件在其他播放器或设备上无法播放
**原因**：部分播放器、手机和车载音响不支持 AIFF 格式。

**解决方法**：
1. 转为 MP3 格式（兼容性最强，几乎所有设备支持）
2. 转为 AAC/M4A 格式（苹果设备原生支持，音质好于 MP3）
3. 转为 FLAC 格式（无损压缩，高端播放器支持）
4. 用 Audacity 批量转换格式

---

### 问题4：AIFF 文件损坏或截断，播放时卡顿或有杂音
**原因**：文件传输不完整、存储介质损坏、录音时设备异常等。

**解决方法**：
1. 用 VLC 播放器尝试播放（容错性较好）
2. 用 Audacity 导入原始数据尝试恢复（文件 → 导入 → 原始数据）
3. 用音频修复工具如 iZotope RX（专业音频修复软件）
4. 从备份恢复
5. 如果是录音中断导致，检查录音设备是否有自动保存的临时文件

---

## 💡 小知识

AIFF 格式和 WAV 格式几乎是"双胞胎"——它们都是存储未压缩 PCM 音频数据的容器，音质完全一致，区别只是文件结构和元数据格式。AIFF 是苹果推出的（1988年），WAV 是微软和 IBM 推出的（1991年）。在 Mac 生态中，AIFF 一直是专业音频的首选格式。不过近年来，越来越多的音频工作者开始转向 FLAC（无损压缩）和 ALAC（Apple Lossless），因为它们在保持无损音质的同时大幅减少了文件体积。

## 🔗 相关链接

- [AIFF 格式说明 - 维基百科](https://zh.wikipedia.org/wiki/AIFF)
- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [Audacity 免费音频编辑器](https://www.audacityteam.org/)
- [Logic Pro 官网](https://www.apple.com/cn/logic-pro/)
- [ffmpeg 官网](https://ffmpeg.org/)
- [.wav 格式详解](./wav.md)
- [.flac 格式详解](./flac.md)

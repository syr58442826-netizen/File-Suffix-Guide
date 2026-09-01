# .ogg 文件后缀详解

## 1. 文件定义 & 用途

OGG（准确说是 Ogg Vorbis）是一种**开源免费的有损音频压缩格式**，由 Xiph.org 基金会开发。它对标 MP3，但完全免费开放——任何人都可以免费用，不像 MP3 那样曾有专利收费。Ogg 是容器，Vorbis 是里面的音频编码，二者常被一起称作 OGG。

- **全称**：Ogg Vorbis（Ogg 是容器，Vorbis 是音频编码）
- **类型**：有损音频压缩格式
- **开发者**：Xiph.org 基金会（开源社区）
- **发布年份**：2002 年
- **特点**：开源免费无专利、同等码率音质优于 MP3、支持多声道
- **对比 MP3**：同码率音质更好，但兼容性不如 MP3（部分老设备不支持）

## 2. 适用场景

- **游戏音频**：很多游戏（如 Minecraft）用 OGG 存音效和音乐
- **开源软件/系统**：Linux 系统铃声、开源软件默认音频格式
- **流媒体**：Spotify 早期用 OGG 传输音频
- **网络电台**：Icecast/Shoutcast 网络电台常用格式
- **音乐存储**：追求免费开放格式的人用它替代 MP3
- **语音/播客**：部分播客用 OGG 分发

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | VLC、foobar2000、AIMP、QQ音乐/网易云音乐（部分支持） | Adobe Audition、Audacity |
| Mac | VLC、Cog、IINA | Adobe Audition、Audacity |
| Linux | VLC、Rhythmbox、Audacious、死鱼（DeaDBeeF） | Audacity、Ardour |
| 手机 | VLC、Poweramp（Android） | - |

**新手推荐**：
- 万能播放：**VLC**（跨平台，几乎所有音频都能放）
- Windows 本地听歌：**foobar2000**（轻量、音质好、支持 OGG）
- 免费编辑：**Audacity**（开源，原生支持 OGG 读写）
- 在线播放：现代浏览器（Chrome/Firefox）原生支持 OGG

## 4. 如何编辑、如何导出

### 如何编辑
1. **Audacity**：免费开源，原生支持导入/导出 OGG，可裁剪、混音、加效果
2. **Adobe Audition**：专业音频编辑，支持 OGG
3. **foobar2000**：可转换格式、加标签，但非波形编辑
4. **标签编辑**：用 Mp3tag、MusicBrainz Picard 编辑 OGG 的元数据（标题/作者/封面）

### 如何导出/转换
- **Audacity 导出 OGG**：文件 → 导出 → 导出为 OGG
- **MP3 转 OGG**：用 foobar2000、格式工厂、ffmpeg 转换
- **ffmpeg 命令行**：`ffmpeg -i input.mp3 -c:a libvorbis -q:a 6 output.ogg`
- **OGG 转 MP3**：`ffmpeg -i input.ogg -c:a libmp3lame -q:a 2 output.mp3`
- **批量转换**：foobar2000 或格式工厂支持批量

## 5. 常见报错与解决

### 问题1：OGG 文件在 Windows Media Player 里放不出来
**原因**：Windows Media Player 默认不支持 OGG（微软偏好自家 WMA 格式）。

**解决方法**：
1. 装 **VLC** 或 **foobar2000**，直接能放 OGG
2. 装 OGG 编解码器包（如 K-Lite Codec Pack），WMP 也能播放
3. 现代浏览器（Chrome/Firefox/Edge）可直接拖入 OGG 播放
4. 转 MP3 后用任何播放器都能放

### 问题2：OGG 转成 MP3 后音质下降明显
**原因**：OGG 本身已是有损压缩，转 MP3 是"二次有损压缩"，会累积损失。

**解决方法**：
1. 尽量从原始无损源（FLAC/WAV）直接转目标格式，避免有损转有损
2. 必须转时用高码率 MP3（320kbps）减少损失
3. OGG 用高质量编码（Vorbis quality 6-8）也能减小转换损失
4. 保留 OGG 原件，只转一份 MP3 备用，不要反复转

### 问题3：OGG 文件元数据（标签）显示乱码
**原因**：标签编码不一致（GBK vs UTF-8），跨平台/跨语言时易乱码。

**解决方法**：
1. 用 **Mp3tag** 打开，把标签编码统一改为 UTF-8
2. 用 **MusicBrainz Picard** 重新匹配并写入标签
3. foobar2000 的"属性"里可批量重写标签为 UTF-8
4. 转格式时用 foobar2000，会自动处理编码

---
## 💡 小知识

OGG 的诞生是一场"专利自由"运动。1990 年代 MP3 一统天下，但 MP3 背后有 Thomson 和 Fraunhofer 的专利，1998 年他们宣布向开发者收专利费。开源社区不干了——Xiph.org 推出 Ogg Vorbis，誓要做"完全免费的 MP3 替代品"。"Ogg"这个名字来自网络游戏 Netrek，指一种战术策略；"Vorbis"则来自小说《Small Gods》里的角色。虽然 OGG 音质确实优于 MP3，但 MP3 的先发优势太强，OGG 始终没能在主流消费市场取代 MP3。不过在游戏和开源世界里，OGG 是当之无愧的音频标准。Xiph.org 后来还开发了 Opus（更现代的编码）和 FLAC（无损），都是开源音频的中坚。

## 🔗 相关链接

- [Xiph.org 基金会](https://xiph.org/)
- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [Audacity 官网](https://www.audacityteam.org/)
- [foobar2000 官网](https://www.foobar2000.org/)
- [.opus 文件后缀详解](./opus.md)
- [.mp3 文件后缀详解](../03-音视频媒体类/mp3.md)

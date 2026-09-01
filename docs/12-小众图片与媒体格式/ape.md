# .ape 文件后缀详解

## 1. 文件定义 & 用途

APE 是 **Monkey's Audio** 无损音频格式的扩展名，由 Matthew T. Ashland 在 2000 年开发。它是一种**无损压缩音频**——压缩后体积比 WAV 小约一半，但解压后和原始 WAV 一模一样，不丢任何音质。它比 FLAC 压缩率更高（体积更小），但代价是编解码更慢。

- **全称**：Monkey's Audio
- **类型**：无损音频压缩格式
- **开发者**：Matthew T. Ashland
- **发布年份**：2000 年
- **特点**：无损（解压=原 WAV）、压缩率高于 FLAC、编解码较慢、常配 CUE 分轨
- **对比 FLAC**：APE 压缩率更高（体积更小），但解码更慢、开源程度不如 FLAC

国内 APE 曾非常流行，因为配合 CUE 文件可以把整张 CD 压成一个 APE + 一个 CUE（分轨信息），方便分享整张专辑。

## 2. 适用场景

- **无损音乐收藏**：发烧友收藏 CD 级音质音乐
- **整张专辑存档**：一张 CD 一个 APE + 一个 CUE 分轨文件
- **音质敏感场景**：古典乐、爵士等对音质要求高的音乐
- **音频备份**：CD 翻录的无损备份
- **国内音乐圈**：早期电驴、论坛分享无损音乐的常见格式

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | foobar2000、AIMP、VLC、QQ音乐（部分）、酷狗（部分） | Adobe Audition、JRiver Media Center |
| Mac | VLC、Cog、XLD | Adobe Audition、JRiver Media Center |
| Linux | VLC、deadbeef、ffmpeg | - |

**新手推荐**：
- Windows 播放：**foobar2000**（对 APE+CUE 支持最好，可分轨显示）
- 跨平台播放：**VLC**
- 转换工具：**foobar2000**（Windows）或 **XLD**（Mac）或 **ffmpeg**
- 注意：APE 常配 .cue 文件，播放时要用支持 CUE 的播放器才能分轨

## 4. 如何编辑、如何导出

### 如何编辑
1. **foobar2000**：可播放 APE+CUE，按 CUE 分轨；可转换、加标签
2. **Audacity**：需额外支持才能导入 APE（通常先转 WAV）
3. **CUE 分轨**：用 foobar2000 打开 CUE 文件，可单独转换每首歌
4. **标签编辑**：Mp3tag 可编辑 APE 和 CUE 的元数据

### 如何导出/转换
- **APE 转 FLAC**（推荐）：`ffmpeg -i input.ape output.flac`，FLAC 兼容性更好
- **APE 转 WAV**：解压回无损 WAV
- **APE 转 MP3/AAC**：`ffmpeg -i input.ape -c:a libmp3lame -q:a 0 output.mp3`
- **分轨转换**：用 foobar2000 打开 CUE → 选中歌曲 → 右键转换
- **CD 翻录为 APE**：用 Exact Audio Copy（EAC）翻录，选 Monkey's Audio

## 5. 常见报错与解决

### 问题1：APE 文件只有一首，没有分轨，整张专辑成一个文件
**原因**：APE 通常配一个 .cue 文件记录每首歌的起止时间，缺少 CUE 就无法分轨。

**解决方法**：
1. 找到配套的 .cue 文件，和 APE 放同一目录，用 foobar2000 打开 CUE 即可分轨
2. 没有 CUE：可手动找分轨信息，或用音频编辑软件（Audacity）按静音手动切分
3. foobar2000 直接打开 APE 也能播放，只是不能选曲
4. 网上搜索同名专辑的 CUE 文件补上

### 问题2：APE 文件在 Mac/手机上播放卡顿或不支持
**原因**：APE 解码消耗 CPU 较多，且移动端/部分播放器原生不支持 APE。

**解决方法**：
1. 用 **VLC** 播放（跨平台支持 APE）
2. 转 **FLAC**（兼容性远好于 APE，移动端支持广）：`ffmpeg -i input.ape output.flac`
3. 移动端装支持 APE 的播放器（如 Poweramp）
4. 长期方案：把 APE 音乐库统一转成 FLAC，省心

### 问题3：APE 转 MP3 后文件名/标签混乱
**原因**：从 APE+CUE 转换时，标签信息来自 CUE，CUE 编码或信息不全会导致混乱。

**解决方法**：
1. 转换前用 foobar2000 打开 CUE，检查歌曲信息是否正确
2. 用 Mp3tag 编辑 CUE 和转换后文件的标签，统一为 UTF-8 编码
3. CUE 文件编码问题（GBK/UTF-8）会导致中文乱码，转码后再用
4. 用 MusicBrainz Picard 自动匹配专辑信息补全标签

### 问题4：APE 文件损坏，无法播放或转换中断
**原因**：APE 压缩率高但容错性差，文件任何一处损坏都可能导致后续无法解码。

**解决方法**：
1. 用 VLC 尝试播放（容错性较好，可能能播到损坏点之前）
2. 用 ffmpeg 尝试转换，加 `-err_detect ignore_err` 忽略错误：`ffmpeg -err_detect ignore_err -i input.ape output.wav`
3. 重新下载或从原 CD 重新翻录
4. 这也是 APE 不如 FLAC 的地方——FLAC 有帧级别的容错，APE 损坏基本没救

---
## 💡 小知识

APE 在国内一度比 FLAC 还流行，这有点反直觉——毕竟 FLAC 开源、兼容性好。原因有两个：一是早年国内网络带宽小，APE 压缩率更高（体积更小）更利于电驴/BT 传播；二是 Exact Audio Copy（EAC）默认推荐 APE，国内翻 CD 的人多跟着用了。APE+CUE 的"整盘一张"模式也契合"整张专辑分享"的需求。但随着移动设备和 Mac 普及，APE 兼容性差、解码慢、容错差的缺点暴露，FLAC 逐渐反超。如今国际无损音乐圈基本是 FLAC 的天下，APE 沦为"国内老资料"的代名词。如果你有 APE 收藏，建议转成 FLAC 一劳永逸。

## 🔗 相关链接

- [Monkey's Audio 官网](https://www.monkeysaudio.com/)
- [foobar2000 官网](https://www.foobar2000.org/)
- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [XLD（Mac 音频转换）](https://tmkk.moo.jp/xld/index_e.html)
- [ffmpeg 官网](https://ffmpeg.org/)

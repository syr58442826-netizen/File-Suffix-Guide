# .mpg 文件后缀详解

## 1. 文件定义 & 用途

MPG 是 **MPEG 视频**的通用扩展名，指基于 MPEG 标准压缩的视频文件。它涵盖 MPEG-1 和 MPEG-2 两代标准，是 VCD、DVD 时代的视频格式主力。你早年看的 VCD、DVD，以及数字电视广播，底层都是 MPEG。

- **全称**：MPEG video（MPEG-1 / MPEG-2）
- **类型**：视频压缩格式
- **开发者**：MPEG 组织（ISO/IEC）
- **发布年份**：MPEG-1（1993）、MPEG-2（1995）
- **特点**：VCD/DVD 标准格式、兼容性极广、被早期设备广泛支持
- **常见扩展名**：.mpg、.mpeg、.mpe、.vob（DVD 用）

注意区分：MPG（MPEG-1/2）和 MP4（MPEG-4）是不同标准，别搞混。MPG 是老标准，MP4 是现代标准。

## 2. 适用场景

- **VCD/DVD 视频**：VCD 用 MPEG-1，DVD 用 MPEG-2
- **数字电视广播**：有线/卫星电视多用 MPEG-2
- **老视频资料**：2000 年代早期的视频文件
- **DVD 翻录/备份**：DVD 的 .vob 本质是 MPEG-2
- **老设备播放**：老 DVD 机、车载音响、老电视支持的格式

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | VLC、Windows Media Player（系统自带）、MPC-HC、PotPlayer | Adobe Premiere Pro、PowerDVD |
| Mac | VLC、QuickTime Player（部分）、mpv、IINA | Adobe Premiere Pro |
| Linux | VLC、mpv、Totem | Kdenlive、DaVinci Resolve |
| 手机 | VLC、MX Player（Android） | - |

**新手推荐**：
- 通用播放：**VLC**（跨平台，完美支持 MPEG-1/2）
- Windows 自带：**Windows Media Player** 支持 MPG
- 播放 DVD：**VLC** 或 **PotPlayer**（Windows）
- 转换工具：**ffmpeg**、**HandBrake**

## 4. 如何编辑、如何导出

### 如何编辑
1. **Adobe Premiere Pro**：支持导入 MPG 编辑
2. **DaVinci Resolve**：支持 MPG 导入
3. **Kdenlive/Shotcut**：免费开源，支持 MPG
4. **会声会影**：老牌消费级剪辑，对 MPG/DVD 友好
5. **DVD 翻录**：用 MakeMKV 翻录 DVD，或 HandBrake 转码

### 如何导出/转换
- **MPG 转 MP4**：`ffmpeg -i input.mpg -c:v libx264 -c:a aac output.mp4`
- **DVD VOB 转 MP4**：`ffmpeg -i input.vob -c:v libx264 -c:a aac output.mp4`
- **MP4 转 DVD 格式**：用 DVD 制作软件（如 DVDStyler、Burn）
- **HandBrake**：图形界面转码，适合 DVD 转 MP4
- **批量转换**：ffmpeg 脚本或格式工厂

## 5. 常见报错与解决

### 问题1：MPG 视频播放时画面有横向条纹/交错线
**原因**：MPEG-2 视频可能是隔行扫描（interlaced，用于老电视），在逐行显示器上出现梳状条纹。

**解决方法**：
1. 用 VLC 播放，开启"去隔行"（Deinterlace）：视频 → 去隔行 → 开启/自动
2. 转换时加去隔行滤镜：`ffmpeg -i input.mpg -vf yadif -c:v libx264 output.mp4`
3. HandBrake 转换时勾选"去隔行"（Deinterlace: Fast/Yadif）
4. 这是老视频的通病，去隔行后画面更顺滑

### 问题2：DVD 的 VOB 文件播放/转换时断点不连续
**原因**：DVD 一部电影常被拆成多个 1GB 的 VOB 文件（VTS_01_1.VOB、VTS_01_2.VOB...），单独处理会有断点。

**解决方法**：
1. 用 MakeMKV 整片翻录成一个 MKV，避免拼接问题
2. ffmpeg 拼接：先建 filelist.txt 列出各 VOB，`ffmpeg -f concat -i filelist.txt -c copy output.mpg`
3. 用 VLC 直接打开 VIDEO_TS.IFO 播放整片
4. HandBrake 打开 DVD 源可直接选整片转码

### 问题3：MPG 文件体积很大，想压缩
**原因**：MPEG-1/2 压缩效率低，同画质体积比 H.264 大好几倍。

**解决方法**：
1. 转 H.264 MP4：`ffmpeg -i input.mpg -c:v libx264 -crf 23 -c:a aac output.mp4`，体积大幅缩小
2. 转 H.265 MP4 压缩更多：`-c:v libx265 -crf 28`
3. HandBrake 图形界面转换，选 H.264/H.265，调整 CRF
4. 老资料批量转 MP4 既省空间又提升兼容性

### 问题4：老 MPG 文件只有画面没声音
**原因**：MPEG-1 视频可能用 MPEG-1 Audio Layer II 音频，部分播放器不支持；或音频流损坏。

**解决方法**：
1. 用 **VLC** 播放（支持 MPEG 音频）
2. 转 MP4 时音频转 AAC：`ffmpeg -i input.mpg -c:v copy -c:a aac output.mp4`
3. 检查文件是否有音频流：`ffmpeg -i input.mpg` 查看流信息
4. 音频流损坏则需重新获取源文件

---
## 💡 小知识

MPG（MPEG-1/2）是数字视频的"祖师爷"。1993 年的 MPEG-1 让 VCD 成为可能——一张光盘存 74 分钟视频，虽然画质一般，但让家庭看视频摆脱了录像带。1995 年的 MPEG-2 更进一步，支撑了 DVD 和数字电视广播，画质接近模拟电视。当年中国人家里堆的 VCD、DVD 光盘，底层全是 MPEG。MPEG-2 至今仍用于数字电视广播（有线电视、卫星电视）。有趣的是，MPG 虽老，但它的"隔行扫描"设计是为老显像管电视优化的，今天在液晶/手机上看会有条纹，这就是为什么需要"去隔行"。MPG 是视频格式演进的起点，没有它就没有后来的 MP4/AV1。

## 🔗 相关链接

- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [ffmpeg 官网](https://ffmpeg.org/)
- [HandBrake 官网](https://handbrake.fr/)
- [MakeMKV（DVD/蓝光翻录）](https://www.makemkv.com/)
- [.mp4 文件后缀详解](../03-音视频媒体类/mp4.md)

# .vob 文件后缀详解

## 1. 文件定义 & 用途

VOB 是 **Video Object** 的缩写，是 DVD 视频光盘的核心文件格式。它包含了 DVD 中的视频、音频、字幕和菜单数据。当你把一张 DVD 光盘放进电脑查看时，会在 `VIDEO_TS` 文件夹中看到一系列 .vob 文件。

简单来说，.vob 就是 DVD 光盘上的视频文件——一个标准 DVD 电影通常由几个 VOB 文件组成（每个最大 1GB）。

- **全称**：Video Object
- **类型**：视频容器格式（基于 MPEG-2 Program Stream）
- **开发者**：DVD Forum（DVD 论坛）
- **发布年份**：1995年（随 DVD 标准发布）
- **特点**：包含视频（MPEG-2）、多音轨、多字幕、菜单导航
- **限制**：单个 VOB 文件最大约 1GB

## 2. 适用场景

- DVD 光盘中的视频文件
- 从 DVD 光盘翻录/备份的电影和视频
- 传统家庭影院播放（DVD 播放机）
- 旧视频档案的播放和转存
- 需要多音轨/多字幕的视频内容（VOB 支持最多 9 条音轨和 32 条字幕）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | VLC 媒体播放器、PotPlayer、KMPlayer | PowerDVD、WinDVD |
| Mac | VLC 媒体播放器、IINA、MPlayerX | Apple DVD Player |
| Linux | VLC 媒体播放器、MPV、Totem | - |

**新手推荐**：
- 万能播放器：**VLC 媒体播放器**（全平台免费，完美支持 VOB）
- Windows 用户：**PotPlayer**（功能强大，支持 VOB）
- 专业播放：**PowerDVD**（专业 DVD 播放软件，支持菜单导航）

## 4. 如何编辑、如何导出

### 如何编辑
1. 直接用 VLC 播放 VOB 文件即可
2. 剪辑 VOB 建议先转为 MP4 再编辑，直接剪辑 VOB 容易导致音画不同步
3. 用 MPEG Streamclip（免费）可以简单剪切 VOB

### 如何导出/转换
- **VOB 转 MP4**（推荐）：
  - 用 HandBrake（免费开源）：打开 VOB 文件 → 选择 MP4 → 开始转换
  - 用格式工厂（免费）
  - 用 ffmpeg：
    ```bash
    ffmpeg -i input.vob -c:v libx264 -c:a aac output.mp4
    ```
- **合并多个 VOB**：DVD 电影通常分成多个 VOB（VTS_01_1.VOB, VTS_01_2.VOB...），合并时用 ffmpeg 或 MPEG Streamclip
- **从 DVD 翻录**：用 MakeMKV（免费试用）或 HandBrake 直接翻录 DVD 为 MKV/MP4
- **保留字幕和音轨**：转成 MKV 格式可以保留所有音轨和字幕

## 5. 常见报错与解决

### 问题1：VOB 文件只有部分播放，菜单导航不工作
**原因**：单独复制了 VOB 文件，缺少 DVD 的 IFO 和 BUP 文件（菜单和导航信息）。

**解决方法**：
1. 如果只需要看视频内容，用 VLC 直接打开 VOB 文件即可
2. 如果需要菜单导航，需要复制整个 VIDEO_TS 文件夹（包括 .ifo、.bup、.vob 文件）
3. 用 VLC 打开整个 VIDEO_TS 文件夹可以模拟 DVD 菜单
4. 或者用 MakeMKV 翻录为 MKV 格式，保留章节和音轨

---

### 问题2：VOB 转换为 MP4 后音画不同步
**原因**：VOB 中视频和音频的时间戳处理方式特殊，直接转码可能导致同步问题。

**解决方法**：
1. 使用 HandBrake 转换（它对 VOB/MPEG-2 的处理比较成熟）
2. 在 ffmpeg 中指定同步处理：
   ```bash
   ffmpeg -i input.vob -async 1 -vsync 1 -c:v libx264 -c:a aac output.mp4
   ```
3. 先合并多个 VOB 文件为一个完整文件再转码
4. 尝试用不同工具（如格式工厂、Avidemux）转换

---

### 问题3：VOB 文件太大，占满硬盘空间
**原因**：VOB 使用 MPEG-2 编码，压缩率远低于现代的 H.264/H.265，一个 DVD 电影通常 4-8GB。

**解决方法**：
1. 用 HandBrake 转为 H.264/HEVC MP4，体积可缩小到原来的 1/3 到 1/5
2. 设置合适的编码参数（CRF 20-23 视觉无损）
3. 只保留主要音轨，删除不需要的语言音轨
4. 删除原 VOB 文件前确认转换后的视频质量满意

---

### 问题4：播放 VOB 时字幕不显示
**原因**：VOB 中的字幕是 DVD 图形字幕（位图），部分播放器不支持显示。

**解决方法**：
1. 用 VLC 播放器打开（支持 DVD 字幕）
2. 在 VLC 中：字幕 → 字幕轨 → 选择需要的字幕
3. 转换为 MKV 时可以提取字幕（用 MakeMKV 或 ffmpeg）
4. 转为 MP4 时字幕可能丢失，需要单独提取字幕并嵌入

---

## 💡 小知识

DVD 的文件结构其实很有规律：VIDEO_TS 文件夹中，`.VOB` 是音视频数据，`.IFO` 是导航和控制信息（告诉播放器哪个菜单在哪、章节怎么分），`.BUP` 是 IFO 的备份。一个标准的 DVD 电影会被拆分成多个最大约 1GB 的 VOB 文件（VTS_01_1.VOB、VTS_01_2.VOB...），播放器会自动连续播放。在流媒体时代之前，DVD 是家庭影院的绝对主流，而 VOB 就是承载这些电影的核心文件格式。

## 🔗 相关链接

- [VOB 格式说明 - 维基百科](https://zh.wikipedia.org/wiki/VOB)
- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [HandBrake 视频转换工具](https://handbrake.fr/)
- [MakeMKV - DVD 翻录工具](https://www.makemkv.com/)
- [ffmpeg 官网](https://ffmpeg.org/)
- [.mp4 格式详解](./mp4.md)

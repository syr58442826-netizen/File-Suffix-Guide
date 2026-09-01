# .webm 文件后缀详解

## 1. 文件定义 & 用途

WebM 是谷歌在 2010 年推出的**开放免费视频格式**，专为网页视频设计。它基于 Matroska（MKV）容器，搭配 VP8/VP9/AV1 视频编码和 Vorbis/Opus 音频编码，全部开源免费，旨在打破 H.264/H.265 的专利收费壁垒。

- **全称**：WebM
- **类型**：开放视频容器格式
- **开发者**：Google（基于 Matroska 容器）
- **发布年份**：2010 年
- **特点**：完全开源免费、专为网页优化、支持 VP8/VP9/AV1 视频编码
- **对比 MP4**：WebM 免费开放，MP4 的 H.264/H.265 涉及专利费；WebM 在网页端支持好，MP4 通用性更广

WebM 是 HTML5 视频时代的"开放选择"，YouTube、维基百科大量使用 WebM。

## 2. 适用场景

- **网页视频**：HTML5 `<video>` 标签的开放格式选择
- **YouTube 等视频平台**：YouTube 高清视频常用 VP9/AV1 编码的 WebM
- **开源项目视频**：维基百科、Mozilla 等开源生态的视频
- **动画贴图/GIF 替代**：短循环动画用 WebM 比 GIF 体积小、画质好
- **屏幕录制/演示**：部分录屏软件支持 WebM 输出
- **AV1 视频容器**：AV1 编码常封装在 WebM 中用于网页

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | VLC、mpv、Edge/Chrome 浏览器、MPC-HC | Adobe Premiere Pro（新版）、DaVinci Resolve |
| Mac | VLC、mpv、IINA、Safari/Chrome | Adobe Premiere Pro、DaVinci Resolve、Final Cut Pro（需转换） |
| Linux | VLC、mpv、Firefox/Chrome、Totem | DaVinci Resolve、Kdenlive |
| 手机 | VLC、系统浏览器 | - |

**新手推荐**：
- 通用播放：**VLC** 或 **mpv**
- 网页播放：**Chrome/Edge/Firefox** 浏览器原生支持
- 免费剪辑：**DaVinci Resolve**（免费版支持 WebM）或 **Kdenlive**（Linux）
- 转换工具：**ffmpeg**、**HandBrake**

## 4. 如何编辑、如何导出

### 如何编辑
1. **DaVinci Resolve**：免费版支持导入 WebM（VP9）编辑
2. **Kdenlive**：开源剪辑软件，支持 WebM
3. **Adobe Premiere Pro**：2020+ 版本支持 WebM 导入导出
4. **Shotcut**：免费开源，跨平台，支持 WebM
5. **OBS Studio**：录屏可直接输出 WebM

### 如何导出/转换
- **转 MP4**：`ffmpeg -i input.webm -c:v libx264 -c:a aac output.mp4`
- **MP4 转 WebM**：`ffmpeg -i input.mp4 -c:v libvpx-vp9 -c:a libopus output.webm`
- **HandBrake**：图形界面转换，可选 WebM 输出
- **压缩 WebM**：用 VP9 编码 `-crf 33 -b:v 0` 控制质量
- **GIF 转 WebM**：`ffmpeg -i input.gif -c:v libvpx-vp9 -b:v 0 -crf 35 output.webm`（体积大减）

## 5. 常见报错与解决

### 问题1：WebM 在某些浏览器（如老 Safari）播放不了
**原因**：Safari 对 WebM 支持较晚（Safari 14+ 才部分支持 VP9，AV1 支持更晚）。

**解决方法**：
1. 网页提供 MP4 备选源：`<video><source src="video.webm"><source src="video.mp4"></video>`
2. 桌面用 Chrome/Edge/Firefox 播放，这些浏览器原生支持
3. 检查 WebM 用的编码：VP8 兼容性最好，VP9 次之，AV1 需要新浏览器
4. 必须全兼容就提供 H.264 MP4 作为兜底

### 问题2：WebM 转 MP4 后体积变大很多
**原因**：WebM 常用 VP9/AV1 高效编码，转 H.264 MP4 同画质体积会变大。

**解决方法**：
1. 接受体积增加，或转成 H.265 MP4（HEVC）体积接近 VP9
2. 用两遍编码控制码率：`ffmpeg -i input.webm -c:v libx264 -crf 23 -preset slow output.mp4`
3. 适当降低分辨率或码率
4. 如不需 MP4，保留 WebM 体积最小

### 问题3：Premiere/Final Cut 导入 WebM 失败
**原因**：部分剪辑软件版本对 WebM/VP9 支持不全，需插件或转换。

**解决方法**：
1. 用 ffmpeg 先转成 MP4（H.264）再导入剪辑
2. Premiere 装 WebM 插件（如 VFMWebM）
3. Final Cut Pro 用户：转成 ProRes 或 MP4 再编辑
4. 或用免费剪辑 DaVinci Resolve / Kdenlive，对 WebM 支持更好

### 问题4：WebM 视频有画面没声音
**原因**：WebM 音频通常用 Opus 或 Vorbis，部分播放器不支持。

**解决方法**：
1. 用 **VLC** 播放（支持 Opus/Vorbis 音轨）
2. 转 MP4 时音频转 AAC：`ffmpeg -i input.webm -c:v copy -c:a aac output.mp4`（视频不变，只转音频）
3. 检查 WebM 音轨编码，确认播放器支持
4. 现代浏览器播放 WebM 不应有此问题

---
## 💡 小知识

WebM 是谷歌"开放 Web 视频战略"的核心。2010 年谷歌收购 On2 公司，拿到 VP8 编码后立刻开源，推出 WebM 对抗 H.264 的专利收费。这一举动被开源社区视为英雄行为——H.264 每台设备要交专利费，对免费软件和网页视频是沉重负担。WebM 配合 HTML5 的 `<video>` 标签，让网页摆脱 Flash 插件，直接原生播放视频。YouTube 率先用 WebM 传输高清视频，带动整个行业跟进。后来 WebM 升级到 VP9（压缩率接近 H.265），再到 AV1（开源且超越 H.265）。今天 WebM/AV1 已是 YouTube 4K/8K 视频的主力格式。可以说，没有 WebM 这步棋，网页视频可能至今被专利格式卡脖子。

## 🔗 相关链接

- [WebM 官方网站](https://www.webmproject.org/)
- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [ffmpeg 官网](https://ffmpeg.org/)
- [HandBrake 官网](https://handbrake.fr/)
- [.mp4 文件后缀详解](../03-音视频媒体类/mp4.md)

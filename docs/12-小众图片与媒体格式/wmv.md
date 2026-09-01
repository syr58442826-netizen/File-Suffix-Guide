# .wmv 文件后缀详解

## 1. 文件定义 & 用途

WMV 是 **Windows Media Video** 的缩写，微软开发的视频压缩格式，2000 年代曾是 Windows 生态的主力视频格式。它集成在 Windows Media Player 中，主打"同画质体积比 MPEG-2 小"，并支持 DRM 版权保护。

- **全称**：Windows Media Video
- **类型**：视频压缩格式（常封装在 ASF 容器，扩展名 .wmv）
- **开发者**：Microsoft
- **发布年份**：1999-2000 年
- **特点**：与 Windows 集成、支持 DRM、低码率下表现不错、WMV HD 高清变体
- **现状**：被 MP4/H.264 取代，但在老资料、企业内部视频、部分在线课程中仍存在

WMV 早年很流行，因为 Windows 自带播放，不用装额外软件。但随着 MP4 通用化和跨平台需求增加，WMV 逐渐边缘化。

## 2. 适用场景

- **Windows 老视频资料**：2000 年代用 WMP 录制/转换的视频
- **企业内部培训视频**：早期企业用 WMV+DRM 保护培训内容
- **在线课程/课件**：部分老课件用 WMV
- **屏幕录制**：早期录屏软件默认 WMV 输出
- **低带宽视频传输**：低码率 WMV 适合早期窄带网络

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Windows Media Player（系统自带）、VLC、mpv、MPC-HC | Adobe Premiere Pro（需插件） |
| Mac | VLC、Flip4Mac（QuickTime 组件）、mpv | - |
| Linux | VLC、mpv、ffplay | - |
| 手机 | VLC（iOS/Android） | - |

**新手推荐**：
- Windows 用户：**Windows Media Player** 原生支持；**VLC** 更通用
- Mac/Linux 用户：**VLC**（系统不原生支持 WMV）
- 长期方案：把 WMV 转 MP4，通用性更好

## 4. 如何编辑、如何导出

### 如何编辑
1. **Adobe Premiere Pro**：需装 Windows Media 插件才能导入 WMV
2. **Windows Movie Maker**（老 Windows 自带）：原生编辑 WMV，但已停更
3. **VSDC Free Video Editor**（Windows）：免费，支持 WMV
4. **Shotcut/Kdenlive**：跨平台免费剪辑，部分支持 WMV
5. **录屏输出**：OBS/Bandicam 可输出 WMV

### 如何导出/转换
- **WMV 转 MP4**：`ffmpeg -i input.wmv -c:v libx264 -c:a aac output.mp4`
- **MP4 转 WMV**：`ffmpeg -i input.mp4 -c:v wmv2 -c:a wmav2 output.wmv`
- **HandBrake**：不支持 WMV 输出，但可转成 MP4
- **格式工厂**：图形界面，支持 WMV 互转
- **批量转换**：ffmpeg 脚本或格式工厂

## 5. 常见报错与解决

### 问题1：Mac/Linux 上打不开 WMV
**原因**：WMV 是微软格式，Mac/Linux 系统默认不支持。

**解决方法**：
1. 装 **VLC** 播放器，跨平台支持 WMV
2. Mac 装 **Flip4Mac** 组件让 QuickTime 支持 WMV
3. 用 ffmpeg 转 MP4：`ffmpeg -i input.wmv output.mp4`
4. 在线转换工具转格式

### 问题2：WMV 文件播放时提示"需要许可证"
**原因**：文件带微软 DRM 版权保护，只能在授权设备播放。

**解决方法**：
1. 用原购买账号授权的 Windows 电脑播放
2. 微软 DRM 服务已部分停用，老 DRM WMV 基本无法在非授权设备播放
3. 非法破解 DRM 违法，不建议
4. 教训：避免购买 DRM 锁定的视频，选 MP4 无 DRM 格式

### 问题3：WMV 转 MP4 后音画不同步或花屏
**原因**：WMV 的帧率/时间戳处理与 MP4 不同，转换工具处理不当导致不同步。

**解决方法**：
1. 用 ffmpeg 转换并重设时间戳：`ffmpeg -fflags +genpts -i input.wmv -c:v libx264 -c:a aac output.mp4`
2. 转换前先用 VLC 播放确认原文件是否正常
3. 尝试不同转换工具（格式工厂、HandBrake 预转）
4. 花屏可能是原文件损坏，重新获取源文件

### 问题4：老 WMV 文件在现代系统上播放卡顿
**原因**：老 WMV 编码（WMV7/WMV8）在新硬件上无硬件解码，纯软件解码卡顿。

**解决方法**：
1. 转 MP4（H.264）后播放，硬件解码流畅
2. 用 VLC 播放（软件解码优化较好）
3. 升级 WMV 到 WMV9/VC-1 编码（有硬件解码支持）
4. 老资料批量转 MP4 一劳永逸

---
## 💡 小知识

WMV 是微软"称霸数字视频"的尝试。2000 年代初，微软想让 WMV 成为数字视频的 Windows——无处不在、绑定生态。WMV HD（高清版）曾和 HD DVD 阵营合作，想把蓝光打趴。微软甚至拉来好莱坞片商支持 WMV DRM。但历史重演：苹果和开源社区推动的 H.264/MP4 更开放跨平台，微软的封闭策略再次落败。WMV 的 DRM 生态在 iPod/MP4 潮流下崩溃，WMV HD 也随 HD DVD 败给蓝光而式微。今天 WMV 只剩"历史遗留"价值。微软自己也转向支持 MP4/H.264，Windows 10/11 默认推荐 MP4。WMV 是又一个"巨头押注封闭格式却输给开放方案"的教科书案例，和它的姐妹 WMA 命运如出一辙。

## 🔗 相关链接

- [VLC 媒体播放器](https://www.videolan.org/vlc/)
- [ffmpeg 官网](https://ffmpeg.org/)
- [格式工厂官网](http://www.pcfreetime.com/)
- [.mp4 文件后缀详解](../03-音视频媒体类/mp4.md)
- [.wma 文件后缀详解](./wma.md)

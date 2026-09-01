# .magnet 文件后缀详解

## 1. 文件定义 & 用途

首先要澄清一个核心概念：**.magnet 严格来说不是一个文件后缀，而是一种"链接协议"——磁力链接（Magnet Link）**。它本质上是一段 URI（统一资源标识符），形如 `magnet:?xt=urn:btih:哈希值...`，用来通过内容哈希定位资源，而非依赖服务器上的文件地址。

简单来说，磁力链接就是一段"资源身份证号"，BT 客户端拿到它后，去 P2P 网络里通过哈希找到拥有对应内容的人，再下载拼凑。它和 .torrent 的区别：磁力链接是一段文本/链接，.torrent 是一个小文件；磁力链接不依赖 Tracker 服务器，靠 DHT 分布式网络找资源。

> ⚠️ **法律与安全提醒**：与 .torrent 一样，磁力链接技术本身是中性的 P2P 定位协议。但通过磁力链接下载/分享受版权保护的内容（影视、软件、游戏）属违法行为。磁力链接来源不明时可能下载到恶意软件，务必从可信源获取，下载后用杀毒软件扫描。

**主要用途：**
- 通过 BT 客户端下载合法的 P2P 资源
- 不依赖 Tracker 服务器的资源定位
- 在网页/聊天里以文本形式分享资源（无需下载 .torrent 文件）
- 开源资源、公开数据集的分享

## 2. 适用场景

- 没有现成 .torrent 文件，只有磁力链接时下载资源
- 分享资源时只需发一段链接文本（不用上传 .torrent 文件）
- 资源在 DHT 网络中广泛分布，靠哈希即可找到

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [qBittorrent](https://www.qbittorrent.org/)、[Transmission](https://transmissionbt.com/)、aria2 | [BitComet](https://www.bitcomet.com/)、迅雷 |
| Mac | [qBittorrent](https://www.qbittorrent.org/)、[Transmission](https://transmissionbt.com/) | [BitComet](https://www.bitcomet.com/) |
| Linux | [qBittorrent](https://www.qbittorrent.org/)、[Transmission](https://transmissionbt.com/)、aria2 | Deluge |

**新手推荐：** qBittorrent（开源免费、跨平台、无广告、支持磁力链接）。需要命令行/脚本化可用 aria2。

## 4. 如何编辑、如何导出

### 使用方法（下载）

**方法一：复制磁力链接到 BT 客户端**
1. 复制完整的磁力链接（以 `magnet:?xt=urn:btih:` 开头的那段文本）
2. 打开 qBittorrent
3. 文件 → 添加磁力链接（Ctrl+M 或 Add Torrent Link）
4. 粘贴链接 → 确认 → 选择保存路径 → 开始下载
5. 客户端通过 DHT 找到节点后开始下载

**方法二：浏览器点击磁力链接**
1. 在浏览器里点击 `magnet:` 开头的链接
2. 浏览器会询问"用什么程序打开"
3. 选择你的 BT 客户端（qBittorrent 等）
4. 客户端自动接管，弹出下载确认

**方法三：命令行 aria2**
```bash
# 安装 aria2（跨平台）
# Mac: brew install aria2
# Linux: sudo apt install aria2

# 下载磁力链接
aria2c "magnet:?xt=urn:btih:你的哈希值..."
```

### 磁力链接的结构（理解它）

一个典型磁力链接长这样：
```
magnet:?xt=urn:btih:08ada5a7a674c2e3a2b5b5b5b5b5b5b5b5b5b5b5
&dn=ubuntu-22.04.iso
&tr=https://tracker.example.com/announce
&xl=3000000000
```
- `xt`：资源的哈希（urn:btih: 后是 Info Hash，是定位核心）
- `dn`：显示名（资源名，仅展示用）
- `tr`：Tracker 地址（可选，有则加速）
- `xl`：文件大小（可选，仅参考）

> 关键是 `xt` 哈希，它是资源的"身份证号"。哈希对得上就是你要的内容，对不上就找错了。

### 如何"导出"磁力链接

- 在 qBittorrent 里，右键已有任务 → 复制磁力链接（Copy Magnet URI），即可分享给别人
- 或从 .torrent 文件生成：很多在线工具能从 .torrent 提取磁力链接

## 5. 常见报错与解决

### 问题1：添加磁力链接后一直"正在获取元数据"或"下载中 0%"

**原因：** 客户端通过 DHT 找节点和元数据，需要时间；或 DHT 网络没起来、没有人在做种。

**解决方法：**
1. 等待几分钟到几十分钟，DHT 寻找需要时间
2. 确认 DHT 已开启（qBittorrent 设置 → BitTorrent → 启用 DHT）
3. 检查端口是否被防火墙拦截，做端口映射
4. 链接里带 Tracker（`tr=`）的话下载会更快
5. 没人做种（老资源）就是下不完，换资源

### 问题2：浏览器点击磁力链接没反应/提示"没有应用可处理"

**原因：** 浏览器没关联 BT 客户端处理 `magnet:` 协议。

**解决方法：**
1. 手动复制磁力链接到 BT 客户端添加
2. 浏览器设置里把 `magnet` 协议关联到 BT 客户端程序
3. Windows：设置 → 应用 → 默认应用 → 按协议选择 → 找 magnet 关联
4. 临时方案：勾选"总是用此应用打开"

### 问题3：下载到假文件 / 文件名和内容不符

**原因：** 磁力链接的 `dn`（显示名）可任意填写，哈希对得上才是真内容；有人故意填假名骗下载，或资源本身被投毒。

**解决方法：**
1. 从可信源（官网、知名社区）获取磁力链接
2. 下载完成后核对文件哈希（SHA256 等）与官方一致
3. 下载到可执行文件先杀毒再运行
4. 用沙箱或虚拟机运行不明文件
5. 远离不明资源站，从源头降低风险

### 问题4：aria2 报 "No URI to download" 或链接不完整

**原因：** 磁力链接不完整、被截断，或没加引号被 shell 转义破坏。

**解决方法：**
1. 磁力链接必须用双引号包裹（含特殊字符）
2. 确认链接完整，以 `magnet:?xt=urn:btih:` 开头
3. 检查是否复制时漏了字符
4. aria2 默认开 DHT 即可，加 `--enable-dht=true`（新版默认开）

---

## 💡 小知识

- 磁力链接不依赖 Tracker 服务器，靠 DHT（分布式哈希表）在 P2P 网络里找资源，更抗封锁
- 磁力链接核心是内容的哈希值（Info Hash），"靠内容找资源"而非"靠地址找资源"
- 因为磁力链接是纯文本，可以发在聊天、邮件里，不需要上传/下载 .torrent 文件
- 磁力链接常和 .torrent 互为补充：.torrent 信息更全（含分块哈希）下载启动快，磁力链接更灵活省事

## 🔗 相关链接

- [qBittorrent 官网](https://www.qbittorrent.org/)
- [Transmission 官网](https://transmissionbt.com/)
- [aria2 官网](https://aria2.github.io/)
- [磁力链接规范（MAGNET URI）](https://en.wikipedia.org/wiki/Magnet_URI_scheme)
- [VirusTotal 病毒扫描](https://www.virustotal.com/)
- [Ubuntu 官方 BT 下载](https://www.ubuntu.com/download/alternative-downloads)

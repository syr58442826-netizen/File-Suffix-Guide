# .torrent 文件后缀详解

## 1. 文件定义 & 用途

.torrent 是 **BitTorrent 种子文件**的后缀。BitTorrent 是一种点对点（P2P）的文件分发协议，.torrent 文件本身不含目标文件内容，而是包含目标文件的**元数据**（文件名、大小、分块信息、Tracker 服务器地址、内容哈希等）。

简单来说，.torrent 文件是一个"下载任务清单"，BT 客户端读取它后，从全球其他下载者那里一点点拼凑出完整文件。下载的人越多，速度反而可能越快。

> ⚠️ **法律与安全提醒**：BitTorrent 技术本身是中性的文件分发协议，但用 .torrent 下载的内容必须符合版权法。下载/分享盗版影视、软件、游戏等受版权保护的内容属违法行为，可能面临法律追责。此外 .torrent 来源不明时可能被恶意者投毒（下载到病毒/恶意软件），务必从可信官方源获取种子。

**主要用途：**
- 大文件分发（Linux 发行版官方镜像、开源软件、公开数据集）
- 开源社区共享大体积资源
- 软件更新分发（如部分游戏平台更新）
- 个人备份分发

## 2. 适用场景

- 下载 Linux 系统 ISO 镜像（Ubuntu、CentOS 官方都提供 BT 下载）
- 下载开源软件、公开数据集等合法大文件
- 自己制作种子分享大文件给多人

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [qBittorrent](https://www.qbittorrent.org/)、[Transmission](https://transmissionbt.com/) | [BitComet](https://www.bitcomet.com/)、迅雷 |
| Mac | [qBittorrent](https://www.qbittorrent.org/)、[Transmission](https://transmissionbt.com/) | [BitComet](https://www.bitcomet.com/) |
| Linux | [qBittorrent](https://www.qbittorrent.org/)、[Transmission](https://transmissionbt.com/)、aria2 | Deluge |

**新手推荐：** qBittorrent（开源免费、跨平台、无广告，公认最干净的 BT 客户端）。强烈不建议用各种"下载站"捆绑广告的客户端。

## 4. 如何编辑、如何导出

### 使用方法（下载）

**步骤：**
1. 安装一个 BT 客户端（推荐 qBittorrent）
2. 双击 .torrent 文件，或打开客户端 → 文件 → 添加种子
3. 选择保存路径，确认下载
4. 客户端连接 Tracker 和其他节点，开始下载分块
5. 下载完成（达到 100%）后，建议继续上传一段时间（做种），让 BT 生态持续运转

### 制作种子（分享）

以 qBittorrent 为例：
1. qBittorrent → 工具 → 制作种子（或 Torrent Creator）
2. 选择要分享的文件或文件夹
3. 填写 Tracker 服务器地址（可用公开 Tracker 列表）
4. 可选：填备注、设置分块大小
5. 生成 .torrent 文件，分享给他人

### 下载加速设置

- 在客户端设置里开启 DHT、PEX、LPD（无需 Tracker 也能找节点）
- 路由器/防火墙做端口映射，让外部能连入你（提升下载和做种速度）
- 限制上传速度避免占满带宽（上传过慢会影响下载速度，BT 靠上传换下载）

## 5. 常见报错与解决

### 问题1：下载一直 0% 或速度极慢，连不上节点

**原因：** Tracker 失效、没有做种者、端口被封锁，或网络运营商限制 BT 流量。

**解决方法：**
1. 更新 Tracker 列表：在客户端里添加多个公开 Tracker（如 https://github.com/ngosang/trackerslist）
2. 确认开启了 DHT/PEX/LPD（即使 Tracker 失效也能找节点）
3. 路由器做端口映射，确保端口可被外部连接
4. 换一个有做种者的种子（老种没人做种就是下不完）
5. 检查防火墙是否放行了 BT 客户端
6. 运营商限速可尝试启用"协议加密"或换用 WebRTC/代理

### 问题2：下载到 99% 就卡住不动

**原因：** 缺少最后一块，没有人有这块（做种者都跑了），或文件有"毒块"被哈希校验拒绝。

**解决方法：**
1. 耐心等待，可能有人上线补块
2. 强制重新校验（Recheck）：客户端右键 → 重新检查哈希
3. 删除后换个新种子重下
4. 用"跳过校验"风险大（可能下到损坏文件），不推荐

### 问题3：下载的文件被杀毒软件报毒

**原因：** 种子来源不明，可能夹带了恶意软件；或是破解版/汉化版的"误报"。

**解决方法：**
1. **优先从官方源下载**（如 Linux 镜像用官网的 BT）
2. 用 VirusTotal（virustotal.com）多引擎扫描可疑文件
3. 不要禁用杀毒软件运行来历不明的 exe
4. 下载后用沙箱或虚拟机运行，避免直接在主系统执行
5. 远离盗版资源站，这是中毒的最大来源

### 问题4：做种一直在上传占满带宽

**原因：** 下载完成后客户端默认继续做种（上传给他人），这是 BT 的互助机制，但会占上行带宽。

**解决方法：**
1. 在客户端设置上传速度上限（如设为带宽的 1/3）
2. 设置做种时间或分享率（如分享率到 1.0 自动停止）
3. 不想再做种，手动停止该任务即可
4. 注意：完全不分享会被某些 Tracker 封号，建议至少做到分享率 1.0

---

## 💡 小知识

- BitTorrent 协议由 Bram Cohen 在 2001 年发明，是 P2P 文件分发的代表
- .torrent 文件用 bencode 编码，体积很小（几 KB 到几十 KB）
- 现代 BT 支持 DHT（分布式哈希表），即使 Tracker 服务器挂了也能找节点下载
- Linux 发行版（Ubuntu、Debian、CentOS）官方都提供 .torrent 下载，是最合法、最推荐的用途

## 🔗 相关链接

- [qBittorrent 官网](https://www.qbittorrent.org/)
- [Transmission 官网](https://transmissionbt.com/)
- [BitTorrent 协议规范](https://www.bittorrent.org/)
- [公开 Tracker 列表](https://github.com/ngosang/trackerslist)
- [Ubuntu 官方 BT 下载](https://www.ubuntu.com/download/alternative-downloads)
- [VirusTotal 病毒扫描](https://www.virustotal.com/)

# .zst 文件后缀详解

## 1. 文件定义 & 用途

ZST 是 **Zstandard** 压缩格式的文件扩展名，由 Facebook（现 Meta）开发并于 2015 年开源。它的目标是同时实现高压缩率和快速度——压缩率接近 .xz，但速度远超 .xz 和 .gz。

简单来说，.zst 是"又快又狠"的新一代压缩格式——比 zip 快、比 gz 压得小、比 xz 快得多。

- **全称**：Zstandard Compressed File
- **类型**：压缩归档文件
- **开发者**：Facebook（现 Meta Platforms）
- **发布年份**：2015年
- **特点**：高压缩率 + 高速度、支持多线程、可调节压缩级别（1-22）
- **常见组合**：.tar.zst（先用 tar 打包，再用 zst 压缩）

## 2. 适用场景

- Linux 软件包压缩（Arch Linux、Debian/Ubuntu 正在转向 zst）
- 需要快速压缩同时高压缩率的场景
- 大规模日志和数据库备份
- 实时数据压缩（速度足够快，适合在线压缩）
- 软件分发和源代码打包

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 7-Zip（21.07+）、PeaZip（9.9+）、zstd 命令行工具 | Bandizip（较新版本） |
| Mac | The Unarchiver、Keka、zstd（Homebrew 安装） | BetterZip |
| Linux | zstd（命令行）、File Roller、Ark | - |

**新手推荐**：
- Windows 用户：**7-Zip**（21.07 以上版本支持 zst 格式）
- Mac 用户：**The Unarchiver** 或 **Keka**（支持 zst 解压）
- Linux 用户：安装 `zstd` 包（`sudo apt install zstd` 或 `sudo pacman -S zstd`）
- 命令行操作：用 `zstd` 命令

## 4. 如何编辑、如何导出

### 如何解压
**命令行：**
```bash
# 解压 .zst 文件
zstd -d file.zst

# 解压 .tar.zst 文件（一步到位）
tar -xvf archive.tar.zst

# 或用 zstd 先解压再 tar
zstd -d archive.tar.zst && tar -xvf archive.tar
```

**图形界面：**
1. Windows：右键 .zst 文件 → 7-Zip → 解压到当前文件夹
2. Mac：双击 .zst 文件，The Unarchiver 自动解压
3. Linux：双击或右键 → 提取

### 如何压缩
```bash
# 压缩单个文件
zstd file.txt

# 创建 .tar.zst 归档
tar --zstd -cvf archive.tar.zst 文件夹/

# 指定压缩级别（1-22，默认 3）
zstd -19 largefile.log

# 超高压缩级别（22，极慢但压得最小）
zstd -22 largefile.log

# 多线程压缩
zstd -T0 file.txt
```

## 5. 常见报错与解决

### 问题1：Windows 上打不开 .zst 文件
**原因**：Windows 系统自带功能不支持 zst 格式，且较旧版本的解压软件也不支持。

**解决方法**：
1. 更新 **7-Zip** 到 21.07 或更高版本
2. 更新 **PeaZip** 到 9.9 或更高版本
3. 安装 **zstd 命令行工具**（Windows 版可从 GitHub 下载）
4. 确认软件版本是否支持 zst（这是个较新的格式，旧版软件不支持）

---

### 问题2：解压 .tar.zst 提示"unsupported format"
**原因**：旧版 tar 不支持 zst 压缩，或系统未安装 zstd 工具。

**解决方法**：
1. 更新 tar 到较新版本（tar 1.31+ 原生支持 zst）
2. 先安装 zstd：`sudo apt install zstd`
3. 使用 `--zstd` 参数：`tar --zstd -xvf archive.tar.zst`
4. 或分两步：`zstd -d archive.tar.zst && tar -xvf archive.tar`

---

### 问题3：压缩时想调节速度和压缩率的平衡
**原因**：zstd 有 22 个压缩级别，不了解如何选择合适的级别。

**解决方法**：
1. 默认级别 3：速度快，压缩率不错（日常使用推荐）
2. 级别 1：最快，压缩率一般（实时压缩推荐）
3. 级别 19：压缩率高，速度较慢（长期存档推荐）
4. 级别 22：最高压缩率，极慢（极限压缩场景）
5. 使用 `--ultra` 参数解锁 20-22 级别：`zstd -19 --ultra file`
6. 多线程加速：`zstd -T0 -19 file`（利用所有 CPU 核心）

---

### 问题4：zst 文件损坏或下载不完整，无法解压
**原因**：下载中断、传输错误或存储介质损坏导致文件截断。

**解决方法**：
1. 重新下载文件
2. 验证文件校验和（SHA256）确认完整性
3. zstd 有一定的错误恢复能力，尝试：`zstd -d --sparse file.zst`
4. 如果 .tar.zst 损坏，尝试先恢复 tar 部分：`zstd -cd archive.tar.zst | tar -tvf -`
5. 严重损坏时无法恢复，需要重新获取

---

## 💡 小知识

Zstandard 是压缩领域的"新秀"，2015 年由 Facebook 开源后迅速被各大 Linux 发行版采用。它的核心优势是"全能"——在同等压缩率下比 .xz 快 10 倍以上，在同等速度下比 .gz 压得小 10-15%。Arch Linux 已经把软件包格式从 .xz 转为 .zst，Debian/Ubuntu 也在逐步跟进。可以说，zst 正在成为 Linux 世界新一代的压缩标准。不过 Windows 和 Mac 生态跟进较慢，普通用户接触 zst 的机会还不多，但随着 7-Zip 等工具的支持普及，它正在走进更多人的视野。

## 🔗 相关链接

- [Zstandard 官方 GitHub](https://github.com/facebook/zstd)
- [7-Zip 官网](https://www.7-zip.org/)
- [PeaZip 免费解压软件](https://peazip.github.io/)
- [Zstandard 格式说明 - 维基百科](https://en.wikipedia.org/wiki/Zstandard)
- [.xz 格式详解](./xz.md)
- [.gz 格式详解](./gz.md)

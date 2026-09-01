# .gz 文件后缀详解

## 1. 文件定义 & 用途

GZ（全称 Gzip，GNU zip）是 Linux/Unix 系统中最常用的压缩格式之一，由 Jean-loup Gailly 和 Mark Adler 开发。它通常和 tar 搭配使用，形成 .tar.gz（或 .tgz）组合，是 Linux 世界最经典的压缩格式。

GZ 格式的核心特点：
- **只压缩单个文件**：gzip 只能压缩一个文件，不能打包多个文件
- **压缩速度快**：压缩和解压速度都很快
- **Linux 标配**：几乎所有 Linux/Unix 系统都自带 gzip 命令
- **无损压缩**：使用 DEFLATE 算法，压缩后能完美还原
- **保留原文件名**：压缩后文件名加 .gz 后缀，解压后还原

## 2. 适用场景

- **Linux 软件源码包**：大多数开源软件源码是 .tar.gz 格式
- **日志文件压缩**：系统日志常用 gzip 压缩存档
- **网页传输**：HTTP 协议的 gzip 压缩就是用这个算法
- **单个大文件压缩**：压缩单个大文件，速度快效果好
- **配合 tar 使用**：tar 打包 + gzip 压缩 = .tar.gz
- **嵌入式系统**：体积小，资源占用低，适合嵌入式设备

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 7-Zip、Bandizip、PeaZip、WinRAR | - |
| Mac | 归档实用工具（系统自带）、Keka、The Unarchiver | BetterZip |
| Linux | gzip 命令（系统自带）、File Roller、Ark、7-Zip | - |
| 手机 | ZArchiver（安卓） | - |

## 4. 如何编辑、如何导出

### Linux 下的 gzip 命令

**压缩文件：**
```bash
# 压缩单个文件（原文件会被替换成 file.gz）
gzip filename.txt

# 压缩后保留原文件
gzip -k filename.txt

# 显示压缩率信息
gzip -v filename.txt

# 调整压缩级别（1 最快，9 压缩率最高，默认 6）
gzip -9 filename.txt    # 最高压缩率
gzip -1 filename.txt    # 最快速度
```

**解压文件：**
```bash
# 解压（.gz 文件会被替换成原文件）
gunzip filename.txt.gz
# 或者
gzip -d filename.txt.gz

# 解压后保留原 .gz 文件
gzip -dk filename.txt.gz

# 查看压缩文件内容（文本文件）
zcat filename.txt.gz
zless filename.txt.gz
```

### .tar.gz 的使用（最常见）

```bash
# 打包并压缩
tar -czvf archive.tar.gz /path/to/files/

# 解压 .tar.gz
tar -xzvf archive.tar.gz

# 查看 .tar.gz 内容
tar -tzvf archive.tar.gz

# 参数说明：
# c - 创建  x - 提取  t - 列出
# z - 使用 gzip 压缩/解压
# v - 显示过程  f - 指定文件名
```

### Windows 下操作 gz 文件

**使用 7-Zip：**
1. 右键 → 7-Zip → 提取到当前位置
2. 如果是 .tar.gz，第一次解压得到 .tar，再解压一次得到文件
3. 7-Zip 也可以直接把文件拖进去压缩成 .gz

**使用 Bandizip：**
1. 双击 .gz 文件直接打开
2. 拖拽或点击解压
3. Bandizip 支持直接解压 .tar.gz 到原始文件

### 注意事项

- gzip 只能压缩单个文件，压缩多个文件需要先 tar 打包
- gzip 压缩后默认删除原文件，加 `-k` 参数可以保留
- gzip 的压缩率不如 bzip2 和 xz，但速度最快
- .tgz 和 .tar.gz 是一样的，只是后缀名不同

## 5. 常见报错与解决

### 问题 1：gzip: stdin: not in gzip format

**原因：** 文件不是真正的 gzip 格式，可能是后缀名被改错了。

**解决方法：**
1. 用 `file` 命令检查文件真实类型：
   ```bash
   file filename.gz
   ```
2. 如果显示的不是 gzip 压缩数据，说明文件格式不对
3. 检查下载是否完整，重新下载试试
4. 可能是其他格式（如 zip、rar）被改了后缀名，换工具试试
5. 用 7-Zip 打开试试（支持格式多，也许能识别）

### 问题 2：tar.gz 解压失败，提示"意外结束文件"

**原因：** 文件下载不完整，或传输过程中损坏。

**解决方法：**
1. 重新下载文件
2. 检查文件大小是否和源文件一致
3. 用 `gzip -t` 测试压缩包完整性：
   ```bash
   gzip -t filename.gz
   ```
4. 如果是网络下载，试试用 wget -c 续传
5. 检查磁盘空间是否充足

### 问题 3：解压后文件名乱码

**原因：** 原始文件名编码和解压环境编码不同。

**解决方法：**
1. 如果是 tar.gz，乱码通常是 tar 的问题，参考 tar 格式的解决方法
2. 使用 7-Zip 或 Bandizip 解压，切换代码页
3. Linux 下用 `convmv` 工具转换文件名编码
4. 建议压缩时使用 UTF-8 编码

### 问题 4：gzip 压缩后文件反而变大了

**原因：** 文件已经是压缩过的（如 JPG、MP3、ZIP），再压缩反而会增加文件头开销。

**解决方法：**
1. 已经压缩过的文件不要再用 gzip 压缩
2. 图片、视频、音频等多媒体文件压缩率很低
3. 文本、代码、文档类文件压缩率高
4. 如果是很多小文件，先 tar 打包再压缩（打包后压缩率更高）
5. 压缩后检查大小，如果变大了就不用压缩了

### 问题 5：zcat 查看内容是乱码

**原因：** 文件不是文本文件，或者是 tar.gz 不是纯 gz。

**解决方法：**
1. zcat 只能查看纯文本压缩后的内容
2. 如果是 .tar.gz，用 `tar -tzf` 查看内容列表
3. 如果是二进制文件，用 `file` 命令先检查类型
4. 要查看文本内容，先确认是纯文本再用 zcat/zless

---

## 💡 小知识

gzip 是 GNU 项目的一部分，诞生于 1992 年。它的名字"gzip"就是"GNU zip"的缩写——因为当时 Unix 系统自带的 compress 命令是专利软件，GNU 项目就开发了一个完全免费的替代品。

gzip 使用的 DEFLATE 算法也是一个传奇。这个算法由 Phil Katz（也就是 ZIP 格式的发明者）开发，并且被 gzip 采用。后来 DEFLATE 还成为了 PNG 图片格式、HTTP gzip 压缩、ZIP 格式的核心算法，可以说是世界上使用最广泛的压缩算法之一。

你每天上网时都在和 gzip 打交道——浏览器请求网页时，服务器会用 gzip 压缩网页内容再传输，这样加载速度更快。所以你打开的每一个网页，背后可能都有 gzip 的功劳。

## 🔗 相关链接

- [Gzip 官方网站](https://www.gnu.org/software/gzip/)
- [7-Zip 官方下载](https://www.7-zip.org/)
- [.tar 格式详解](./tar.md)
- [.bz2 格式详解](./bz2.md)
- [.zip 格式详解](./zip.md)

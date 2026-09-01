# .iso 文件后缀详解

## 1. 文件定义 & 用途

ISO（全称 ISO 9660，简称 ISO Image）是一种光盘镜像文件格式。它完整地复制了 CD、DVD、蓝光光盘的所有数据，包括文件系统、引导信息、音频轨道等。你可以把它理解为一张"电子版的光盘"。

ISO 格式的核心特点：
- **完整复制光盘**：1:1 复制光盘内容，包括引导扇区
- **可引导启动**：系统安装盘的 ISO 可以用来启动电脑
- **跨平台兼容**：Windows、Mac、Linux 都能读取
- **体积较大**：大小和原光盘差不多（CD 约 700MB，DVD 约 4.7GB）
- **只读属性**：ISO 是只读的，不能直接修改内容

## 2. 适用场景

- **操作系统安装**：Windows、Linux 系统安装盘都是 ISO 格式
- **光盘备份**：把物理光盘备份成 ISO 文件，保存到硬盘
- **虚拟机安装**：VMware、VirtualBox 直接挂载 ISO 安装系统
- **软件分发**：大型软件、游戏的光盘版常以 ISO 形式发布
- **PE 启动盘**：制作 WinPE、Linux Live USB 启动盘
- **数据归档**：把光盘内容归档保存，避免光盘损坏

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 文件资源管理器（Win10/11 自带挂载）、7-Zip、Virtual CloneDrive、Daemon Tools Lite | Daemon Tools Pro、PowerISO、UltraISO |
| Mac | 磁盘工具（系统自带）、DiskImageMounter | Toast Titanium |
| Linux | mount 命令、GNOME Disks、AcetoneISO | - |
| 刻录 | ImgBurn（免费）、BurnAware Free | Nero Burning ROM |

## 4. 如何编辑、如何导出

### 如何挂载 ISO（虚拟光驱）

**Windows 10/11 系统自带：**
1. 直接双击 ISO 文件，系统会自动挂载为虚拟光驱
2. 在"此电脑"中可以看到新的光驱盘符
3. 使用完后，右键光驱 → 弹出

**使用 Daemon Tools Lite（免费版）：**
1. 安装 Daemon Tools Lite
2. 右键 ISO 文件 → 装载
3. 自动创建虚拟光驱并加载

**Mac 系统自带：**
1. 双击 ISO 文件，自动挂载到 Finder
2. 桌面上会出现光盘图标
3. 使用完后右键 → 推出

**Linux 命令行挂载：**
```bash
# 创建挂载点
sudo mkdir /mnt/iso

# 挂载 ISO
sudo mount -o loop filename.iso /mnt/iso

# 卸载
sudo umount /mnt/iso
```

### 如何创建 ISO 文件

**从光盘创建 ISO（物理光盘转镜像）：**

**Windows 使用 ImgBurn（免费）：**
1. 放入光盘，打开 ImgBurn
2. 选择"创建光盘镜像文件"
3. 选择源光驱和目标 ISO 文件路径
4. 点击开始读取

**Linux 命令行：**
```bash
# 把光盘复制为 ISO
dd if=/dev/cdrom of=output.iso bs=4M
# 或者
cat /dev/sr0 > output.iso
```

**从文件夹创建 ISO：**

**Windows 使用 UltraISO 或 AnyBurn：**
1. 打开软件，添加文件和文件夹
2. 设置光盘类型和标签
3. 保存为 ISO 文件

**Linux 命令行（mkisofs/genisoimage）：**
```bash
mkisofs -o output.iso /path/to/folder/
# 或者更完整的选项
genisoimage -o output.iso -J -R -V "LABEL" /path/to/folder/
```

### 如何制作启动 U 盘

**使用 Rufus（免费推荐）：**
1. 下载 Rufus（单文件，免安装）
2. 插入 U 盘
3. 选择 ISO 文件
4. 点击开始，等待完成
5. 注意：U 盘数据会被清空

**使用 Ventoy（更方便，一个 U 盘放多个 ISO）：**
1. 下载 Ventoy
2. 安装到 U 盘
3. 把 ISO 文件直接复制到 U 盘
4. 启动时选择要启动的 ISO

## 5. 常见报错与解决

### 问题 1：ISO 文件挂载后打开是空的或文件不完整

**原因：** ISO 文件损坏，或下载不完整。

**解决方法：**
1. 重新下载 ISO 文件
2. 校验文件的 MD5/SHA256 值（官方通常会提供校验值）
   ```bash
   # Linux 下校验
   sha256sum filename.iso
   ```
3. 用 7-Zip 打开试试，如果也显示文件损坏，说明文件确实有问题
4. 检查下载工具是否有断点续传问题
5. 尽量从官方或可信渠道下载

### 问题 2：用 ISO 制作的 U 盘无法启动

**原因：** BIOS 设置问题、U 盘制作失败、或 ISO 本身不可引导。

**解决方法：**
1. 确认 ISO 是可引导的（系统安装盘一般都是）
2. 进入 BIOS/UEFI 设置，调整启动顺序为 U 盘优先
3. 尝试切换 Legacy BIOS 模式或 UEFI 模式
4. 关闭 Secure Boot（安全启动）
5. 换一个 USB 接口（优先 USB 2.0，兼容性更好）
6. 用 Rufus 重新制作，选择正确的分区方案

### 问题 3：ISO 文件太大，无法刻录到光盘

**原因：** ISO 文件超过了光盘的容量（比如 DVD ISO 想刻到 CD 上）。

**解决方法：**
1. 确认光盘类型和容量：
   - CD：约 700MB
   - DVD-5：约 4.7GB
   - DVD-9：约 8.5GB
   - BD-25：约 25GB
2. 使用容量更大的光盘
3. 或者用 U 盘代替光盘（现在大多用 U 盘装系统）
4. 如果是数据 ISO，可以用分卷压缩后再刻盘
5. 检查 ISO 大小是否正确（下载不完整也可能导致大小异常）

### 问题 4：解压 ISO 后文件不能用（如游戏/软件无法运行）

**原因：** ISO 是光盘镜像，有些软件需要从光盘运行（需要光盘验证），直接解压文件会丢失引导信息和轨道信息。

**解决方法：**
1. 用虚拟光驱挂载 ISO，而不是解压
2. 安装 Daemon Tools 或用系统自带功能挂载
3. 从虚拟光驱中运行安装程序
4. 有些游戏需要打免 CD 补丁
5. 如果是混合光盘（数据+音轨），解压会丢失音轨，必须用虚拟光驱

### 问题 5：Mac 无法打开 Windows 的 ISO 或反之

**原因：** ISO 是跨平台格式，一般不会有兼容性问题，可能是文件损坏或特殊格式。

**解决方法：**
1. ISO 9660 是标准格式，Windows 和 Mac 都能读取
2. 如果打不开，可能是文件损坏，重新下载
3. 检查文件后缀是否是 .iso
4. Mac 用户可以用磁盘工具 → 文件 → 打开磁盘映像
5. 如果是 UDF 格式的 DVD 镜像，系统也能识别

---

## 💡 小知识

ISO 格式的名字来源于国际标准化组织（International Organization for Standardization）制定的 ISO 9660 文件系统标准。这个标准在 1988 年发布，目的是让不同操作系统都能读取 CD-ROM 上的文件。

你知道吗？一张 CD 的容量为什么是 700MB 左右？这背后有一个有趣的故事——当年索尼和飞利浦制定 CD 标准时，据说因为索尼副社长的坚持，CD 的播放时长被定为 74 分钟，这样才能完整放下贝多芬的《第九交响曲》。而 74 分钟的 16bit/44.1kHz 立体声，算下来正好是大约 650MB-700MB。

如今，物理光盘已经越来越少见了，但 ISO 格式却依然活跃。它从"光盘的镜像"变成了"虚拟光盘"，广泛用于系统安装、虚拟机、数据备份等场景。可以说，ISO 是光盘时代留给我们的珍贵遗产。

## 🔗 相关链接

- [Rufus 官方下载](https://rufus.ie/)
- [Ventoy 官方网站](https://www.ventoy.net/)
- [7-Zip 官方下载](https://www.7-zip.org/)
- [ImgBurn 官方网站](https://www.imgburn.com/)
- [.zip 格式详解](./zip.md)
- [分卷压缩说明](./分卷压缩说明.md)

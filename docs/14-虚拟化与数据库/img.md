# .img 文件后缀详解

## 1. 文件定义 & 用途

.img 是一种通用的**磁盘镜像**文件后缀，它是对整个磁盘或分区的逐扇区复制，内容和原始磁盘完全一致（bit-for-bit copy）。.img 是"原始格式"（raw），没有压缩和特殊元数据，因此兼容性极好。

简单来说，.img 文件就是"把一整块硬盘/光盘/软盘/分区原样复制成一个文件"。系统烧录工具（如 balenaEtcher、Rufus）可以把 .img 写到 U 盘或 SD 卡里，让设备变成镜像里的系统。

> 注意：.img 是个泛用后缀，可能装的是系统镜像（树莓派）、软盘镜像、光盘镜像、分区镜像等，具体用途看内容。

**主要用途：**
- 树莓派（Raspberry Pi）等单板机的系统镜像
- 系统安装镜像（部分系统用 .img 而非 .iso）
- 软盘/光盘镜像（老式或特殊用途）
- 磁盘/分区备份与克隆
- 嵌入式设备固件刷写

## 2. 适用场景

- 给树莓派、香橙派等单板机刷系统
- 把系统镜像写入 U 盘启动盘
- 磁盘分区备份与恢复
- 嵌入式设备刷机
- 老式软盘/光盘镜像归档

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [balenaEtcher](https://etcher.balena.io/)、[Rufus](https://rufus.ie/)、[7-Zip](https://www.7-zip.org/)（解压） | Win32 Disk Imager、PowerISO |
| Mac | [balenaEtcher](https://etcher.balena.io/)、[Raspberry Pi Imager](https://www.raspberrypi.com/software/) | PowerISO |
| Linux | [balenaEtcher](https://etcher.balena.io/)、dd 命令、[7-Zip](https://www.7-zip.org/) | Gnome Disks（自带） |

**新手推荐：** balenaEtcher（跨平台、图形界面、烧录树莓派/U盘系统镜像首选）。

## 4. 如何编辑、如何导出

### 烧录到设备（写 U 盘/SD 卡）

**方法一：balenaEtcher（图形界面，新手首选）**
1. 下载并安装 balenaEtcher
2. 插入 U 盘或 SD 卡
3. Etcher → Flash from file → 选 .img 镜像
4. 选目标设备 → Flash → 等待完成

**方法二：Rufus（Windows）**
1. 下载 [Rufus](https://rufus.ie/)（免安装）
2. 插入 U 盘，打开 Rufus
3. 设备选 U 盘 → 引导类型选 .img 文件
4. 点"开始"，等待写入完成

**方法三：Linux 用 dd 命令（命令行）**
```bash
# 先查看 U 盘设备名（如 /dev/sdb）
lsblk

# 把 .img 写入 U 盘（注意 of= 后是设备名不是分区名！）
sudo dd if=image.img of=/dev/sdb bs=4M status=progress

# 写完后安全弹出
sync
sudo eject /dev/sdb
```
> ⚠️ dd 命令非常危险，`of=` 写错设备会清空整块硬盘！务必先 `lsblk` 确认 U 盘设备名。

### 挂载/查看内容

**Linux 挂载 .img：**
```bash
# 查看镜像分区布局
fdisk -l image.img

# 用 offset 参数挂载某个分区（offset 是分区的起始字节数）
sudo mount -o loop,offset=$((512*2048)) image.img /mnt

# 卸载
sudo umount /mnt
```

**Windows 查看 .img 内容：** 用 7-Zip 打开，能浏览/提取文件。

### 制作 .img 备份

```bash
# Linux 把整盘备份成 .img（如备份 SD 卡）
sudo dd if=/dev/sdb of=backup.img bs=4M status=progress

# 用 gzip 压缩节省空间
sudo dd if=/dev/sdb bs=4M | gzip > backup.img.gz
```

## 5. 常见报错与解决

### 问题1：Etcher/Rufus 写入失败或提示设备被占用

**原因：** U 盘被其他程序占用、有写保护，或文件系统损坏。

**解决方法：**
1. 关闭可能访问 U 盘的程序（资源管理器、杀毒软件）
2. 拔插 U 盘，必要时重启电脑
3. 先用系统格式化工具格式化 U 盘（清空）
4. 用 diskpart（Win）或 fdisk（Linux）清理分区表后再写
5. U 盘本身损坏就换一个

### 问题2：dd 写入后 U 盘容量变小 / Windows 不识别

**原因：** .img 镜像写入后，U 盘分区表被替换为镜像的分区布局，剩余空间未分配，Windows 资源管理器看不到。

**解决方法：**
1. 这属正常现象，启动盘可用即可
2. 想恢复 U 盘：用 diskpart 清理后重新分区
   ```
   diskpart
   list disk
   select disk X（X 是 U 盘号，务必确认！）
   clean
   create partition primary
   format fs=fat32 quick
   assign
   ```
3. Linux 用 `fdisk /dev/sdb` 删掉旧分区，新建占满全盘的分区，再 `mkfs.vfat`

### 问题3：树莓派烧录后无法启动

**原因：** 镜像写入不完整、镜像本身不对、U 盘/SD 卡质量问题、或树莓派供电不足。

**解决方法：**
1. 用 Etcher 校验（Etcher 写完会自动验证）
2. 确认下载的镜像与树莓派型号匹配（Pi 3/4/5 镜像不同）
3. 换高质量 SD 卡（劣质卡是常见原因）
4. 检查电源：用 5V 3A 的官方电源，供电不足会无法启动
5. 用 Raspberry Pi Imager（官方工具，自动下载匹配镜像）

### 问题4：dd 写入速度很慢或卡住

**原因：** 缓冲块大小不对，或设备读取瓶颈，或 status 参数没开。

**解决方法：**
1. 用 `bs=4M` 提升块大小（太小会很慢）
2. 加 `status=progress` 看进度
3. 确认写入的是设备（`/dev/sdb`）而非分区（`/dev/sdb1`），写分区可能只写了一部分
4. SD 卡写入速度本身有限，耐心等待
5. 完成后务必 `sync` 确保数据写完再拔

---

## 💡 小知识

- .img 是"原始镜像"（raw），没有文件头和压缩，所以兼容性最强，几乎所有工具都支持
- 树莓派官方系统 Raspbian/Raspberry Pi OS 的镜像就是 .img 格式
- .img 和 .iso 都是磁盘镜像，但 .iso 针对 ISO 9660 文件系统（光盘），.img 更通用
- dd 命令被称为"磁盘毁灭者"（Disk Destroyer），因为它无差别复制，写错目标会瞬间清空数据

## 🔗 相关链接

- [balenaEtcher 官网](https://etcher.balena.io/)
- [Rufus 官网](https://rufus.ie/)
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [树莓派官网](https://www.raspberrypi.com/)
- [dd 命令教程](https://wiki.archlinux.org/title/Dd_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
- [7-Zip 官网](https://www.7-zip.org/)

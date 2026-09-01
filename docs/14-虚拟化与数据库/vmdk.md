# .vmdk 文件后缀详解

## 1. 文件定义 & 用途

.vmdk 是 **VMware 虚拟磁盘**（Virtual Machine Disk）文件后缀，是 VMware 开发的虚拟机硬盘镜像格式。一个 .vmdk 文件在虚拟机里就像一块真实硬盘，里面装着操作系统和文件。

简单来说，.vmdk 文件就是"虚拟机的硬盘"，虚拟机软件（VMware Workstation、ESXi 等）把它挂载为虚拟机的 C 盘等盘符，开机后虚拟机里的系统就从这块"硬盘"启动。

> 现在的 .vmdk 常分两种：单文件（monolithic）和多文件（split，每个 2GB 一片，便于复制和绕开文件大小限制）。

**主要用途：**
- VMware 虚拟机的系统盘和数据盘
- 虚拟机分发和迁移（OVA/OVF 包里常含 .vmdk）
- 云虚拟化平台（部分兼容 VMDK）
- 备份与恢复虚拟机

## 2. 适用场景

- 用 VMware 运行多个操作系统（Windows/Linux/macOS 客户机）
- 测试软件、搭建隔离环境
- 服务器虚拟化（vSphere/ESXi）
- 虚拟机镜像分发和迁移

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VirtualBox](https://www.virtualbox.org/)（可转换使用）、VMware Workstation Player（个人免费） | VMware Workstation Pro、[7-Zip](https://www.7-zip.org/)（解压查看内容） |
| Mac | VMware Fusion Player（个人免费）、[VirtualBox](https://www.virtualbox.org/) | VMware Fusion Pro |
| Linux | [VirtualBox](https://www.virtualbox.org/)、QEMU | VMware Workstation |

**新手推荐：** VMware Workstation Player（Windows 个人免费）或 VirtualBox（跨平台免费，需先转换格式）。

## 4. 如何编辑、如何导出

### 挂载/打开方法

**方法一：在 VMware 中直接使用（最常用）**
1. VMware Workstation/Player → 新建虚拟机
2. 选择"使用现有虚拟磁盘"，指向 .vmdk 文件
3. 完成后启动虚拟机即可

**方法二：用 7-Zip 直接提取里面的文件**
1. 右键 .vmdk → 7-Zip → 打开压缩包
2. 能浏览/提取里面虚拟硬盘上的文件（只读，不改盘内容）

**方法三：挂载到宿主机当普通盘（VMware 功能）**
1. VMware → 虚拟机设置 → 硬盘 → 映射
2. 把 .vmdk 映射为宿主机的一个盘符，可直接读写文件

### 格式转换

不同虚拟机软件磁盘格式互转，用工具转换：
```bash
# 用 QEMU 转换为其他格式
qemu-img convert -f vmdk -O qcow2 source.vmdk target.qcow2
qemu-img convert -f vmdk -O raw source.vmdk target.img

# 用 VBoxManage（VirtualBox 自带）转换
VBoxManage clonehd source.vmdk target.vdi --format vdi
```

### 如何导出/迁移

- 导出为 OVA/OVF 分发：VMware → 文件 → 导出为 OVF
- 复制 .vmdk 文件到另一台机器直接用（关机状态下复制）

## 5. 常见报错与解决

### 问题1：打开时提示 "The file is not a valid virtual disk" 或损坏

**原因：** .vmdk 文件被非正常关闭、复制中断、或被其他软件改坏，导致描述文件与数据不一致。

**解决方法：**
1. VMware 试图自动修复，按提示操作
2. 多文件的 .vmdk，确认所有分片（-s001.vmdk、-s002.vmdk...）都在同目录
3. 用 `vmware-vdiskmanager -R 损坏.vmdk` 尝试修复
4. 用备份恢复，或从快照回滚

### 问题2：提示 "磁盘空间不足" 但虚拟机内还有很多空间

**原因：** .vmdk 是"动态分配"或"预分配"的，虚拟机内删除文件不会自动回收宿主机的物理空间。

**解决方法：**
1. 虚拟机内用清理工具清理，然后做"压缩"
2. VMware → 虚拟机设置 → 硬盘 → 工具 → 压缩
3. 或命令行：`vmware-vdiskmanager -k 磁盘.vmdk`
4. 预分配的厚盘需先转为稀疏盘

### 问题3：复制到别的机器后无法启动 / 网卡变成 eth1

**原因：** 虚拟机迁移后，VMware 会认为环境变了，可能提示"已移动或已复制"。复制会改变网卡的 MAC，Linux 客户机里网卡名变 eth1 导致没网络。

**解决方法：**
1. VMware 提示时选"我已移动它"（保留原 MAC）
2. 已复制的情况：编辑网卡设置 → 高级 → 重新生成 MAC
3. Linux 客户机删除持久化网卡规则：`rm /etc/udev/rules.d/70-persistent-net.rules` 后重启

### 问题4：VirtualBox 无法直接用 .vmdk，提示格式问题

**原因：** VirtualBox 原生用 .vdi/.vhd，部分 .vmdk（特别是 stream-optimized 或 ESXi 导出的）兼容性差。

**解决方法：**
1. 用 VBoxManage 转换格式：`VBoxManage clonehd source.vmdk target.vdi --format vdi`
2. 或用 QEMU 转换：`qemu-img convert -f vmdk -O vdi source.vmdk target.vdi`
3. 转换后用新的 .vdi 创建虚拟机

---

## 💡 小知识

- VMDK 格式由 VMware 开发，2006 年公开规范，现在已是开放格式
- VMDK 支持快照（snapshot），可以做时间点回滚，本质是写时复制（COW）
- 一个虚拟机目录里除了 .vmdk 数据文件，还有同名的 .vmdk 描述文件（小文本文件，几 KB），两者缺一不可
- VMDK 的"精简置备"（thin provisioning）可以超分：声明 100GB 但实际只占用使用的空间

## 🔗 相关链接

- [VMware 官网](https://www.vmware.com/)
- [VMware Workstation 下载](https://www.vmware.com/products/workstation-pro.html)
- [VirtualBox 官网](https://www.virtualbox.org/)
- [QEMU 下载](https://www.qemu.org/)
- [7-Zip 官网](https://www.7-zip.org/)

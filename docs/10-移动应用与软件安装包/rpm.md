# .rpm 文件后缀详解

## 1. 文件定义 & 用途

RPM（RPM Package Manager，最初全称 Red Hat Package Manager）是 Red Hat Linux 及其衍生发行版（Fedora、CentOS、RHEL、openSUSE、Rocky Linux 等）使用的软件包格式。一个 RPM 文件是一个特殊的 cpio 归档（加上了文件头和签名），包含编译后的二进制文件、配置文件、文档以及元数据（包名、版本、依赖、文件列表、安装前后脚本等）。

RPM 与 DEB 是 Linux 世界两大并行存在的包格式阵营。RPM 主要服务于 Red Hat 系生态，使用 rpm 和 dnf/yum/zypper 等包管理工具进行安装和管理。

## 2. 适用场景

- 在 Red Hat/Fedora/CentOS/openSUSE 等 RPM 系 Linux 上安装软件
- 企业服务器软件部署（RHEL是企业Linux市场占有率最高的发行版）
- 软件厂商分发 Linux 商业版（如 Oracle Database、NVIDIA驱动提供 .rpm）
- 软件包仓库管理与签名验证
- Linux 系统更新与补丁分发

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 7-Zip（解压查看内容）、WSL（Fedora/openSUSE子系统） | - |
| Mac | The Unarchiver（解压查看） | - |
| Linux | rpm、dnf/yum、zypper（openSUSE）、PackageKit | rpmbuild、mock（构建工具） |
| 跨平台(网页) | - | - |

> 安全提示：RPM 安装时以 root 权限运行 pre/post 脚本。请只安装来自可信仓库（官方源、EPEL、RPM Fusion）的 RPM 包。可用 `rpm --checksig 包名.rpm` 验证 GPG 签名。

## 4. 如何编辑、如何导出

**查看方式：**
- 查询包信息：`rpm -qpi 包名.rpm`（显示包元数据）；`rpm -qpl 包名.rpm`（显示文件列表）。
- 查看脚本：`rpm -qp --scripts 包名.rpm`（显示安装/卸载脚本）。
- 解压内容：`rpm2cpio 包名.rpm | cpio -idmv`；或用 7-Zip 在 Windows 上解压。

**编辑/制作方式：**
- 使用 rpmbuild + SPEC 文件描述构建规则，`rpmbuild -bb 软件名.spec` 构建 RPM。
- 使用 mock 在干净 chroot 中构建（确保环境干净）。
- 使用 alien 工具可在 RPM 和 DEB 格式之间转换（但转换后可能有兼容问题）。

**命令行安装/卸载：**
```bash
sudo rpm -ivh 软件名.rpm      # 安装（i=install, v=verbose, h=hash进度）
sudo rpm -Uvh 软件名.rpm      # 升级安装（U=upgrade）
sudo dnf install 软件名.rpm    # 用dnf安装（自动处理依赖，推荐）
sudo dnf remove 软件包名      # 卸载
rpm -qa                      # 列出所有已安装的RPM包
rpm -ql 软件包名              # 查看已安装包的文件列表
dnf repoquery --requires 软件包名  # 查询依赖关系
```

## 5. 常见报错与解决

**问题1：安装时提示"依赖失败"或"missing dependency"**
- 原因：rpm 命令不自动下载依赖，只检查当前系统是否满足。
- 解决：使用 `sudo dnf install 软件名.rpm` 让 dnf 自动下载并安装依赖（推荐）；或手动 `dnf install 缺失的依赖包名` 后再安装目标RPM；配置 EPEL/RPM Fusion 等第三方仓库以获得更多依赖包。

**问题2：安装时提示"文件冲突（file conflict）"或"already exists"**
- 原因：RPM 要安装的文件路径已被另一个已安装包占用。
- 解决：先卸载冲突的旧包 `sudo rpm -e 冲突包名`；或使用 `sudo rpm -ivh --force 软件名.rpm` 强制覆盖（有风险，慎用）；使用 `dnf install` 通常更智能，会提示更明确的冲突信息。

**问题3：在 Fedora 上安装针对 RHEL 7 编译的 RPM 报错或不工作**
- 原因：RPM 是针对特定发行版和版本编译的，glibc、库版本可能不兼容。
- 解决：下载针对当前发行版和版本编译的 RPM；或使用 Flatpak/Snap 容器化应用跨发行版运行；或从源码编译安装。

**问题4：RPM 安装时提示"错误：GPG 检查失败"**
- 原因：RPM 包来自未签名的仓库，或 GPG 公钥未导入。
- 解决：导入对应仓库的 GPG 公钥 `sudo rpm --import 公钥文件`；确认包来源可信后用 `sudo dnf install --nogpgcheck 软件名.rpm` 跳过验证（仅限可信来源）；或用 `rpm -ivh --nosignature 软件名.rpm` 跳过签名检查。

---
## 小知识

RPM 是"递归缩写"——RPM 的全称就是"RPM Package Manager"（早期叫"Red Hat Package Manager"，后来改为递归形式）。RPM 最初由 Red Hat 在1997年发布，是 Linux 第一个被广泛采用的包管理格式。与 DEB 不同，RPM 强制要求包签名验证（GPG），这是它在企业环境中更受信任的原因之一。RPM 系发行版中 RHEL/CentOS/Rocky Linux 在企业服务器市场份额极高（尤其金融、电信、政府行业），因此 RPM 是企业 Linux 运维的必备知识。Fedora 项目是 RPM 新技术的试验场，许多包管理创新（如 dnf 取代 yum）都先在 Fedora 落地。

## 相关链接

- RPM 官方文档：https://rpm.org/
- Fedora 包管理指南：https://docs.fedoraproject.org/en-US/quick-docs/package-management/
- EPEL 仓库（企业级附加软件包）：https://docs.fedoraproject.org/en-US/epel/
- RPM Fusion（多媒体/驱动包仓库）：https://rpmfusion.org/
- rpmbuild 构建指南：https://rpm-packaging-guide.github.io/

# .pkg 文件后缀详解

## 1. 文件定义 & 用途

PKG（macOS Installer Package）是 macOS 操作系统的标准化安装包格式，由 Apple 的 Installer 程序（/System/Library/CoreServices/Installer.app）处理。与 DMG 的"拖拽安装"不同，PKG 通过向导式安装流程完成软件部署，可以执行复杂的安装操作：选择安装目标磁盘、运行预检脚本、按组件选择性安装、执行安装前/后脚本、要求管理员密码等。

PKG 文件本质上是一个 xar 归档，内部包含：PackageInfo（元数据）、Payload（实际文件，用cpio+gzip压缩）、Scripts（安装脚本）等组件。PKG 分为"flat package"（.pkg 单文件，现代标准）和"bundle package"（.pkg 目录结构，旧格式）两种形式。

## 2. 适用场景

- macOS 系统级软件安装（需要写系统目录、加载驱动等）
- Apple 官方软件分发（如 Xcode、macOS 补丁、Safari更新）
- 企业IT批量部署（配合 Apple Remote Desktop / MDM 推送 PKG）
- 需要预检/后处理脚本的复杂安装场景
- macOS 命令行工具和驱动安装
- 替代 DMG 用于需要正式安装流程的软件

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 7-Zip（解压查看内容） | - |
| Mac | 系统自带 Installer（双击运行）、productbuild（命令行）、pkgutil | Packages（开发工具）、Iceberg |
| Linux | xar（解压工具） | - |
| 跨平台(网页) | - | - |

> 安全提示：PKG 安装以 root 权限运行预检/后处理脚本，可修改任意系统文件。请只安装来自 Apple 或可信开发者的 PKG。安装前可在终端用 `pkgutil --check-signature 文件.pkg` 验证签名，或用 `pkgutil --expand 文件.pkg 输出目录` 查看脚本内容。

## 4. 如何编辑、如何导出

**查看方式：**
- 双击 PKG 通过 Installer 向导运行安装。
- 解压查看内容：`pkgutil --expand 文件.pkg 输出目录`，可查看 Payload 和 Scripts。
- 解开 Payload 查看实际文件：先 expand，再 `cd 输出目录 && cat Payload | gzip -d | cpio -i`。
- 查看 PackageInfo 元数据：`pkgutil --expand` 后查看 PackageInfo 文件。

**制作方式：**
- 使用 productbuild（macOS自带）：组合多个组件生成分发 PKG。
- 使用 pkgbuild：
```bash
pkgbuild --root /path/to/files --identifier com.example.app --version 1.0 --scripts 脚本目录 输出.pkg
```
- 使用 Packages（第三方图形工具，免费）：可视化设计 PKG 安装内容和脚本。

**命令行安装：**
```bash
sudo installer -pkg 软件名.pkg -target /        # 安装到系统盘
sudo installer -pkg 软件名.pkg -target /Volumes/外置盘  # 安装到指定盘
pkgutil --pkgs                                     # 列出已安装的PKG
pkgutil --pkg-info 包标识符                        # 查看安装信息
sudo pkgutil --forget 包标识符                     # 清除安装记录
```

## 5. 常见报错与解决

**问题1：安装时提示"安装遇到错误"或"安装失败"**
- 原因：可能是目标磁盘空间不足、预检脚本失败、或权限问题。
- 解决：查看安装日志（`/var/log/install.log`）定位具体失败原因；确保磁盘有足够空间；尝试以管理员身份重新安装；关闭其他可能干扰的程序。

**问题2：PKG 被Gatekeeper拦截"无法打开，因为来自身份不明的开发者"**
- 原因：PKG 未被 Apple 公证（notarization）或签名无效。
- 解决：右键 → "打开"确认后继续；或 `系统设置 → 隐私与安全性` 中允许打开；开发者需使用 `xcrun notarytool submit` 进行公证后重新分发。

**问题3：卸载PKG安装的软件很困难，找不到卸载程序**
- 原因：PKG 通常不提供卸载向导（不像DMG可手动删除.app）。
- 解决：用 `pkgutil --pkgs` 找到包标识符；`pkgutil --files 包标识符` 查看安装了哪些文件；手动删除对应文件；最后 `sudo pkgutil --forget 包标识符` 清除记录；或使用 UninstallPKG 等第三方工具。

**问题4：在终端安装PKG时提示"volume not found"或目标盘不识别"**
- 原因：-target 参数指定的目标盘不存在或未挂载。
- 解决：先用 `diskutil list` 确认目标盘的挂载点路径；使用 `installer -pkg xxx.pkg -target /` 安装到当前系统盘；确保目标盘文件系统格式兼容（一般需APFS或HFS+）。

---
## 小知识

PKG 的前身是 macOS Classic 时代的 Installer Vise 格式。Apple 在 Mac OS X 10.5 Leopard 时引入了 flat package（.pkg 单文件格式，基于 xar 归档），取代了旧的 bundle package（外观是一个目录）。PKG 和 DMG 在 macOS 上各司其职：DMG 适合简单的"拖拽即装"应用，PKG 则适合需要脚本、系统级配置、多组件选择的企业级安装。有趣的是，macOS 的系统更新和补丁本身就是 PKG 格式——你每次更新 macOS 系统，背后运行的就是 PKG 安装流程。Apple Remote Desktop 和 MDM（移动设备管理）方案可以远程批量推送 PKG 到成百上千台 Mac，这是企业 IT 管理Mac的标准做法。

## 相关链接

- Apple Installer 文档：https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/PackageManagementUserGuide/
- pkgbuild 命令手册：https://www.ss64.com/mac/pkgbuild.html
- pkgutil 命令手册：https://www.ss64.com/mac/pkgutil.html
- Packages（PKG制作工具）：https://s.sudre.free.fr/Software/Packages/about.html
- Apple 公证指南：https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution

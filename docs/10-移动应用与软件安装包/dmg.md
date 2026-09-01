# .dmg 文件后缀详解

## 1. 文件定义 & 用途

DMG（Apple Disk Image）是 macOS 操作系统原生支持的磁盘镜像文件格式。一个 DMG 文件本质上是一个虚拟磁盘容器，挂载后会在 Finder 侧边栏和桌面上显示为一个"磁盘"图标，里面可以存放任何文件。DMG 支持压缩、加密（AES-128/AES-256）和只读/读写/稀疏等多种模式。

在 macOS 生态中，DMG 最常见的用途是软件分发：开发者将应用打包到 DMG 中，用户下载后双击挂载，然后按提示将 .app 拖到 Applications 文件夹即可完成安装。DMG 也可以用作文件归档和加密存储容器。

## 2. 适用场景

- macOS 应用程序的下载与分发（最常见用途）
- macOS 软件安装（拖拽安装方式）
- 文件压缩归档（DMG压缩率高）
- 加密文件容器（保护敏感文件）
- macOS 系统安装镜像（如 macOS 安装器）
- 备份与传输大量文件

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 7-Zip、PeaZip（可解压查看DMG内容） | TransMac、PowerISO、UltraISO |
| Mac | 系统自带（双击挂载）、磁盘工具（Disk Utility） | DropDMG、DMG Canvas |
| Linux | 7-Zip、dmg2img（命令行转换） | - |
| 跨平台(网页) | - | - |

> 注意：在 Windows 上只能解压查看 DMG 内容，无法"运行"其中的 macOS 应用。macOS 应用只能在 Mac 上运行。

## 4. 如何编辑、如何导出

**使用方式（macOS）：**
- 双击 DMG 文件自动挂载到 Finder，像U盘一样使用。
- 完成后右键弹出（Eject）或在磁盘工具中卸载。
- 加密 DMG 需输入密码才能挂载。

**制作 DMG（macOS）：**
- 磁盘工具：`文件 → 新建映像 → 来自文件夹的映像`，可设置压缩、加密、格式。
- 命令行 hdiutil：
```bash
hdiutil create -volname "我的应用" -srcfolder /path/to/app -fs HFS+ -format UDZO 输出.dmg   # 压缩只读
hdiutil create -encryption AES-256 -size 500m -volname "加密盘" -fs HFS+ -type SPARSE 加密.dmg  # 加密读写
```
- 使用 DropDMG / DMG Canvas 等工具可制作带自定义背景图和拖拽提示的精美 DMG。

**转换格式：**
```bash
hdiutil convert 输入.dmg -format UDTO -o 输出.cdr     # 转为CD/DVD主镜像
hdiutil convert sparse.dmg -format UDZO -o 压缩.dmg    # 稀疏转压缩
```

## 5. 常见报错与解决

**问题1：DMG 打开后提示"无法打开，因为来自身份不明的开发者"**
- 原因：macOS 的 Gatekeeper 安全机制拦截了未签名或未公证的 DMG。
- 解决：右键点击 DMG → 选择"打开" → 在弹窗中确认"打开"；或到 `系统设置 → 隐私与安全性 → 允许下载的应用` 中点击"仍要打开"；如果来源可信，可临时 `sudo xattr -d com.apple.quarantine 文件路径` 去除隔离属性。

**问题2：DMG 挂载后只读，无法往里拖文件**
- 原因：大部分分发用 DMG 是只读格式（UDZO等），不可写入。
- 解决：将内容复制到其他位置编辑；如需可写镜像，创建时选择读写格式（`hdiutil create -type UDIF` 或磁盘工具选择"读/写"映像格式）。

**问题3：在 Windows 上打不开 DMG 或解压后乱码**
- 原因：DMG 使用 HFS+/APFS 文件系统，Windows 原生不支持。
- 解决：使用 7-Zip 最新版可直接解压大部分 DMG；使用 TransMac / PowerISO 挂载或解压；如果 DMG 是加密的，Windows 工具可能无法直接解密，需在 Mac 上先挂载后导出内容。

**问题4：DMG 文件无法弹出（Eject），提示"正在使用中"**
- 原因：有程序正在使用 DMG 内的文件，或 Finder/Spotlight 进程占用。
- 解决：关闭所有使用 DMG 内文件的程序；在磁盘工具中强制卸载；终端执行 `hdiutil detach /Volumes/卷名 -force` 强制卸载；重启 Mac 通常可解决卡死。

---
## 小知识

DMG 格式是 Apple 在1994年随 Mac OS 7.1 引入的，最初用于软盘镜像。如今 DMG 已成为 macOS 软件分发的标准载体——"下载DMG → 挂载 → 拖App到Applications"几乎成了 Mac 用户的肌肉记忆。DMG 相比传统安装包有个独特优点：它本身不需要"安装"过程，用户只需挂载后拖拽即可。Apple 自家的所有软件（包括 macOS 系统安装器本身）都以 DMG 形式分发。DMG 还支持对内容进行数字签名和公证（notarization），这是 macOS 软件安全体系的重要一环。有趣的是，DMG 文件可以通过自定义背景图和图标位置，呈现非常精美的"安装引导"效果，这是很多 Mac 软件的第一印象。

## 相关链接

- Apple 磁盘工具文档：https://support.apple.com/guide/disk-utility
- hdiutil 命令手册：https://ss64.com/mac/hdiutil.html
- DropDMG（DMG制作工具）：https://c-command.com/dropdmg/
- DMG Canvas：https://www.joltsoft.com/dmgcanvas/
- 7-Zip（解压DMG）：https://www.7-zip.org/

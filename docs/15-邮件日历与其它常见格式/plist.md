# .plist 文件后缀详解

## 1. 文件定义 & 用途

PLIST 是**属性列表文件**（Property List）的后缀，由苹果公司开发，是 macOS 和 iOS 系统中用来存储配置数据的标准格式。它类似于 Windows 的注册表或 INI 文件，用于保存应用的设置、偏好、权限信息等。

- **全称**：Property List（属性列表）
- **类型**：配置/数据文件
- **开发者**：苹果公司（Apple Inc.）
- **适用平台**：macOS、iOS、iPadOS、watchOS、tvOS
- **标准**：苹果开源的 Property List 格式（基于 NeXTSTEP 的 plist）

PLIST 文件可以有两种存储格式：
- **XML 格式**（传统）：纯文本，可读性好，可用文本编辑器直接编辑
- **二进制格式**（Binary Plist）：体积小、读取快，但不能用文本编辑器直接查看

## 2. 适用场景

- **macOS 应用配置**：存储应用的设置和偏好
- **iOS App 配置**：Info.plist 存储应用的基本配置（权限、版本号、图标等）
- **系统偏好设置**：macOS 系统设置存储在 plist 文件中
- **快捷方式信息**：.webloc 等快捷方式文件本质上是 plist
- **数据序列化**：开发者用 plist 存储结构化数据（数组、字典、字符串等）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 文本编辑器（记事本/Notepad++/VS Code）、Plist Editor | - |
| Mac | Xcode（免费）、文本编辑（TextEdit，可打开 XML 格式）、Quick Look（空格预览） | BBEdit、PlistEdit Pro |
| Linux | 文本编辑器、libplist 工具（plutil） | - |
| 跨平台 | VS Code（XML 格式可直接查看） | - |

**新手推荐**：
- Mac 用户：用 **Xcode**（苹果免费）或**文本编辑**打开
- Windows 用户：用 **Notepad++** 打开 XML 格式的 plist；二进制格式用 **Plist Editor**
- 快速查看：Mac 上选中 plist 文件按 **空格键**（Quick Look）预览

## 4. 如何编辑、如何导出

### 如何打开 PLIST 文件
1. **XML 格式**：直接用文本编辑器（记事本/Notepad++/VS Code）打开，可读可编辑
2. **二进制格式**：需要用 plist 编辑器或 `plutil` 工具转换后查看
3. **Mac 上**：用 Xcode 打开（双击 plist 文件，Xcode 提供树形编辑界面）
4. **Mac 上快速查看**：选中文件按空格键（Quick Look）预览内容

### 如何编辑 PLIST 文件
1. **Mac 上用 Xcode**：双击 plist 文件 → Xcode 打开 → 编辑键值对 → 保存
2. **XML 格式直接编辑**：用文本编辑器打开，修改 XML 内容后保存
3. **命令行转换**（Mac）：`plutil -convert xml1 file.plist`（二进制转 XML）
4. **命令行转换**（Mac）：`plutil -convert binary1 file.plist`（XML 转二进制）

### XML 格式 PLIST 示例
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>MyApp</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>UIRequiredDeviceCapabilities</key>
    <array>
        <string>armv7</string>
    </array>
</dict>
</plist>
```

### 格式转换
- **二进制转 XML**：`plutil -convert xml1 file.plist`（Mac 命令行）
- **XML 转二进制**：`plutil -convert binary1 file.plist`
- **转 JSON**：`plutil -convert json file.plist`
- **Windows 上**：用 Plist Editor 工具查看和转换二进制 plist

## 5. 常见报错与解决

### 问题1：二进制 PLIST 用记事本打开是乱码
**原因**：该 plist 文件是二进制格式（Binary Plist），不是 XML 文本格式，文本编辑器无法正确显示。

**解决方法**：
1. Mac 上用 Xcode 打开（自动识别二进制格式）
2. Mac 命令行转换：`plutil -convert xml1 file.plist`，然后用文本编辑器打开
3. Windows 用户安装 Plist Editor 工具查看二进制 plist
4. 在线工具：搜索"binary plist viewer online"使用在线查看器
5. 用 libplist 工具（Linux/Mac）：`plistutil -i file.plist -o file.xml`

---

### 问题2：修改 PLIST 文件后应用无法打开
**原因**：修改了 plist 中的关键配置项（如 Info.plist 中的 Bundle ID、权限声明等），导致应用无法正常加载。

**解决方法**：
1. 先备份原文件，修改前务必保留原始 plist 副本
2. 如果已修改且应用崩溃：恢复备份的原 plist 文件
3. 确保 XML 格式正确：用 `plutil -lint file.plist` 检查语法
4. 确保 plist 结构完整：所有 `<dict>`、`<array>`、`<key>`、`<string>` 标签必须正确配对
5. Info.plist 中的关键键值（如 CFBundleIdentifier）不要随意修改
6. 修改系统 plist 需要管理员权限：`sudo nano /Library/Preferences/...`

---

### 问题3：Windows 上打开 plist 提示编码错误
**原因**：plist XML 文件使用了 UTF-8 编码，但 Windows 记事本可能以其它编码打开。

**解决方法**：
1. 用 Notepad++ 或 VS Code 打开（支持 UTF-8 编码）
2. 在 Notepad++ 中：编码 → UTF-8
3. 用 VS Code 打开：右下角状态栏选择 UTF-8 编码
4. 如果文件含中文内容，确保编辑器设为 UTF-8
5. 保存时也选 UTF-8 编码，不要保存为 ANSI 格式

---
## 💡 小知识

PLIST 格式的历史可以追溯到 NeXTSTEP 操作系统（乔布斯离开苹果后创立的公司开发的系统）。当苹果收购 NeXT 后，NeXTSTEP 的很多技术（包括 plist）被带入了 macOS。所以你今天在 Mac 上看到的 plist 文件，其实已经有三十多年的历史了。

在 iOS 开发中，每个 App 都有一个 `Info.plist` 文件——它是应用的"身份证"，记录了应用名称、版本号、支持的设备方向、需要的权限等关键信息。没有这个文件，App 根本无法安装运行。

## 🔗 相关链接

- [苹果 Property List 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/)
- [Plist Editor for Windows](https://www.icopybot.com/plist-editor.htm)
- [libplist 开源工具](https://github.com/libimobiledevice/libplist)
- [plutil 命令行文档](https://www.unix.com/man-page/osx/1/plutil/)

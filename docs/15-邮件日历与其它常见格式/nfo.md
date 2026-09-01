# .nfo 文件后缀详解

## 1. 文件定义 & 用途

NFO 是**信息文件**（Info File 或 "ReadMe" File）的后缀，是一种纯文本文件，通常包含软件的说明信息、版本说明、安装指南、团队介绍等。在软件发布和场景中，NFO 文件相当于一个"自我介绍"文件。

- **全称**：Info / Information File
- **类型**：纯文本信息文件
- **特点**：纯文本格式，常用 ASCII/Unicode 艺术（ASCII Art）制作精美排版
- **历史**：源于 BBS（电子公告板）时代，场景常用它作为发布说明

NFO 文件的内容通常包括：软件名称、版本号、发布日期、系统要求、安装步骤、破解说明、发布团队名称和签名等。很多 NFO 文件还包含精美的 ASCII 艺术图案——用字符拼出大标题和图案。

## 2. 适用场景

- **软件发布说明**：压缩包中附带的说明文件，介绍软件信息
- **场景发布信息**：破解组/发布组的信息文件（常见于盗版/场景发布）
- **安装指南**：提供软件安装和使用说明
- **版本信息**：记录软件版本变更历史
- **ASCII 艺术展示**：用字符制作的精美图案和标题

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 记事本（系统自带，需等宽字体）、Notepad++、DAMN NFO Viewer | - |
| Mac | 文本编辑（TextEdit，需设等宽字体）、BBEdit（免费版） | - |
| Linux | Gedit/VS Code（需等宽字体）、终端 `cat` | - |
| 跨平台 | VS Code（设等宽字体）、浏览器（需配合等宽 CSS） | - |

**新手推荐**：
- **Windows 专用**：**DAMN NFO Viewer**（专门查看 NFO，自动用等宽字体和正确编码）
- **通用方案**：用 **Notepad++** 打开，设置字体为"等宽字体"（如 Consolas、Courier New）
- **命令行**：Linux/Mac 用终端 `cat file.nfo` 查看（终端默认等宽字体）

## 4. 如何编辑、如何导出

### 如何正确打开 NFO 文件
1. **用 DAMN NFO Viewer**（Windows）：专为 NFO 设计，正确显示 ASCII 艺术和编码
2. **用 Notepad++**：打开后 → 设置字体为 Consolas 或 Courier New（等宽字体）→ 编码选 OEM/IBM PC 或 UTF-8
3. **用记事本**：打开后 → 格式 → 字体 → 选择 Courier New 或 Consolas（否则 ASCII 艺术会错位）
4. **终端查看**：Linux/Mac 终端 `cat file.nfo`（终端默认等宽字体）

### 为什么需要等宽字体
NFO 文件中的 ASCII 艺术依赖字符等宽对齐——每个字符占相同宽度。如果用非等宽字体（如 Arial），字符宽度不一致，图案就会错乱变形。等宽字体（如 Consolas、Courier New、Monaco）保证每个字符等宽，图案才能正确显示。

### 如何编辑 NFO 文件
1. 用文本编辑器（Notepad++/VS Code）打开直接编辑
2. 编码注意：NFO 文件常用 CP437（OEM/IBM PC 编码）或 UTF-8，用 Notepad++ 切换编码查看
3. 制作 ASCII 艺术：可以用文本编辑器手动绘制，或用 ASCII 艺术生成工具

### 如何创建 NFO 文件
1. 用文本编辑器创建一个新文件
2. 写入说明内容（软件名、版本、说明等）
3. 可选：用 ASCII 艺术制作标题图案
4. 保存为 .nfo 后缀，编码选 UTF-8 或 CP437

## 5. 常见报错与解决

### 问题1：NFO 文件打开后 ASCII 艺术图案错乱变形
**原因**：使用了非等宽字体（如 Arial、微软雅黑），字符宽度不一致导致对齐错乱。

**解决方法**：
1. 用 DAMN NFO Viewer 打开（自动使用等宽字体和正确编码）
2. 用 Notepad++ 打开 → 设置 → 首选项 → 字体 → 选择 Consolas 或 Courier New
3. 用记事本打开 → 格式 → 字体 → 选择"Courier New"或"Consolas"
4. 用 VS Code 打开 → 设置字体为 monospace（等宽）系列
5. 在终端中用 `cat file.nfo` 查看（终端默认等宽字体）

---

### 问题2：NFO 文件打开后乱码或特殊字符显示异常
**原因**：NFO 文件通常使用 CP437（DOS/OEM 编码），而现代编辑器默认用 UTF-8 打开，导致部分特殊字符乱码。

**解决方法**：
1. 用 DAMN NFO Viewer 打开（自动检测 DOS 编码）
2. 用 Notepad++ 打开 → 编码 → 字符集 → DOS/OEM → CP437
3. 也可以尝试其它 OEM 编码：CP850（西欧）、CP866（俄文）
4. 如果 NFO 是 UTF-8 编码的：Notepad++ → 编码 → UTF-8
5. 如果不确定编码：逐个尝试 CP437、UTF-8、Windows-1252 直到显示正常

---

### 问题3：Windows 中双击 NFO 文件打开了"系统信息"工具
**原因**：Windows 系统的"系统信息"工具（msinfo32.exe）默认关联了 .nfo 后缀，但场景中的 NFO 文件其实是文本文件，不是系统信息文件。

**解决方法**：
1. 右键 NFO 文件 → 打开方式 → 选择记事本或 Notepad++
2. 或右键 → 打开方式 → 选择其它应用 → 浏览 → 选择 Notepad++ → 勾选"始终使用此应用"
3. 安装 DAMN NFO Viewer 并设为 .nfo 默认程序
4. 修改文件关联：Windows 设置 → 应用 → 默认应用 → 按 .nfo 文件类型 → 选择文本编辑器
5. 也可以把 .nfo 文件拖到文本编辑器窗口中打开

---
## 💡 小知识

NFO 文件的历史可以追溯到 1980 年代的 BBS（电子公告板系统）时代。当时，破解团队（cracker groups）在发布破解软件时，会附带一个 NFO 文件，里面用 ASCII 艺术绘制团队 Logo 和签名，加上软件说明和问候语。这成了一种独特的"场景文化"（Scene Culture）——不同团队用不同风格的 ASCII 艺术来展示自己的"门面"。

有趣的是，Windows 系统的"系统信息"工具也使用 .nfo 后缀（它的 NFO 文件是 XML 格式的系统信息导出），这经常导致冲突——双击 NFO 文件会打开系统信息工具而不是文本编辑器。所以当你收到一个来自场景发布的 NFO 文件时，记得用右键 → 打开方式 → 记事本来查看。

## 🔗 相关链接

- [DAMN NFO Viewer 下载](https://www.softpedia.com/get/Office-tools/Other-Office-Tools/DAMN-NFO-Viewer.shtml)
- [Notepad++ 官网](https://notepad-plus-plus.org/)
- [ASCII 艺术生成器](https://patorjk.com/software/taag/)
- [CP437 编码说明](https://en.wikipedia.org/wiki/Code_page_437)

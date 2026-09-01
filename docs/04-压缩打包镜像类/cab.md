# .cab 文件后缀详解

## 1. 文件定义 & 用途

CAB 是 **Windows Cabinet** 的缩写，是微软开发的一种压缩归档文件格式。它主要用于 Windows 系统的软件安装包、系统组件更新和驱动程序打包。很多 Windows 系统更新（Windows Update）和驱动安装包内部都使用 CAB 格式。

简单来说，.cab 是微软自家的压缩包格式——常用于 Windows 系统组件安装和驱动打包。

- **全称**：Microsoft Cabinet File
- **类型**：压缩归档文件
- **开发者**：Microsoft（微软）
- **发布年份**：1997年（随 Internet Explorer 4 推出）
- **特点**：支持数据压缩、数字签名、可嵌入安装脚本
- **常见用途**：Windows 更新包（.msu 内部包含 .cab）、驱动安装包

## 2. 适用场景

- Windows 系统更新和补丁安装（通过 DISM 命令安装 .cab 补丁）
- Windows 驱动程序打包安装
- 软件安装程序内部组件打包
- Windows 系统组件的添加和删除（如启用/关闭 Windows 功能）
- 企业 IT 批量部署 Windows 更新

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 系统自带（expand/dism 命令）、7-Zip、PeaZip | WinRAR |
| Mac | The Unarchiver（部分支持）、7-Zip（命令行） | - |
| Linux | cabextract（命令行工具） | - |

**新手推荐**：
- 查看/解压内容：**7-Zip**（免费开源，可以右键解压 cab 文件）
- 安装 Windows 补丁：用系统自带的 **DISM 命令**
- 命令行解压：`expand file.cab -F:* 输出目录`

## 4. 如何编辑、如何导出

### 如何解压
**图形界面：**
1. 右键 .cab 文件 → 7-Zip → 解压到当前文件夹
2. 双击 .cab 文件可以用 7-Zip 查看内部文件列表

**命令行解压：**
```cmd
# 使用 expand 命令解压
expand example.cab -F:* C:\目标目录

# 使用 7-Zip 命令行
7z x example.cab -oC:\目标目录
```

### 如何安装 Windows 补丁（.cab 格式）
```cmd
# 用 DISM 安装 cab 格式的 Windows 更新
DISM /Online /Add-Package /PackagePath:C:\update.cab

# 用 pkgmgr（旧版方法，不推荐）
start /w pkgmgr /ip /m:C:\update.cab /quiet
```

### 如何创建 cab 文件
```cmd
# 使用 makecab 呺令创建 cab 文件
makecab /v3 /d cabinetname=MyArchive.cab file1.txt file2.txt
```

## 5. 常见报错与解决

### 问题1：安装 cab 补丁时 DISM 报错 0x800f081f
**原因**：系统组件存储损坏、cab 文件不适用于当前 Windows 版本、或缺少依赖组件。

**解决方法**：
1. 确认 cab 文件适用于你的 Windows 版本（如 Win10 vs Win11）
2. 运行系统文件检查：`sfc /scannow`
3. 修复组件存储：`DISM /Online /Cleanup-Image /RestoreHealth`
4. 重启电脑后重新尝试安装
5. 从微软官网重新下载对应的更新包

---

### 问题2：cab 文件用 7-Zip 打开后只有部分文件，缺少安装脚本
**原因**：cab 文件可能只包含数据文件，安装脚本（.inf 或 .xml）在另一位置或已丢失。

**解决方法**：
1. 检查 cab 文件是否是某个 .msu 或 .msi 安装包的一部分
2. 如果是驱动安装包，可能需要用 `pnputil` 命令安装：`pnputil /add-driver driver.cab /install`
3. 尝试用 expand 命令解压所有文件后再手动安装
4. 从原始下载页面获取完整的安装包

---

### 问题3：cab 文件损坏，解压时报错或安装失败
**原因**：下载不完整、文件被修改、存储介质损坏等。

**解决方法**：
1. 重新下载 cab 文件
2. 验证文件哈希值（SHA256）确认完整性
3. 用 7-Zip 尝试解压（容错性可能比系统工具好）
4. 从微软官网或设备厂商官网重新获取
5. 检查磁盘是否有坏道

---

### 问题4：makecab 创建 cab 文件时报错或参数不对
**原因**：makecab 命令语法复杂，参数设置不正确。

**解决方法**：
1. 使用正确的 makecab 语法，参考微软文档
2. 使用 .ddf（Diamond Directive File）定义文件来简化操作
3. 或者用 7-Zip 命令行创建：`7z a -tcab output.cab file1 file2`
4. 对于简单的文件打包，建议直接用 .zip 格式更简单

---

## 💡 小知识

CAB 格式虽然不如 zip 和 7z 那样被普通用户熟知，但它在 Windows 系统内部无处不在。每次你通过 Windows Update 安装更新、安装新打印机驱动、添加 Windows 功能时，底层几乎都在处理 .cab 文件。CAB 格式支持微软的 Authenticode 数字签名技术，这意味着你可以验证一个 cab 文件是否来自微软或可信厂商、是否被篡改。对于 IT 运维人员来说，DISM + CAB 是批量管理 Windows 更新的标准操作。

## 🔗 相关链接

- [CAB 格式说明 - 维基百科](https://zh.wikipedia.org/wiki/Cabinet_(file_format))
- [7-Zip 官网](https://www.7-zip.org/)
- [DISM 命令参考 - 微软文档](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/deployment-image-servicing-and-management--dism--command-line-options)
- [cabextract 工具](https://www.cabextract.org.uk/)
- [.zip 格式详解](./zip.md)
- [.7z 格式详解](./7z.md)

# .msg 文件后缀详解

## 1. 文件定义 & 用途

MSG 是**微软 Outlook 邮件格式**（Outlook Message Format），由微软开发，专门用于保存 Outlook 中的邮件、约会、联系人、任务等项目。与通用的 EML 不同，MSG 是 Outlook 的私有二进制格式，基于 MAPI（消息应用程序编程接口）结构。

- **全称**：MSG（Outlook Message Format）
- **类型**：电子邮件消息文件（私有格式）
- **开发者**：微软（Microsoft）
- **特点**：可保存邮件全部信息（正文+附件+元数据），与 Outlook 深度绑定
- **兼容性**：Outlook 原生支持，其他客户端需要转换

MSG 文件的优势是完整保留了 Outlook 邮件的所有信息——发件人、收件人、抄送、正文、附件、甚至邮件格式和 Outlook 特有的属性。缺点是它是私有格式，在非 Outlook 环境下打开比较麻烦。

## 2. 适用场景

- **Outlook 邮件存档**：从 Outlook 中单独保存某封邮件
- **邮件共享转发**：把邮件连同附件打包成一个文件发给同事
- **法律取证保留**：完整保留 Outlook 邮件原始状态
- **Outlook 邮件迁移**：在不同 Outlook 之间迁移单封邮件
- **项目文档管理**：将关键邮件作为项目文档保存

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Mozilla Thunderbird（需插件）、Kernel MSG Viewer、Free MSG Viewer | Microsoft Outlook、SysTools MSG Converter |
| Mac | Mozilla Thunderbird（需插件）、Apple 邮件（需先转换） | Microsoft Outlook for Mac |
| Linux | MailConverter、命令行工具 libpst | - |
| 跨平台 | 在线 MSG 转 EML/PDF 工具 | SysTools、Kernel 等付费转换工具 |

**新手推荐**：
- 有 Outlook：直接双击打开，Outlook 原生支持最好
- 没 Outlook：用 **Free MSG Viewer** 或 **Kernel MSG Viewer** 免费查看
- 跨平台方案：用在线工具将 MSG 转成 EML 或 PDF 后打开

## 4. 如何编辑、如何导出

### 如何打开 MSG 文件
1. **有 Outlook 的情况**：双击 MSG 文件，Outlook 自动打开并显示邮件
2. **没有 Outlook 的情况**：安装 Free MSG Viewer / Kernel MSG Viewer 免费查看
3. **浏览器方式**：将 MSG 拖入支持的在线查看器（注意隐私）
4. **命令行方式**：Linux/Mac 可用 `libpst` 工具的 `readpst` 命令转换

### 如何导出 MSG 文件
- **从 Outlook 导出**：选中邮件 → 文件 → 另存为 → 保存类型选择"Outlook 消息格式 (*.msg)"
- **拖拽导出**：直接从 Outlook 邮件列表拖拽到桌面或文件夹，自动生成 MSG 文件
- **批量导出**：使用 Outlook 的导出功能或第三方工具批量保存为 MSG

### 如何关联邮件客户端
- **Windows**：右键 MSG 文件 → 属性 → 打开方式 → 更改 → 选择 Outlook
- **设置默认**：设置 → 应用 → 默认应用 → 按文件类型选择 .msg → 选择 Outlook
- **注意**：MSG 文件与 Outlook 关联后，双击会以 Outlook 窗口形式打开

### 格式转换
- **MSG 转 EML**：用 Outlook 打开后另存为 EML；或用在线转换工具
- **MSG 转 PDF**：Outlook 打开后打印为 PDF；或用 SysTools MSG to PDF Converter
- **MSG 转 PST**：用 Outlook 导入功能，将 MSG 文件导入到 PST 存储文件中

## 5. 常见报错与解决

### 问题1：没有安装 Outlook，无法打开 MSG 文件
**原因**：MSG 是 Outlook 私有格式，系统自带工具无法直接打开。

**解决方法**：
1. 安装免费的 **Free MSG Viewer** 或 **Kernel MSG Viewer** 查看邮件内容
2. 用 Mozilla Thunderbird + ImportExportTools NG 插件导入 MSG
3. 使用在线转换工具（如 Zamzar、Converter365）将 MSG 转为 EML 或 PDF
4. 如果只是想看内容，可以让发件人把邮件转发给你，或者改存为 EML 格式

---

### 问题2：MSG 文件打开后附件丢失或无法保存
**原因**：MSG 文件中附件未正确嵌入，或 Outlook 版本不兼容导致附件解析失败。

**解决方法**：
1. 确保使用与创建 MSG 文件相同或更高版本的 Outlook 打开
2. 用 Outlook 打开后，右键附件 → 保存为，手动逐个保存
3. 尝试将 MSG 导入 Outlook 后再查看附件（导入比直接打开更稳定）
4. 用第三方工具（如 SysTools MSG Converter）提取附件
5. 让发件人改为 EML 格式发送，EML 格式的附件兼容性更好

---

### 问题3：MSG 文件在 Mac 上打不开
**原因**：macOS 没有原生的 MSG 文件支持，Outlook for Mac 的 MSG 兼容性也有差异。

**解决方法**：
1. 安装 Microsoft Outlook for Mac，尝试导入 MSG 文件
2. 使用在线转换工具将 MSG 转为 EML（Mac 的 Apple 邮件可以打开 EML）
3. 用 Mozilla Thunderbird for Mac + 插件导入
4. 在 Windows 电脑上打开 MSG，另存为 EML 或 PDF 后传到 Mac 上
5. 如果只需查看内容，用在线 MSG 查看器直接在浏览器中打开

---

### 问题4：MSG 文件打开后显示"无法读取该文件"
**原因**：MSG 文件损坏、被截断，或 Outlook 数据文件关联异常。

**解决方法**：
1. 尝试用 Outlook 的"打开和修复"功能（文件 → 打开 → 打开 Outlook 数据文件）
2. 用 Free MSG Viewer 尝试打开（容错性有时比 Outlook 好）
3. 如果文件在传输过程中损坏，重新获取一份
4. 检查文件大小是否异常（过小可能意味着被截断）
5. 用 SCANPST 工具修复 Outlook 数据文件后重新导入

---
## 💡 小知识

MSG 和 EML 都是保存邮件的格式，但本质完全不同：EML 是通用的纯文本格式（基于 MIME 标准），任何邮件客户端都能打开；而 MSG 是微软 Outlook 的私有格式，基于 MAPI 接口，完整保存了 Outlook 特有的邮件属性。简单来说，EML 像是一封"标准信件"，谁都能读懂；MSG 则像一封"Outlook 专属信件"，只有在 Outlook 家门口才能拆开。

如果你需要在非 Outlook 环境下分享邮件，建议先转成 EML 或 PDF 格式，兼容性要好得多。

## 🔗 相关链接

- [Free MSG Viewer 下载](https://www.freeopentool.com/)
- [SysTools MSG Converter](https://www.systoolsgroup.com/)
- [在线 MSG 转 EML 工具](https://www.zamzar.com/convert/msg/to/eml/)
- [.eml 文件后缀详解](./eml.md)

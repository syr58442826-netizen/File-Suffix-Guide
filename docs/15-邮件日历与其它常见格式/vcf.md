# .vcf 文件后缀详解

## 1. 文件定义 & 用途

VCF 是 **vCard 格式**（Virtual Contact File）的文件后缀，是一种标准的电子名片格式。它用于存储联系人信息，包括姓名、电话、邮箱、地址、公司、职位、照片等。几乎所有手机和电脑的通讯录应用都支持 VCF 格式。

- **全称**：vCard / Virtual Contact File
- **类型**：电子名片/联系人文件
- **开发者**：互联网联盟（IETF），由 Versit 联盟发起
- **特点**：纯文本格式、跨平台兼容、可包含照片和多类型联系信息
- **标准**：RFC 6350（vCard 4.0），向后兼容 vCard 2.1/3.0

VCF 文件是纯文本，以 `BEGIN:VCARD` 开头、`END:VCARD` 结尾。中间用 `FN`（显示名）、`TEL`（电话）、`EMAIL`（邮箱）等字段来描述联系人信息。一个 VCF 文件可以包含一个或多个联系人。

## 2. 适用场景

- **联系人交换**：把名片以 VCF 格式发送给别人，对方直接导入通讯录
- **通讯录迁移**：从安卓手机导出联系人 VCF，导入到 iPhone 或新手机
- **联系人备份**：导出全部联系人为 VCF 文件存档
- **邮件签名附件**：在邮件中附上个人 VCF 名片
- **批量导入联系人**：从 Excel/CSV 转为 VCF 后批量导入手机

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Windows 联系人（系统自带）、Outlook 免费版、Mozilla Thunderbird | Microsoft Outlook |
| Mac | Apple 通讯录/Contacts（系统自带） | Microsoft Outlook for Mac、Cardhop |
| Linux | Evolution、Mozilla Thunderbird、GNOME Contacts | - |
| 手机 | 手机自带通讯录（安卓/iOS）、Google 通讯录 | - |
| 跨平台 | Google 通讯录网页版、文本编辑器（记事本/VS Code） | - |

**新手推荐**：
- 最简单方式：**双击 VCF 文件**，系统通讯录会提示添加联系人
- 手机用户：通过邮件/微信/蓝牙收到 VCF 后，用通讯录 App 打开
- 批量管理：通过 **Google 通讯录**网页版批量导入导出

## 4. 如何编辑、如何导出

### 如何打开 VCF 文件
1. **双击打开**：系统通讯录自动提示"添加到联系人"
2. **拖拽导入**：把 VCF 文件拖到通讯录应用窗口中
3. **手机打开**：在邮件/文件管理器中点击 VCF 文件，选择用通讯录打开
4. **文本编辑器打开**：右键 → 打开方式 → 记事本，查看源码

### 如何导出 VCF 文件
- **Android 手机**：通讯录 → 设置 → 导出 → 导出为 .vcf 文件
- **iPhone**：通过 iCloud 通讯录或第三方 App 导出；或用"分享联系人"功能
- **Google 通讯录**：通讯录网页版 → 导出 → 选择 vCard 格式
- **Windows 通讯录**：选中联系人 → 导出 → 选择 vCard 格式
- **Outlook**：选中联系人 → 文件 → 打开和导出 → 导入/导出 → 导出为 vCard

### 如何手动编辑/创建 VCF 文件
VCF 是纯文本，可以直接用记事本创建：
```
BEGIN:VCARD
VERSION:3.0
FN:张三
N:三;张;;;
TEL;TYPE=CELL:13800138000
EMAIL:zhangsan@example.com
ORG:某某公司
TITLE:产品经理
END:VCARD
```
- 用记事本/VS Code 编辑上述内容，保存为 `.vcf` 即可

### 格式转换
- **CSV/Excel 转 VCF**：用在线工具（如 CSV to vCard Converter）转换
- **VCF 转 CSV**：用在线工具导出为 Excel 可读的 CSV 格式
- **VCF 合并**：多个 VCF 可直接用文本编辑器合并内容（注意 BEGIN/END 配对）

## 5. 常见报错与解决

### 问题1：VCF 导入后中文姓名乱码
**原因**：VCF 文件编码不是 UTF-8（常见于旧手机导出的 vCard 2.1，可能用了 GBK 编码）。

**解决方法**：
1. 用文本编辑器（如 Notepad++ 或 VS Code）打开 VCF 文件
2. 将编码从 GBK/GB2312 转换为 UTF-8 后保存
3. 重新导入到通讯录
4. 如果是 vCard 2.1 格式，建议升级为 vCard 3.0（将 `VERSION:2.1` 改为 `VERSION:3.0`）
5. 通过 Google 通讯录导入（Google 对编码兼容性较好）

---

### 问题2：VCF 文件导入手机后联系人数量不对
**原因**：一个 VCF 文件中包含多个联系人，但某些手机只导入了第一个联系人；或者 VCF 格式不兼容。

**解决方法**：
1. 用文本编辑器打开 VCF，确认是否包含多个 `BEGIN:VCARD`...`END:VCARD` 块
2. 如果手机不支持多联系人 VCF，用在线工具拆分为单个 VCF 文件后再导入
3. 改用 Google 通讯录导入：先导入到 Google 账号，再同步到手机
4. 检查 VCF 版本：vCard 3.0 兼容性最好，旧版 2.1 可能不被某些手机支持
5. 确保 `VERSION:` 字段存在且值正确

---

### 问题3：VCF 联系人中的照片导入后不显示
**原因**：照片以 Base64 编码嵌入 VCF，部分通讯录应用不支持内嵌照片或照片编码不完整。

**解决方法**：
1. 用文本编辑器打开 VCF，搜索 `PHOTO` 字段确认照片数据是否存在
2. 确认 `PHOTO` 字段格式正确：`PHOTO;ENCODING=b;TYPE=JPEG:` 后跟 Base64 编码
3. 部分手机要求照片数据在一行内（不能换行），检查是否有意外截断
4. 如果照片太大，压缩后再嵌入（大照片可能导致 VCF 文件过大，解析失败）
5. 替代方案：先导入联系人（不含照片），然后手动在通讯录中添加照片
6. 通过 Google 通讯录导入后再同步，Google 会处理照片兼容性问题

---
## 💡 小知识

VCF（vCard）和 ICS（iCalendar）是一对"兄弟"格式——它们都由 Versit 联盟（苹果、AT&T、IBM、西门子于 1996 年组成）发起制定，后来都成为了 IETF 标准。vCard 管联系人，iCalendar 管日程，两者经常搭配使用：比如一封会议邀请邮件中，可能同时包含一个 ICS 日程文件和一个 VCF 联系人名片。

如今 vCard 已经发展到 4.0 版本，支持社交媒体账号、GPS 坐标等现代信息。但兼容性最好的还是 3.0 版本——如果你需要跨平台使用，建议导出为 vCard 3.0 格式。

## 🔗 相关链接

- [RFC 6350 vCard 4.0 标准](https://www.rfc-editor.org/rfc/rfc6350)
- [Google 通讯录](https://contacts.google.com/)
- [CSV 转 vCard 在线工具](https://csv-to-vcard.com/)
- [.ics 日历日程文件后缀详解](./ics.md)

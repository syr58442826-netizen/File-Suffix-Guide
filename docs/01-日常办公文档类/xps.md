# .xps 文件后缀详解

## 1. 文件定义 & 用途

XPS 是 **XML 纸张规范**（XML Paper Specification）的缩写，是微软推出的一种固定版式文档格式，定位和 PDF 类似——确保在任何设备上打开，排版都完全一致。它是 Windows 系统内置支持的格式，但普及率远不如 PDF。

- **全称**：XML Paper Specification
- **类型**：固定版式文档
- **开发者**：Microsoft（微软）
- **发布年份**：2006年（随 Windows Vista 推出）
- **特点**：Windows 原生支持、基于 XML、无需额外软件即可查看
- **优势**：Windows 自带 XPS 查看器，不用装 PDF 阅读器就能看

## 2. 适用场景

- 在 Windows 上打印预览和保存电子文档
- 不需要安装 PDF 阅读器时的文档分发
- Windows 环境下的文档存档
- 某些 Windows 应用的导出格式
- 电子发票和电子票据（部分地区使用）
- 扫描文件的保存格式（部分扫描仪支持）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | XPS 查看器（系统自带）、Edge 浏览器 | Microsoft XPS Document Writer、Adobe Acrobat（需转换） |
| Mac | 没有原生支持，需转换为 PDF 查看 | Pagemark XpsViewer（第三方） |
| Linux | 没有原生支持，需转换格式 | Evince（部分支持）、Okular（部分支持） |
| 手机 | 基本不支持，需转换为 PDF | - |

**新手推荐**：
- Windows 用户：双击即可用系统自带的 **XPS 查看器** 打开
- 非 Windows 用户：建议转成 PDF 再看
- 最通用方案：把 XPS 转成 PDF，然后用任何 PDF 阅读器打开

## 4. 如何编辑、如何导出

### 如何编辑
XPS 和 PDF 类似，是固定版式格式，主要用于查看，编辑比较困难：

1. **注释标记**：Windows 自带的 XPS 查看器可以添加批注和高亮
2. **转换后编辑**：转成 Word/PDF 格式后再编辑
3. **重新生成**：编辑原始文档（Word/WPS 等），重新打印为 XPS

### 如何导出/转换
- **生成 XPS**：在任何软件中选择"打印" → 打印机选 "Microsoft XPS Document Writer" → 保存
- **XPS 转 PDF**：
  - 用 Adobe Acrobat 打开后另存为 PDF
  - 在线转换工具（如 Zamzar、CloudConvert）
  - 用 XPS 查看器打开 → 打印 → 选择 PDF 打印机
- **XPS 转 Word**：先转成 PDF，再用 PDF 转 Word 工具
- **XPS 转图片**：用截图工具，或用专业转换软件批量转换

## 5. 常见报错与解决

### 问题1：Windows 10/11 找不到 XPS 查看器
**原因**：从 Windows 10 1803 版本开始，XPS 查看器不再是默认安装的组件，需要手动添加。

**解决方法**：
1. 设置 → 应用 → 可选功能 → 添加功能
2. 搜索 "XPS 查看器"
3. 勾选后点击"安装"
4. 安装完成后就能打开 XPS 文件了
5. 或者直接用 Edge 浏览器打开（新版 Edge 也支持 XPS）

---

### 问题2：XPS 文件在 Mac 或手机上打不开
**原因**：XPS 是微软的格式，苹果和安卓系统没有原生支持。

**解决方法**：
1. 先在 Windows 电脑上把 XPS 转成 PDF，再传到其他设备
2. 用在线转换工具（如 Online-Convert、Zamzar）转换
3. Mac 用户可以安装 **Pagemark XpsViewer**（但功能有限）
4. 建议：如果需要跨平台分享，直接生成 PDF 格式，不要用 XPS

---

### 问题3："Microsoft XPS Document Writer" 打印机不见了
**原因**：XPS 打印驱动被误删或损坏。

**解决方法**：
1. 设置 → 蓝牙和设备 → 打印机和扫描仪 → 添加设备
2. 选择"我需要的打印机不在列表中"
3. 选择"使用现有的端口" → 端口选 "XPSPort:"
4. 厂商选 "Microsoft"，型号选 "Microsoft XPS Document Writer"
5. 完成安装即可

---

### 问题4：XPS 文件太大，怎么压缩
**原因**：XPS 中包含大量高清图片或矢量图形。

**解决方法**：
1. 生成 XPS 前，先在原软件中压缩图片
2. 打印为 XPS 时，选择较低的打印质量（如"普通"而不是"高质量"）
3. 转成 PDF 后再压缩（PDF 压缩工具更多）
4. 用在线 XPS 压缩工具（较少，建议转 PDF 后压缩）

---
## 💡 小知识

XPS 可以说是微软的"PDF 杀手"梦碎的产物。当年微软推出 XPS，就是想挑战 PDF 的地位——毕竟 PDF 是 Adobe 的，而微软想把文档格式的标准掌握在自己手里。XPS 在技术上其实有不少优势：基于 XML、和 Windows 深度整合、打印效果更精准。但无奈 PDF 的生态太强大了，几乎所有设备和软件都支持 PDF，而 XPS 只有 Windows 上能用。结果就是 XPS 推出十几年了，一直不温不火，大部分人甚至不知道有这个格式。现在微软自己也放弃了推广 XPS，转而支持 PDF。

## 🔗 相关链接

- [Microsoft XPS 官方文档](https://learn.microsoft.com/zh-cn/windows/win32/printdocs/xpsdrv)
- [XPS 格式标准（ECMA-388）](https://www.ecma-international.org/publications-and-standards/standards/ecma-388/)
- [Zamzar 在线转换](https://www.zamzar.com/convert/xps-to-pdf/)
- [Adobe Acrobat 官网](https://www.adobe.com/cn/acrobat.html)

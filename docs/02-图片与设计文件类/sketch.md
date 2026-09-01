# .sketch 文件后缀详解

## 1. 文件定义 & 用途

SKETCH 是 **Sketch** 应用程序的原生设计源文件格式。Sketch 是一款专为 UI/UX 设计打造的矢量设计工具，在 macOS 平台上非常流行，是很多设计师做界面设计的首选工具。

.sketch 文件保存了所有设计元素：画板（Artboard）、图层、矢量图形、文字样式、组件（Symbol）、样式库等完整的设计信息。

- **全称**：Sketch Document
- **类型**：矢量设计源文件
- **开发者**：Sketch B.V.（荷兰）
- **发布年份**：2010年
- **特点**：矢量为主、支持组件系统、专为 UI 设计优化、仅限 macOS
- **官网**：https://www.sketch.com/

## 2. 适用场景

- App 界面设计（iOS/Android UI 设计稿）
- 网页设计（响应式页面设计稿）
- 图标设计（矢量图标集）
- 设计系统/组件库搭建
- 品牌视觉设计（Logo、插画）
- 原型设计和交互流程展示

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Figma（在线，可导入 sketch）、Photopea（有限支持） | Figma（专业版）、Lunacy（免费查看和编辑） |
| Mac | Sketch（30天免费试用）、Lunacy | Sketch（正版授权）、Figma 桌面版 |
| Linux | Figma（在线，可导入 sketch） | Figma 桌面版 |

**新手推荐**：
- Mac 用户：**Sketch**（原生工具，需要购买授权）
- Windows 用户：**Lunacy**（免费，原生支持打开和编辑 sketch 文件）
- 跨平台协作：**Figma**（在线工具，可导入 sketch 文件，协作方便）
- 仅查看：导出为 PNG/PDF 即可

## 4. 如何编辑、如何导出

### 如何编辑
1. 在 Mac 上用 Sketch 打开 .sketch 文件
2. 在左侧图层面板选择元素进行编辑
3. 使用画板（Artboard）管理不同页面/屏幕
4. 使用组件（Symbol）实现可复用元素
5. 按 `Cmd + S` 保存

### 如何导出/转换
- **导出为 PNG/JPG**：选中元素或画板 → 右侧面板设置导出 → 点击导出
- **导出为 SVG**：选中矢量元素 → 导出面板选择 SVG 格式
- **导出为 PDF**：文件 → 导出为 PDF
- **导入 Figma**：在 Figma 中 File → Import → 选择 .sketch 文件
- **导出切图**：使用"Make Exportable"功能批量导出多种尺寸
- **交付标注**：使用 Sketch Measure 插件或上传到 Zeplin、蓝湖等标注平台

## 5. 常见报错与解决

### 问题1：Windows 用户收到 .sketch 文件打不开
**原因**：Sketch 是 Mac 专属软件，没有 Windows 版本。

**解决方法**：
1. 使用 **Lunacy**（免费，Windows 原生支持打开和编辑 sketch 文件）
2. 上传到 **Figma** 在线版（支持导入 sketch 文件）
3. 请对方导出为 PNG/PDF 后再发送
4. 请对方把文件上传到 Figma，共享链接协作

---

### 问题2：sketch 文件打开后提示"字体缺失"
**原因**：文件使用了你电脑上没有安装的字体。

**解决方法**：
1. 查看缺失字体提示，下载安装对应字体
2. 在 Sketch 中 Edit → Find and Replace → 替换字体
3. 使用 Google Fonts 等免费字体替代
4. 发送方可以将文字转为轮廓（Outline）避免字体问题，但会失去可编辑性

---

### 问题3：sketch 文件损坏，打不开
**原因**：保存时软件崩溃、磁盘错误、版本不兼容等。

**解决方法**：
1. Sketch 有自动保存功能，检查 Time Machine 备份（Mac）
2. 尝试用 Figma 导入（有时 Figma 的解析器容错性更好）
3. 用 Lunacy 尝试打开
4. 检查 Sketch 的 Auto Save 文件夹
5. 联系 Sketch 官方支持

---

### 问题4：导入 Figma 后部分组件/样式丢失
**原因**：Sketch 和 Figma 的组件系统不完全对等，部分高级功能转换时有差异。

**解决方法**：
1. 导入后检查关键画板和组件是否完整
2. 复杂组件可能需要手动重新设置
3. 样式（Style）和组件（Symbol）的嵌套关系可能有变化，需要调整
4. 如果只是查看和简单修改，导入 Figma 完全够用

---

## 💡 小知识

Sketch 的出现彻底改变了 UI 设计行业。在 2010 年之前，UI 设计师大多用 Photoshop 做界面设计——但 PS 是为照片修图设计的，做 UI 有很多不便。Sketch 凭借矢量编辑、画板管理、组件系统、轻量快速等特性，迅速成为 UI 设计师的标配工具。后来 Figma 的崛起又进一步推动了设计工具从本地软件走向云端协作。如今虽然 Figma 越来越流行，但 Sketch 在 Mac 平台上仍然拥有大量忠实用户。

## 🔗 相关链接

- [Sketch 官网](https://www.sketch.com/)
- [Lunacy - Windows 免费 sketch 编辑器](https://icons8.com/lunacy)
- [Figma 在线设计工具](https://www.figma.com/)
- [Sketch 社区资源](https://www.sketch.com/community/)
- [.psd 格式详解](./psd.md)
- [.svg 格式详解](./svg.md)

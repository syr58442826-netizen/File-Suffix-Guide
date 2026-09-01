# .dwg 文件后缀详解

## 1. 文件定义 & 用途

DWG（Drawing）是 Autodesk 公司开发的二维和三维设计数据文件格式，也是 AutoCAD 的原生文件格式。它包含了矢量图形数据、文字注释、标注尺寸、图层信息以及工程元数据等，是建筑、土木工程、机械设计和电力工程领域最广泛使用的工程图纸格式。

DWG 文件可以保存精确到小数点后多位的几何数据，支持图层管理、块（Block）定义、外部参照等高级功能。由于其在工程界的事实标准地位，几乎所有主流CAD软件都提供对 DWG 格式的读写支持。

## 2. 适用场景

- 建筑施工图纸绘制（平面图、立面图、剖面图）
- 机械零件设计与加工图纸
- 电气与管道工程布线图
- 城市规划与地形测绘图
- 室内装修设计图纸
- 工程图纸归档与团队协作交付

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | DWG FastView、LibreCAD、FreeCAD | AutoCAD、BricsCAD、ZWCAD、DraftSight、GstarCAD |
| Mac | DWG FastView、LibreCAD、FreeCAD | AutoCAD for Mac、BricsCAD、ZWCAD for Mac |
| Linux | LibreCAD、FreeCAD、DWG FastView (网页版) | BricsCAD、ARES Commander |
| 跨平台(网页) | Autodesk Viewer（在线免费查看） | - |

## 4. 如何编辑、如何导出

**编辑方式：**
- 使用 AutoCAD 或兼容CAD软件直接打开编辑，支持所有工程功能。
- 使用 FreeCAD / LibreCAD 可进行基本编辑，但部分高级功能可能不完整。
- 在线编辑可使用 AutoCAD Web（需Autodesk账号）。

**导出方式：**
- 在 AutoCAD 中：`文件 → 另存为` 可导出为 DXF、DWF、PDF、SVG 等。
- 导出 PDF 时可设置图纸尺寸、打印比例和线宽。
- 降版本保存：`另存为` 时可选择 DWG 早期版本（如 R14、2000、2007等），以兼容旧版软件。

## 5. 常见报错与解决

**问题1：打开时提示"图形文件无效"或"文件已损坏"**
- 原因：文件下载不完整、传输损坏或版本不兼容。
- 解决：尝试使用 AutoCAD 的 `RECOVER` 命令修复；使用 `AUDIT` 命令检查并修复图形错误；如果仍无法打开，尝试用 Autodesk Viewer 在线查看以确认文件是否真的损坏。

**问题2：用其他软件打开后文字和标注显示为问号或乱码**
- 原因：缺少原始文件中使用的特定字体文件（如 .shx）。
- 解决：安装缺失的字体文件到CAD软件的字体目录；或在原软件中将文字样式替换为通用字体（如 txt.shx）。

**问题3：图层丢失或颜色显示不正确**
- 原因：不同CAD软件的图层标准和颜色映射规则不一致。
- 解决：打开时选择"按原图层设置导入"；手动检查图层管理器，修复丢失的图层定义；导入时启用"线型/颜色/图层映射"选项。

**问题4：高版本 DWG 在低版本软件中打不开**
- 原因：DWG 格式版本随 AutoCAD 升级而更新，存在向后兼容问题。
- 解决：在原作者软件中另存为较早的 DWG 版本；或使用在线工具（如 Autodesk 提供的格式转换）进行降版本。

---
## 小知识

DWG 格式最早出现于1979年，由 Autodesk 联合创始人 Michael Riddle 开发。DWG 在2006年被美国国家 CAD 标准（U.S. National CAD Standard）采纳。据统计，全球约有超过数百亿份 DWG 文件在使用，它可以说是工程世界最庞大的数字资产之一。DWG 文件格式虽然长期封闭，但通过 Open Design Alliance 的逆向工程努力，如今已实现了广泛的第三方读写支持。

## 相关链接

- Autodesk 官方 DWG 说明：https://www.autodesk.com/developerzone/autocad/dwg
- Open Design Alliance：https://www.opendesign.com/
- FreeCAD 官网：https://www.freecad.org/
- Autodesk Viewer（在线查看DWG）：https://viewer.autodesk.com/

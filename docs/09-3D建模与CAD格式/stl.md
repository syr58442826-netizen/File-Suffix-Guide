# .stl 文件后缀详解

## 1. 文件定义 & 用途

STL（STereoLithography）是3D打印领域最广泛使用的文件格式。它只存储3D模型的表面几何信息——用一系列三角形面片来逼近模型的表面，每个面片记录其三个顶点坐标和法线方向。STL 不包含颜色、材质、纹理、动画等任何附加数据。

STL 文件可以是 ASCII 文本格式或二进制格式。二进制版本体积更小、读取更快，是实际3D打印中最常用的形式。STL 由3D Systems 公司在1987年为其立体光固化3D打印技术开发，如今已成为3D打印行业的事实标准输入格式。

## 2. 适用场景

- 3D打印（FDM、SLA、SLS等所有工艺）的模型输入
- 3D打印切片软件（Cura、PrusaSlicer等）的输入源
- 快速原型制作（Rapid Prototyping）
- 医疗建模（如CT扫描数据转3D打印）
- 简单几何模型的数据交换
- CAD模型到打印的最终转换格式

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Blender、MeshLab、FreeCAD、Windows 3D Builder、Cura | Materialise Magics、3D Systems 3DXpert |
| Mac | Blender、MeshLab、Cura | Materialise Magics |
| Linux | Blender、MeshLab、Cura、PrusaSlicer | Materialise Magics |
| 跨平台(网页) | Online 3D Viewer、ViewSTL.com | - |

## 4. 如何编辑、如何导出

**编辑方式：**
- STL 是"只读几何"格式，不适合直接编辑。推荐先导入到 Blender / FreeCAD 中编辑，然后再导出为 STL。
- MeshLab 适合修复STL网格（补洞、修复法线、简化面数等）。
- 3D打印切片软件（Cura、PrusaSlicer）可对 STL 进行缩放、旋转、切片预览。

**导出方式：**
- Blender：`文件 → 导出 → STL`，可选择二进制或ASCII、选件方向等。
- FreeCAD：`文件 → 导出 → STL Mesh`。
- SolidWorks：`文件 → 另存为 → STL`，可设置精度（如偏差、角度公差）。
- Fusion 360：右键模型体 → `另存为 STL`。

## 5. 常见报错与解决

**问题1：切片软件提示"模型不是封闭网格"或有破洞**
- 原因：STL模型表面有开口、重叠面或缺失面，无法生成打印路径。
- 解决：使用 MeshLab 或 Windows 3D Builder 自动修复（3D Builder 会自动补洞和修复）；Blender中使用3D Print Toolbox插件检查并修复；Cura等切片软件通常也有自动修复功能。

**问题2：STL文件在3D打印机上打印出来的尺寸不对**
- 原因：建模时单位设置与打印机单位不一致（如mm vs inch）。
- 解决：在切片软件中手动设置正确缩放比例；建模时始终使用毫米为单位（3D打印行业标准单位）；导出前确认模型尺寸。

**问题3：STL文件体积巨大（上百MB）**
- 原因：模型三角形面数过多，导出精度过高。
- 解决：在 MeshLab 中使用 `Filters → Remeshing → Quadric Edge Collapse Decimation` 减面（通常3万-10万面足够打印）；导出时降低精度设置；确保使用二进制STL而非ASCII。

**问题4：STL模型法线翻转导致打印出错**
- 原因：法线方向不一致，切片软件无法判断内外侧。
- 解决：在 MeshLab 中使用 `Filters → Normals, Curvatures and Orientation → Recompute Normals`；在 Blender 中 `编辑模式 → 全选 → Mesh → Normals → Recalculate Outside`；大多数现代切片软件也能自动处理。

---
## 小知识

STL 格式虽然名字叫 STereoLithography，但有人开玩笑说它应该是 "Standard Triangle Language" 或 "Standard Tessellation Language"，因为它确实就是用三角形来拼接描述3D表面。STL 格式的最大优点是简单到极致——任何人都能解析它，任何3D软件都能导出它。但缺点也很明显：没有颜色、没有材质、没有动画。现在有些3D打印软件开始支持3MF格式（含颜色信息），但 STL 的统治地位短期内难以撼动。有趣的是，一个STL文件你可以用记事本打开看到一堆数字，但如果改一个数字就可能导致整个模型破裂。

## 相关链接

- STL 格式维基百科：https://en.wikipedia.org/wiki/STL_(file_format)
- MeshLab 官网：https://www.meshlab.net/
- Cura（UltiMaker切片软件）：https://ultimaker.com/software/ultimaker-cura
- ViewSTL（在线查看STL）：https://www.viewstl.com/

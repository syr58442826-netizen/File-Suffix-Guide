# .fbx 文件后缀详解

## 1. 文件定义 & 用途

FBX（Filmbox）是 Autodesk 公司开发的专有3D数据交换格式。它是一种"全能型"3D格式，不仅能存储模型几何数据，还支持骨骼动画、关键帧动画、蒙皮绑定、材质贴图、灯光、摄像机、形态键（Blend Shape/Morph Target）等丰富的场景数据。

FBX 是游戏开发、影视动画和3D建模行业中最常用的数据交换格式。它最初由 Kaydara 公司为其 MotionBuilder（原Filmbox）动画软件开发，Autodesk 在2006年收购后将其推广为行业标准。FBX 可以是二进制格式或ASCII格式。

## 2. 适用场景

- 游戏引擎（Unity、Unreal Engine）导入3D模型与动画
- 3D动画角色与骨骼绑定的跨软件传递
- 动作捕捉（Motion Capture）动画数据传递
- 3D软件之间的场景数据交换（Maya、Max、Blender互传）
- 建筑可视化场景导出
- VR/AR 资产准备

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Blender、Unity、Unreal Engine（免费） | Maya、3ds Max、Cinema 4D、MotionBuilder、Houdini |
| Mac | Blender、Unity | Maya、Cinema 4D、MotionBuilder |
| Linux | Blender、Unreal Engine | Maya、Houdini |
| 跨平台(网页) | Autodesk Viewer（在线查看） | - |

> 注意：FBX SDK 由 Autodesk 提供免费SDK，但格式本身为专有格式。Blender 等开源软件的FBX导入导出通过逆向工程实现，可能存在兼容性问题。

## 4. 如何编辑、如何导出

**编辑方式：**
- 使用 Maya、3ds Max、Blender 等3D软件打开编辑。
- 在 Unity/Unreal Engine 中可查看FBX内容，但编辑能力有限。

**导出方式：**
- Blender：`文件 → 导出 → FBX`，关键选项包括：版本（FBX 7.4 binary）、坐标系转换、嵌入纹理、导出动画。
- Maya / 3ds Max：`文件 → 导出选择/全部 → FBX`，可在选项中设置版本、嵌入媒体、动画范围等。
- 导出后建议用 Autodesk FBX Converter 或其他3D软件验证导入效果。

## 5. 常见报错与解决

**问题1：Blender导出的FBX导入Unity后模型方向不对或缩放异常**
- 原因：Blender默认Z轴向上，而Unity默认Y轴向上；Blender缩放也需应用。
- 解决：导出FBX前在Blender中 `Ctrl+A → 全部变换（All Transforms）` 应用缩放；导出时勾选"变换：Y轴向上"（Transform: +Y Up）；或Unity 2020.2+可在导入设置中处理。

**问题2：FBX动画导入后骨骼位置错误或动画变形**
- 原因：骨骼绑定坐标轴不一致，或蒙皮权重格式差异。
- 解决：Blender导出时勾选"Armature: 仅选中的骨骼"并确保骨骼的本地坐标轴正确；导出前应用骨骼的变换；检查骨骼的前向轴设置。

**问题3：FBX文件导入后材质变成纯色或丢失**
- 原因：FBX材质导出兼容性问题，不同软件的材质系统差异。
- 解决：导出时勾选"嵌入纹理（Embed Textures/Media）"；使用基础材质而非复杂节点材质；或导出后手动在目标软件中重新链接贴图（Diffuse、Normal、Specular等通道）。

**问题4：导出的FBX文件体积过大**
- 原因：嵌入了高分辨率纹理图片，或保留了过多历史/未使用数据。
- 解决：导出前清理未使用的网格、材质和图片；取消嵌入纹理改用外部文件引用；使用"仅导出选中对象"减少范围；后期可用 Autodesk FBX Converter 压缩版本。

---
## 小知识

FBX 的名字来自 Kaydara 公司的 MotionBuilder 原名 "Filmbox"。虽然 FBX 是专有格式，但 Autodesk 提供了免费的 FBX SDK 供开发者使用，这是它成为行业标准的重要原因。FBX 的二进制版本比 ASCII 版本小得多，读取速度也更快。有趣的是，Blender 社区花费多年时间逆向工程 FBX 格式，最终实现了相当不错的兼容性导入导出，这在开源界算是一段传奇故事。如果你只需要传模型不需要动画，OBJ 或 glTF 是更轻量的选择。

## 相关链接

- Autodesk FBX 官网：https://www.autodesk.com/developer-network/platform-technologies/fbx-sdk
- Blender FBX 导出文档：https://docs.blender.org/manual/en/latest/files/import_export.html#fbx
- Unity FBX 导入指南：https://docs.unity3d.com/Manual/FBXImporter-Model.html
- Autodesk Viewer（在线查看FBX）：https://viewer.autodesk.com/

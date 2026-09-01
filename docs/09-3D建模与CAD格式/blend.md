# .blend 文件后缀详解

## 1. 文件定义 & 用途

BLEND 是开源三维创作软件 Blender 的原生项目文件格式。一个 .blend 文件不仅包含3D模型的几何数据，还可以包含完整的场景信息：材质纹理、灯光、摄像机、动画关键帧、物理模拟数据、粒子系统、骨骼绑定、节点合成、甚至视频序列编辑时间线。

也就是说，.blend 文件本质上是一个完整的3D创作项目，而不仅仅是一个模型文件。Blender 的这种"全包"设计让用户可以将整个项目打包在一个文件中，非常方便项目管理和迁移。

## 2. 适用场景

- 3D角色建模与骨骼动画
- 短片与动画电影制作（如开源电影 Spring、Sintel 均使用 Blender）
- 游戏资产建模与导出
- 建筑可视化渲染
- 产品展示与工业设计渲染
- VFX 视觉特效制作
- 3D打印模型设计

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Blender（完全免费开源） | Blender、Cinema 4D（可导入）、Maya（需插件转换） |
| Mac | Blender | Blender、Cinema 4D |
| Linux | Blender | Blender |
| 跨平台(网页) | - | - |

> 注意：.blend 是 Blender 专属格式，其他3D软件无法直接打开。需在 Blender 中先导出为 OBJ、FBX、glTF 等通用格式。

## 4. 如何编辑、如何导出

**编辑方式：**
- 使用 Blender 直接打开即可编辑，支持全部功能。
- Blender 是唯一能完整读写 .blend 文件的软件。

**导出方式：**
- `文件 → 导出（Export）`，可选择 OBJ、FBX、glTF/GLB、STL、PLY、X3D、Collada（.dae）、Alembic（.abc）、USD 等格式。
- 导出 FBX/OBJ 时注意勾选选项：应用变换（Apply Transform）、切线空间、材质、动画等。
- 可使用 `文件 → 外部数据 → 打包（Make Pack All Into .blend）` 将所有外部图片和链接资源打包进 .blend 文件，方便迁移。

## 5. 常见报错与解决

**问题1：Blender 崩溃后 .blend 文件无法打开**
- 原因：文件写入时被中断导致数据损坏。
- 解决：Blender 每隔几分钟会自动保存到临时目录，查找路径为 `C:\Users\用户名\AppData\Local\Temp\`（Windows）或 `/tmp/`（Linux/Mac），文件名为 `.blend1` 或 `.blend2` 后缀的备份。也可尝试使用 Blender 的 `文件 → 恢复 → 从自动保存恢复` 功能。

**问题2：打开 .blend 文件后纹理图片显示为粉红色**
- 原因：纹理图片路径丢失或文件被移动。
- 解决：使用 `文件 → 外部数据 → 查找缺失文件（Find Missing Files）` 重新定位图片文件夹；或手动在Shader编辑器中重新链接图片路径；建议养成打包资源的习惯。

**问题3：导出 OBJ/FBX 后材质丢失或显示为纯色**
- 原因：Blender 的 Cycles/Eevee 材质节点和导出格式不兼容。
- 解决：导出前将复杂节点材质简化为基础材质；或使用 glTF 格式导出（对PBR材质支持最好）；FBX导出时勾选"嵌入纹理（Embed Textures）"。

**问题4：.blend 文件体积越来越大**
- 原因：Blender 会保留撤销历史和Orphan数据（未使用的网格、图片等）。
- 解决：使用 `文件 → 清理 → 清除未使用数据（Clean Up → Purge All）`；保存时取消勾选"保存撤销步骤（Save Undo Steps）"；或使用 `文件 → 另存为` 重新保存来精简文件。

---
## 小知识

Blender 是世界上最成功的开源3D软件项目之一，完全免费。它最初由荷兰程序员 Ton Roosendaal 于1995年创建，后在2002年通过众筹7天筹集10万欧元买回了源代码版权并开源。Blender 的 .blend 文件格式设计得非常紧凑高效，使用类似内存dump的方式保存数据，因此打开速度极快，甚至可以直接用文本编辑器部分查看其内部结构。Blender 基金会每年都使用 Blender 制作开源动画短片来展示和提升软件能力。

## 相关链接

- Blender 官网：https://www.blender.org/
- Blender 文档：https://docs.blender.org/
- Blender 文件格式说明：https://wiki.blender.org/wiki/Reference/File_Format
- Blender 教程（Blender Guru）：https://www.blenderguru.com/

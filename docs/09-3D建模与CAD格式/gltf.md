# .gltf 文件后缀详解

## 1. 文件定义 & 用途

glTF（GL Transmission Format）是 Khronos Group 制定的现代开放3D格式标准，被称为"3D领域的JPEG"。它专为高效传输和加载而设计，基于 JSON 结构组织数据，支持 PBR（基于物理的渲染）材质、骨骼动画、形态键变形、灯光、摄像机等丰富内容。

glTF 有两种存储形式：
- **.gltf**：JSON文本文件 + 外部 .bin（二进制数据）和图片纹理文件，适合开发和调试。
- **.glb**：将所有数据打包进单个二进制文件，适合网络传输和分发。

glTF 正在逐渐取代 OBJ 和 FBX，成为 Web3D、AR/VR和游戏引擎的首选格式。

## 2. 适用场景

- Web3D 和网页端3D展示（Three.js、Babylon.js等WebGL框架）
- AR/VR 应用（Google AR、Microsoft HoloLens 等）
- 游戏引擎资产导入（Unity、Unreal Engine 原生支持glTF）
- 3D模型素材分发（Sketchfab 等平台推荐格式）
- 移动端3D应用中的轻量模型加载
- 实时渲染和数字孪生可视化

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Blender、Windows 3D Builder、3D Viewer | Maya（需插件）、Houdini、Substance Painter |
| Mac | Blender、Quick Look（原生预览） | Maya、Houdini、Substance Painter |
| Linux | Blender | Houdini |
| 跨平台(网页) | Online 3D Viewer、Sketchfab、gltf-viewer.donmccurdy.com | - |

## 4. 如何编辑、如何导出

**编辑方式：**
- Blender 支持 glTF/GLB 的完整导入和导出（2.8版本起原生支持）。
- 在 Three.js / Babylon.js 中可通过代码加载和操作 glTF 场景树。
- 可用文本编辑器打开 .gltf 文件查看 JSON 结构（方便调试材质和动画引用）。

**导出方式：**
- Blender：`文件 → 导出 → glTF 2.0`，可导出为 .gltf 或 .glb。
  - 关键选项：格式（GLB/gltf）、应用变换、切线空间、材质（KHR_materials扩展）、动画。
- Maya / 3ds Max：通过 Babylon.js 插件或 CESIUM 插件导出 glTF。
- Substance Painter：`文件 → 导出纹理 → glTF PBR Metal Roughness` 可输出材质。

## 5. 常见报错与解决

**问题1：在网页中加载glTF后模型全黑**
- 原因：渲染器未启用环境光照（环境贴图/IBL），PBR材质需要环境光照才能正确显示。
- 解决：在 Three.js 中添加环境光和 HDR 环境贴图（如使用 `RoomEnvironment` 或 PMREMGenerator 处理HDR）；检查材质的 `metalness` 和 `roughness` 值是否合理。

**问题2：glTF模型动画不播放**
- 原因：代码中未正确调用动画播放器，或导出时未包含动画。
- 解决：在Three.js中使用 `THREE.AnimationMixer` 加载并播放动画；导出时确保勾选"动画"选项并检查动画轨道类型；检查控制台是否有 `THREE.AnimationClip` 相关报错。

**问题3：glb文件在加载时报错"Cannot read properties of undefined"**
- 原因：gltf/glb 文件损坏，或外部资源引用断裂（gltf格式引用的bin/纹理文件缺失）。
- 解决：使用 GLB 打包格式避免外部依赖；使用在线 glTF Validator（https://github.khronos.org/glTF-Validator/）检查文件结构是否合规；使用 Blender 重新导出。

**问题4：导出的glTF材质颜色和Blender中显示不一致**
- 原因：Blender的材质节点和 glTF PBR 规范有差异，某些节点类型不被glTF支持。
- 解决：使用 Blender 的 Principled BSDF 材质（glTF兼容性最好）；避免使用 procedural texture（程序化纹理），使用图片贴图；导出时勾选"导出材质"和"KHR材质扩展"。

---
## 小知识

glTF 由 Khronos Group（也是 OpenGL、Vulkan 的维护组织）在2017年正式发布1.0版本。它的设计理念是"最小运行时开销"：数据布局与GPU内存结构对齐，可以直接送入显卡渲染管线，无需运行时解析转换。glTF 是目前唯一被 WebGL、WebGPU、Unity、Unreal、Babylon.js、Three.js 等几乎所有3D平台同时支持的现代格式。Khronos 的愿景是让 glTF 成为"3D的HTML"——就像 HTML 让文字和图片在任何浏览器中显示一样，glTF 让3D内容在任何设备上即开即用。

## 相关链接

- glTF 官网（Khronos Group）：https://www.khronos.org/gltf/
- glTF 规范文档：https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html
- glTF Validator（在线校验工具）：https://github.khronos.org/glTF-Validator/
- Babylon.js glTF 查看器：https://sandbox.babylonjs.com/
- Three.js glTF 示例：https://threejs.org/examples/?q=gltf

# .dds 文件后缀详解

## 1. 文件定义 & 用途

DDS 是 **DirectDraw Surface** 纹理格式，由微软为 DirectX 开发。它是游戏和实时图形的"原生纹理格式"——图片直接以显卡能读取的压缩格式存储，加载到游戏里无需再压缩转换，速度快、显存省。

- **全称**：DirectDraw Surface
- **类型**：纹理图片格式（专为 GPU 实时渲染设计）
- **开发者**：Microsoft（DirectX 的一部分）
- **特点**：原生支持 GPU 压缩纹理（DXT/BC 压缩）、支持 mipmap、支持立方体贴图、显存占用低
- **对比 TGA/PNG**：DDS 是"显卡直接吃的格式"，TGA/PNG 是"通用图片格式"，需引擎运行时转成纹理

DDS 的核心价值是**块压缩（BC/DXT）**：图片在文件里就是压缩好的纹理格式，GPU 直接搬运到显存就能用，不像 PNG 要先解压再上传。这让游戏加载快、显存省。

## 2. 适用场景

- **游戏纹理资源**：Unity、Unreal、自研引擎的角色/场景贴图
- **实时渲染贴图**：3D 场景中需要快速加载的纹理
- **mipmap 贴图**：DDS 可内嵌多级 mipmap（远近不同精度的纹理），GPU 自动选择
- **立方体贴图/天空盒**：DDS 支持六面立方体贴图，用于环境反射、天空盒
- **Mod 制作**：给游戏做 MOD 贴图替换时，常需编辑 DDS

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Paint.NET（原生支持）、XnView、IrfanView（需插件）、GIMP（需插件） | Adobe Photoshop（需 NVTT/Intel 插件）、Substance Designer、Affinity Photo |
| Mac | XnView、GIMP（需插件） | Substance Designer、Photoshop |
| Linux | GIMP（需插件）、ImageMagick | Substance Designer |

**新手推荐**：
- Windows 编辑 DDS：**Paint.NET**（免费，原生支持 DDS 读写，最方便）
- 查看浏览：**XnView** 或 **IrfanView**
- 专业贴图：**Substance Designer** 或 **Photoshop + NVIDIA DDS 插件**
- 命令行批量：**NVIDIA Texture Tools（NVTT）** 或 **ImageMagick**

## 4. 如何编辑、如何导出

### 如何编辑
1. **Paint.NET**：直接打开编辑，保存时选 DDS，可选压缩格式（DXT1/DXT5 等）
2. **Photoshop + NVIDIA DDS 插件**：装 NVTT 插件后可读写 DDS，保存时选择压缩格式和 mipmap 生成
3. **GIMP + dds 插件**：安装后可编辑保存
4. **Substance Designer**：专业贴图工具，DDS 是常用导出格式

### 如何导出/转换
- **导出 DDS（带压缩）**：在 Paint.NET/Photoshop 中另存为 DDS，选压缩格式：
  - DXT1：无透明通道，体积最小（适合不透明贴图）
  - DXT5：有透明通道，体积中等（适合带 Alpha 的贴图）
  - BC7：高质量新压缩（需要现代 GPU 支持）
- **DDS 转 PNG/TGA**：用 Paint.NET、XnView、ImageMagick（`magick input.dds output.png`）
- **PNG/TGA 转 DDS**：用 NVIDIA Texture Tools 或 Paint.NET 转换，可选生成 mipmap
- **批量转换**：NVTT 的 `nvcompress` 命令行工具

## 5. 常见报错与解决

### 问题1：DDS 在普通看图软件里显示不出来或花屏
**原因**：DDS 用的是 GPU 块压缩格式（DXT/BC），普通看图软件不解码这种压缩。

**解决方法**：
1. 用支持 DDS 的软件：Paint.NET、XnView、Photoshop（装插件）
2. 用 ImageMagick 转 PNG 预览：`magick input.dds preview.png`
3. 游戏里看不到贴图但文件没问题，可能是游戏本身的加载问题，不是文件损坏

### 问题2：导出的 DDS 在游戏里颜色发暗或有色块
**原因**：DDS 块压缩（DXT）是有损的，对渐变色和平滑过渡的图片压缩损失明显；选错了压缩格式也会导致问题。

**解决方法**：
1. 对颜色精度要求高的贴图，用 **BC7** 压缩（质量最高，需 GPU 支持）或**不压缩**的 DDS
2. 透明贴图用 DXT5 而非 DXT1（DXT1 只有 1 位 Alpha，半透明会出问题）
3. 法线贴图（normal map）要用专门的 BC5 压缩，避免色块
4. 制作时在高分辨率下编辑，最后再压缩成 DDS，减少累积损失

### 问题3：DDS 文件带 mipmap 后体积变大，不知道要不要 mipmap
**原因**：mipmap 是多级缩略图（1/2、1/4、1/8...），会让文件体积增加约 1/3，但能提升 3D 场景远处的渲染质量和性能。

**解决方法**：
1. 用于 3D 场景的贴图（地面、墙壁等）：**生成 mipmap**，远处不闪烁、性能更好
2. 用于 UI/2D 的贴图：**不需要 mipmap**，省体积
3. 法线贴图、细节贴图：建议生成 mipmap
4. 在 Paint.NET/Photoshop 保存时勾选"生成 mipmap"选项即可

---
## 💡 小知识

DDS 是 DirectX 家族的"亲儿子"——微软在 1999 年随 DirectX 7 推出它，目的就是让纹理在文件里就以 GPU 能直接吃的压缩格式存在。普通图片格式（JPG/PNG）要先解压再传给 GPU，而 DDS 是"开箱即食"，游戏加载时直接拷贝到显存，零转换开销。DDS 的 DXT 压缩（现称 BC 块压缩）是 GPU 硬件解码的，压缩率固定 4:1 或 6:1，且 GPU 边读边解压不占额外显存。这就是为什么几乎所有 3A 游戏的纹理都是 DDS。随着 GPU 演进，BC7、BC6H（HDR）等新压缩格式加入，DDS 也在进化，仍是实时渲染纹理的事实标准。

## 🔗 相关链接

- [NVIDIA Texture Tools](https://github.com/castano/nvidia-texture-tools)
- [Paint.NET 官网](https://www.getpaint.net/)
- [DDS 编程指南（微软）](https://learn.microsoft.com/windows/win32/direct3ddds/dx-graphics-dds-pguide)
- [.tga 文件后缀详解](./tga.md)

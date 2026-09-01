# .tga 文件后缀详解

## 1. 文件定义 & 用途

TGA 是 **Truevision TGA**（Truevision Graphics Adapter）图片格式，由 Truevision 公司在 1984 年推出。它是早期少数支持**透明通道（Alpha 通道）**的格式之一，因此在游戏开发、3D 贴图、影视动画领域长期占有一席之地。

- **全称**：Truevision Graphics Adapter（也称 Targa）
- **类型**：位图图片格式
- **开发者**：Truevision（现属 Pinnacle Systems）
- **特点**：支持 Alpha 透明通道、支持无损 RLE 压缩、结构简单、读取速度快
- **对比 PNG**：TGA 更老，但读取快、被游戏引擎广泛支持；PNG 压缩率更高、更现代

TGA 至今活跃在游戏开发中，因为它的结构简单、读取快，几乎所有 3D 引擎（Unity、Unreal、自研引擎）都原生支持。

## 2. 适用场景

- **游戏开发贴图**：角色、场景的纹理贴图（Unity、Unreal 默认支持）
- **带透明通道的图片**：UI 素材、图标、特效贴图（需要 Alpha 通道）
- **影视/动画序列帧**：渲染输出的单帧序列（TGA 序列）
- **老项目兼容**：90-00 年代的游戏、软件资源
- **3D 渲染输出**：Maya、3ds Max 等渲染输出的无损序列帧

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | IrfanView、ImageGlass、XnView、GIMP、Paint.NET | Adobe Photoshop、Affinity Photo |
| Mac | 预览（部分支持）、GIMP、XnView | Adobe Photoshop、Affinity Photo |
| Linux | GIMP、ImageMagick、digiKam | - |

**新手推荐**：
- 查看贴图：**IrfanView** 或 **XnView**（快速批量查看）
- 编辑贴图：**Photoshop** 或 **Paint.NET**（Windows 免费，支持 Alpha 通道）
- 免费全能：**GIMP**（跨平台，支持 TGA 透明通道）

## 4. 如何编辑、如何导出

### 如何编辑
1. **Photoshop**：打开 TGA 时会询问位深度（24/32 位），32 位含 Alpha 通道；编辑后"另存为 Targa"选 32 位保留透明
2. **Paint.NET**：装 TGA 插件后可编辑
3. **GIMP**：原生支持，导出时选 TGA 格式，勾选保留 Alpha 通道
4. **游戏引擎**：Unity/Unreal 直接导入 TGA 作为贴图，无需额外处理

### 如何导出/转换
- **Photoshop 导出 TGA**：文件 → 导出 → 另存为 → Targa（.tga），选 32 位/像素含 Alpha
- **转 PNG**：用 IrfanView/XnView 批量转，PNG 体积更小且通用
- **批量转换**：XnConvert、ImageMagick（`magick *.tga output.png`）
- **序列帧转视频**：用 ffmpeg：`ffmpeg -i frame_%04d.tga -c:v ffv1 output.mkv`

## 5. 常见报错与解决

### 问题1：TGA 图片打开后背景是黑色而非透明
**原因**：查看器不支持或不显示 Alpha 透明通道，把透明区域渲染成了黑色。

**解决方法**：
1. 用支持 Alpha 通道的查看器：Photoshop、GIMP、XnView（设置中开启透明背景棋盘格）
2. 用 Photoshop 打开时选"32 位"以正确读取 Alpha 通道
3. 若需在通用查看器看，转成 PNG（保留透明），多数查看器能正确显示 PNG 透明
4. 检查 TGA 是否真的有 Alpha 通道（24 位无 Alpha，32 位才有）

### 问题2：TGA 在 Photoshop 里打开提示选 16/24/32 位，不知道选哪个
**原因**：TGA 支持多种位深度，对应不同的通道数。

**解决方法**：
1. **32 位**：含 Alpha 透明通道（RGBA），游戏贴图、UI 素材选这个
2. **24 位**：无 Alpha（RGB），普通不透明图片选这个
3. **16 位**：旧格式，色彩少，一般不用
4. 不确定就先选 32 位，打开后看"通道"面板有没有 Alpha 通道

### 问题3：TGA 文件体积比 PNG 大很多
**原因**：TGA 的 RLE 压缩效率低，尤其对颜色丰富的照片类图片几乎不压缩。

**解决方法**：
1. 不需要 Alpha 通道的图片，转成 JPG 体积最小
2. 需要 Alpha 通道的，转成 PNG，压缩率更高且通用
3. 仅在游戏引擎明确要求 TGA 时才保留 TGA（引擎内部会转成压缩纹理）
4. 用 ImageMagick 转 PNG：`magick input.tga output.png`

---
## 💡 小知识

TGA 是图片格式里的"活化石"。1984 年它诞生时，是为 Truevision 的 Targa 视频卡设计的——那是第一批能显示真彩色的 PC 显卡之一。TGA 当年的杀手锏是"支持 Alpha 通道"，这让它在游戏和影视特效中无可替代（PNG 1996 年才出现）。即使今天 PNG 在通用图片领域完胜 TGA，但游戏引擎仍然偏爱 TGA：它的结构极其简单，引擎读取解码几乎零开销，且能无损保留 Alpha 通道。所以你打开任何一款 3A 游戏的资源文件，里面大概率还有一堆 TGA。这个 40 岁的老格式，靠着"简单可靠"在游戏行业续命至今。

## 🔗 相关链接

- [IrfanView 官网](https://www.irfanview.com/)
- [GIMP 官网](https://www.gimp.org/)
- [Paint.NET 官网](https://www.getpaint.net/)
- [ImageMagick 官网](https://imagemagick.org/)
- [.dds 文件后缀详解](./dds.md)
- [.png 文件后缀详解](../02-图片与设计文件类/png.md)

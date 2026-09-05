# .wad 文件后缀详解

## 1. 文件定义 & 用途

WAD（Where's All the Data?，"所有数据在哪？"）是 id Software 公司为 DOOM（毁灭战士）系列游戏开发的一种资源打包格式。WAD 文件包含了 DOOM 游戏的所有数据——关卡、怪物、武器、贴图、声音、音乐等等。WAD 格式是游戏 MOD 文化的鼻祖，DOOM 的 MOD 社区至今仍然活跃。

WAD 格式的核心特点：
- **DOOM 专属**：id Software 为 DOOM 游戏设计的资源包格式
- **资源打包**：包含关卡、贴图、精灵、声音、音乐等所有游戏数据
- **MOD 文化鼻祖**：WAD 催生了最早的游戏 MOD 社区
- **格式简单**：文件结构简单，易于解析和修改
- **两种类型**：IWAD（主游戏数据）和 PWAD（附加/补丁 WAD）
- **生命力强**：虽然 DOOM 已经 30 多年了，但至今仍有新 WAD 发布

## 2. 适用场景

- **玩 DOOM 游戏**：DOOM 游戏的主数据文件（DOOM.WAD、DOOM2.WAD）
- **DOOM MOD**：加载自定义 WAD 文件，玩玩家制作的关卡和 MOD
- **资源提取**：从 DOOM 游戏中提取贴图、音效、音乐等资源
- **关卡制作**：使用 DOOM 关卡编辑器制作自定义关卡，保存为 WAD
- **复古游戏**：体验经典的 DOOM 游戏和 MOD
- **游戏历史研究**：研究早期 FPS 游戏的资源格式

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | SLADE3、Doom Builder、ZDoom、GZDoom | - |
| Mac | SLADE3、GZDoom | - |
| Linux | SLADE3、GZDoom、Eternity Engine | - |
| 关卡编辑 | Doom Builder 2、Ultimate Doom Builder、SLADE3 | - |

**新手推荐：**
- **玩 DOOM MOD**：GZDoom（最流行的 DOOM 源码端口，功能最强）
- **查看/编辑 WAD**：SLADE3（全能 WAD 编辑器）
- **制作关卡**：Ultimate Doom Builder（最好用的 DOOM 关卡编辑器）

## 4. 如何编辑、如何导出

### WAD 文件的两种类型

**IWAD（Internal WAD，内部 WAD）：**
- 是游戏的主数据文件
- 包含游戏运行所需的所有基本资源
- 例如：`DOOM.WAD`（毁灭战士1）、`DOOM2.WAD`（毁灭战士2）
- 文件较大（10MB+）

**PWAD（Patch WAD，补丁 WAD）：**
- 是附加/修改用的 WAD
- 只包含新增或修改的资源
- 玩家制作的 MOD、关卡包通常都是 PWAD
- 体积从几十 KB 到几 MB 不等
- 需要配合 IWAD 一起使用

### 如何玩 DOOM MOD / 加载自定义 WAD

**使用 GZDoom（推荐）：**
1. 安装 GZDoom
2. 确保你有 DOOM.WAD 或 DOOM2.WAD（IWAD 文件）
3. 把自定义 WAD（PWAD）和 GZDoom 放在一起
4. 有几种加载方式：
   - 直接把 PWAD 文件拖到 GZDoom.exe 上
   - 命令行：`gzdoom -file mymod.wad`
   - 使用 ZDL（ZDoom Launcher）前端工具，图形化选择 MOD

**加载多个 WAD：**
```bash
# 可以同时加载多个 PWAD
gzdoom -file map1.wad weapon_mod.wad hud_mod.wad

# 指定 IWAD
gzdoom -iwad doom2.wad -file mymod.wad
```

### 如何查看和编辑 WAD 内容

**使用 SLADE3（最强大的 WAD 编辑器）：**
1. 下载安装 SLADE3
2. 文件 → 打开 → 选择 WAD 文件
3. 左侧显示资源分类：
   - **Maps**：关卡地图
   - **Textures**：贴图
   - **Sprites**：精灵图（怪物、武器等）
   - **Sounds**：音效
   - **Music**：音乐
4. 双击可以查看/预览资源
5. 可以导入、导出、替换资源
6. 保存修改后的 WAD

### 如何制作 DOOM 关卡

**使用 Ultimate Doom Builder：**
1. 下载安装 Ultimate Doom Builder
2. 新建地图 → 选择 IWAD（DOOM2 推荐）
3. 在 2D 视图中绘制房间和走廊（画线创建区域）
4. 切换到 3D 视图查看效果
5. 放置怪物、道具、武器等
6. 测试地图（F5 快速测试）
7. 保存为 WAD 文件

## 5. 常见报错与解决

### 问题 1：GZDoom 提示找不到 DOOM.WAD

**原因：** 没有 IWAD 文件，或 GZDoom 找不到 IWAD 的位置。

**解决方法：**
1. 你需要有正版的 DOOM 游戏 WAD 文件（可以在 Steam 或 GOG 上购买）
2. 把 DOOM.WAD 或 DOOM2.WAD 放到 GZDoom 同一目录
3. 或在 GZDoom 设置中指定 IWAD 的搜索路径
4. 启动时指定：`gzdoom -iwad C:\path\to\doom2.wad`

### 问题 2：加载 WAD 后游戏崩溃或花屏

**原因：** WAD 文件损坏、版本不兼容、或 MOD 需要特定的源码端口。

**解决方法：**
1. 确认 WAD 文件完整（重新下载）
2. 检查 MOD 需要哪个源码端口（ZDoom、GZDoom、Boom 等）
3. 有些高级 MOD 需要 GZDoom 或特定版本
4. 尝试用不同的源码端口加载
5. 检查 MOD 的说明文档，看有没有特殊要求

### 问题 3：WAD 和 PK3 有什么区别？

**解答：** 这是两种不同的 DOOM 资源格式：
- **WAD**：传统格式，二进制结构，较老但兼容性最好
- **PK3**：ZDoom 引入的新格式，其实就是 ZIP 压缩包（把后缀改成 .pk3），更容易编辑
- 现代的 DOOM MOD 很多用 PK3 格式，因为用普通压缩软件就能打开
- 但经典的关卡和 MOD 仍然是 WAD 格式
- GZDoom 两种格式都支持

### 问题 4：修改后的 WAD 保存了，但游戏里没变

**原因：** 保存有问题，或加载方式不对。

**解决方法：**
1. 在 SLADE3 中修改后，确认保存了（Ctrl+S）
2. 确认游戏加载的是你修改后的那个 WAD 文件
3. 如果有同名缓存，清空缓存
4. 用命令行加载确认路径正确：`gzdoom -file "C:\path\to\your.wad"`
5. 有些修改（如贴图）需要注意格式和尺寸限制

---

## 💡 小知识

WAD 格式的名字特别有意思——WAD 是 "Where's All the Data?"（所有数据去哪了？）的缩写。这个名字的由来有个小故事：当年 id Software 的程序员在设计 DOOM 的资源格式时，开玩笑说这些数据文件就像一个"黑洞"——你知道数据在里面，但不知道在哪。于是就给这个格式起名叫 WAD（"数据在哪？"）。

WAD 格式在游戏史上有着非常特殊的地位，因为它催生了整个游戏 MOD 文化。在 DOOM 之前，游戏的资源文件都是加密的、不公开的，玩家想修改游戏非常困难。但 id Software 做了一件非常前卫的事——他们公开了 WAD 格式的结构，甚至鼓励玩家制作自己的关卡和 MOD。

这个决定开启了一个全新的时代。玩家们开始疯狂地制作自定义 WAD 文件——新关卡、新武器、新怪物、新玩法……DOOM 的 MOD 社区迅速壮大，诞生了无数经典的自定义 WAD。有些 MOD 的质量甚至超过了官方游戏。

最传奇的故事之一是《最终毁灭》（Final DOOM）——它其实是 id Software 从玩家制作的 WAD 中挑选出最好的关卡，打包成了官方资料片来卖。也就是说，玩家的业余作品直接变成了官方产品。

直到今天，DOOM 的 MOD 社区仍然非常活跃。每年都有新的 WAD 发布，有些 WAD 的规模堪比一款完整的游戏。而 GZDoom 等现代源码端口更是把 DOOM 引擎的潜力推到了极致——你甚至可以在 DOOM 引擎里做出 3D 效果、复杂的剧情、甚至 RPG 系统。一个 30 多年前的游戏引擎，至今仍然充满活力，这本身就是一个奇迹。

## 🔗 相关链接

- [GZDoom 官方网站](https://zdoom.org/index)
- [SLADE3 WAD 编辑器](https://slade.mancubus.net/)
- [Ultimate Doom Builder](https://forum.zdoom.org/viewtopic.php?f=232&t=76834)
- [id Software 官方网站](https://www.idsoftware.com/)
- [Doomworld（DOOM 社区门户）](https://www.doomworld.com/)
- [.vpk Valve Pak 格式详解](./vpk.md)
- [.zip 压缩格式详解](../04-压缩打包镜像类/zip.md)

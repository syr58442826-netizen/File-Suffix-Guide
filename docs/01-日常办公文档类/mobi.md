# .mobi 文件后缀详解

## 1. 文件定义 & 用途

MOBI 是 **Mobipocket** 电子书格式的后缀名，最初由 Mobipocket 公司开发，后来被亚马逊收购，成为 Kindle 电子书阅读器的主要格式。虽然亚马逊正在推新的 KFX 格式，但 MOBI 仍然是 Kindle 生态中最通用的格式。

- **全称**：Mobipocket eBook
- **类型**：电子书格式
- **开发者**：Mobipocket SA（后被 Amazon 收购）
- **发布年份**：2000年
- **特点**：体积小、适合黑白电纸书、Kindle 原生支持
- **衍生格式**：AZW、AZW3（亚马逊的加密/增强版 MOBI）

## 2. 适用场景

- 在 Kindle 电子书阅读器上看书
- 亚马逊 Kindle 商店购买的电子书
- 把电子书发送到 Kindle 设备
- 适合黑白墨水屏阅读的小说和文字书
- 老旧电子书阅读器的兼容格式

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Calibre、Kindle for PC、Sumatra PDF、FBReader | Icecream Ebook Reader Pro |
| Mac | Calibre、Kindle for Mac、Apple Books（部分支持） | Kindle for Mac、MarginNote |
| Linux | Calibre、FBReader、Okular | Calibre（已足够强大） |
| Kindle 设备 | Kindle 原生系统直接支持 | Kindle 原生系统 |
| 手机 | Kindle App、多看阅读 | Kindle Unlimited 会员 |

**新手推荐**：
- Kindle 用户：直接放到 Kindle 里看，无需额外软件
- 电脑上看：**Calibre**（免费强大）或 **Kindle for PC**
- 手机上看：**Kindle App** 或 **多看阅读**

## 4. 如何编辑、如何导出

### 如何编辑
MOBI 主要是阅读格式，编辑比较麻烦：

1. **Calibre 编辑**：先用 Calibre 转成 EPUB，再用 Calibre 的编辑功能修改，最后转回 MOBI
2. **转换后编辑**：转成 EPUB/Word/TXT 编辑，再转回 MOBI
3. **专业工具**：Mobipocket Creator（官方工具，但比较老旧）
4. 一般不建议直接编辑 MOBI，建议从源文件（EPUB/Word）生成

### 如何导出/转换
- **转成 EPUB**：用 Calibre → 添加书籍 → 选中 → 转换书籍 → 输出格式 EPUB
- **转成 PDF**：Calibre 转换，适合打印或在电脑上阅读
- **转成 TXT**：Calibre 转换，最简单的纯文本格式
- **转成 AZW3**：Calibre 转换，Kindle 上显示效果更好
- **EPUB 转 MOBI**：最常见的转换需求，用 Calibre 一键转换
- **推送到 Kindle**：通过邮箱发送，亚马逊会自动转成适配格式

## 5. 常见报错与解决

### 问题1：把 MOBI 放到 Kindle 里找不到
**原因**：放错了文件夹，或者格式不完全兼容。

**解决方法**：
1. 确认文件放在了 Kindle 的 `documents` 文件夹里（根目录不行）
2. 检查文件后缀是不是 .mobi，有时候下载下来是压缩包需要解压
3. 用 Calibre 重新转换一遍，输出格式选 MOBI
4. 尝试 AZW3 格式（新版 Kindle 支持更好）
5. 重启 Kindle 试试

---

### 问题2：MOBI 转 EPUB 后排版错乱
**原因**：MOBI 格式的排版信息在转换过程中可能丢失，尤其是复杂排版。

**解决方法**：
1. 用 Calibre 转换时，选择"启发式样式识别"可以改善排版
2. 转换后手动调整：Calibre → 编辑书籍 → 微调 CSS 样式
3. 简单排版的小说转换效果最好，复杂排版建议找原版 EPUB
4. 如果图片很多，检查图片是否正确转换

---

### 问题3：MOBI 文件有 DRM 保护，无法转换或在别的设备上看
**原因**：从亚马逊购买的正版 MOBI/AZW 电子书通常带有 DRM 加密，只能在绑定的 Kindle 设备上阅读。

**解决方法**：
1. 正版书籍请在 Kindle 设备或 Kindle App 上阅读
2. 不要尝试破解 DRM，这可能违反法律和用户协议
3. 如果是自己的文档，请确保转换的是无 DRM 的版本
4. 可以通过"发送到 Kindle"功能把个人文档推送到 Kindle，这些是没有 DRM 的

---

### 问题4：MOBI 文件中的中文显示乱码或不显示
**原因**：MOBI 对中文字体的支持有限，尤其是旧版本的 MOBI。

**解决方法**：
1. 用 Calibre 转换时，输出格式选 AZW3（对中文支持更好）
2. 在转换设置中指定中文字体：Calibre → 转换 → 界面外观 → 字体 → 嵌入字体
3. Kindle 设备上可以安装自定义中文字体
4. 尽量找专门制作的中文版 MOBI，而不是自动转换的

---
## 💡 小知识

MOBI 格式有个有趣的"前世今生"。它最早是基于一种叫 PalmDoc 的格式——对，就是那个当年很火的 Palm 掌上电脑的电子书格式。Mobipocket 公司在 PalmDoc 基础上扩展了 HTML 支持和图片支持，才有了 MOBI。2005年亚马逊收购了 Mobipocket，把 MOBI 作为 Kindle 的核心格式。不过，亚马逊已经宣布从 2022 年开始，Send to Kindle 服务不再支持 MOBI 格式，转而支持 EPUB。这意味着 MOBI 正在慢慢退出历史舞台，EPUB 才是电子书的未来。

## 🔗 相关链接

- [Calibre 官方网站](https://calibre-ebook.com/)
- [Kindle 阅读软件下载](https://www.amazon.cn/kindle-dbs/fd/kcp)
- [亚马逊 Send to Kindle](https://www.amazon.cn/gp/sendtokindle)
- [Mobipocket 历史（维基百科）](https://en.wikipedia.org/wiki/Mobipocket)
- [多看阅读官网](https://www.duokan.com/)

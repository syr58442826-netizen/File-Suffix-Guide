# .woff 文件后缀详解

## 1. 文件定义 & 用途

WOFF（Web Open Font Format，Web 开放字体格式）是专为网页设计的字体格式，由 W3C 推荐使用。它本质上是对 TrueType（TTF）和 OpenType（OTF）字体的一种封装和压缩，让字体文件在网络传输时体积更小、加载更快。WOFF2 是其升级版，压缩率更高。

WOFF 格式的核心特点：
- **网页专用**：专为 Web 字体设计，是 W3C 推荐的标准字体格式
- **体积更小**：使用 zlib（WOFF）或 Brotli（WOFF2）压缩，比 TTF/OTF 小 30%-50%
- **加载更快**：更小的体积意味着网页加载速度更快
- **版权友好**：支持元数据和字体厂商信息，部分格式支持 DRM
- **浏览器支持好**：所有现代浏览器都支持 WOFF，绝大多数支持 WOFF2
- **WOFF2 更优**：WOFF2 比 WOFF 压缩率再提高约 30%，是目前的首选

## 2. 适用场景

- **网页字体嵌入**：网站使用自定义字体时，首选 WOFF/WOFF2 格式
- **前端开发**：CSS @font-face 规则中引入字体
- **Web 性能优化**：减小字体文件体积，加快网页加载速度
- **跨平台显示一致**：确保网站在不同设备上显示相同的字体效果
- **图标字体**：Font Awesome 等图标字体通常提供 WOFF 格式

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | FontForge、百度字体编辑器、woff2otf（命令行） | FontLab Studio、Glyphs |
| Mac | FontForge、自带"字体册"（需先转格式） | FontLab Studio、Glyphs |
| Linux | FontForge、fonttools（命令行） | - |
| 跨平台（在线） | Convertio（在线转换）、Font Squirrel Webfont Generator | - |

**注意：** WOFF 是网页字体格式，不是用来"安装使用"的字体格式。要查看或安装字体，通常需要先转为 TTF/OTF。

## 4. 如何编辑、如何导出

### 如何查看 WOFF 字体

**在线预览（最简单）：**
1. 使用在线工具如 FontDrop（fontdrop.info）
2. 拖入 WOFF 文件即可预览字体效果
3. 可以查看字形、字重、支持的字符等

**用 FontForge 打开：**
1. 下载安装 FontForge（免费开源）
2. 文件 → 打开 → 选择 WOFF 文件
3. 可以查看和编辑每个字形

### TTF/OTF 转 WOFF/WOFF2（生成网页字体）

**使用在线工具（推荐新手）：**
1. 访问 Font Squirrel Webfont Generator
2. 上传 TTF/OTF 字体文件
3. 选择转换模式（推荐 Optimal）
4. 下载生成的 Web 字体包（包含 WOFF、WOFF2、CSS 等）

**使用命令行工具（开发者）：**
```bash
# 安装 woff2 工具（Google 官方）
# Windows: 下载预编译二进制
# Mac: brew install woff2
# Linux: sudo apt install woff2

# TTF 转 WOFF2
woff2_compress font.ttf   # 生成 font.woff2

# WOFF2 转 TTF
woff2_decompress font.woff2   # 生成 font.ttf
```

**使用 fonttools（Python，功能强大）：**
```python
# 安装
pip install fonttools brotli zopfli

# TTF 转 WOFF2
from fontTools.ttLib import TTFont
font = TTFont('font.ttf')
font.flavor = 'woff2'
font.save('font.woff2')
```

### 在网页中使用 WOFF 字体

**CSS @font-face 写法：**
```css
@font-face {
  font-family: 'MyFont';
  src: url('font.woff2') format('woff2'),
       url('font.woff') format('woff');
  font-weight: normal;
  font-style: normal;
  font-display: swap;  /* 提高性能：先显示系统字体，再替换 */
}

body {
  font-family: 'MyFont', sans-serif;
}
```

**最佳实践：**
1. 优先使用 WOFF2，WOFF 作为降级
2. 使用 `font-display: swap` 避免文字"看不见"
3. 只引入需要的字重和样式，减少加载体积
4. 中文字体太大时，考虑使用字体子集化（只包含需要的汉字）

## 5. 常见报错与解决

### 问题 1：WOFF 文件无法安装到系统

**原因：** WOFF 是网页字体格式，操作系统不直接支持安装 WOFF 字体。

**解决方法：**
1. 将 WOFF 转换为 TTF 或 OTF 格式后再安装
2. 在线转换：使用 Convertio 或 CloudConvert
3. 命令行转换：`woff2_decompress font.woff2` 得到 TTF
4. 转换后双击安装即可

### 问题 2：网页中字体不生效，显示的是默认字体

**原因：** 可能是字体路径错误、CSS 语法错误、浏览器不支持格式，或 CORS 跨域问题。

**解决方法：**
1. 检查字体文件路径是否正确（相对路径或绝对路径）
2. 检查 CSS @font-face 语法是否正确
3. 打开浏览器开发者工具（F12）→ Network 面板，看字体文件是否加载成功
4. 如果报 CORS 错误，需要在服务器配置允许跨域字体访问
5. 确保同时提供 WOFF2 和 WOFF 两种格式以兼容旧浏览器

### 问题 3：WOFF 字体加载太慢，影响网页性能

**原因：** 字体文件太大（尤其是中文字体），或没有做优化。

**解决方法：**
1. 使用 WOFF2 替代 WOFF（体积小 30% 左右）
2. 中文字体使用"字体子集化"——只提取页面需要的汉字
   - 工具：fontTools、字蛛（font-spider）、fontmin
3. 使用 `font-display: swap` 让文字先显示出来
4. 使用预加载 `<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>`
5. 只引入需要的字重（Regular、Bold 各一个就够了）

### 问题 4：WOFF2 在某些旧浏览器上不显示

**原因：** 旧版浏览器（如 IE、老版本 Android 浏览器）不支持 WOFF2。

**解决方法：**
1. 同时提供 WOFF2 和 WOFF 两种格式，CSS 中 WOFF2 写在前面
2. 浏览器会优先使用它支持的第一种格式
3. 如果还需要兼容 IE9+，可以再加上 TTF/OTF 格式作为最后降级
4. 参考 Can I Use 网站查询各浏览器对 WOFF/WOFF2 的支持情况

---

## 💡 小知识

WOFF 格式的诞生是 Web 字体发展史上的一个重要里程碑。在 WOFF 出现之前，网页要使用自定义字体非常麻烦——有的浏览器支持 EOT（IE 专用），有的支持 TTF/OTF，格式混乱、兼容性差，而且字体文件体积大、加载慢。

2010 年，Mozilla、Opera 等公司联合提出了 WOFF 格式，并提交给 W3C。WOFF 的思路很巧妙：它不是发明一种新的字体轮廓格式，而是对已有的 TrueType 和 OpenType 字体进行封装和压缩——就像是给字体文件穿上了一件"压缩外衣"，专门为网络传输优化。这样既解决了体积问题，又能和现有的字体技术无缝衔接。

WOFF2 则是更进一步，使用了 Google 开发的 Brotli 压缩算法，比 WOFF 的 zlib 压缩率再提高约 30%。现在 WOFF2 已经是所有现代浏览器的标配，是网页字体的首选格式。

有趣的是，中文字体的 Web 字体一直是个难题——因为汉字太多，一个中文字体文件动辄几 MB 甚至十几 MB，直接放在网页上加载太慢。所以国内开发者想出了"字体子集化"的办法：只提取网页中实际用到的汉字，生成一个小的 WOFF2 文件。这样一个网页的中文字体可能只有几十 KB，加载速度就快多了。

## 🔗 相关链接

- [W3C WOFF 规范](https://www.w3.org/TR/WOFF/)
- [W3C WOFF2 规范](https://www.w3.org/TR/WOFF2/)
- [Font Squirrel Webfont Generator](https://www.fontsquirrel.com/tools/webfont-generator)
- [FontForge 字体编辑器](https://fontforge.org/)
- [Google woff2 工具](https://github.com/google/woff2)
- [.ttf 格式详解](./ttf.md)
- [.otf 格式详解](./otf.md)

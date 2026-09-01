# .scss 文件后缀详解

## 1. 文件定义 & 用途

.scss 是 **Sass**（Syntactically Awesome Style Sheets）的 SCSS 语法文件后缀。Sass 是一种 CSS 预处理器，SCSS 是其中一种语法（与 CSS 语法完全兼容，用大括号和分号）。它让 CSS 支持变量、嵌套、混入（mixin）、函数、模块化等高级功能，最终编译成普通 CSS。

简单来说，.scss 文件就是"增强版 CSS"，写完后用编译器转成浏览器认识的 .css 文件。

> 补充：Sass 还有另一种语法叫缩进式语法，后缀是 .sass，不用大括号和分号，靠缩进表示嵌套。SCSS（.scss）更主流、更接近 CSS 习惯，新人首选 SCSS。

**主要用途：**
- 大型前端项目的样式管理
- 多主题、多皮肤方案
- 设计系统 / 组件库样式
- 需要复用样式逻辑的项目

## 2. 适用场景

- 中大型 Web 项目的样式开发
- 需要变量、嵌套、混入等高级特性的样式
- 团队协作、需要样式可维护性的项目
- 使用 Bootstrap、Element Plus 等基于 SCSS 的框架时定制主题

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Live Sass Compiler 扩展、Notepad++ | WebStorm、Prepros |
| Mac | [VS Code](https://code.visualstudio.com/) + Live Sass Compiler 扩展、Vim | WebStorm、Prepros |
| Linux | [VS Code](https://code.visualstudio.com/) + Live Sass Compiler 扩展、Vim | WebStorm |

**新手推荐：** VS Code + Live Sass Compiler 扩展（保存即自动编译成 CSS，零配置）。

## 4. 如何编辑、如何导出

### 环境准备

现代项目里 SCSS 通常由构建工具（Vite、Webpack）自动编译，无需手动装。如要单独用，可装 Dart Sass 编译器。

**安装 Dart Sass（官方推荐）：**
```bash
# 用 npm 全局安装
npm install -g sass

# 验证
sass --version
```

### 如何编辑

**一个简单的 SCSS 示例：**
```scss
// style.scss
$primary-color: #42b883;
$font-size: 16px;

@mixin button-style($bg) {
  background: $bg;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  &:hover {
    opacity: 0.85;
  }
}

.navbar {
  font-size: $font-size;

  .logo {
    color: $primary-color;
    font-weight: bold;
  }

  .btn {
    @include button-style($primary-color);
  }
}
```

注意 SCSS 用 `$` 声明变量、`@mixin` 定义混入、`@include` 引用混入、`&` 表示父选择器、可以嵌套选择器。

### 如何编译导出（转成 CSS）

**方法一：命令行手动编译**
```bash
# 编译单个文件（输出 style.css）
sass style.scss style.css

# 监听文件变化自动编译
sass --watch style.scss:style.css

# 监听整个目录
sass --watch input-dir:output-dir

# 压缩输出（生产环境）
sass style.scss style.css --style=compressed
```

**方法二：VS Code + Live Sass Compiler 扩展**
1. 装 Live Sass Compiler 扩展
2. 打开 .scss 文件，点底部状态栏的 "Watch Sass"
3. 保存文件时自动生成同目录的 .css 和 .css.map

**方法三：项目集成（Vite/Webpack）**
现代前端项目（如 Vue 3 + Vite）自动支持 SCSS：
```bash
# 安装 sass 作为开发依赖
npm install -D sass-embedded
# 然后在 .vue 文件里 <style lang="scss"> 即可
```

## 5. 常见报错与解决

### 问题1：报错 "Error: Undefined variable"

**原因：** 用了未定义的 `$变量`，或变量作用域问题。

**解决方法：**
1. 确认变量已用 `$` 声明
2. 注意变量作用域：嵌套块内声明的变量是局部的，外层访问不到
3. 全局变量用 `!default` 设置默认值：`$color: red !default;`
4. 跨文件用变量，需在用到的文件 `@use 'vars' as *;`（注意新版用 @use 不是 @import）

### 问题2：报错 "Error: no module named 'xxx'" 或 @use 找不到模块

**原因：** Sass 新版用 `@use` 替代了旧的 `@import`，规则不同；或路径不对。

**解决方法：**
1. 新项目统一用 `@use '文件名'`，弃用 `@import`
2. 注意 `@use` 的命名空间：`@use 'vars';` 后用 `vars.$color`，或加 `as *` 直接用变量
3. 文件路径以相对当前 .scss 文件为准，前缀下划线表示是 partial（部分文件，如 `_vars.scss`，引用时写 `vars`）
4. 检查大小写（部分系统区分）

### 问题3：CSS 没生成 / 编译没反应

**原因：** 没开监听，或扩展没生效，或文件名/路径有误。

**解决方法：**
1. 命令行方式：确认执行了 `sass --watch`，且监听的路径正确
2. VS Code 方式：确认 Live Sass Compiler 扩展已开启 "Watch"（底部状态栏）
3. 检查 .scss 文件是否在配置的输出目录下
4. 项目方式：确认 `sass` 已在 devDependencies 里，构建工具已识别

### 问题4：编译后的 CSS 体积很大或有重复

**原因：** 多次 @include 同一个 mixin 导致代码重复，或没开压缩。

**解决方法：**
1. 生产环境编译加 `--style=compressed` 压缩
2. 用 `@use` 而非 `@import`（@import 会导致重复和全局污染）
3. 公共样式用 placeholder 选择器 `%xxx` + `@extend`，减少重复
4. 检查是否有无用样式，用工具如 purgecss 清理

---

## 💡 小知识

- Sass 是最早的 CSS 预处理器之一（2006 年），SCSS 语法是后来为贴近 CSS 习惯而新增的
- "SCSS" 的 S 代表 "Sassy"（时髦的），与旧式缩进语法 .sass 区分
- Sass 的主要竞品是 Less（.less），两者功能相似，SCSS 在生态上更主流
- Bootstrap 4+、Element Plus、Vuetify 等主流框架都用 SCSS 作为样式基础

## 🔗 相关链接

- [Sass 官网](https://sass-lang.com/)
- [Sass 中文文档](https://www.sass.hk/)
- [Dart Sass GitHub](https://github.com/sass/dart-sass)
- [VS Code Live Sass Compiler](https://marketplace.visualstudio.com/items?itemName=ritwickdey.live-sass)
- [Bootstrap 官网](https://getbootstrap.com/)

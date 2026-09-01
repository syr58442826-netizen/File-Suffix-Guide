# 高级编程与脚本

本分类收录了现代开发中常用的高级编程语言和前端工程化相关文件后缀。

> 这些后缀对应的是当前业界主流的编程语言与前端工具链。源码本质都是纯文本，但运行它们需要安装对应的语言环境（编译器/解释器/运行时）。

## 后缀列表

### 编程语言

| 后缀 | 名称 | 简介 |
|------|------|------|
| [.ts](./ts.md) | TypeScript 源代码 | JavaScript 的类型安全超集，大型项目首选 |
| [.go](./go.md) | Go 语言源代码 | Google 出品的高性能并发编程语言 |
| [.rs](./rs.md) | Rust 源代码 | 内存安全的高性能系统编程语言 |
| [.rb](./rb.md) | Ruby 源代码 | 简洁优雅的动态脚本语言，Rails 框架闻名 |
| [.php](./php.md) | PHP 源代码 | 经典的 Web 后端开发语言 |
| [.swift](./swift.md) | Swift 源代码 | Apple 推出的现代编程语言 |
| [.kt](./kt.md) | Kotlin 源代码 | JetBrains 出品，Android 开发首选 |
| [.cs](./cs.md) | C# 源代码 | 微软的跨平台面向对象语言 |
| [.lua](./lua.md) | Lua 脚本 | 轻量级嵌入式脚本语言，游戏开发首选 |
| [.r](./r.md) | R 语言源代码 | 统计分析与数据可视化的专业语言 |
| [.dart](./dart.md) | Dart 源代码 | Google 出品，Flutter 跨平台开发核心语言 |
| [.scala](./scala.md) | Scala 源代码 | JVM 上的函数式+面向对象语言，Spark 生态首选 |
| [.pl](./pl.md) | Perl 脚本 | 经典的文本处理与系统运维脚本语言 |
| [.jl](./jl.md) | Julia 语言源代码 | 高性能科学计算与数值分析语言 |
| [.asm](./asm.md) | 汇编语言源文件 | 最接近机器语言的底层编程文件 |

### 前端工程化

| 后缀 | 名称 | 简介 |
|------|------|------|
| [.vue](./vue.md) | Vue 单文件组件 | 前端框架 Vue 的组件文件 |
| [.scss](./scss.md) | Sass/SCSS 样式表 | 功能强大的 CSS 预处理器 |
| [.less](./less.md) | Less 样式表 | 另一种流行的 CSS 预处理器 |
| [.jsx](./jsx.md) | React JSX 文件 | React 组件文件，JSX 语法扩展 |
| [.tsx](./tsx.md) | React TSX 文件 | React + TypeScript，带类型安全的组件文件 |

### 构建工具

| 后缀 | 名称 | 简介 |
|------|------|------|
| [.cmake](./cmake.md) | CMake 构建脚本 | C/C++ 跨平台构建系统配置文件 |
| [.gradle](./gradle.md) | Gradle 构建脚本 | Java/Android 项目的自动化构建配置 |

### 服务端页面

| 后缀 | 名称 | 简介 |
|------|------|------|
| [.aspx](./aspx.md) | ASP.NET 网页 | 微软的服务端渲染动态网页文件 |
| [.jsp](./jsp.md) | JavaServer Pages | Java 平台的服务端渲染动态网页文件 |

### 配置格式

| 后缀 | 名称 | 简介 |
|------|------|------|
| [.toml](./toml.md) | TOML 配置文件 | 语义清晰的新一代配置文件格式 |

## 学习建议

1. **前端进阶**：从 JavaScript 学起，再进阶 TypeScript 和 Vue，理解现代前端工程化。React 生态可从 JSX 入手，再进阶 TSX 获得类型安全
2. **后端开发**：Go 适合高并发服务，PHP 适合快速建站，Ruby on Rails 适合快速产品迭代，Scala 适合大数据与高性能 JVM 后端
3. **系统/高性能**：Rust 内存安全、性能极致，适合系统级开发；汇编（.asm）用于底层硬件操作和极限优化，但学习曲线陡峭
4. **移动开发**：Swift 做 iOS/macOS，Kotlin 做 Android，Dart + Flutter 一套代码覆盖全平台
5. **数据科学**：R 专注统计分析与可视化，Julia 兼具 Python 的易用性和 C 的性能，适合科学计算
6. **脚本与运维**：Lua 轻量嵌入游戏和 Nginx，Perl 擅长文本处理与正则，适合运维和数据处理
7. **构建管理**：CMake 是 C++ 跨平台构建标准，Gradle 是 Java/Android 项目的主流构建工具
8. **服务端渲染**：ASP.NET（.aspx）是微软生态的服务端页面，JSP 是 Java 平台的动态页面技术，现代项目已逐渐转向前后端分离架构
9. **样式进阶**：SCSS 和 Less 让 CSS 支持变量、嵌套、混入，大幅提升维护效率
10. **配置管理**：TOML 正逐步替代 INI/JSON 成为 Rust/Python 等项目的配置标准

# .toml 文件后缀详解

## 1. 文件定义 & 用途

.toml 是 **TOML**（Tom's Obvious, Minimal Language）配置文件的后缀。TOML 是一种语义清晰、可读性强的配置文件格式，目标是取代 INI 等老旧格式，成为"比 YAML 简单、比 JSON 友好"的配置标准。

简单来说，.toml 文件就是用来给程序写配置的文本文件，语法类似 INI 的 `键 = 值`，但支持更丰富的数据类型（数组、表、日期等）。

**主要用途：**
- Rust 项目的依赖配置（Cargo.toml）
- Python 项目的构建配置（PEP 518 的 pyproject.toml）
- 静态网站生成器的配置（Hugo、Zola）
- 应用的配置文件
- 数据序列化和交换

## 2. 适用场景

- 给程序/项目写配置文件
- Rust 项目的依赖管理（Cargo.toml 是必备）
- Python 项目的现代化配置（pyproject.toml）
- 喜欢清晰语法、不想被 YAML 的缩进和陷阱折磨的开发者
- 需要注释的配置文件（JSON 不支持注释，TOML 支持）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Even Better TOML 扩展、Notepad++ | WebStorm、Sublime Text |
| Mac | [VS Code](https://code.visualstudio.com/) + Even Better TOML 扩展、Vim | WebStorm |
| Linux | [VS Code](https://code.visualstudio.com/) + Even Better TOML 扩展、Vim | WebStorm |

**新手推荐：** VS Code + Even Better TOML 扩展（语法高亮和格式化）。任何文本编辑器都能编辑，因为就是纯文本。

## 4. 如何编辑、如何导出

### 环境准备

TOML 是纯文本配置文件，**不需要安装运行时**，只要有解析它的程序即可。常见场景里：
- Rust 项目：Cargo 自动解析 Cargo.toml
- Python 项目：用 `tomllib`（3.11+ 内置）或 `tomli`/`toml` 包解析
- Hugo/Zola：工具自身解析

### 如何编辑

**一个完整的 TOML 示例：**
```toml
# 这是注释，以 # 开头

# 基本键值对
title = "我的项目"
version = "1.0.0"
is_published = true

# 数字
port = 8080
pi = 3.14

# 日期（RFC 3339 格式）
created_at = 2024-01-15T10:30:00Z

# 数组
tags = ["web", "frontend", "vue"]
authors = ["Alice", "Bob"]

# 表（table），用方括号定义一个区块
[server]
host = "localhost"
port = 3000

[database]
url = "postgres://localhost/mydb"
max_connections = 100

# 内联表
[owner]
name = "小明"
contact = { email = "xm@example.com", phone = "13800000000" }

# 数组里的表
[[fruits]]
name = "apple"
color = "red"

[[fruits]]
name = "banana"
color = "yellow"
```

注意 TOML 用 `#` 注释、`[表名]` 定义表、`[[表名]]` 定义数组表、字符串用双引号、布尔值是小写 `true/false`。

### 如何解析和使用

TOML 不需要"编译导出"，程序读取它即可。

**Rust（Cargo.toml）：** Cargo 自动解析，无需手动操作。
```toml
# Cargo.toml
[package]
name = "myapp"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = "1.0"
```

**Python 读取 TOML：**
```python
import tomllib  # Python 3.11+ 内置

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

print(config["title"])          # 我的项目
print(config["server"]["port"])  # 3000
```

**Node.js 读取 TOML：**
```bash
npm install @iarna/toml
```
```javascript
const fs = require('fs');
const TOML = require('@iarna/toml');
const config = TOML.parse(fs.readFileSync('config.toml', 'utf-8'));
console.log(config.title);
```

## 5. 常见报错与解决

### 问题1：报错 "Expected key, but found ..." 或解析失败

**原因：** TOML 语法错误，常见于：
- 键名没加引号但有特殊字符
- 值的类型写错
- 表头重复定义

**解决方法：**
1. 键名含特殊字符时用引号：`"my key" = "value"`
2. 字符串值用引号包裹，数字不用引号
3. 布尔值用小写 `true/false`，别写 `True/False`
4. 表头 `[server]` 在文件中只能出现一次，重复定义会报错
5. 用 TOML 校验器（如 toml-lint）检查

### 问题2：表/数组表的层级混乱，值读不到

**原因：** TOML 中表定义后，其下的键值对都属于该表，直到下一个表头。新人常把键写错位置。

**解决方法：**
1. 表头 `[表名]` 后的键值对都属于这个表
2. 数组表 `[[表名]]` 每出现一次就新增一个数组元素
3. 嵌套表用点：`[server.tls]` 表示 server 表下的 tls 表
4. 注意"内联表" `{ a = 1, b = 2 }` 是单行的，不能换行加更多键

### 问题3：Python 报 "ModuleNotFoundError: No module named 'tomllib'"

**原因：** Python 版本低于 3.11，没有内置 tomllib。

**解决方法：**
```bash
# 升级 Python 到 3.11+（推荐）
# 或安装第三方包
pip install tomli
```
```python
# 用 tomli 替代（接口与 tomllib 几乎一致）
import tomli
with open("config.toml", "rb") as f:
    config = tomli.load(f)
```

### 问题4：值类型识别错误（如端口号读成字符串）

**原因：** TOML 中值加不加引号决定类型：`port = 8080` 是整数，`port = "8080"` 是字符串。程序期望某类型但 TOML 写成了另一种。

**解决方法：**
1. 数字不加引号：`port = 8080`（整数）
2. 浮点数：`pi = 3.14`
3. 字符串必须加引号：`title = "项目"`
4. 布尔值不加引号：`is_on = true`
5. 如果是版本号字符串（含点），必须加引号：`version = "1.0.0"`（否则会被解析成浮点数！）

---

## 💡 小知识

- TOML 的名字来源于其作者 Tom Preston-Werner（GitHub 联合创始人）
- TOML 设计目标：最小化、可读性强、语义清晰映射到哈希表
- TOML 的解析规范比 YAML 简单得多，没有 YAML 的"挪威问题"等陷阱
- TOML 已成为 Rust 生态的事实配置标准，并逐步在 Python、Go 社区流行

## 🔗 相关链接

- [TOML 官网](https://toml.io/)
- [TOML 中文文档](https://toml.io/cn/)
- [TOML 规范](https://toml.io/en/v1.0.0)
- [Cargo 配置文档](https://doc.rust-lang.org/cargo/reference/manifest.html)
- [Python tomllib 文档](https://docs.python.org/zh-cn/3/library/tomllib.html)
- [VS Code Even Better TOML 扩展](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)

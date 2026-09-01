# .rs 文件后缀详解

## 1. 文件定义 & 用途

.rs 是 **Rust** 编程语言的源代码文件后缀。Rust 由 Mozilla 开发，主打**内存安全和高性能**，号称"C/C++ 的安全替代品"。它通过所有权（ownership）机制，在编译阶段就杜绝了大部分内存错误，无需垃圾回收（GC）。

简单来说，.rs 文件就是用 Rust 语言写的程序代码，编译后会生成高效的原生机器码。

**主要用途：**
- 系统级编程（操作系统、驱动、嵌入式）
- WebAssembly（Rust 是编译 WASM 的一流选择）
- 高性能命令行工具（ripgrep、fd、zoxide 都是 Rust 写的）
- 区块链底层（Solana、Polkadot）
- 浏览器引擎、游戏引擎、Web 框架

## 2. 适用场景

- 对性能和安全性都有极高要求的场景
- 系统编程、底层开发
- 需要编译成 WebAssembly 的前端加速
- 想要替代 C/C++ 但又怕内存问题的项目
- 编写高性能命令行工具

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + rust-analyzer 扩展、Vim | RustRover（JetBrains，有社区免费版） |
| Mac | [VS Code](https://code.visualstudio.com/) + rust-analyzer 扩展、Vim | RustRover |
| Linux | [VS Code](https://code.visualstudio.com/) + rust-analyzer 扩展、Vim | RustRover |

**新手推荐：** VS Code + rust-analyzer 扩展（提供代码补全和实时类型检查）。

## 4. 如何编辑、如何导出

### 环境准备

**安装 Rust（用官方的 rustup 工具）：**
1. 去 [Rust 官网](https://www.rust-lang.org/) 按提示安装
2. Windows：下载 rustup-init.exe，按提示装（需要 Visual Studio C++ Build Tools，安装器会提示）
3. Mac/Linux：终端执行 `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
4. 验证：`rustc --version` 和 `cargo --version`

### 如何编辑

**一个简单的 Rust 示例：**
```rust
// hello.rs
fn main() {
    println!("你好，Rust！");
    let name = String::from("小明");
    println!("欢迎，{}！", name);
}
```

### 如何运行、如何导出

Rust 项目通常用 **Cargo**（官方构建工具和包管理器）管理。

**方法一：直接编译运行单文件**
```bash
# 编译单文件（生成可执行文件 hello 或 hello.exe）
rustc hello.rs

# 运行
./hello        # Linux/Mac
hello.exe      # Windows
```

**方法二：用 Cargo 管理项目（推荐）**
```bash
# 创建新项目
cargo new myproject
cd myproject

# 运行项目（自动编译并执行）
cargo run

# 编译发布版（优化、更快）
cargo build --release

# 添加第三方依赖（编辑 Cargo.toml 后）
cargo build

# 检查代码是否编译通过（不生成产物，速度更快）
cargo check
```

**方法三：编译成 WebAssembly**
```bash
# 安装 wasm-pack 工具
cargo install wasm-pack

# 构建 WASM 包
wasm-pack build --target web
```

## 5. 常见报错与解决

### 问题1：Windows 上报 "linker 'link.exe' not found"

**原因：** Windows 编译 Rust 需要 C++ 链接器（来自 Visual Studio Build Tools）。

**解决方法：**
1. 下载 [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. 安装时勾选"使用 C++ 的桌面开发"工作负载
3. 重启终端后重新 `cargo build`

### 问题2：报错 "cannot borrow ... as mutable, because it is also borrowed as immutable"

**原因：** 触发了 Rust 的借用检查规则：同一作用域内不能同时有可变借用和不可变借用。这是 Rust 保证内存安全的核心机制。

**解决方法：**
1. 让借用不重叠，把不可变借用用完再创建可变借用
2. 用 `.clone()` 复制一份数据，避免借用冲突
3. 重新设计代码，让所有权关系更清晰
4. 如果实在绕不开，考虑用 `RefCell` 在运行时借用（但失去编译期保证）

### 问题3：编译很慢 / 下载依赖超时

**原因：** Rust 的依赖从 crates.io 拉取，国内网络访问慢。

**解决方法：**
```bash
# 设置国内镜像（修改 ~/.cargo/config.toml 或项目 .cargo/config.toml）
# 内容：
# [source.crates-io]
# replace-with = "ustc"
# [source.ustc]
# registry = "https://mirrors.ustc.edu.cn/crates.io-index"
```

### 问题4：报错 "expected one of ... found ...", "mismatched types"

**原因：** Rust 是强类型语言，类型不匹配或语法位置不对。

**解决方法：**
1. 仔细看错误提示的行号和位置标记（Rust 的报错信息非常友好，会指明位置）
2. 检查函数返回类型、变量类型是否对得上
3. 需要类型转换时用 `as`（如 `let x = y as i32`）或 `From/Into`
4. 善用 `cargo check` 快速发现编译错误

---

## 💡 小知识

- Rust 连续多年蝉联 Stack Overflow "最受开发者喜爱的语言"榜首
- Rust 用"所有权"机制替代垃圾回收，做到零运行时开销的内存安全
- Rust 没有 null，用 `Option<T>` 类型表达可能为空的值，从根源杜绝空指针
- Rust 的报错信息被认为是所有语言里最友好的，会给你具体建议

## 🔗 相关链接

- [Rust 官网](https://www.rust-lang.org/)
- [Rust 程序设计语言（中文版）](https://rustwiki.org/zh-CN/book/)
- [Rust By Example（中文版）](https://rustwiki.org/zh-CN/rust-by-example/)
- [crates.io 官方包仓库](https://crates.io/)
- [RustRover 官网](https://www.jetbrains.com/rust/)

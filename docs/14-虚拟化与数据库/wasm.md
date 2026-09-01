# .wasm 文件后缀详解

## 1. 文件定义 & 用途

.wasm 是 **WebAssembly** 的二进制文件后缀。WebAssembly（简称 WASM）是一种可移植、体积小、加载快的二进制指令格式，可以让 C/C++/Rust/Go 等语言编译后的代码在浏览器或 WASM 运行时中接近原生速度运行。

简单来说，.wasm 文件就是"编译后的可移植二进制程序"，浏览器和 Node.js 等运行时可以直接加载执行它，用来做 JavaScript 难以胜任的高性能计算。

> 补充：还有一个相关后缀 .wat，是 WASM 的文本格式（WAT，WebAssembly Text Format），可读性强，可手动编写，能和 .wasm 互相转换。

**主要用途：**
- 浏览器中的高性能计算（图像/视频处理、游戏、3D 渲染）
- 把 C/C++/Rust 代码搬到 Web 端复用
- 服务器端无服务器计算（Cloudflare Workers、Fastly Compute）
- 区块链智能合约（部分链用 WASM 作为执行引擎）
- 跨平台应用运行时（如即时编译运行各种语言）

## 2. 适用场景

- 需要在浏览器跑性能敏感的任务
- 复用已有 C/C++/Rust 代码到 Web
- 嵌入式/边缘计算场景
- 需要跨平台二进制可移植性的场景

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 浏览器（Chrome/Edge/Firefox）、[VS Code](https://code.visualstudio.com/) + WASM 扩展、Node.js | Binaryen（wasm-opt 等工具） |
| Mac | 浏览器（Chrome/Safari/Firefox）、[VS Code](https://code.visualstudio.com/)、Node.js | Binaryen |
| Linux | 浏览器、[VS Code](https://code.visualstudio.com/)、Node.js、wabt 工具链 | Binaryen |

**新手推荐：** 浏览器（直接能跑 .wasm）。开发用 VS Code + WebAssembly 相关扩展，配合 wabt 工具链（wat2wasm 等命令）。

## 4. 如何编辑、如何导出

### 环境准备

.wasm 是编译产物，不直接手写（除非用 .wat 文本格式）。需要用对应语言的工具链从源码编译。

**安装 wabt 工具链（处理 wat/wasm 互转、查看）：**
```bash
# Mac
brew install wabt

# Linux/WSL
sudo apt install wabt

# 或从源码 https://github.com/WebAssembly/wabt
```

### 如何编辑（用源码编写后编译）

**方式一：用 Rust 编译 WASM（Rust 是编译 WASM 的一流选择）**
```bash
# 安装 wasm-pack
cargo install wasm-pack

# 在 Rust 项目里编译为 WASM
wasm-pack build --target web
# 产物在 pkg/ 目录下的 .wasm
```

Rust 示例代码：
```rust
// src/lib.rs
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

**方式二：用 C/C++ + Emscripten 编译**
```bash
# 安装 Emscripten（见 https://emscripten.org/）
emcc hello.c -o hello.wasm -O3
```

**方式三：手写 .wat 文本格式再转 .wasm**
```wat
;; add.wat
(module
  (func $add (export "add") (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.add))
```
```bash
# wat 转 wasm
wat2wasm add.wat -o add.wasm

# wasm 反编译回 wat（查看内容）
wasm2wat add.wasm -o add.wat
```

### 如何运行

**在浏览器中加载（JavaScript 调用）：**
```javascript
// 加载并调用 WASM
const response = await fetch('add.wasm');
const bytes = await response.arrayBuffer();
const { instance } = await WebAssembly.instantiate(bytes);

const result = instance.exports.add(3, 4);
console.log(result);  // 7
```

**在 Node.js 中运行：**
```javascript
const fs = require('fs');
const wasmBuffer = fs.readFileSync('add.wasm');
WebAssembly.instantiate(wasmBuffer).then(({ instance }) => {
    console.log(instance.exports.add(3, 4));  // 7
});
```

### 如何查看 .wasm 内容

```bash
# 反编译成可读的 .wat 文本
wasm2wat add.wasm -o add.wat

# 查看 wasm 模块结构
wasm-objdump add.wasm -x

# 用 wasm-opt 优化
wasm-opt add.wasm -o add.opt.wasm -O3
```

## 5. 常见报错与解决

### 问题1：浏览器加载报错 "CompileError: wasm validation error"

**原因：** .wasm 文件损坏、不完整，或不符合 WASM 规范（如手工修改了二进制）。

**解决方法：**
1. 重新从源码编译，确保编译过程完整
2. 用 wabt 工具验证：`wasm-validate add.wasm`
3. 确认下载的 .wasm 没被截断或改坏
4. 检查目标环境支持的 WASM 特性（如 SIMD、异常处理需要浏览器支持）

### 问题2：Rust 编译 WASM 报 "wasm32-unknown-unknown target not installed"

**原因：** Rust 没装 WASM 编译目标。

**解决方法：**
```bash
# 添加 wasm32 编译目标
rustup target add wasm32-unknown-unknown

# 或用 wasm-pack（自动处理）
cargo install wasm-pack
wasm-pack build --target web
```

### 问题3：调用 WASM 函数报 "TypeError: instance.exports.xxx is not a function"

**原因：** 想调用的函数没导出，或导出名与调用的名字不一致。

**解决方法：**
1. 源码里用 `#[no_mangle]`（Rust）或 `__attribute__((visibility("default")))`（C/C++）确保导出
2. 在 .wat 里用 `(export "名字" (func $func))` 导出
3. 用 `wasm-objdump 文件.wasm -x` 查看实际导出的函数名
4. 注意 Rust 编译后可能给函数名加前缀，用 `#[export_name = "add"]` 显式指定

### 问题4：WASM 程序运行时报内存溢出或访问越界

**原因：** WASM 默认有线性内存，越界访问或内存分配不足会失败。

**解决方法：**
1. 编译时增加初始内存：Rust 用 `Config::new().wasm_bindgen` 相关配置，或 .wat 里设置 `(memory $memory (export "memory") 1)`
2. 检查源码是否有缓冲区越界
3. 用 `-O0` 关闭优化调试，看是否能定位问题
4. WASM 不会像 C 那样直接崩溃，但会 trap，检查报错栈

---

## 💡 小知识

- WebAssembly 不是要取代 JavaScript，而是与之互补，专注高性能场景
- WebAssembly 1.0 在 2017 年所有主流浏览器支持，是 Web 平台最快的标准化进程之一
- WebAssembly 名字里有"Web"，但它也能在浏览器外运行（Node.js、WASI、边缘计算）
- Rust 是编译到 WASM 体验最好的语言之一，体积小、无需 GC 运行时

## 🔗 相关链接

- [WebAssembly 官网](https://webassembly.org/)
- [MDN WebAssembly 文档](https://developer.mozilla.org/zh-CN/docs/WebAssembly)
- [wabt 工具链 GitHub](https://github.com/WebAssembly/wabt)
- [Emscripten 官网](https://emscripten.org/)
- [wasm-pack 官网](https://rustwasm.github.io/wasm-pack/)
- [WebAssembly 中文社区](https://wasmer.io/)

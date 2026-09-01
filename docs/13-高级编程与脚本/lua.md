# .lua 文件后缀详解

## 1. 文件定义 & 用途

.lua 是 **Lua 语言**的源代码文件后缀。Lua 是一种轻量、快速、可嵌入的脚本语言，由巴西 PUC-Rio 大学开发。它的核心只有一个几十 KB 的 C 库，非常适合嵌入到其他程序中作为扩展脚本使用。

Lua 最大的特点是"小而美"——语法简洁，运行速度极快，内存占用极低。它不是用来写大型独立应用的，而是作为"胶水语言"嵌入到 C/C++ 程序中，让用户可以用脚本扩展功能。

**主要用途：**
- **游戏脚本**：Roblox、魔兽世界、Angry Birds 等大量游戏用 Lua 写游戏逻辑
- **嵌入式扩展**：Redis、Nginx（OpenResty）、Wireshark 等支持 Lua 扩展
- **Nginx 高性能 Web 服务**：OpenResty 用 Lua 实现动态 Web 逻辑
- **桌面应用插件**：Adobe Lightroom、Neovim 等用 Lua 做插件脚本
- **物联网和嵌入式设备**：NodeMCU（ESP8266）固件支持 Lua

## 2. 适用场景

- 游戏开发中的逻辑脚本和热更新
- 给 C/C++ 程序写扩展脚本（通过 Lua C API 嵌入）
- Redis 服务端脚本（事务性操作）
- OpenResty / Nginx 动态 Web 服务
- Neovim 插件开发
- 物联网关设备编程

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Lua 扩展、Notepad++ | IntelliJ IDEA + EmmyLua 插件 |
| Mac | [VS Code](https://code.visualstudio.com/) + Lua 扩展、Vim | IntelliJ IDEA + EmmyLua 插件 |
| Linux | [VS Code](https://code.visualstudio.com/) + Lua 扩展、Vim | IntelliJ IDEA + EmmyLua 插件 |

**新手推荐：** VS Code + 安装 "Lua" 扩展（由 sumneko 开发，提供语言服务器支持，代码补全和诊断功能强大）。

## 4. 如何编辑、如何导出

### 环境准备

**安装 Lua：**
- Windows：去 [LuaBinaries](https://luabinaries.sourceforge.net/) 下载，或用 `scoop install lua`
- Mac：`brew install lua`
- Linux：`sudo apt install lua5.4`（Debian/Ubuntu）

验证安装：
```bash
lua -v
```

### 如何编辑

**一个简单的 Lua 示例：**
```lua
-- hello.lua
-- Lua 中注释用两个减号
local function greet(name)
    return "你好，" .. name .. "！"
end

local user = "小明"
print(greet(user))

-- Lua 的表（table）是唯一的数据结构
local config = {
    host = "localhost",
    port = 8080,
    enabled = true
}

print("服务器地址：" .. config.host .. ":" .. config.port)
```

注意：Lua 用 `..` 做字符串拼接，用 `local` 声明局部变量（默认是全局变量），数组和字典都叫 `table`，索引从 1 开始（不是 0）。

### 如何运行

**直接运行：**
```bash
# 直接执行脚本文件
lua hello.lua

# 交互式命令行（REPL）
lua
> print("Hello Lua!")
> os.exit()
```

**编译为字节码（加速加载，不加密）：**
```bash
# 将 .lua 编译为 .luac 字节码文件
luac -o hello.luac hello.lua

# 运行字节码
lua hello.luac
```

**嵌入 C 程序中运行（了解原理）：**
```c
#include <lua.h>
#include <lualib.h>
#include <lauxlib.h>

int main() {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    luaL_dofile(L, "hello.lua");
    lua_close(L);
    return 0;
}
```

## 5. 常见报错与解决

### 问题1：报错 "attempt to index a nil value (global 'xxx')"

**原因：** 访问了不存在的变量或表字段，Lua 中未定义的变量返回 nil，对 nil 做索引操作就报错。

**解决方法：**
1. 检查变量名拼写是否正确
2. 确认变量已在当前作用域声明（用了 `local` 的变量有作用域限制）
3. 对于 table 字段，先判断是否为 nil：
```lua
-- 安全访问
if config and config.database and config.database.host then
    print(config.database.host)
end
```

### 问题2：报错 "attempt to call a nil value"

**原因：** 调用了一个不存在的函数，或函数名拼错了。Lua 把不存在的变量当作 nil，对 nil 做函数调用就报错。

**解决方法：**
1. 检查函数名拼写和定义位置
2. 确认函数在调用前已定义（Lua 中函数必须先定义后使用，或用前向声明）
3. 确认模块已正确 require：
```lua
-- 引入模块
local json = require("cjson")
-- 如果模块没装好，json 就是 nil
```

### 问题3：运行提示 "'lua' 不是内部或外部命令"（Windows）

**原因：** Lua 没有安装，或没有添加到系统 PATH。

**解决方法：**
1. 去 [LuaBinaries](https://luabinaries.sourceforge.net/) 下载 Windows 版
2. 解压后将 lua54.dll 和 lua.exe 所在目录添加到系统环境变量 PATH
3. 或用包管理器安装：
```bash
# 用 scoop 安装
scoop install lua

# 用 chocolatey 安装
choco install lua
```

### 问题4：表遍历结果顺序不确定

**原因：** Lua 的 table 是哈希表，用 `pairs` 遍历时顺序不保证，新手容易困惑。

**解决方法：**
```lua
-- 有序遍历用数组部分 + ipairs
local fruits = {"apple", "banana", "cherry"}
for i, v in ipairs(fruits) do
    print(i, v)  -- 1 apple  2 banana  3 cherry
end

-- 需要排序的字典，先提取 key 再排序
local scores = {math=90, english=85, science=95}
local keys = {}
for k in pairs(scores) do table.insert(keys, k) end
table.sort(keys)
for _, k in ipairs(keys) do
    print(k, scores[k])
end
```

---

## 💡 小知识

- Lua 在葡萄牙语中是"月亮"的意思
- Lua 的 table 是它唯一的数据结构，数组、字典、对象、面向对象都基于 table 实现
- Lua 的索引从 1 开始，不是 0，这是从 Lua 诞生延续至今的设计
- 魔兽世界插件、Roblox 游戏平台、Angry Birds 都用 Lua 写游戏逻辑
- LuaJIT（即时编译版）的速度接近原生 C 代码，是性能最强的脚本语言之一

## 🔗 相关链接

- [Lua 官网](https://www.lua.org/)
- [Lua 中文教程](https://www.runoob.com/lua/lua-tutorial.html)
- [LuaBinaries 下载](https://luabinaries.sourceforge.net/)
- [OpenResty 官网](http://openresty.org/)
- [EmmyLua 插件](https://github.com/EmmyLua/EmmyLua)
- [Lua 参考手册](https://www.lua.org/manual/5.4/)

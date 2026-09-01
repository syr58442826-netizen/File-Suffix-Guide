# .cmake 文件后缀详解

## 1. 文件定义 & 用途

.cmake 是 **CMake 构建系统**的脚本文件后缀。CMake 是一个跨平台的自动化构建工具，它本身不编译代码，而是根据配置文件生成对应平台的构建文件（如 Makefile、Visual Studio 工程、Ninja 文件等），再用这些构建文件去编译 C/C++ 项目。

简单来说，.cmake 文件描述"怎么编译项目"，CMake 读取后生成具体的编译指令。CMake 解决了"在不同平台上用不同编译器构建同一份 C/C++ 代码"的问题。

**主要用途：**
- C/C++ 项目的跨平台构建管理
- 管理 C/C++ 第三方库的依赖和链接
- 配置编译选项（Debug/Release、优化级别等）
- 生成 Visual Studio 工程、Makefile、Ninja 等
- 开源 C++ 项目的标准构建方案

## 2. 适用场景

- C/C++ 项目需要跨平台编译
- 管理多文件、多目录的 C/C++ 项目构建
- 依赖第三方库（如 OpenCV、Boost、Protobuf 等）
- 开源 C++ 项目发布给社区使用
- 嵌入式和系统级项目构建

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + CMake 扩展、Notepad++ | Visual Studio（Community 免费版）、CLion（JetBrains） |
| Mac | [VS Code](https://code.visualstudio.com/) + CMake 扩展、Vim | CLion、Visual Studio for Mac |
| Linux | [VS Code](https://code.visualstudio.com/) + CMake 扩展、Vim | CLion |

**新手推荐：** VS Code + CMake Tools 扩展（图形化配置和一键构建）。或直接用 CLion（JetBrains 出品，CMake 项目支持最佳）。

## 4. 如何编辑、如何导出

### 环境准备

**安装 CMake：**
- Windows：去 [CMake 官网](https://cmake.org/download/) 下载安装包，或 `scoop install cmake`
- Mac：`brew install cmake`
- Linux：`sudo apt install cmake`

验证安装：
```bash
cmake --version
```

**安装编译器：**
- Windows：安装 [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)（含 MSVC 编译器）或 [MinGW](https://www.mingw-w64.org/)
- Mac：安装 Xcode Command Line Tools：`xcode-select --install`
- Linux：`sudo apt install build-essential g++`

### 如何编辑

CMake 项目通常从 `CMakeLists.txt` 开始。.cmake 文件一般作为辅助模块被 `include()` 引用。

**一个简单的 CMakeLists.txt 示例：**
```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.15)
project(MyApp)

# C++ 标准
set(CMAKE_CXX_STANDARD 17)

# 添加可执行文件
add_executable(hello hello.cpp)
```

**一个 .cmake 模块文件示例：**
```cmake
# custom_rules.cmake - 可被多个项目复用的 CMake 模块
# 设置编译选项
function(set_common_compile_options target)
    target_compile_options(${target} PRIVATE
        $<$<CXX_COMPILER_ID:MSVC>:/W4 /O2>
        $<$<CXX_COMPILER_ID:GNU>:-Wall -Wextra -O2>
    )
endfunction()

# 查找第三方库的示例
# FindMyLib.cmake
find_path(MYLIB_INCLUDE_DIR mylib.h PATHS /usr/include /usr/local/include)
find_library(MYLIB_LIBRARY NAMES mylib PATHS /usr/lib /usr/local/lib)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(MyLib DEFAULT_MSG MYLIB_LIBRARY MYLIB_INCLUDE_DIR)
```

注意：CMake 语法用 `()` 包裹参数，变量用 `set()` 赋值，用 `${变量名}` 引用。

### 如何运行（构建项目）

**标准构建流程：**
```bash
# 1. 创建构建目录（推荐用外部构建，不污染源码目录）
mkdir build && cd build

# 2. 生成构建文件
cmake ..

# 3. 编译
cmake --build .            # 通用方式
# 或直接用生成的工具
make                       # Linux/Mac
ninja                      # 如果用 Ninja 生成器

# 4. 运行程序
./hello
```

**指定生成器和编译器：**
```bash
# 生成 Visual Studio 工程（Windows）
cmake -G "Visual Studio 17 2022" ..

# 生成 MinGW Makefile
cmake -G "MinGW Makefiles" ..

# 生成 Ninja 文件（最快）
cmake -G "Ninja" ..
```

**指定构建类型（Debug/Release）：**
```bash
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake -DCMAKE_BUILD_TYPE=Debug ..
```

## 5. 常见报错与解决

### 问题1：报错 "Could not find CMAKE_C_COMPILER" 或 "No CMAKE_CXX_COMPILER"

**原因：** 系统中没有安装 C/C++ 编译器，CMake 找不到编译器。

**解决方法：**
1. Windows：安装 Visual Studio Build Tools（勾选"使用 C++ 的桌面开发"）或 MinGW
2. Mac：安装 Xcode Command Line Tools：`xcode-select --install`
3. Linux：`sudo apt install build-essential g++`
4. 安装后重新运行 `cmake ..`

### 问题2：报错 "Could NOT find xxx"（找不到第三方库）

**原因：** CMake 的 `find_package()` 没有找到目标库。

**解决方法：**
1. 确认库已安装在系统中
2. 手动指定库的路径：
```bash
cmake -DXXX_DIR=/path/to/xxx/lib/cmake/xxx ..
```
3. 如果是 vcpkg 或 conan 管理的库，配置对应工具链：
```bash
# vcpkg
cmake -DCMAKE_TOOLCHAIN_FILE=/path/to/vcpkg/scripts/buildsystems/vcpkg.cmake ..
```
4. 确认库是否提供了 CMake 配置文件（xxxConfig.cmake）

### 问题3：报错 "CMake Error: The source directory does not appear to contain CMakeLists.txt"

**原因：** 在没有 `CMakeLists.txt` 的目录下运行了 `cmake ..`。

**解决方法：**
1. 确认上级目录有 `CMakeLists.txt` 文件
2. 确认路径正确，检查是否在 `build` 目录中运行
3. 如果文件名拼错（如 `CmakeLists.txt` 大小写不对），Linux/Mac 下大小写敏感

### 问题4：修改了 CMakeLists.txt 后构建没有更新

**原因：** build 目录中有缓存，CMake 没有重新读取配置。

**解决方法：**
```bash
# 方法一：强制重新生成
cmake ..          # 在 build 目录中重新运行

# 方法二：删除缓存重新生成
rm CMakeCache.txt   # 删除缓存文件
rm -rf *            # 清空 build 目录
cmake ..
```

---

## 💡 小知识

- CMake 由 Kitware 公司开发，2000 年发布，初衷是为了管理 ITK/VTK 等大型 C++ 项目
- CMake 是"meta build system"——它不直接编译代码，而是生成其他构建系统的文件
- CMake 是 C++ 生态的事实标准构建工具，几乎所有知名 C++ 开源项目（OpenCV、LLVM、Boost、protobuf）都用 CMake
- CMake 配置文件的主文件叫 `CMakeLists.txt`，`.cmake` 文件通常作为可复用的模块被 include
- vcpkg 和 Conan 是 C++ 的包管理器，通常和 CMake 配合使用

## 🔗 相关链接

- [CMake 官网](https://cmake.org/)
- [CMake 官方教程](https://cmake.org/cmake/help/latest/guide/tutorial/)
- [CMake 中文教程](https://www.hahack.com/codes/cmake/)
- [CLion 官网](https://www.jetbrains.com/clion/)
- [vcpkg 包管理器](https://vcpkg.io/)
- [CMake Tools 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

# .cs 文件后缀详解

## 1. 文件定义 & 用途

.cs 是 **C#**（读作 C-Sharp）编程语言的源代码文件后缀。C# 是微软在 2000 年推出的面向对象编程语言，语法类似 Java/C++，运行在 .NET 平台上，现在已全面开源跨平台。

简单来说，.cs 文件就是用 C# 写的程序代码，通过 .NET 编译器编译后运行在跨平台的 .NET 运行时上。

**主要用途：**
- Windows 桌面应用开发（WPF、WinForms）
- Unity 游戏开发（Unity 的主要脚本语言）
- Web 后端开发（ASP.NET Core）
- 跨平台移动/桌面应用（.NET MAUI）
- 企业级应用和云服务（Azure）

## 2. 适用场景

- 开发 Windows 桌面应用
- 用 Unity 做游戏开发
- 构建高性能 Web API 和后端服务
- 跨平台移动/桌面应用
- 企业级业务系统开发

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [Visual Studio Community](https://visualstudio.microsoft.com/)（免费社区版）、[VS Code](https://code.visualstudio.com/) + C# 扩展 | Visual Studio Professional/Enterprise、Rider（JetBrains） |
| Mac | [VS Code](https://code.visualstudio.com/) + C# 扩展、[Visual Studio for Mac](https://visualstudio.microsoft.com/) | Rider |
| Linux | [VS Code](https://code.visualstudio.com/) + C# 扩展、Vim | Rider |

**新手推荐：** Windows 上用 Visual Studio Community（功能最全，免费）。跨平台用 VS Code + C# Dev Kit 扩展，或 JetBrains Rider（有 30 天试用）。

## 4. 如何编辑、如何导出

### 环境准备

**安装 .NET SDK：**
1. 去 [dotnet.microsoft.com](https://dotnet.microsoft.com/download) 下载 .NET SDK
2. Windows/Mac 安装包直接装，Linux 按官方指引用包管理器装
3. 验证：`dotnet --version`

**验证安装：**
```bash
dotnet --version
dotnet --list-sdks
```

### 如何编辑

**一个简单的 C# 示例：**
```csharp
// hello.cs
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("你好，C#！");

        string name = "小明";
        Console.WriteLine($"欢迎，{name}！");
    }
}
```

注意 C# 的字符串插值用 `$"..."`，语句以分号结尾，代码块用大括号。

### 如何运行、如何导出

**方法一：命令行（.NET CLI，最基础）**
```bash
# 创建控制台项目
dotnet new console -n HelloApp
cd HelloApp

# 运行
dotnet run

# 发布成单文件（跨平台分发）
dotnet publish -c Release -r win-x64 --self-contained
```

**方法二：Visual Studio 中开发**
1. File → New → Project → Console App
2. 写代码，按 F5 运行调试
3. Build → Build Solution（Ctrl+Shift+B）编译

**方法三：Unity 游戏开发**
1. 在 Unity 中创建 C# 脚本（自动生成 .cs）
2. 双击用 Visual Studio 打开编辑
3. Unity 会自动编译运行

**如何导出/发布：**
- **控制台/库**：`dotnet publish -c Release`，产物在 `bin/Release/netX.X/publish/`
- **Unity 游戏**：File → Build Settings → 选择平台 → Build

## 5. 常见报错与解决

### 问题1：报错 "The type or namespace name 'xxx' could not be found"

**原因：** 引用了未 using 的命名空间，或缺少 NuGet 包引用。

**解决方法：**
1. 在文件顶部加 `using xxx;`（VS 会用快捷键自动导入，Alt+Shift+F10）
2. 如果是第三方库，用 NuGet 安装：`dotnet add package 包名`
3. 确认项目的 target framework 满足要求

### 问题2：报错 "CS0122: 'xxx' is inaccessible due to its protection level"

**原因：** 访问了不可见的成员（如访问了 private、internal 修饰的类/方法）。

**解决方法：**
1. 检查成员的访问修饰符（public/private/protected/internal）
2. 如果是自己的代码，把成员改成 public 或 internal
3. 如果是第三方库，看文档找 public 的等价方法
4. 确认是否引用了正确的程序集

### 问题3：运行时 "System.IO.FileNotFoundException: Could not load file or assembly"

**原因：** 运行时缺少依赖的程序集（DLL），常见于：
- 发布时没包含依赖
- 目标机器 .NET 版本不对

**解决方法：**
1. 用 `dotnet publish --self-contained` 把运行时一起打包
2. 确认目标机器装了对应版本的 .NET Runtime
3. 检查 .csproj 的 TargetFramework 与运行环境一致

### 问题4：报错 "Main method not found" 或多个 Main 冲突

**原因：** C# 程序的入口是 Main 方法，新版支持顶级语句（top-level statements），混用会导致冲突。

**解决方法：**
1. 新项目默认用顶级语句（Program.cs 里直接写代码，不需要 class/ Main）
2. 不要在同一项目混用顶级语句和传统 Main 方法
3. 如果要传统写法，删掉顶级语句，定义带 Main 的 class

---

## 💡 小知识

- C# 的名字 C-Sharp 借用乐谱符号 ♯（升半音），寓意 C 的升级版
- C# 的设计者也是 Anders Hejlsberg（同时也是 Turbo Pascal 和 Delphi 的作者）
- .NET 在 2016 年开源并跨平台（.NET Core，现统一为 .NET 5+），C# 不再是 Windows 专属
- Unity 引擎的脚本语言就是 C#，大量游戏用 C# 开发

## 🔗 相关链接

- [C# 官网](https://learn.microsoft.com/zh-cn/dotnet/csharp/)
- [.NET 下载](https://dotnet.microsoft.com/download)
- [Visual Studio 官网](https://visualstudio.microsoft.com/)
- [C# 编程指南（中文）](https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/)
- [Rider 官网](https://www.jetbrains.com/rider/)
- [Unity 官网](https://unity.com/)

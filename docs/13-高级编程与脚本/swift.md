# .swift 文件后缀详解

## 1. 文件定义 & 用途

.swift 是 **Swift** 编程语言的源代码文件后缀。Swift 是 Apple 在 2014 年推出的现代编程语言，用来取代 Objective-C，成为 iOS、macOS、watchOS、tvOS 开发的首选语言。

简单来说，.swift 文件就是用 Swift 写的程序代码，编译后运行在苹果设备或通过 Swift 工具链跨平台运行。

**主要用途：**
- iOS / iPadOS App 开发
- macOS 应用开发
- watchOS、tvOS 应用
- Swift 跨平台服务端（Vapor、Hummingbird 框架）
- 命令行工具

## 2. 适用场景

- 开发苹果生态的 App
- 移动应用开发入门（相比 Objective-C 更现代易学）
- 跨平台命令行工具
- 服务端 Swift 开发

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Swift 扩展 | [Xcode](https://developer.apple.com/xcode/)（仅 Mac）、Swift for Windows |
| Mac | [VS Code](https://code.visualstudio.com/) + Swift 扩展、Xcode（免费） | Xcode（Apple 官方 IDE，免费但仅 Mac） |
| Linux | [VS Code](https://code.visualstudio.com/) + Swift 扩展、Vim | Sourcegear Swift（社区工具链） |

**新手推荐：** 苹果开发用 Xcode（Mac 上免费下载，功能最全）。跨平台用 VS Code + Swift 扩展。注意：开发 iOS App 必须有一台 Mac。

## 4. 如何编辑、如何导出

### 环境准备

- **Mac**：去 App Store 安装 [Xcode](https://developer.apple.com/xcode/)（自带完整 Swift 工具链）
- **Linux**：从 [Swift.org](https://www.swift.org/install/linux/) 下载工具链安装
- **Windows**：从 [Swift.org](https://www.swift.org/install/windows/) 下载 Windows 版工具链

**验证安装：**
```bash
swift --version
```

### 如何编辑

**一个简单的 Swift 示例：**
```swift
// hello.swift
import Foundation

print("你好，Swift！")

let name = "小明"
print("欢迎，\(name)！")
```

注意 Swift 用 `let` 声明常量、`var` 声明变量，用 `\(变量)` 做字符串插值。

### 如何运行、如何导出

**方法一：直接运行单文件（Swift 解释器模式）**
```bash
swift hello.swift
```

**方法二：用 Swift Package Manager 管理项目**
```bash
# 创建新项目
swift package init --type executable
# 或用 Xcode: File > New > Project

# 编译并运行
swift run

# 编译发布版（优化）
swift build -c release

# 测试
swift test
```

**方法三：Xcode 中开发 iOS App**
1. Xcode → File → New → Project → App
2. 选 iOS，填写信息创建
3. 选模拟器或真机，按 Cmd+R 运行
4. Cmd+B 编译，Cmd+R 运行，Cmd+. 停止

**如何导出/打包：**
- **命令行工具**：`swift build -c release` 后产物在 `.build/release/`
- **iOS App**：Xcode → Product → Archive 归档，再导出 IPA 或上传到 App Store Connect

## 5. 常见报错与解决

### 问题1：Windows/Linux 上报 "swift: command not found"

**原因：** Swift 工具链没装，或 PATH 没配置。

**解决方法：**
1. 从 [Swift.org](https://www.swift.org/install/) 下载对应平台工具链
2. Windows 安装时勾选添加到 PATH，或手动把 Swift 安装目录的 `bin` 加到 PATH
3. 重启终端，用 `swift --version` 验证

### 问题2：Xcode 报 "Cannot find 'xxx' in scope"

**原因：** 用了未定义的标识符，常见于：
- 变量/函数名拼写错误
- 没导入对应模块（`import UIKit` 等）
- 作用域问题（局部变量在别处使用）

**解决方法：**
1. 检查拼写和大小写（Swift 区分大小写）
2. 在文件顶部 `import` 对应模块
3. 确认变量在当前作用域可见（如函数内的局部变量不能在外面用）
4. Xcode 的"Fix"建议（红色感叹号处点 Fix）

### 问题3：报错 "Value of optional type 'xxx?' must be unwrapped"

**原因：** Swift 的可选类型（Optional）必须解包后才能使用，这是 Swift 安全性的体现。

**解决方法：**
```swift
var name: String? = "小明"

// 方式1：可选绑定（推荐，安全）
if let n = name {
    print(n)
}

// 方式2：强制解包（必须确信非 nil，否则崩溃！）
print(name!)

// 方式3：空合运算符提供默认值
let n = name ?? "匿名"
```

### 问题4：报错 "Type 'XXX' does not conform to protocol 'YYY'"

**原因：** 类/结构体声明遵守某协议（如 `Equatable`、`Codable`），但没实现协议要求的方法/属性。

**解决方法：**
1. 查阅协议定义，补齐要求的方法/属性
2. 部分协议（如 `Codable`）只需声明遵守，编译器会自动合成实现
3. 确保方法签名（参数、返回类型）与协议完全一致

---

## 💡 小知识

- Swift 在 2014 年 WWDC 上发布，2015 年开源
- Swift 的吉祥物是燕子（tail），Logo 是只飞翔的鸟
- Swift 取代了有 30 多年历史的 Objective-C，成为苹果生态主力语言
- Swift 设计吸收了 Rust、Haskell、Python 等语言的优点，语法现代且安全

## 🔗 相关链接

- [Swift 官网](https://www.swift.org/)
- [Swift 官方文档（中文）](https://swiftgg.gitbook.io/swift/)
- [Xcode 官网](https://developer.apple.com/xcode/)
- [Apple 开发者官网](https://developer.apple.com/)
- [Swift Package Index](https://swiftpackageindex.com/)

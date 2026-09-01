# .dart 文件后缀详解

## 1. 文件定义 & 用途

.dart 是 **Dart 语言**的源代码文件后缀。Dart 是 Google 开发的现代化编程语言，语法类似 Java/C#/JavaScript，最大用途是配合 **Flutter 框架**开发跨平台移动应用（iOS + Android）、Web 应用和桌面应用。

简单来说，.dart 文件里写的是 Dart 代码，配合 Flutter 可以一套代码同时生成 iOS、Android、Web、Windows、Mac、Linux 六个平台的应用。

**主要用途：**
- **Flutter 移动应用开发**（Dart 最核心用途）
- Flutter Web 应用
- Flutter 桌面应用（Windows/Mac/Linux）
- 服务端开发（Dart 可写后端，有 Shelf 框架）
- 命令行工具

## 2. 适用场景

- 用 Flutter 开发跨平台移动 App
- 需要一套代码覆盖 iOS + Android + Web
- 移动端 UI 组件和页面逻辑开发
- Dart 后端 API 服务
- 学习 Dart 语言本身

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Dart 扩展、Android Studio | IntelliJ IDEA Ultimate + Flutter 插件 |
| Mac | [VS Code](https://code.visualstudio.com/) + Dart 扩展、Android Studio | IntelliJ IDEA Ultimate |
| Linux | [VS Code](https://code.visualstudio.com/) + Dart 扩展、Vim | IntelliJ IDEA Ultimate |

**新手推荐：** VS Code + Dart 和 Flutter 扩展，轻量好用。如果同时做 Android 原生调试，用 Android Studio（自带 Flutter 插件）。

## 4. 如何编辑、如何导出

### 环境准备

**安装 Flutter SDK（包含 Dart）：**
1. 去 [Flutter 官网](https://docs.flutter.dev/get-started/install) 下载对应平台 SDK
2. 解压后将 `flutter/bin` 添加到系统 PATH
3. Flutter SDK 自带 Dart，不需要单独安装

验证安装：
```bash
flutter --version
dart --version
```

**检查环境（重要）：**
```bash
# 检查所有依赖是否安装齐全
flutter doctor

# 根据提示安装缺失的组件（如 Android SDK、Xcode 等）
```

### 如何编辑

**一个简单的 Dart 示例：**
```dart
// hello.dart
void greet(String name) {
  print('你好，$name！');
}

void main() {
  greet('小明');

  // 列表和循环
  var fruits = ['苹果', '香蕉', '橙子'];
  for (var fruit in fruits) {
    print(fruit);
  }
}
```

**一个 Flutter 组件示例：**
```dart
// counter.dart
import 'package:flutter/material.dart';

class CounterPage extends StatefulWidget {
  @override
  _CounterPageState createState() => _CounterPageState();
}

class _CounterPageState extends State<CounterPage> {
  int _count = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('计数器')),
      body: Center(child: Text('$_count', style: TextStyle(fontSize: 48))),
      floatingActionButton: FloatingActionButton(
        onPressed: () => setState(() => _count++),
        child: Icon(Icons.add),
      ),
    );
  }
}
```

注意：Dart 用 `$变量名` 或 `${表达式}` 做字符串插值。Flutter 中一切皆 Widget，UI 通过嵌套 Widget 构建。

### 如何运行

**运行 Dart 脚本：**
```bash
# 直接运行
dart run hello.dart

# 或直接执行
dart hello.dart
```

**运行 Flutter 项目：**
```bash
# 创建新项目
flutter create my_app
cd my_app

# 运行到模拟器或连接的设备
flutter run

# 指定平台运行
flutter run -d chrome      # Web
flutter run -d windows     # Windows
```

### 如何导出（打包发布）

```bash
# 打包 Android APK
flutter build apk

# 打包 Android App Bundle（上传 Google Play）
flutter build appbundle

# 打包 iOS（需要 Mac + Xcode）
flutter build ios

# 打包 Web
flutter build web

# 打包 Windows
flutter build windows
```

打包产物在 `build/` 目录下。

## 5. 常见报错与解决

### 问题1：`flutter doctor` 报 Android toolchain 问题

**原因：** 没装 Android SDK 或 Android Studio，或没有接受许可协议。

**解决方法：**
1. 安装 [Android Studio](https://developer.android.com/studio)
2. 在 Android Studio 的 SDK Manager 中安装 Android SDK
3. 接受许可协议：
```bash
flutter doctor --android-licenses
```
4. 重新检查：`flutter doctor`

### 问题2：报错 "Error: Member not found: 'xxx'" 或 Widget 报红

**原因：** 使用了不存在的 Widget 或 API，或 Flutter 版本太旧/太新导致 API 变化。

**解决方法：**
1. 检查 Widget 名拼写
2. 确认 import 了 `package:flutter/material.dart`
3. 清理缓存重新构建：
```bash
flutter clean
flutter pub get
flutter run
```
4. 升级 Flutter 到最新稳定版：`flutter upgrade`

### 问题3：运行报错 "No connected devices" 或 "No supported devices found"

**原因：** 没有连接模拟器或真机。

**解决方法：**
1. 启动 Android 模拟器（在 Android Studio 的 Device Manager 中创建并启动）
2. 或用 USB 连接手机，开启开发者模式和 USB 调试
3. 查看可用设备：`flutter devices`
4. 如果只是想跑 Web 版：`flutter run -d chrome`

### 问题4：报错 "pub get failed" 或依赖下载缓慢（国内常见）

**原因：** Dart 的包仓库 pub.dev 在国外，国内访问慢。

**解决方法：**
```bash
# 设置国内镜像（推荐 FLUTTER_STORAGE_BASE_URL 和 PUB_HOSTED_URL）
# Windows（PowerShell）：
$env:PUB_HOSTED_URL = "https://pub.flutter-io.cn"
$env:FLUTTER_STORAGE_BASE_URL = "https://storage.flutter-io.cn"

# Mac/Linux：
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn

# 然后重新获取依赖
flutter pub get
```

---

## 💡 小知识

- Dart 语言由 Google 的 Lars Bak 和 Kasper Lund 设计，2011 年发布
- Dart 2.0 引入了强类型系统，之前是可选类型
- Flutter 最初基于 Dart 是因为 Dart 同时支持 JIT（开发热重载）和 AOT（发布时编译为原生代码）
- Flutter 的"热重载"（Hot Reload）让修改代码后一秒看到效果，这是 Flutter 开发体验的核心卖点
- Dart 的空安全（Null Safety）从 2.12 版本开始默认启用

## 🔗 相关链接

- [Dart 官网](https://dart.dev/)
- [Flutter 官网](https://flutter.dev/)
- [Dart 中文文档](https://dart.cn/)
- [Flutter 中文社区](https://flutter.cn/)
- [pub.dev 包仓库](https://pub.dev/)
- [VS Code Dart 扩展](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code)

# .kt 文件后缀详解

## 1. 文件定义 & 用途

.kt 是 **Kotlin** 编程语言的源代码文件后缀。Kotlin 由 JetBrains 在 2011 年发布，2017 年成为 Android 官方首选开发语言。它与 Java 100% 互通，语法更简洁安全，能跑在 JVM 上。

简单来说，.kt 文件就是用 Kotlin 写的程序代码，编译后产生 JVM 字节码（与 Java 共存），也可编译成 JavaScript 或原生二进制。

**主要用途：**
- Android App 开发（官方推荐语言）
- 后端服务开发（Spring Boot、Ktor 框架）
- 跨平台移动开发（Kotlin Multiplatform）
- 服务器端应用
- 脚本（.kts 文件）

## 2. 适用场景

- Android 应用开发（新项目几乎都用 Kotlin）
- 想要更简洁安全的 JVM 后端开发
- 与现有 Java 代码库混合开发
- 跨平台移动应用

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Kotlin 扩展、[Android Studio](https://developer.android.com/studio) | IntelliJ IDEA Ultimate |
| Mac | [VS Code](https://code.visualstudio.com/) + Kotlin 扩展、[Android Studio](https://developer.android.com/studio) | IntelliJ IDEA Ultimate |
| Linux | [VS Code](https://code.visualstudio.com/) + Kotlin 扩展、[Android Studio](https://developer.android.com/studio) | IntelliJ IDEA Ultimate |

**新手推荐：** Android 开发用 Android Studio（基于 IntelliJ，社区免费版 IDEA 也支持 Kotlin）。

## 4. 如何编辑、如何导出

### 环境准备

- **Android 开发**：装 [Android Studio](https://developer.android.com/studio)（自带 JDK 和 Kotlin 编译器）
- **通用 Kotlin**：装 JDK（[Adoptium](https://adoptium.net/)），然后用 IntelliJ IDEA Community 或命令行 Kotlin 编译器

**验证（命令行方式）：**
```bash
# 安装 Kotlin 编译器（独立工具链）
# 从 https://github.com/JetBrains/kotlin/releases 下载
kotlinc -version
```

### 如何编辑

**一个简单的 Kotlin 示例：**
```kotlin
// hello.kt
fun main() {
    println("你好，Kotlin！")

    val name = "小明"  // val 不可变，相当于 Java 的 final
    println("欢迎，$name！")
}
```

注意 Kotlin 用 `val` 声明不可变变量、`var` 声明可变变量，用 `$变量` 做字符串插值。`main()` 函数是入口，可以不带参数。

### 如何运行、如何导出

**方法一：命令行编译运行**
```bash
# 编译成 jar（需要 kotlin 的 jar 库）
kotlinc hello.kt -include-runtime -d hello.jar

# 运行 jar
java -jar hello.jar
```

**方法二：用 IntelliJ IDEA / Android Studio**
1. 创建 Kotlin 项目
2. 写 .kt 文件
3. 右键 → Run 'main()' 直接运行
4. Android 项目按 Run 按钮构建安装到设备/模拟器

**方法三：用 Gradle 管理项目**
```bash
# 初始化 Gradle 项目
gradle init --type kotlin-application

# 运行
./gradlew run

# 构建
./gradlew build
```

**如何导出：**
- **Android**：Android Studio → Build → Generate Signed Bundle/APK → 输出 .apk 或 .aab
- **JVM 应用**：`./gradlew build` 产物在 `build/libs/` 下的 .jar

## 5. 常见报错与解决

### 问题1：报错 "Unresolved reference: xxx"

**原因：** 用了未导入的类/函数，或依赖没配置好。

**解决方法：**
1. 在文件顶部用 `import` 导入对应类（IDE 会提示自动导入）
2. 检查 build.gradle 中是否声明了依赖
3. 同步 Gradle：`./gradlew --refresh-dependencies`
4. 重启 IDE 让索引刷新

### 问题2：报错 "Cannot find a method with a signature"

**原因：** 函数签名不匹配，常见于：
- 调用 Java 代码时类型不一致
- 参数数量/类型对不上
- 使用了未实现的接口

**解决方法：**
1. 检查方法名、参数类型和数量
2. Kotlin 调 Java 时注意可空性（Java 默认返回平台类型，Kotlin 需显式标注）
3. 用 IDE 的"查看定义"功能确认真实签名

### 问题3：编译时报 "warning: variable never used" 或代码有黄色警告

**原因：** Kotlin 编译器对潜在问题（未用变量、可空性、API 弃用）给出警告，虽不致命但建议处理。

**解决方法：**
1. 删掉或使用未用变量
2. 处理可空类型：`var x: String? = null` 必须判空后用
3. 按警告提示的"快速修复"操作（Alt+Enter）

### 问题4：运行时 "java.lang.NoClassDefFoundError"

**原因：** 编译时类在，但运行时类路径里没有这个类，常见于打成 jar 后缺少依赖。

**解决方法：**
1. 用 `-include-runtime` 编译（把 Kotlin 运行时打进去）
2. 用 Gradle 的 `shadowJar` 或 `application` 插件打 fat jar
3. 运行时确保 classpath 包含所有依赖

---

## 💡 小知识

- Kotlin 名字来自圣彼得堡附近的科特林岛（Kotlin Island）
- Kotlin 与 Java 完全互通：可以在同一项目混用 Java 和 Kotlin
- Kotlin 大幅减少样板代码，同样逻辑比 Java 简洁约 40%
- Kotlin 用空安全类型系统（`String` vs `String?`）从源头杜绝 NullPointerException

## 🔗 相关链接

- [Kotlin 官网](https://kotlinlang.org/)
- [Kotlin 官方文档（中文）](https://book.kotlincn.net/)
- [Android Studio 官网](https://developer.android.com/studio)
- [Kotlin GitHub](https://github.com/JetBrains/kotlin)
- [Kotlin Playground（在线运行）](https://play.kotlinlang.org/)

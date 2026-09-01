# .gradle 文件后缀详解

## 1. 文件定义 & 用途

.gradle 是 **Gradle 构建工具**的构建脚本文件后缀。Gradle 是一个基于 Groovy/Kotlin DSL 的自动化构建工具，主要用于 Java/Kotlin/Android 项目的构建管理，是 Maven 的现代替代品。

简单来说，.gradle 文件是 Gradle 的配置脚本，描述"项目依赖什么库、怎么编译、怎么打包、怎么发布"。它取代了传统的 `pom.xml`（Maven）和 `build.xml`（Ant），用更灵活的脚本语法来定义构建逻辑。

**主要用途：**
- **Android 应用构建**（Gradle 是 Android 官方构建工具）
- Java 和 Kotlin 项目构建管理
- Spring Boot 和企业级 Java 应用
- 多模块项目的构建管理
- 自定义构建流程和任务自动化
- 持续集成（CI/CD）中的构建步骤

## 2. 适用场景

- Android 应用开发（每个 Android 项目都用 Gradle）
- Java/Kotlin 后端项目（Spring Boot 等）
- 多模块大型项目构建
- 需要灵活自定义构建逻辑的场景
- 从 Maven 迁移到更灵活的构建工具

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Gradle 扩展、Notepad++ | IntelliJ IDEA（Community 免费）、Android Studio |
| Mac | [VS Code](https://code.visualstudio.com/) + Gradle 扩展、Vim | IntelliJ IDEA、Android Studio |
| Linux | [VS Code](https://code.visualstudio.com/) + Gradle 扩展、Vim | IntelliJ IDEA、Android Studio |

**新手推荐：** IntelliJ IDEA（Java 项目）或 Android Studio（Android 项目），它们内置了 Gradle 集成。VS Code + Gradle 扩展也可以。

## 4. 如何编辑、如何导出

### 环境准备

**安装 JDK（必须）：** Gradle 依赖 Java，至少需要 JDK 8 以上。

**安装 Gradle：**
- Windows：去 [Gradle 官网](https://gradle.org/install/) 下载，或 `scoop install gradle`
- Mac：`brew install gradle`
- Linux：通过 [SDKMAN](https://sdkman.io/) 安装：`sdk install gradle`

验证安装：
```bash
gradle --version
```

**注意：** Android Studio 自带 Gradle，不需要单独安装。大多数项目使用 `gradlew`（Gradle Wrapper）来确保团队成员使用相同的 Gradle 版本。

### 如何编辑

Gradle 有两种 DSL：Groovy DSL（`build.gradle`）和 Kotlin DSL（`build.gradle.kts`）。传统项目多用 Groovy DSL。

**一个简单的 build.gradle 示例（Groovy DSL）：**
```groovy
// build.gradle
plugins {
    id 'java'
    id 'application'
}

// 项目基本信息
group = 'com.example'
version = '1.0.0'

// Java 版本
java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

// 依赖仓库
repositories {
    mavenCentral()          // Maven 中央仓库
    google()                // Google 仓库（Android 项目）
}

// 项目依赖
dependencies {
    // 测试依赖
    testImplementation 'org.junit.jupiter:junit-jupiter:5.9.2'

    // 运行时依赖
    implementation 'com.google.guava:guava:32.0.0-jre'
}

// 应用主类
application {
    mainClass = 'com.example.Main'
}
```

**一个 Android build.gradle 示例：**
```groovy
// app/build.gradle (Android)
plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    namespace 'com.example.myapp'
    compileSdk 34

    defaultConfig {
        applicationId "com.example.myapp"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
    testImplementation 'junit:junit:4.13.2'
}
```

注意：Android 项目有项目级 `build.gradle` 和模块级 `build.gradle` 两个文件。

### 如何运行（构建项目）

**标准构建命令：**
```bash
# 编译项目
gradle build

# 运行应用（如果有 application 插件）
gradle run

# 运行测试
gradle test

# 清理构建
gradle clean
```

**使用 Gradle Wrapper（推荐）：**
```bash
# Wrapper 是项目自带的 Gradle 版本管理脚本
./gradlew build          # Linux/Mac
gradlew.bat build         # Windows

# 初始化 Wrapper（新项目）
gradle wrapper
```

### 如何导出（打包）

```bash
# 打包为 JAR
gradle jar

# 打包为可执行 JAR（application 插件）
gradle installDist

# Android 打包 APK
./gradlew assembleDebug       # Debug 版 APK
./gradlew assembleRelease     # Release 版 APK/AAB

# 发布到 Maven 仓库
gradle publish
```

## 5. 常见报错与解决

### 问题1：报错 "Could not resolve xxx"（依赖无法解析）

**原因：** 依赖库在仓库中找不到，或网络问题导致下载失败（国内常见）。

**解决方法：**
1. 检查依赖坐标（group:artifact:version）是否正确
2. 配置国内镜像（推荐阿里云）：
```groovy
// 在 build.gradle 或 settings.gradle 中添加
repositories {
    maven { url 'https://maven.aliyun.com/repository/public' }
    maven { url 'https://maven.aliyun.com/repository/google' }
    mavenCentral()
    google()
}
```
3. 清理 Gradle 缓存重新下载：`gradle --refresh-dependencies build`

### 问题2：报错 "Unsupported class file major version" 或 JDK 版本不匹配

**原因：** 项目要求的 JDK 版本和系统安装的 JDK 版本不一致。

**解决方法：**
1. 检查 Java 版本：`java -version`
2. 在 build.gradle 中指定正确的 Java 版本：
```groovy
java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}
```
3. 如果 Gradle 版本太旧不支持新 JDK，升级 Gradle：
```bash
gradle wrapper --gradle-version 8.5
```

### 问题3：报错 "Gradle build daemon disappeared" 或 Gradle 卡死

**原因：** 内存不足或 JVM 参数配置不对，Gradle daemon 进程崩溃。

**解决方法：**
1. 增加 Gradle JVM 内存（在 `gradle.properties` 中）：
```properties
org.gradle.jvmargs=-Xmx2048m -XX:MaxMetaspaceSize=512m
```
2. 停止所有 daemon：`gradle --stop`
3. 禁用 daemon（临时排查用）：`gradle build --no-daemon`

### 问题4：Android 项目报错 "SDK location not found"

**原因：** 没有配置 Android SDK 路径。

**解决方法：**
1. 在项目根目录的 `local.properties` 文件中指定 SDK 路径：
```properties
sdk.dir=C\:\\Users\\用户名\\AppData\\Local\\Android\\Sdk
# Mac: sdk.dir=/Users/用户名/Library/Android/sdk
# Linux: sdk.dir=/home/用户名/Android/Sdk
```
2. 或设置环境变量 `ANDROID_HOME` 指向 SDK 目录
3. 用 Android Studio 打开项目会自动配置

---

## 💡 小知识

- Gradle 由 Gradle Inc. 开发，2012 年发布 1.0 版本
- Gradle 结合了 Ant 的灵活性和 Maven 的依赖管理，同时用 Groovy/Kotlin 脚本代替了 XML
- Android 从 2013 年起官方采用 Gradle 作为构建工具，这是 Gradle 最大的用户群体
- Gradle 的构建速度优化（增量构建、构建缓存、Daemon）是它的核心优势
- `gradlew`（Gradle Wrapper）确保团队成员用同一个 Gradle 版本，即使没装 Gradle 也能用

## 🔗 相关链接

- [Gradle 官网](https://gradle.org/)
- [Gradle 中文文档](https://docs.gradle.org/current/userguide/userguide.html)
- [Android Studio 官网](https://developer.android.com/studio)
- [IntelliJ IDEA 官网](https://www.jetbrains.com/idea/)
- [Gradle 插件门户](https://plugins.gradle.org/)
- [阿里云 Maven 镜像](https://maven.aliyun.com/)

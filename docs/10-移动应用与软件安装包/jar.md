# .jar 文件后缀详解

## 1. 文件定义 & 用途

JAR（Java ARchive）是基于 ZIP 格式的 Java 平台归档文件格式。一个 JAR 文件将多个 Java 编译后的类文件（.class）、资源文件（图片、配置、属性文件）以及其他资源打包到一个文件中，并附带一个 META-INF/MANIFEST.MF 清单文件描述归档内容。

JAR 是 Java 应用程序和库分发的基本单位。它可以是可执行的应用（当 Main-Class 指定了入口类时，可用 `java -jar` 运行），也可以是供其他Java程序引用的库（如第三方API库）。JAR 文件还支持数字签名验证完整性和来源，这是企业级 Java 应用安全的重要组成部分。

## 2. 适用场景

- Java 桌面/命令行应用程序分发
- Java 第三方库分发（如 Apache Commons、Google Guava）
- Java Web 服务和中间件组件
- Android 应用开发的库依赖
- Minecraft Java 版的 Mod 和插件
- 企业级 Java 应用的打包部署

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 7-Zip/WinRAR（解压）、JDK（运行）、Eclipse（查看编辑） | IntelliJ IDEA、JProfiler（分析） |
| Mac | The Unarchiver、JDK、VS Code | IntelliJ IDEA、JProfiler |
| Linux | unzip、JDK、Eclipse | IntelliJ IDEA、JProfiler |
| 跨平台(网页) | - | - |

> 注意：JAR 需要安装 Java 运行时环境（JRE/JDK）才能运行。查看内容用任何解压软件即可，但运行需要 Java。

## 4. 如何编辑、如何导出

**查看方式：**
- 用 7-Zip / WinRAR / unzip 直接解压查看 JAR 内部文件结构。
- 使用 `jar tf 文件名.jar` 命令列出内容清单。
- 用 JD-GUI（Java Decompiler）将 .class 反编译为可读的 Java 源码。
- 用 IntelliJ IDEA 直接打开 JAR 查看反编译代码。

**运行方式：**
```bash
java -jar 应用名.jar          # 运行可执行JAR
java -cp 应用名.jar 主类全名   # 指定主类运行
```

**制作方式：**
- 命令行：`jar cvf 输出.jar -C 目录 .` 打包指定目录内容。
- Maven：`mvn package` 生成 target/ 下的 JAR。
- Gradle：`gradle jar` 生成 build/libs/ 下的 JAR。
- IntelliJ IDEA / Eclipse：右键项目 → Export → JAR file。

**设置可执行JAR的入口点：**
在 MANIFEST.MF 中指定：
```
Manifest-Version: 1.0
Main-Class: com.example.Main
```
或打包时指定：`jar cvfe 输出.jar com.example.Main -C 目录 .`

## 5. 常见报错与解决

**问题1：双击JAR无法运行或闪退**
- 原因：未安装 Java 运行时；或 .jar 文件关联到了错误的程序；MANIFEST.MF 未指定 Main-Class。
- 解决：安装 JDK/JRE（推荐 Temurin/Eclipse OpenJ9），在终端用 `java -jar 文件名.jar` 运行测试；右键 .jar → 打开方式 → 选择 javaw.exe（Windows）；检查 MANIFEST.MF 是否包含 Main-Class 属性。

**问题2：运行JAR时提示"NoClassDefFoundError"或"ClassNotFoundException"**
- 原因：JAR 依赖的其他库（第三方JAR）不在 classpath 中。
- 解决：用 `java -cp "app.jar;lib/*" 主类` 将依赖库加入 classpath；使用 fat-jar/uber-jar（将所有依赖打包进同一个JAR）避免依赖问题；使用 Maven/Gradle 的 shade/assembly 插件生成包含所有依赖的JAR。

**问题3：JAR 运行时提示"UnsupportedClassVersionError"**
- 原因：JAR 是用更高版本的 JDK 编译的，当前 JRE 版本过低无法运行。
- 解决：升级 JRE/JDK 到编译时使用的版本或更高；或重新用低版本 JDK 编译（`javac --release 8 ...`）；查看报错中提示的版本号对应关系（如 52=Java 8, 55=Java 11, 61=Java 17）。

**问题4：修改JAR内部文件后重新打包，签名失效或MANIFEST被破坏**
- 原因：手动修改破坏了 MANIFEST.MF 结构或签名校验值。
- 解决：使用 `jar` 命令重新打包确保 MANIFEST 正确生成；如果JAR有签名，修改后需用 `jarsigner` 重新签名；建议用 Maven/Gradle 构建而非手动改JAR。

---
## 小知识

JAR 格式发布于1996年随 Java 1.1 推出，其本质就是 ZIP 加上了 META-INF 目录和 MANIFEST.MF 文件——你甚至可以把 .jar 改成 .zip 直接用解压软件打开。JAR 这个名字是对 .war 和后面要说的 .war 等命名风格奠定了基础（Java的世界喜欢用 AR 结尾的缩写：JAR、WAR、EAR、RAR）。JAR 最重要的文件就是 MANIFEST.MF，它告诉JVM 这个JAR该用什么主类运行、包含什么扩展、签名信息等。有趣的是，Minecraft Java版的所有Mod本质都是 JAR 文件，所以 Minecraft 玩家其实就是JAR文件的"重度用户"。Java 9 引入的 JMOD 和 JLink 正在改变 Java 的打包方式，但 JAR 作为"最基础的 Java 归档"短期内不会被取代。

## 相关链接

- Oracle JAR 文件指南：https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jarGuide.html
- Adoptium（免费JDK）：https://adoptium.net/
- Maven 官网：https://maven.apache.org/
- JD-GUI（Java反编译器）：http://java-decompiler.github.io/
- IntelliJ IDEA：https://www.jetbrains.com/idea/

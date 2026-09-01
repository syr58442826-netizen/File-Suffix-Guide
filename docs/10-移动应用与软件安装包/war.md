# .war 文件后缀详解

## 1. 文件定义 & 用途

WAR（Web Application ARchive）是 Java EE/Jakarta EE 平台的 Web 应用程序归档格式，基于 ZIP/JAR 格式。一个 WAR 文件将一个完整的 Java Web 应用打包成一个文件，内部包含：编译后的Servlet类文件、JSP页面、HTML/CSS/JS等静态资源、配置文件（web.xml、application.yml等）、以及依赖的库JAR文件。

WAR 与 JAR 的核心区别在于用途：JAR 是通用 Java 库/应用，而 WAR 专门用于部署到 Java Web 容器/应用服务器（如 Tomcat、Jetty、WildFly、WebLogic）。WAR 不能直接用 `java -jar` 运行，必须部署到Servlet容器中才能执行。

## 2. 适用场景

- Java Web 应用打包分发与部署
- 部署到 Tomcat / Jetty / WildFly / WebLogic 等服务器
- 企业级 Web 应用的版本管理与发布
- Spring Boot 之前的传统 Spring Web 应用部署
- 遗留 Java EE 系统的维护与迁移
- 跨团队/跨组织的 Web 应用交付

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | 7-Zip/WinRAR（解压）、Apache Tomcat（部署运行） | IntelliJ IDEA Ultimate、JProfiler |
| Mac | The Unarchiver、Apache Tomcat | IntelliJ IDEA Ultimate |
| Linux | unzip、Apache Tomcat | IntelliJ IDEA Ultimate、JProfiler |
| 跨平台(网页) | - | - |

> 注意：WAR 文件不能直接双击运行。必须部署到 Java Web 容器（如 Tomcat）中才能执行。查看内容可用解压软件直接解压。

## 4. 如何编辑、如何导出

**查看方式：**
- 用 7-Zip / WinRAR / unzip 直接解压查看 WAR 内部结构。
- 典型 WAR 内部结构：
  ```
  WEB-INF/
    classes/        # 编译后的 .class 文件
    lib/           # 依赖的 .jar 库
    web.xml        # 部署描述符
  index.jsp        # JSP 页面
  static/          # 静态资源
  META-INF/
    MANIFEST.MF
  ```

**部署方式：**
- 将 WAR 文件复制到 Tomcat 的 `webapps/` 目录，Tomcat 启动时自动解压部署。
- 命令行部署（使用 Tomcat Manager）：
  ```
  curl -u 用户名:密码 -T 应用名.war "http://localhost:8080/manager/text/deploy?path=/app"
  ```
- 使用 Maven Cargo 插件自动部署。

**制作方式：**
- Maven：在 `pom.xml` 中设置 `<packaging>war</packaging>`，执行 `mvn package` 生成 target/ 下的 WAR。
- Gradle：应用 `war` 插件，执行 `gradle war` 生成 build/libs/ 下的 WAR。
- IntelliJ IDEA：配置 Web Application 工件（Artifact），构建生成 WAR。

## 5. 常见报错与解决

**问题1：部署到 Tomcat 后访问报404，应用未启动**
- 原因：WAR 部署失败，常见原因有 web.xml 配置错误、依赖库冲突、Servlet 版本不匹配。
- 解决：查看 Tomcat 日志（`logs/catalina.out` 或 `logs/localhost.YYYY-MM-DD.log`）定位具体错误；检查 web.xml 是否符合 Servlet 规范；确保 WAR 中的 lib/ 下没有与 Tomcat 自带库冲突的版本。

**问题2：部署后提示"UnsupportedClassVersionError"**
- 原因：WAR 中的 class 文件是用比 Tomcat 运行环境更高版本的 JDK 编译的。
- 解决：升级 Tomcat 使用的 JDK 到编译时版本或更高；或在 Maven 中用 `<maven.compiler.release>` 指定低版本编译；确认 Tomcat 版本与 JDK 版本兼容（如 Tomcat 10 需 JDK 11+）。

**问题3：WAR 文件过大，部署慢，包含大量重复依赖**
- 原因：WAR 的 WEB-INF/lib/ 中打包了大量第三方库，可能存在版本冲突。
- 解决：使用 Maven 的 `dependency:tree` 分析依赖树，排除重复依赖；使用 `<scope>provided</scope>` 将 Tomcat 自带的库排除；考虑迁移到 Spring Boot 的 fat-jar 方式（更现代，部署更简单）。

**问题4：WAR 部署后 JSP 页面报错或无法编译**
- 原因：Tomcat 版本太新（如 Tomcat 10+）使用了 Jakarta EE 命名空间（`jakarta.*`），而旧 WAR 使用 `javax.*`；或缺少 JSP 编译器依赖。
- 解决：Tomcat 9 使用 `javax.*`，Tomcat 10+ 使用 `jakarta.*`，需匹配版本；如果是 Tomcat 10+ 但 WAR 是旧版，需迁移代码包名或降级到 Tomcat 9；确认 Tomcat 中有 jasper（JSP引擎）模块。

---
## 小知识

WAR 格式在 Java EE 早期（1999年 Servlet 2.2 规范）就确立了。在过去20年间，WAR + Tomcat 是 Java Web 开发的标配。但近年来 Spring Boot 的崛起改变了部署方式——Spring Boot 倾向于打 fat-jar（包含嵌入Tomcat），用 `java -jar` 直接运行，不再需要外部部署到容器。尽管如此，大量遗留的企业系统和传统Java EE项目仍使用 WAR 部署，所以 WAR 仍然是Java Web运维的必备知识。WAR 的命名遵循 Java 归档的"AR"传统：JAR（通用归档）、WAR（Web归档）、EAR（企业归档，含多个WAR）、RAR（资源适配器归档）。一个 EAR 文件可以打包多个 WAR，用于企业级多模块应用部署。随着云原生和微服务兴起，WAR 正在向容器化（Docker/K8s）+ fat-jar 的方向迁移。

## 相关链接

- Java EE / Jakarta EE 教程：https://eclipse-ee4j.github.io/jakartaee-tutorial/
- Apache Tomcat 官网：https://tomcat.apache.org/
- Maven WAR 插件：https://maven.apache.org/plugins/maven-war-plugin/
- Spring Boot 部署指南：https://docs.spring.io/spring-boot/docs/current/reference/html/howto.html#howto.traditional-deployment
- WildFly（开源Java EE服务器）：https://www.wildfly.org/

# .jsp 文件后缀详解

## 1. 文件定义 & 用途

.jsp 是 **JavaServer Pages**（Java 服务器页面）文件的后缀。JSP 是 Java EE/Jakarta EE 平台的**服务端渲染**技术，允许在 HTML 中嵌入 Java 代码，在服务器上动态生成网页。

简单来说，.jsp 文件里混合了 HTML 和 Java 代码。用户请求页面时，JSP 引擎（如 Tomcat）把 .jsp 编译成 Servlet（Java 类），执行后生成 HTML 发送给浏览器。浏览器看到的只是渲染后的静态 HTML。

**主要用途：**
- Java Web 应用的动态页面
- 企业级管理系统的界面层
- 配合 Servlet 和 Java Bean 做 MVC 架构
- 数据库查询结果的动态展示
- 传统 Java EE Web 项目

## 2. 适用场景

- 使用 Java 技术栈的 Web 应用开发
- 企业内部管理系统和门户
- 需要服务端生成 HTML 的 Java 项目
- 维护传统 JSP 项目
- 配合 Spring MVC 做 View 层

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Java 扩展、Notepad++ | IntelliJ IDEA Ultimate、Eclipse EE |
| Mac | [VS Code](https://code.visualstudio.com/) + Java 扩展、Vim | IntelliJ IDEA Ultimate、Eclipse EE |
| Linux | [VS Code](https://code.visualstudio.com/) + Java 扩展、Vim | IntelliJ IDEA Ultimate、Eclipse EE |

**新手推荐：** IntelliJ IDEA Community（免费版）可以编辑 Java 代码，但 JSP 调试需要 Ultimate 版。Eclipse IDE for Enterprise Java Developers（免费）是 JSP 开发的经典选择。

## 4. 如何编辑、如何导出

### 环境准备

**安装 JDK：** JSP 是 Java 技术，需要先安装 JDK 8 以上版本。验证：`java -version`

**安装 Servlet 容器（Web 服务器）：**
- **Apache Tomcat**（最流行）：去 [Tomcat 官网](https://tomcat.apache.org/) 下载，解压即可用
- 或用 Eclipse/IntelliJ IDEA 内置的 Tomcat 集成

验证 Tomcat：
```bash
# 启动 Tomcat
cd tomcat/bin
./startup.sh        # Linux/Mac
startup.bat         # Windows

# 访问 http://localhost:8080 确认正常运行
```

### 如何编辑

**一个简单的 JSP 页面示例：**
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>欢迎页面</title>
</head>
<body>
    <h1>你好，<%= request.getParameter("name") != null ? request.getParameter("name") : "访客" %>！</h1>

    <%
        // 在 <% %> 中写 Java 代码（Scriptlet）
        String[] fruits = {"苹果", "香蕉", "橙子"};
        for (String fruit : fruits) {
            out.println("<p>" + fruit + "</p>");
        }
    %>

    <p>当前时间：<%= new java.util.Date() %></p>
</body>
</html>
```

JSP 的几种代码元素：
- `<%@ page %>` — 页面指令（设置编码、语言等）
- `<% ... %>` — Scriptlet，写 Java 代码块
- `<%= ... %>` — 表达式，输出值到 HTML
- `<%-- ... --%>` — 注释
- `${表达式}` — EL 表达式，更简洁的数据访问方式

**使用 JSTL 标签库的示例（推荐，避免在 JSP 中写 Java）：**
```jsp
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:forEach var="fruit" items="${fruits}">
    <p>${fruit}</p>
</c:forEach>
<c:if test="${not empty userName}">
    <p>欢迎回来，${userName}！</p>
</c:if>
```

### 如何运行

**方法一：用 Tomcat 直接运行**
1. 将 .jsp 文件放到 Tomcat 的 `webapps/ROOT/` 目录下
2. 启动 Tomcat
3. 浏览器访问 `http://localhost:8080/hello.jsp`

**方法二：用 IDE 运行**
1. 在 Eclipse/IntelliJ 中配置 Tomcat Server
2. 创建 Dynamic Web Project 或 Web Application
3. 将 .jsp 放到 `webapp/` 或 `WebContent/` 目录
4. 运行项目，IDE 自动启动 Tomcat 并打开浏览器

**方法三：用 Spring Boot 内嵌容器运行**
```bash
# Spring Boot 内嵌 Tomcat，不需要单独安装
# 把 .jsp 放到 src/main/webapp/WEB-INF/jsp/ 目录
# 运行项目
mvn spring-boot:run
```

### 如何导出（打包部署）

```bash
# 打包为 WAR 文件
mvn clean package        # Maven 项目
# 或
gradle war               # Gradle 项目

# 部署到 Tomcat：
# 将 .war 文件复制到 Tomcat 的 webapps/ 目录
# Tomcat 启动后自动解压部署
cp myapp.war tomcat/webapps/
```

## 5. 常见报错与解决

### 问题1：浏览器访问 .jsp 显示源代码而不是渲染后的 HTML

**原因：** JSP 没有被正确编译和执行，可能是 Tomcat 没有正确配置或没有安装 Servlet/JSP 引擎。

**解决方法：**
1. 确认 Tomcat 已正常启动
2. 检查 URL 是否正确（应该是 `http://localhost:8080/xxx.jsp`）
3. 确认 .jsp 文件在正确的目录（webapps/ROOT/ 或项目的 webapp 目录）
4. 检查 Tomcat 的 conf/web.xml 中 JSP servlet 映射是否正常

### 问题2：报错 "HTTP Status 500 - Unable to compile class for JSP"

**原因：** JSP 代码中有 Java 语法错误，编译成 Servlet 时失败。

**解决方法：**
1. 查看报错信息中的具体行号和错误描述
2. 检查 `<% %>` 中的 Java 代码语法是否正确
3. 确认 JDK 版本与 Tomcat 要求的版本匹配
4. 清理 Tomcat 的 work 目录（缓存的编译文件可能过期）：
```bash
# 删除编译缓存
rm -rf tomcat/work/Catalina/*
# 然后重启 Tomcat
```

### 问题3：中文乱码

**原因：** 编码设置不一致，JSP 文件编码、页面编码声明、服务器响应编码三者不统一。

**解决方法：**
1. 在 JSP 页面顶部设置编码（必须有）：
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
```
2. 确认 .jsp 文件本身保存为 UTF-8 编码
3. 在 HTML head 中声明编码：`<meta charset="UTF-8">`
4. 如果是 POST 表单乱码，在接收数据的 Servlet 中设置：
```java
request.setCharacterEncoding("UTF-8");
```

### 问题4：报错 "ClassNotFoundException" 或 "NoClassDefFoundError"

**原因：** JSP 中使用的 Java 类找不到，可能是缺少依赖 JAR 包或类路径配置问题。

**解决方法：**
1. 确认依赖的 JAR 包已放到 `WEB-INF/lib/` 目录
2. 用 Maven/Gradle 管理依赖，确认 scope 设置正确
3. 重新打包部署
4. 检查 import 语句是否正确，类名是否拼写正确

---

## 💡 小知识

- JSP 由 Sun Microsystems（后被 Oracle 收购）开发，1999 年发布，是 ASP（微软）的 Java 对标产品
- JSP 第一次访问时会编译成 Servlet 的 .java 文件再编译成 .class，所以首次访问较慢，后续很快
- 现代 Java Web 开发推荐用 Spring Boot + Thymeleaf 模板引擎，不再推荐直接在 JSP 中写 Java 代码
- JSP 的 EL 表达式（`${}`）和 JSTL 标签库是推荐用法，替代 Scriptlet（`<% %>`），让页面更干净
- Jakarta EE（原 Java EE）已移交 Eclipse 基金会管理，包名从 `javax.servlet` 变为 `jakarta.servlet`

## 🔗 相关链接

- [JSP 教程（菜鸟教程）](https://www.runoob.com/jsp/jsp-tutorial.html)
- [Apache Tomcat 官网](https://tomcat.apache.org/)
- [Jakarta EE 官网](https://jakarta.ee/)
- [IntelliJ IDEA 官网](https://www.jetbrains.com/idea/)
- [Eclipse IDE](https://www.eclipse.org/downloads/packages/)
- [Spring Boot 官网](https://spring.io/projects/spring-boot)

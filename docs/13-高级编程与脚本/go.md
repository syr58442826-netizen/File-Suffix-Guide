# .go 文件后缀详解

## 1. 文件定义 & 用途

.go 是 **Go 语言**（又称 Golang）的源代码文件后缀。Go 是 Google 在 2009 年开源的静态编译型语言，主打**简单、高效、强大的原生并发支持**。

简单来说，.go 文件就是用 Go 语言写的程序代码，用 `go` 工具链编译后会生成一个独立的可执行文件（无需安装运行时，直接运行）。

**主要用途：**
- 云原生与后端服务（Docker、Kubernetes、etcd 都用 Go 写）
- 高并发网络服务（goroutine 让并发编程异常简单）
- 命令行工具（编译成单文件，跨平台分发方便）
- 微服务、API 网关
- 运维工具和 DevOps 工具链

## 2. 适用场景

- 编写高性能 Web 服务和 API
- 需要高并发处理（如聊天、推送、实时数据）
- 开发命令行工具（CLI）
- 云原生、容器化相关开发
- 系统级工具和中间件

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Go 扩展、Vim | GoLand（JetBrains） |
| Mac | [VS Code](https://code.visualstudio.com/) + Go 扩展、Vim | GoLand |
| Linux | [VS Code](https://code.visualstudio.com/) + Go 扩展、Vim | GoLand |

**新手推荐：** VS Code + 官方 Go 扩展（安装时会自动拉取相关工具链）。专业开发可上 GoLand。

## 4. 如何编辑、如何导出

### 环境准备

**安装 Go：**
1. 去 [Go 官网下载页](https://go.dev/dl/) 下载对应平台安装包
2. Windows/Mac 直接下一步安装，Linux 解压到 `/usr/local/go`
3. 安装后会自动配置 `go` 命令到 PATH
4. 验证安装：`go version`

**设置模块代理（国内必做，否则下载依赖会失败）：**
```bash
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
```

### 如何编辑

**一个简单的 Go 示例：**
```go
// hello.go
package main

import "fmt"

func main() {
    fmt.Println("你好，Go！")
}
```

注意：Go 文件第一行必须声明 `package`，可执行程序的包名必须是 `main`，并且要有 `func main()` 作为入口。

### 如何运行、如何导出

**方法一：直接运行（不生成可执行文件，开发时最常用）**
```bash
go run hello.go
```

**方法二：编译成可执行文件**
```bash
# 编译（生成 hello.exe / hello）
go build hello.go

# 跨平台编译（Go 的杀手锏功能！）
# 在 Windows 上编译 Linux 版
set GOOS=linux
set GOARCH=amd64
go build hello.go

# Mac/Linux 用 export
export GOOS=linux
export GOARCH=amd64
go build hello.go
```

**方法三：初始化项目模块**
```bash
# 初始化项目（生成 go.mod 依赖管理文件）
go mod init myproject

# 拉取第三方依赖
go get github.com/gin-gonic/gin

# 运行项目
go run .
```

## 5. 常见报错与解决

### 问题1：`go run` 时报 "go: go.mod file not found"

**原因：** 当前目录没有 go.mod 文件，Go 默认开启了模块模式。

**解决方法：**
```bash
# 在项目根目录初始化模块
go mod init 你的项目名

# 然后再运行
go run .
```

### 问题2：`go get` 下载依赖超时或失败（国内常见）

**原因：** 默认从 golang.org 拉取，国内网络访问不畅。

**解决方法：**
```bash
# 设置国内代理（七牛云提供）
go env -w GOPROXY=https://goproxy.cn,direct

# 或者用阿里云代理
go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/,direct

# 再重新拉取
go get github.com/gin-gonic/gin
```

### 问题3：报 "syntax error: non-declaration statement outside function body"

**原因：** 把代码写在了函数外面。Go 的执行语句必须写在函数内部，函数外面只能声明包、import、变量/常量/类型声明、函数定义。

**解决方法：** 把执行语句移到 `func main()` 里。

```go
// 错误：print 不能写在函数外
package main
import "fmt"
fmt.Println("hi")  // 报错

// 正确
package main
import "fmt"
func main() {
    fmt.Println("hi")
}
```

### 问题4：报 "imported and not used" 或 "declared and not used"

**原因：** Go 强制要求导入的包和声明的变量都必须被使用，否则编译失败。这是 Go 的设计哲学之一。

**解决方法：**
1. 删掉没用到的 import
2. 对于暂时不用的变量，用 `_ = 变量名` 标记为"故意忽略"，或用下划线 `_` 接收
3. 对于只想执行副作用的导入，用空白标识符：`import _ "github.com/lib/pq"`

---

## 💡 小知识

- Go 语言的吉祥物是一只地鼠（Gopher），所以 Go 程序员常自称为 Gopher
- Go 没有 class 关键字，用 struct + method 实现面向对象，没有继承
- Go 的 goroutine 非常轻量，一个程序可以轻松开几十万个 goroutine
- Go 编译产物是单一可执行文件，没有依赖地狱问题，部署极其简单

## 🔗 相关链接

- [Go 官网](https://go.dev/)
- [Go 官方教程（A Tour of Go）](https://go.dev/tour/)
- [Go 语言中文网](https://studygolang.com/)
- [GoLand 官网](https://www.jetbrains.com/go/)
- [Go 模块代理（国内）](https://goproxy.cn/)

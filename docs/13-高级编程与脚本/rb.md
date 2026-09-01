# .rb 文件后缀详解

## 1. 文件定义 & 用途

.rb 是 **Ruby** 编程语言的源代码文件后缀。Ruby 是日本人松本行弘（Matz）在 1995 年开发的动态脚本语言，设计哲学是"让程序员快乐"。它因 **Ruby on Rails** 框架而闻名全球，曾撑起大量早期互联网创业公司。

简单来说，.rb 文件就是用 Ruby 语言写的程序代码，通过 Ruby 解释器运行。

**主要用途：**
- Web 后端开发（Ruby on Rails 框架）
- 快速原型开发和产品迭代
- 自动化脚本和运维工具
- DevOps 工具（如 Chef、Vagrant 用 Ruby）
- 领域特定语言（DSL）编写

## 2. 适用场景

- 需要快速开发上线 Web 应用（Rails 全栈开发极快）
- 编写自动化脚本
- 生态里已有成熟 Ruby 工具链的场景
- 喜欢优雅、接近自然语言语法风格的开发者

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + Ruby 扩展、Notepad++ | RubyMine（JetBrains） |
| Mac | [VS Code](https://code.visualstudio.com/) + Ruby 扩展、Vim | RubyMine |
| Linux | [VS Code](https://code.visualstudio.com/) + Ruby 扩展、Vim | RubyMine |

**新手推荐：** Mac/Linux 用 rbenv 装 Ruby + VS Code。Windows 推荐 RubyInstaller。

## 4. 如何编辑、如何导出

### 环境准备

**安装 Ruby：**
- **Windows**：去 [RubyInstaller](https://rubyinstaller.org/) 下载带 DevKit 的安装包，一键安装
- **Mac**：系统自带 Ruby（但版本旧），建议用 Homebrew 装新版 `brew install ruby`，或用 rbenv 管理多版本
- **Linux**：用包管理器 `sudo apt install ruby` 或用 rbenv/rvm

**验证安装：**
```bash
ruby --version
gem --version   # gem 是 Ruby 的包管理器
```

**换源（国内必备）：**
```bash
# 换用国内镜像源，否则 gem install 会很慢
gem sources --remove https://rubygems.org/
gem sources -a https://gems.ruby-china.com/
```

### 如何编辑

**一个简单的 Ruby 示例：**
```ruby
# hello.rb
puts "你好，Ruby！"

name = gets.chomp
puts "欢迎，#{name}！"
```

### 如何运行、如何导出

**方法一：命令行运行**
```bash
ruby hello.rb

# 交互式运行（IRB）
irb
# 然后直接输入 Ruby 代码
```

**方法二：Rails 项目（Web 开发）**
```bash
# 安装 Rails
gem install rails

# 创建新项目
rails new myapp
cd myapp

# 启动 Web 服务器
rails server
# 访问 http://localhost:3000
```

**方法三：用 Bundler 管理项目依赖**
```bash
# 在项目根目录创建 Gemfile，声明依赖
bundle install   # 安装依赖
bundle exec ruby app.rb   # 在依赖环境下运行
```

**如何导出/打包：** Ruby 是解释型语言，通常不编译成二进制。Web 项目直接部署到服务器即可。如果需要单文件分发，可用 `rubocop`/`ocra`（Windows）等工具，但实际很少用。

## 5. 常见报错与解决

### 问题1：Windows 上提示 "ruby 不是内部或外部命令"

**原因：** Ruby 没装，或 PATH 没配置好。

**解决方法：**
1. 用 [RubyInstaller](https://rubyinstaller.org/) 重装，安装时勾选"Add Ruby executables to your PATH"
2. 或手动把 Ruby 安装目录（如 `C:\Ruby31-x64\bin`）加到系统环境变量 PATH
3. 重启终端后用 `ruby --version` 验证

### 问题2：`gem install` 卡住或报错 "Too many connection resets"

**原因：** 默认从 rubygems.org 拉取，国内访问慢或不稳定。

**解决方法：**
```bash
# 换国内镜像
gem sources --remove https://rubygems.org/
gem sources -a https://gems.ruby-china.com/

# 验证源
gem sources -l

# 再重新安装
gem install rails
```

如果用 Bundler，把 Gemfile 第一行改成：
```
source 'https://gems.ruby-china.com/'
```

### 问题3：报 "Gem::ConflictError" 或版本冲突

**原因：** 不同 gem 依赖同一个库的不同版本，互相冲突。

**解决方法：**
```bash
# 用 Bundler 隔离依赖（推荐）
bundle install

# 在隔离环境运行
bundle exec rails server

# 如果 Bundler 也冲突，尝试更新依赖
bundle update
```

### 问题4：报 "NameError: undefined local variable or method"

**原因：** 用了未定义的变量/方法，或拼写错误。Ruby 不需要声明变量，但首次赋值前使用会报错。

**解决方法：**
1. 检查变量名拼写
2. 确认变量已先赋值再用
3. Ruby 用 `@` 表示实例变量、`@@` 表示类变量、`$` 表示全局变量，注意前缀
4. 方法调用可以省略括号，但有时会引发歧义，建议有参数时加括号

---

## 💡 小知识

- Ruby 的作者松本行弘（Matz）的名言："我要让 Ruby 比 Perl 更强大，比 Python 更面向对象"
- Ruby on Rails 在 2004 年发布时，用 15 分钟建博客的演示震惊了整个 Web 开发圈
- GitHub、Shopify、Airbnb 早期都是用 Ruby on Rails 起家的
- Ruby 的语法允许很多"语法糖"，同一件事常有多种写法，社区推崇"Ruby way"

## 🔗 相关链接

- [Ruby 官网](https://www.ruby-lang.org/)
- [Ruby 中文官网](https://www.ruby-lang.org/zh_cn/)
- [Ruby on Rails 官网](https://rubyonrails.org/)
- [RubyGems 中国镜像](https://gems.ruby-china.com/)
- [RubyMine 官网](https://www.jetbrains.com/ruby/)

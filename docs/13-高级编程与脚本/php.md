# .php 文件后缀详解

## 1. 文件定义 & 用途

.php 是 **PHP** 编程语言的源代码文件后缀。PHP 是一种服务器端脚本语言，专为 Web 开发而生，至今仍是互联网上最常见的后端语言之一（WordPress、Laravel 生态庞大）。

简单来说，.php 文件可以同时包含 HTML 和 PHP 代码，PHP 代码用 `<?php ?>` 标签包裹。放在支持 PHP 的 Web 服务器上，访问时会被服务器解析后输出 HTML 给浏览器。

**主要用途：**
- Web 后端开发（Laravel、Symfony、ThinkPHP 框架）
- 内容管理系统（WordPress、Drupal、Joomla）
- 电商网站（Magento、WooCommerce）
- API 接口开发
- 命令行脚本

## 2. 适用场景

- 搭建动态网站和 Web 应用
- 使用 WordPress 等 CMS 建站
- 中小型企业的 Web 后端
- 快速开发 API 接口
- 已有 PHP 生态的项目维护

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + PHP 扩展、Notepad++ | PhpStorm（JetBrains） |
| Mac | [VS Code](https://code.visualstudio.com/) + PHP 扩展、Vim | PhpStorm |
| Linux | [VS Code](https://code.visualstudio.com/) + PHP 扩展、Vim | PhpStorm |

**新手推荐：** VS Code + PHP Intelephense 扩展。专业开发推荐 PhpStorm（PHP 开发者公认最好用的 IDE）。

## 4. 如何编辑、如何导出

### 环境准备

PHP 可以装在本地跑命令行，也可以用集成环境一键搭 Web 服务器。

**方式一：本地装 PHP（命令行用）**
- **Windows**：去 [windows.php.net](https://windows.php.net/download/) 下载，解压并配置 PATH
- **Mac**：系统自带 PHP（较旧），推荐用 Homebrew `brew install php`
- **Linux**：`sudo apt install php` 或编译安装

验证：`php --version`

**方式二：用集成环境（Web 开发推荐，一键装 Apache/Nginx + PHP + MySQL）**
- **Windows**：XAMPP、phpStudy、WampServer
- **Mac**：MAMP、XAMPP
- **Linux**：XAMPP 或手动装 LAMP/LNMP

### 如何编辑

**一个简单的 PHP 示例：**
```php
<?php
// hello.php
echo "你好，PHP！\n";

$name = "小明";
echo "欢迎，{$name}！\n";

// 和 HTML 混写的示例
?>
<!DOCTYPE html>
<html>
<body>
    <h1><?php echo "这是网页标题"; ?></h1>
</body>
</html>
```

### 如何运行、如何导出

**方法一：命令行运行（CLI 模式）**
```bash
php hello.php

# 启动内置 Web 服务器（开发调试神器，无需配 Apache）
php -S localhost:8000
# 然后浏览器访问 http://localhost:8000/hello.php
```

**方法二：放到集成环境根目录运行**
1. 启动 XAMPP/WampServer/MAMP
2. 把 .php 文件放到 `htdocs`（XAMPP）或 `www`（WampServer）目录
3. 浏览器访问 `http://localhost/文件名.php`

**方法三：用 Composer 管理项目依赖（现代 PHP 标准）**
```bash
# 安装 Composer（PHP 的包管理器，类似 npm）
# 见 https://getcomposer.org/

# 创建新项目（以 Laravel 框架为例）
composer create-project laravel/laravel myapp
cd myapp

# 启动开发服务器
php artisan serve
```

**如何导出/部署：** PHP 不需要编译成二进制。部署时把 .php 文件和资源文件上传到支持 PHP 的 Web 服务器即可。注意用 `composer install --no-dev --optimize-autoloader` 优化依赖加载。

## 5. 常见报错与解决

### 问题1：浏览器访问 .php 文件显示源代码或提示下载文件

**原因：** Web 服务器没有装 PHP 解析器，或没有正确配置 PHP 模块，导致把 .php 当成普通文件返回。

**解决方法：**
1. 确认装了 PHP（`php --version`）
2. 用集成环境（XAMPP 等）的话，确保 Apache 已启动
3. 检查 Apache 配置是否加载了 PHP 模块（`LoadModule php_module`）
4. 确认文件名是 `.php` 后缀且放在 Web 根目录（如 htdocs）
5. 通过 `http://localhost/` 访问，而不是双击文件直接打开

### 问题2：报错 "Fatal error: Uncaught Error: Class 'xxx' not found"

**原因：** 类没有自动加载，或没安装对应的依赖包。

**解决方法：**
```bash
# 现代项目用 Composer 自动加载
composer install

# 如果用了类，但没引入，在文件顶部 use 引入
# use Vendor\Package\ClassName;
```

### 问题3：报错 "Call to undefined function" 或方法不存在

**原因：** 调用了未定义的函数/方法，常见于：
- 没开启某个 PHP 扩展（如 mysqli、mbstring）
- 版本太低，函数在新版才有

**解决方法：**
1. 检查 PHP 版本是否满足要求（`php --version`）
2. 在 php.ini 开启对应扩展（去掉 `;extension=xxx` 前面的分号）
3. 重启 Web 服务器使配置生效

### 问题4：报 "syntax error, unexpected end of file" 或中文乱码

**原因1：** `<?php` 标签没闭合，或者用了短标签 `<?` 但服务器没开 `short_open_tag`。
**原因2：** 文件编码不是 UTF-8 或有 BOM 头导致乱码。

**解决方法：**
1. 统一用 `<?php` 完整标签，不依赖短标签
2. 文件保存为 UTF-8（无 BOM）
3. 检查大括号、分号是否成对闭合
4. 在 php.ini 设置 `default_charset = "UTF-8"`

---

## 💡 小知识

- PHP 原名 "Personal Home Page"，现在递归命名为 "PHP: Hypertext Preprocessor"
- 全球约 70% 的网站后端用的是 PHP，WordPress 占据超过 40% 的网站
- PHP 8 引入了 JIT 编译器，性能比老版本有质的飞跃
- Facebook 早期用 PHP 起家，后来还开发了 PHP 的衍生语言 Hack

## 🔗 相关链接

- [PHP 官网](https://www.php.net/)
- [PHP 中文手册](https://www.php.net/manual/zh/)
- [Composer 官网](https://getcomposer.org/)
- [Laravel 框架官网](https://laravel.com/)
- [PhpStorm 官网](https://www.jetbrains.com/phpstorm/)
- [XAMPP 官网](https://www.apachefriends.org/)

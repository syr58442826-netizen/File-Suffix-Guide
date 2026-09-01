# .sh 文件后缀详解

## 1. 文件定义 & 用途

.sh 是 **shell（壳）** 的缩写，是 Unix/Linux/Mac 系统下的 Shell 脚本文件。它包含一系列 Shell 命令，类似于 Windows 下的 .bat 批处理文件。

简单来说，.sh 文件就是把 Linux/Mac 命令写在一个文件里，一次执行全部命令的脚本文件。最常见的是 Bash 脚本。

**主要用途：**
- 系统管理和自动化运维
- 服务器部署和配置
- 批量文件处理
- 数据备份和恢复
- 软件开发中的构建脚本

## 2. 适用场景

- Linux 服务器运维自动化
- 软件开发的构建和部署脚本
- 数据批量处理
- 系统监控和告警
- 定时任务（配合 crontab）
- Mac 系统下的自动化操作

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/)、[Notepad++](https://notepad-plus-plus.org/)、Git Bash | Sublime Text |
| Mac | 终端（系统自带）、[VS Code](https://code.visualstudio.com/)、TextMate | - |
| Linux | Vim、Gedit、Nano、[VS Code](https://code.visualstudio.com/) | - |

**运行说明：**
- Linux 和 Mac 原生支持 .sh 脚本（通过 Bash/Zsh 等 Shell 执行）
- Windows 需要安装 Git Bash、WSL（Windows 子系统 for Linux）或 Cygwin 才能运行

## 4. 如何编辑、如何导出

### 如何编辑

**方法一：用终端编辑器（Vim/Nano）**
```bash
# 使用 Nano（简单）
nano 脚本名.sh

# 使用 Vim
vim 脚本名.sh
```

**方法二：用 VS Code 编辑（推荐）**
- 语法高亮、代码补全
- 集成终端可以直接运行调试
- 安装 "ShellCheck" 扩展可以检查脚本错误

**一个简单的 .sh 示例：**
```bash
#!/bin/bash
# 这是注释，不会被执行

echo "你好，这是我的第一个 Shell 脚本！"
echo "当前用户是：$USER"
echo "当前目录是：$(pwd)"
echo "今天是：$(date +%Y年%m月%d日)"
```

### 如何运行

**方法一：直接运行（需要执行权限）**
```bash
# 1. 添加执行权限（第一次运行前需要）
chmod +x 脚本名.sh

# 2. 运行
./脚本名.sh
```

**方法二：通过解释器运行（不需要执行权限）**
```bash
bash 脚本名.sh
# 或者
sh 脚本名.sh
# 或者
zsh 脚本名.sh
```

**方法三：带参数运行**
```bash
./脚本名.sh 参数1 参数2
# 脚本中用 $1、$2 获取参数
```

### 如何导出/保存

- 用任意文本编辑器编写
- 保存时后缀为 .sh
- 第一行建议写 `#!/bin/bash`（称为 shebang），指定解释器
- 注意使用 Unix 风格的换行符（LF），不要用 Windows 风格（CRLF）

## 5. 常见报错与解决

### 问题1：提示 "Permission denied"（权限不足）

**原因：** 脚本没有执行权限。

**解决方法：**
```bash
# 添加执行权限
chmod +x 脚本名.sh

# 然后再运行
./脚本名.sh
```

### 问题2：提示 "bad interpreter: No such file or directory"

**原因：** 通常是因为脚本是在 Windows 下编辑的，换行符是 CRLF 而不是 Unix 的 LF。

**解决方法：**
```bash
# 方法一：使用 dos2unix 转换
dos2unix 脚本名.sh

# 方法二：使用 sed 替换
sed -i 's/\r$//' 脚本名.sh

# 方法三：在 VS Code 中点击右下角的 CRLF，切换为 LF
```

### 问题3：提示 "command not found"（命令未找到）

**原因：** 脚本中的命令不存在，或者命令路径没有配置。

**解决方法：**
1. 检查命令拼写是否正确
2. 确认该命令是否已安装，例如 `which 命令名` 查看是否存在
3. 如果是自定义命令，使用完整路径，例如 `/usr/local/bin/命令名`
4. 在脚本中设置 PATH 环境变量：`export PATH=$PATH:/自定义路径`

### 问题4：中文显示乱码

**原因：** 终端编码和脚本编码不一致。

**解决方法：**
1. 在脚本开头设置编码：
   ```bash
   export LANG=zh_CN.UTF-8
   ```
2. 确认终端使用 UTF-8 编码
3. 保存脚本时选择 UTF-8 编码

---

## 安全风险

Shell 脚本功能强大，可以控制系统的方方面面，存在较大安全风险：

1. **不要运行来源不明的 .sh 脚本**，它可能删除数据、植入后门、窃取信息
2. **先看内容再运行**：用 `cat 脚本名.sh` 或编辑器查看脚本内容
3. **root 权限慎用**：不要轻易用 `sudo` 运行不了解的脚本
4. **注意危险命令**：`rm -rf /`（删除所有文件）、`mkfs`（格式化磁盘）等命令极其危险
5. **网上的一键安装脚本要谨慎**：很多教程提供 `curl xxx | bash` 的安装方式，运行前要确认来源可信
6. **路径安全**：脚本中使用 `rm` 等删除命令时，一定要确认路径正确，最好加判断
7. **输入验证**：如果脚本接收用户输入，要做好输入验证，防止命令注入

## 💡 小知识

- `#!/bin/bash` 这行叫 shebang（释伴行），告诉系统用哪个解释器来执行脚本
- `.sh` 后缀不是必须的，只要有 shebang 和执行权限，任何文件名都可以当脚本运行
- 可以用 `shellcheck` 工具检查脚本中的常见错误和不规范写法
- Shell 脚本中，`$?` 表示上一条命令的退出状态（0 表示成功，非 0 表示失败）

## 🔗 相关链接

- [Shell 脚本 - 维基百科](https://zh.wikipedia.org/wiki/Shell%E8%84%9A%E6%9C%AC)
- [Bash 指南](https://www.gnu.org/software/bash/manual/)
- [ShellCheck - 在线脚本检查工具](https://www.shellcheck.net/)
- [VS Code 官方网站](https://code.visualstudio.com/)

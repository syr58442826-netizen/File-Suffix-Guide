# .db 文件后缀详解

## 1. 文件定义 & 用途

.db 是一个通用的**数据库文件**后缀。它并不绑定到某一种数据库，而是多种数据库系统都可能使用的通用后缀。最常见的是 **SQLite 数据库文件**，但也可能是其他格式（如 Berkeley DB、Thumbs.db 缩略图数据库等）。

简单来说，.db 文件就是一个"数据库文件"，里面以结构化方式存储着表、记录等数据，需要对应类型的数据库软件打开，不能直接用文本编辑器查看（看到的是乱码）。

**主要用途：**
- 应用程序的本地数据存储（SQLite 最常见）
- 聊天软件、浏览器、邮件客户端的本地数据
- 桌面应用的配置和数据持久化
- 缩略图缓存（Thumbs.db）
- 移动 App 的本地数据库

## 2. 适用场景

- 查看应用的本地数据库内容
- 备份或迁移应用数据
- 开发时调试数据库
- 数据恢复和取证

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [DB Browser for SQLite](https://sqlitebrowser.org/)、[7-Zip](https://www.7-zip.org/)（部分可解压）、Notepad++ | Navicat、DBeaver |
| Mac | [DB Browser for SQLite](https://sqlitebrowser.org/)、[DB Browser for SQLite](https://sqlitebrowser.org/) | Navicat、DBeaver、TablePlus |
| Linux | [DB Browser for SQLite](https://sqlitebrowser.org/)、[DBeaver Community](https://dbeaver.io/)、sqlite3 命令行 | Navicat、DBeaver Pro |

**新手推荐：** DB Browser for SQLite（开源免费，跨平台，图形界面，打开 SQLite 类 .db 文件首选）。

## 4. 如何编辑、如何导出

### 打开查看方法

**方法一：用 DB Browser for SQLite（推荐，适合 SQLite 类）**
1. 下载安装 [DB Browser for SQLite](https://sqlitebrowser.org/)
2. 启动 → Database → Open Database → 选 .db 文件
3. 在"浏览数据"标签页查看表内容，"执行 SQL"标签可运行查询

**方法二：命令行（sqlite3，如已装）**
```bash
# 打开数据库
sqlite3 mydata.db

# 常用命令
.tables              # 列出所有表
.schema 表名         # 查看表结构
SELECT * FROM 表名;  # 查询数据
.headers on          # 显示列名
.mode column         # 列对齐显示
.quit                # 退出
```

**方法三：DBeaver（通用数据库工具）**
1. 下载 [DBeaver Community](https://dbeaver.io/)
2. 新建连接 → 选 SQLite → 指向 .db 文件
3. 可视化浏览表和数据

### 如何编辑

1. 用 DB Browser for SQLite 打开 .db
2. 切到"浏览数据"标签，直接双击单元格编辑
3. 改完点"写修改"（Write Changes）保存，否则不会落盘

### 如何导出

**方法一：DB Browser 导出为 CSV/SQL**
1. DB Browser → 文件 → 导出 → SQL 文件 / CSV
2. SQL 文件可在其他 SQLite 数据库导入恢复

**方法二：命令行导出**
```bash
# 导出整个数据库为 SQL 脚本
sqlite3 mydata.db .dump > backup.sql

# 导出某表为 CSV
sqlite3 -header -csv mydata.db "SELECT * FROM 表名;" > output.csv

# 从 SQL 脚本恢复
sqlite3 new.db < backup.sql
```

## 5. 常见报错与解决

### 问题1：用 DB Browser 打开提示 "File is not a database" 或 "database disk image is malformed"

**原因：** 这个 .db 不是 SQLite 格式（可能是 Berkeley DB、Thumbs.db 等），或文件损坏、加密。

**解决方法：**
1. 确认 .db 的真实格式：用 7-Zip 打开看文件头，或用 `file mydata.db`（Linux/Mac）
2. SQLite 文件头是 `SQLite format 3\000`，不是的话就不是 SQLite
3. Thumbs.db 是 Windows 缩略图缓存，用专门的工具查看
4. 文件损坏时尝试 `sqlite3 mydata.db ".recover"` 恢复数据
5. 加密的 SQLite（SQLCipher）需要密码才能打开

### 问题2：修改后没保存，关闭后数据丢失

**原因：** DB Browser 里编辑后没点"写修改"（Write Changes），或事务被回滚。

**解决方法：**
1. 编辑完务必点工具栏的"写修改"按钮（或 Ctrl+S）
2. 检查是否在事务中，未提交的事务会回滚
3. 确认文件不是只读（右键属性取消只读）
4. 确认程序（如微信、浏览器）没在占用这个 .db（占用时无法写入）

### 问题3：数据库被锁，提示 "database is locked"

**原因：** 另一个进程（如正在运行的应用）打开了数据库并加了写锁，SQLite 是文件级锁。

**解决方法：**
1. 关闭使用这个 .db 的程序（如关闭对应 App），再操作
2. 复制一份 .db 到别处操作（不影响原程序）
3. SQLite 的 WAL 模式下，检查 .db-wal 和 .db-shm 文件是否存在，恢复时一并复制
4. 杀掉残留进程：Linux `fuser mydata.db`，Windows 用资源监视器看占用

### 问题4：用文本编辑器打开 .db 是乱码

**原因：** .db 是二进制格式（数据库内部格式），不是文本，用文本编辑器打开当然乱码。

**解决方法：**
1. 不要用文本编辑器打开数据库文件
2. 用 DB Browser for SQLite 或 sqlite3 命令行查看
3. 要查看文本形式，先导出为 SQL/CSV 再看

---

## 💡 小知识

- .db 后缀最常被 SQLite 使用，但理论上任何数据库都可命名为 .db
- 微信、QQ 的聊天记录就存在 .db 文件里（SQLite 格式，且加密）
- Windows 的 Thumbs.db 也是 .db 后缀，但它是缩略图缓存，与数据库无关
- SQLite 是全世界部署量最大的数据库（每台手机里都有几十个 SQLite 数据库）

## 🔗 相关链接

- [DB Browser for SQLite 官网](https://sqlitebrowser.org/)
- [SQLite 官网](https://www.sqlite.org/)
- [DBeaver 官网](https://dbeaver.io/)
- [Navicat 官网](https://www.navicat.com/)
- [SQLite 命令行教程](https://www.sqlite.org/cli.html)

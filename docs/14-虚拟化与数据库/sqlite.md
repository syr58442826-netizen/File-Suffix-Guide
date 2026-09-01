# .sqlite 文件后缀详解

## 1. 文件定义 & 用途

.sqlite（或 .sqlite3）是 **SQLite 数据库**文件后缀。SQLite 是一种轻量级、嵌入式、无需服务器的数据库引擎，整个数据库就是单个文件，不需要单独的数据库服务进程。

简单来说，.sqlite 文件就是一个完整的数据库，里面可以有多张表、索引、视图，不需要安装数据库服务器，应用程序直接读写这个文件即可。它是世界上部署最广的数据库。

> 注意：SQLite 数据库文件的后缀可能是 .sqlite、.sqlite3、.db、.db3 等，内容格式一样，只是命名习惯不同。

**主要用途：**
- 桌面/移动应用的本地数据存储
- 浏览器的书签、历史、Cookie（Chrome、Firefox 都用 SQLite）
- 聊天软件的本地消息存储（微信、Telegram）
- 嵌入式设备和 IoT 的数据存储
- 测试和原型开发中的轻量数据库
- 数据交换和归档（一个文件就是完整数据库）

## 2. 适用场景

- 应用程序本地存储结构化数据
- 单机/小型项目不需要数据库服务器
- 数据归档与分发（一个文件就是整个库）
- 移动 App 的本地数据库
- 测试开发，快速验证 SQL

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [DB Browser for SQLite](https://sqlitebrowser.org/)、[DBeaver Community](https://dbeaver.io/)、sqlite3 命令行 | Navicat、TablePlus |
| Mac | [DB Browser for SQLite](https://sqlitebrowser.org/)、[DBeaver Community](https://dbeaver.io/)、sqlite3（系统自带） | Navicat、TablePlus、DB Browser for SQLite |
| Linux | [DB Browser for SQLite](https://sqlitebrowser.org/)、[DBeaver Community](https://dbeaver.io/)、sqlite3 命令行 | Navicat、DBeaver Pro |

**新手推荐：** DB Browser for SQLite（开源免费，图形界面，最简单直观）。

## 4. 如何编辑、如何导出

### 打开查看方法

**方法一：DB Browser for SQLite（图形界面，新手首选）**
1. 下载安装 [DB Browser for SQLite](https://sqlitebrowser.org/)
2. 启动 → 顶部"打开数据库" → 选 .sqlite 文件
3. "数据库结构"看表结构，"浏览数据"看表内容，"执行 SQL"写查询

**方法二：命令行 sqlite3**
```bash
# 打开数据库（Mac 自带 sqlite3，Windows 需从 sqlite.org 下载）
sqlite3 mydata.sqlite

# 常用命令
.tables                       # 列出所有表
.schema 表名                  # 查看建表语句
SELECT * FROM 表名 LIMIT 10;  # 查前 10 行
.headers on                   # 显示列名
.mode column                  # 列对齐显示
.quit                         # 退出
```

**方法三：用编程语言操作（以 Python 为例）**
```python
import sqlite3

# 连接数据库（文件不存在会自动创建）
conn = sqlite3.connect("mydata.sqlite")
cur = conn.cursor()

# 建表
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# 插入数据
cur.execute("INSERT INTO users (name) VALUES (?)", ("小明",))

# 查询
cur.execute("SELECT * FROM users")
print(cur.fetchall())

conn.commit()  # 提交事务
conn.close()   # 关闭连接
```

### 如何编辑

- DB Browser：浏览数据标签双击单元格直接改，改完点"写修改"
- 命令行：`UPDATE 表名 SET 列=值 WHERE 条件;` 后 `COMMIT;`

### 如何导出

**方法一：导出为 SQL 脚本**
```bash
# 导出整个库为 SQL 脚本（可恢复）
sqlite3 mydata.sqlite .dump > backup.sql

# 从脚本恢复
sqlite3 new.sqlite < backup.sql
```

**方法二：DB Browser 导出**
1. 文件 → 导出 → SQL 文件 / CSV / JSON

**方法三：命令行导出 CSV**
```bash
sqlite3 -header -csv mydata.sqlite "SELECT * FROM 表名;" > data.csv
```

## 5. 常见报错与解决

### 问题1：报错 "database is locked"

**原因：** 另一个进程/连接占用了写锁。SQLite 是文件级锁，同一时刻只允许一个写操作。常见于应用还在运行时你打开了同一个 .sqlite。

**解决方法：**
1. 关闭使用该数据库的程序（如关闭对应 App），再操作
2. 复制一份 .sqlite 文件到别处操作（不影响原程序）
3. 开启 WAL 模式提升并发：`PRAGMA journal_mode=WAL;`（需程序配合）
4. 检查并杀掉残留进程
5. 操作完务必关闭连接，避免锁泄漏

### 问题2：报错 "database disk image is malformed" 或 "file is not a database"

**原因：** 文件损坏（断电、写入中断、磁盘问题），或这个文件根本不是 SQLite 格式。

**解决方法：**
1. 确认文件头：用 `head -c 16 file.sqlite`（Linux/Mac），SQLite 文件头是 `SQLite format 3\000`
2. 文件损坏尝试恢复：`sqlite3 损坏.sqlite ".recover" > recovered.sql` 然后 `sqlite3 new.sqlite < recovered.sql`
3. 用 DB Browser 的"完整性检查"（PRAGMA integrity_check）诊断
4. 有备份就从备份恢复
5. 频繁损坏可能是磁盘硬件问题，及时检查硬盘

### 问题3：用 Python/程序写入后数据丢失

**原因：** 没调用 `commit()` 提交事务，连接关闭时改动被回滚。这是新手最常踩的坑。

**解决方法：**
1. 增删改后必须 `conn.commit()` 提交
2. 用上下文管理器自动提交：`with conn: cur.execute(...)`
3. 关闭连接前确认提交：`conn.commit(); conn.close()`
4. 设置 `conn.isolation_level=None` 开启自动提交（每条语句立即生效）

### 问题4：中文乱码或查询返回 None

**原因：** 数据库里存的编码与读取时声明的不一致，或用了错误的数据类型解析。

**解决方法：**
1. SQLite 默认用 UTF-8 存文本，确保写入时是 UTF-8
2. Python 3 默认返回 str，乱码多是数据本身就是乱码
3. 用 `PRAGMA encoding;` 查看数据库编码
4. 读取二进制字段时用 `str(blob, 'utf-8')` 显式转码
5. 检查写入数据的源头编码是否正确

---

## 💡 小知识

- SQLite 由 Richard Hipp 在 2000 年开发，至今仍是世界上最流行的数据库
- SQLite 不需要服务器进程，整个数据库引擎"嵌入"到程序里，一个文件就是完整数据库
- 每部 Android 手机、每个浏览器、每个 iOS App 里都藏着大量 SQLite 数据库
- SQLite 单文件大小限制约 281 TB，对绝大多数应用来说等于无限制

## 🔗 相关链接

- [SQLite 官网](https://www.sqlite.org/)
- [SQLite 中文教程](https://www.runoob.com/sqlite/sqlite-tutorial.html)
- [DB Browser for SQLite 官网](https://sqlitebrowser.org/)
- [DBeaver 官网](https://dbeaver.io/)
- [Python sqlite3 文档](https://docs.python.org/zh-cn/3/library/sqlite3.html)

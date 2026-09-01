# .sql 文件后缀详解

## 1. 文件定义 & 用途

.sql 是 **Structured Query Language（结构化查询语言）** 的缩写，是用于操作关系型数据库的编程语言。.sql 文件就是保存 SQL 语句的文本文件。

简单来说，.sql 文件里面写的是数据库操作命令，包括创建表、插入数据、查询数据、更新数据等。把 SQL 语句保存成文件，可以重复执行、版本管理和分享。

**主要用途：**
- 数据库建表脚本（表结构定义）
- 数据导入和导出
- 数据库备份和恢复
- 存储过程和函数定义
- 数据库迁移脚本
- 查询语句的保存和复用

## 2. 适用场景

- 数据库设计和初始化
- 数据备份和迁移
- 数据库版本管理
- 复杂查询的保存
- 数据库运维脚本
- 学习 SQL 语法

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/)、[MySQL Workbench](https://www.mysql.com/products/workbench/)、DBeaver Community、Notepad++ | Navicat Premium、DataGrip、PL/SQL Developer |
| Mac | [VS Code](https://code.visualstudio.com/)、DBeaver Community、MySQL Workbench | Navicat Premium、DataGrip、Sequel Pro |
| Linux | [VS Code](https://code.visualstudio.com/)、DBeaver Community、MySQL Workbench | DataGrip |

**常用数据库工具：**
- MySQL：MySQL Workbench、Navicat for MySQL
- PostgreSQL：pgAdmin、DBeaver
- 通用：DBeaver、DataGrip、Navicat Premium

**推荐：** 新手用 DBeaver（免费、支持多种数据库），专业开发用 DataGrip

## 4. 如何编辑、如何运行

### 如何编辑

SQL 文件是纯文本文件，用任何文本编辑器都能编辑。

**VS Code 中编辑（推荐）：**
1. 安装 "SQLTools" 或 "mssql" 扩展
2. 语法高亮、自动补全
3. 可以直接连接数据库执行查询

### SQL 基本语法示例

```sql
-- 这是单行注释（用两个减号）
/*
   这是多行注释
*/

-- 1. 创建数据库
CREATE DATABASE IF NOT EXISTS mydb DEFAULT CHARSET utf8mb4;

-- 切换数据库
USE mydb;

-- 2. 创建表
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID',
    username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
    email VARCHAR(100) NOT NULL COMMENT '邮箱',
    age INT DEFAULT 0 COMMENT '年龄',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 3. 插入数据
INSERT INTO users (username, email, age) VALUES
('张三', 'zhangsan@example.com', 25),
('李四', 'lisi@example.com', 30),
('王五', 'wangwu@example.com', 28);

-- 4. 查询数据
SELECT * FROM users;
SELECT username, email FROM users WHERE age > 25;
SELECT * FROM users ORDER BY created_at DESC LIMIT 10;

-- 5. 更新数据
UPDATE users SET age = 26 WHERE username = '张三';

-- 6. 删除数据
DELETE FROM users WHERE id = 3;

-- 7. 聚合查询
SELECT COUNT(*) as total FROM users;
SELECT AVG(age) as avg_age FROM users;
```

### 如何运行 SQL 文件

**方法一：命令行运行（MySQL 为例）**
```bash
# 直接执行 SQL 文件
mysql -u用户名 -p密码 数据库名 < script.sql

# 或者登录后执行
mysql -u用户名 -p密码
mysql> USE 数据库名;
mysql> SOURCE /路径/script.sql;
```

**PostgreSQL：**
```bash
psql -U用户名 -d 数据库名 -f script.sql
```

**SQLite：**
```bash
sqlite3 数据库文件.db < script.sql
```

**方法二：图形界面工具运行**
1. 用 Navicat、DBeaver、MySQL Workbench 等工具连接数据库
2. 打开 .sql 文件
3. 点击"执行"按钮（或按 F5 / Ctrl+Enter）

**方法三：Python 中执行**
```python
import pymysql  # 需要先安装：pip install pymysql

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='mydb',
    charset='utf8mb4'
)

# 读取并执行 SQL 文件
with open('script.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

cursor = conn.cursor()
cursor.execute(sql)
conn.commit()

# 查询
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
conn.close()
```

## 5. 常见报错与解决

### 问题1：提示 "Table 'xxx' doesn't exist" 表不存在

**原因：** 查询的表不存在，或者当前数据库不对。

**解决方法：**
1. 确认表名是否拼写正确（注意大小写，Linux 下 MySQL 区分大小写）
2. 确认当前在正确的数据库中：
   ```sql
   -- 查看当前数据库
   SELECT DATABASE();
   
   -- 切换数据库
   USE 数据库名;
   ```
3. 查看有哪些表：
   ```sql
   SHOW TABLES;
   ```
4. 如果表确实不存在，需要先创建表

### 问题2：提示 "Column 'xxx' doesn't exist" 字段不存在

**原因：** 查询的字段名写错了，或者表中没有这个字段。

**解决方法：**
1. 检查字段名是否拼写正确
2. 查看表结构，确认有哪些字段：
   ```sql
   DESC 表名;
   -- 或者
   SHOW COLUMNS FROM 表名;
   ```
3. 如果是多表查询，注意字段名是否有歧义，加上表名前缀：
   ```sql
   SELECT users.id, orders.id FROM users JOIN orders ON users.id = orders.user_id;
   ```

### 问题3：提示 "Syntax error" SQL 语法错误

**原因：** SQL 语句语法有问题。

**常见错误和解决方法：**
1. **缺少分号**：多条语句时，每条语句末尾要加分号
2. **关键字拼写错误**：`SELECT` 写成 `SELET`，`FROM` 写成 `FORM` 等
3. **使用了中文符号**：逗号、括号、引号等必须是英文的
4. **字符串用了双引号**：SQL 中字符串用单引号（某些数据库也支持双引号）
5. **表名或字段名是关键字**：用反引号包裹（MySQL）或双引号（PostgreSQL）：
   ```sql
   -- order 是关键字，需要用反引号
   SELECT * FROM `order`;
   ```
6. 看错误信息中的行号，定位到具体哪一行出错

### 问题4：中文乱码或插入中文报错

**原因：** 数据库、表、连接的字符集不一致。

**解决方法：**
1. 建库时指定字符集：
   ```sql
   CREATE DATABASE mydb DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
2. 建表时指定字符集：
   ```sql
   CREATE TABLE users (...) DEFAULT CHARSET=utf8mb4;
   ```
3. 连接数据库时指定编码：
   ```bash
   mysql --default-character-set=utf8mb4 -u用户名 -p
   ```
4. 查看当前字符集设置：
   ```sql
   SHOW VARIABLES LIKE 'character%';
   ```
5. 推荐统一使用 utf8mb4（支持 emoji 等 4 字节字符）

---

## 💡 小知识

- SQL 是 1974 年由 IBM 开发的，最初叫 SEQUEL（Structured English Query Language），后来改名为 SQL
- SQL 读作 "S-Q-L"（逐个字母读）或 "sequel"（西阔），两种读法都可以
- SQL 是关系型数据库的标准语言，但不同数据库（MySQL、PostgreSQL、Oracle）的语法略有差异
- SQL 不区分大小写（关键字大写小写都可以），但习惯上关键字大写、表名字段名小写，便于阅读
- 常见的关系型数据库有：MySQL、PostgreSQL、Oracle、SQL Server、SQLite 等
- SQL 注入是一种常见的安全漏洞，开发时要注意使用参数化查询，防止注入攻击

## 🔗 相关链接

- [SQL - 维基百科](https://zh.wikipedia.org/wiki/SQL)
- [MySQL 官方文档](https://dev.mysql.com/doc/)
- [PostgreSQL 官方文档](https://www.postgresql.org/docs/)
- [SQL 教程 - 菜鸟教程](https://www.runoob.com/sql/sql-tutorial.html)
- [LeetCode 数据库题目](https://leetcode.cn/problemset/database/)
- [DBeaver 官方网站](https://dbeaver.io/)

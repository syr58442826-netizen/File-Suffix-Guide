# .yaml 文件后缀详解

## 1. 文件定义 & 用途

.yaml（也常用 .yml）是 **YAML Ain't Markup Language** 的递归缩写，是一种人类可读性高的数据序列化格式。YAML 的设计目标是容易阅读和编写，适合做配置文件。

简单来说，.yaml 文件就是一种用缩进表示层级关系的配置文件，比 JSON 和 XML 更简洁、更易读。现在很多流行的工具都用 YAML 作为配置格式。

**主要用途：**
- 软件配置文件
- DevOps 工具配置（Docker Compose、Kubernetes、Ansible 等）
- CI/CD 流水线配置（GitHub Actions、GitLab CI 等）
- 应用程序配置
- 数据序列化

## 2. 适用场景

- Docker Compose 配置（docker-compose.yml）
- Kubernetes 部署配置
- CI/CD 流水线配置
- Ansible 自动化剧本
- 前端项目配置（Vite、ESLint 等）
- 静态网站生成器配置（Hexo、Jekyll 等）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/)、Notepad++ | Sublime Text |
| Mac | [VS Code](https://code.visualstudio.com/)、TextMate | BBEdit |
| Linux | [VS Code](https://code.visualstudio.com/)、Vim | Sublime Text |

**在线工具：**
- [YAML 校验工具](https://yamlchecker.com/)
- [YAML ↔ JSON 转换](https://www.json2yaml.com/)

**推荐：** VS Code 配合 "YAML" 扩展（Red Hat 出品），支持语法高亮、自动补全、错误校验

## 4. 如何编辑、如何使用

### 如何编辑

YAML 文件是纯文本文件，用任何文本编辑器都能编辑。

**注意：** YAML 对缩进非常敏感，必须使用空格缩进（不能用 Tab），通常使用 2 个空格。

### YAML 基本语法

```yaml
# 这是注释

# 键值对（类似 JSON 的对象）
name: 张三
age: 25
isStudent: true

# 嵌套对象（用缩进表示层级）
address:
  city: 北京
  district: 朝阳区
  street: 某某路 123 号

# 数组/列表（用 - 开头）
hobbies:
  - 读书
  - 编程
  - 游戏

# 数组中的对象
books:
  - title: Python 入门
    author: 张三
    price: 59.9
  - title: JavaScript 高级程序设计
    author: 李四
    price: 89.0

# 多行字符串（| 保留换行）
description: |
  这是一段
  多行文本
  会保留换行符

# 多行字符串（> 折叠换行）
summary: >
  这是一段
  多行文本
  会被合并成一行

# 特殊值
nullValue: null   # 或 ~
emptyValue: ""
booleanValue: true   # true/false/yes/no 都是布尔值（注意可能有坑）
```

### 在 Python 中使用 YAML

```python
import yaml  # 需要先安装：pip install pyyaml

# 读取 YAML 文件
with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(data['name'])
print(data['address']['city'])

# 写入 YAML 文件
data = {
    'name': '王五',
    'age': 28,
    'hobbies': ['音乐', '运动']
}

with open('output.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
```

### 在 JavaScript 中使用 YAML

```javascript
// 需要安装 js-yaml：npm install js-yaml
const yaml = require('js-yaml');
const fs = require('fs');

// 读取 YAML 文件
const data = yaml.load(fs.readFileSync('config.yaml', 'utf8'));
console.log(data.name);

// 写入 YAML 文件
const output = yaml.dump({ name: '王五', age: 28 });
fs.writeFileSync('output.yaml', output, 'utf8');
```

## 5. 常见报错与解决

### 问题1：提示 "YAMLException: can not read an implicit mapping pair" 或缩进错误

**原因：** YAML 对缩进要求严格，缩进不正确会导致解析错误。

**常见错误和解决方法：**
1. **使用了 Tab 缩进**：YAML 不允许 Tab，必须用空格缩进
2. **缩进不一致**：同一层级的缩进必须相同，推荐统一用 2 个空格
3. **缩进数量错误**：子元素比父元素多缩进一层（通常多 2 个空格）
4. **VS Code 设置**：右下角选择 "Spaces: 2"，确保使用空格缩进
5. 用在线 YAML 校验工具定位错误行

### 问题2：数字字符串被自动解析为数字

**原因：** YAML 会自动推断类型，看起来像数字的字符串可能被解析为数字。

**示例：**
```yaml
# 错误示例：port 会被解析为数字 8080，而不是字符串
port: 8080

# 正确：加引号明确表示是字符串
port: "8080"
```

**常见坑：**
- `yes`、`no`、`true`、`false`、`on`、`off` 会被解析为布尔值
- 纯数字字符串会被解析为数字
- `null`、`~` 会被解析为空值

**解决方法：**
1. 给字符串加上引号（单引号或双引号都可以）
2. 不确定类型时，用引号包裹更安全
3. 解析后打印一下，确认类型是否正确

### 问题3：特殊字符导致解析错误

**原因：** YAML 中有一些特殊字符有特殊含义，直接使用会出错。

**常见问题：**
1. **冒号后面没有空格**：`key:value` 是错误的，必须是 `key: value`（冒号后有空格）
2. **值以特殊字符开头**：如 `{`、`}`、`[`、`]`、`&`、`*`、`#`、`?`、`|`、`>`、`%`、`@`、`` ` ``
3. **中文冒号**：必须使用英文冒号

**解决方法：**
1. 冒号后面必须加空格
2. 值包含特殊字符时，用引号包裹：
   ```yaml
   # 错误
   title: Hello: World
   
   # 正确
   title: "Hello: World"
   ```

---

## 💡 小知识

- YAML 的名字是一个递归缩写：YAML Ain't Markup Language（YAML 不是标记语言）
- YAML 最早发布于 2001 年，比 JSON 稍晚
- YAML 是 JSON 的超集，也就是说任何合法的 JSON 都是合法的 YAML
- Docker Compose、Kubernetes、Ansible、GitHub Actions 等 DevOps 工具都选择 YAML 作为配置格式
- YAML 有 3 个基本数据类型：标量（Scalar）、序列（Sequence/数组）、映射（Mapping/对象）
- YAML 支持锚点（&）和引用（*），可以实现配置复用，减少重复

## 🔗 相关链接

- [YAML - 维基百科](https://zh.wikipedia.org/wiki/YAML)
- [YAML 官方网站](https://yaml.org/)
- [YAML 在线校验](https://yamlchecker.com/)
- [YAML ↔ JSON 在线转换](https://www.json2yaml.com/)
- [VS Code YAML 扩展](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml)
- [Ansible YAML 最佳实践](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

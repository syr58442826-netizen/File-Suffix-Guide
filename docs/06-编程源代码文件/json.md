# .json 文件后缀详解

## 1. 文件定义 & 用途

.json 是 **JavaScript Object Notation（JavaScript 对象表示法）** 的缩写，是一种轻量级的数据交换格式。它以纯文本形式存储和表示数据，易于阅读和编写，也易于机器解析和生成。

简单来说，.json 文件就是一种结构化的数据文件，用键值对的方式存储数据。它原本是 JavaScript 的一部分，但现在几乎所有编程语言都支持。

**主要用途：**
- 前后端数据交换（API 接口数据）
- 配置文件（VS Code、npm 等软件的配置）
- 数据存储和传输
- 序列化对象
- Web 应用的数据交换

## 2. 适用场景

- REST API 接口数据格式
- 软件和应用的配置文件
- 前后端数据传递
- 数据持久化存储（小型数据）
- 配置管理
- 日志和数据导出

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/)、Notepad++、记事本 | Sublime Text、010 Editor |
| Mac | [VS Code](https://code.visualstudio.com/)、TextEdit | BBEdit |
| Linux | [VS Code](https://code.visualstudio.com/)、Vim、Gedit | Sublime Text |

**在线工具：**
- [JSON.cn](https://www.json.cn/) - 在线格式化和校验
- [JSONLint](https://jsonlint.com/) - 在线 JSON 校验

**推荐：** VS Code 打开 .json 文件有语法高亮、格式化（Shift+Alt+F）、错误提示等功能

## 4. 如何编辑、如何使用

### 如何编辑

JSON 文件是纯文本文件，用任何文本编辑器都能编辑。

**VS Code 中编辑（推荐）：**
1. 打开 .json 文件
2. 格式化：右键 → 格式化文档（或 Shift+Alt+F）
3. VS Code 会自动标红语法错误
4. 折叠/展开：点击行号旁边的小箭头

### JSON 基本语法

```json
{
    "name": "张三",
    "age": 25,
    "isStudent": true,
    "hobbies": ["读书", "编程", "游戏"],
    "address": {
        "city": "北京",
        "district": "朝阳区"
    },
    "score": null
}
```

**JSON 支持的数据类型：**

| 类型 | 示例 | 说明 |
|------|------|------|
| 对象 | `{ "key": "value" }` | 键值对集合 |
| 数组 | `[1, 2, 3]` | 值的有序列表 |
| 字符串 | `"hello"` | 双引号包裹 |
| 数字 | `123`、`3.14` | 整数或浮点数 |
| 布尔值 | `true` / `false` | 小写 |
| 空值 | `null` | 小写 |

### 在 JavaScript 中使用 JSON

```javascript
// JSON 字符串解析为对象
const jsonStr = '{"name": "张三", "age": 25}';
const obj = JSON.parse(jsonStr);
console.log(obj.name);  // 输出：张三

// 对象转换为 JSON 字符串
const person = { name: "李四", age: 30 };
const jsonString = JSON.stringify(person);
console.log(jsonString);  // 输出：{"name":"李四","age":30}

// 格式化输出（缩进 2 个空格）
const prettyJson = JSON.stringify(person, null, 2);
console.log(prettyJson);
```

### 在 Python 中使用 JSON

```python
import json

# 读取 JSON 文件
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data['name'])

# 写入 JSON 文件
data = {'name': '王五', 'age': 28}
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

## 5. 常见报错与解决

### 问题1：提示 "Unexpected token ... in JSON at position ..."

**原因：** JSON 语法错误，解析失败。

**常见错误和解决方法：**
1. **使用了单引号**：JSON 必须用双引号，不能用单引号
   ```json
   // 错误
   { 'name': '张三' }
   // 正确
   { "name": "张三" }
   ```
2. **最后一个元素后面多了逗号**：JSON 不允许 trailing comma
   ```json
   // 错误
   {
       "name": "张三",
       "age": 25,   // 这里多了逗号
   }
   ```
3. **注释**：标准 JSON 不支持注释（`//` 和 `/* */` 都不行）
4. **使用了中文冒号或引号**：必须使用英文符号
5. 用在线 JSON 校验工具（如 json.cn）检查错误位置

### 问题2：中文显示为 \uXXXX 编码

**原因：** JSON 序列化时中文被转义为 Unicode 编码。

**解决方法：**
- **JavaScript**：`JSON.stringify` 默认会正确处理中文，只有在特殊情况下才会转义
- **Python**：使用 `ensure_ascii=False` 参数
  ```python
  json.dumps(data, ensure_ascii=False)
  ```
- **Java**：配置 Jackson 或 Gson 的序列化选项
- 实际上 `\u4f60\u597d` 就是"你好"的 Unicode 编码，解析后会自动恢复成中文

### 问题3：JSON 文件太大，打开卡顿

**原因：** JSON 文件太大，编辑器加载慢。

**解决方法：**
1. 使用专门的 JSON 查看工具（如 JSON Viewer）
2. VS Code 中关闭语法检查和格式化，或使用大文件模式
3. 用命令行工具处理：
   ```bash
   # Python 格式化查看
   python -m json.tool data.json
   
   # jq 工具（需要安装）
   cat data.json | jq .
   ```
4. 考虑使用数据库存储大量数据，而不是 JSON 文件

---

## 💡 小知识

- JSON 是由 Douglas Crockford 在 2001 年推广的，他被称为"JSON 之父"
- JSON 比 XML 更简洁、更易读，现在已经基本取代了 XML 成为 Web 数据交换的主流格式
- 虽然 JSON 源于 JavaScript，但它是语言无关的，几乎所有编程语言都有 JSON 库
- JSON 的 MIME 类型是 `application/json`
- JSON5 是 JSON 的扩展，支持注释、尾随逗号等更多特性（但不是标准）

## 🔗 相关链接

- [JSON - 维基百科](https://zh.wikipedia.org/wiki/JSON)
- [JSON 官方网站](https://www.json.org/json-zh.html)
- [JSON.cn - 在线 JSON 格式化](https://www.json.cn/)
- [MDN JSON 文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON)
- [jq - 命令行 JSON 处理工具](https://stedolan.github.io/jq/)

# .xls 文件后缀详解（数据处理视角）

## 1. 文件定义 & 用途

XLS 是 Microsoft Excel 97-2003 使用的二进制电子表格格式。在数据处理领域，XLS 是一个"历史遗留格式"——很多老系统、传统企业仍在使用 XLS 格式导出数据，因此数据处理人员经常需要读写 XLS 文件。

从数据处理角度看，XLS 的特点是：

- **二进制格式**：不是纯文本，需要专用库才能读取
- **多工作表**：一个 XLS 文件可以包含多个 Sheet
- **有格式信息**：包含单元格格式、公式、图表等
- **行数限制**：最多 65536 行、256 列（XLSX 则是 1048576 行）
- **兼容性**：新旧系统都能打开，但数据处理上不如 CSV 方便

- **全称**：Excel Spreadsheet
- **类型**：二进制电子表格格式
- **开发者**：Microsoft
- **文件结构**：OLE2 复合文档格式
- **行数上限**：65536 行（2^16）
- **列数上限**：256 列（2^8）

## 2. 适用场景

### 数据处理场景
- 从传统企业系统导出的数据（很多老系统只支持 XLS 导出）
- 历史遗留数据的迁移和清洗
- 财务、会计部门提供的报表数据
- 需要读取多个工作表（Sheet）的数据文件
- 带格式的数据报表生成

### 程序开发场景
- 后端程序生成 Excel 报表供业务人员查看
- 批量导入 Excel 数据到数据库
- 自动化报表生成和邮件发送
- 数据验证和模板填充

### 数据交换场景
- 与非技术部门的数据交换（业务人员只认 Excel）
- 需要保留格式和公式的数据传递
- 多 Sheet 的复杂数据结构（CSV 无法表达）

## 3. 推荐打开软件（数据处理工具）

| 平台 | 免费工具/软件 | 专业工具/软件 |
|------|---------------|---------------|
| Windows | Python（xlrd/xlwt/openpyxl）、WPS 免费版、LibreOffice Calc、DBeaver | Microsoft Excel、WPS 专业版、Tableau、Alteryx |
| Mac | Python（xlrd/xlwt/openpyxl）、LibreOffice Calc、Numbers、DBeaver | Microsoft Excel for Mac、WPS for Mac、Tableau |
| Linux | Python（xlrd/xlwt/openpyxl）、LibreOffice Calc、Gnumeric、DBeaver | SoftMaker Office、Tableau |

**数据处理人员推荐：**
- **Python 处理**：`pandas + xlrd`（读取）或 `pandas + openpyxl`（读写 XLSX，XLS 用 xlrd）
- **批量转换**：LibreOffice 命令行模式（无头模式，适合服务器批量转换）
- **数据库导入**：DBeaver（直接导入 Excel 到数据库表）
- **查看验证**：WPS 或 Excel（确认数据和格式是否正确）

## 4. 如何编辑、如何导出

### 用 Python 读取 XLS（pandas + xlrd）

```python
import pandas as pd

# 读取 XLS 文件（注意：xlrd 2.0+ 不再支持 xls，需要安装 xlrd==1.2.0）
# 安装：pip install xlrd==1.2.0
df = pd.read_excel('data.xls', sheet_name='Sheet1')

# 查看所有 Sheet 名称
xls = pd.ExcelFile('data.xls')
print(xls.sheet_names)  # ['Sheet1', 'Sheet2', '数据汇总']

# 读取指定 Sheet
df1 = pd.read_excel('data.xls', sheet_name=0)       # 第一个 Sheet
df2 = pd.read_excel('data.xls', sheet_name='数据')  # 按名称读取

# 读取所有 Sheet
all_sheets = pd.read_excel('data.xls', sheet_name=None)
for name, df in all_sheets.items():
    print(f"Sheet: {name}, 行数: {len(df)}")
```

### 用 Python 写入 XLS（xlwt）

```python
import xlwt

# 创建工作簿
wb = xlwt.Workbook(encoding='utf-8')

# 创建工作表
ws = wb.add_sheet('数据')

# 写入数据（行, 列, 值）
ws.write(0, 0, '姓名')
ws.write(0, 1, '年龄')
ws.write(0, 2, '城市')

ws.write(1, 0, '张三')
ws.write(1, 1, 25)
ws.write(1, 2, '北京')

# 保存
wb.save('output.xls')
```

### 用 pandas 写入 Excel

```python
# 写入 XLSX 格式（推荐，openpyxl 引擎）
df.to_excel('output.xlsx', index=False, sheet_name='数据')

# 写入多个 Sheet
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='用户数据', index=False)
    df2.to_excel(writer, sheet_name='销售数据', index=False)
    df3.to_excel(writer, sheet_name='统计汇总', index=False)
```

### 格式转换

- **XLS → CSV**：
  ```python
  df = pd.read_excel('data.xls')
  df.to_csv('data.csv', index=False, encoding='utf-8-sig')
  ```
- **XLS → XLSX**：用 Excel/WPS 另存为，或用 Python 转换
- **XLS → 数据库**：
  ```python
  from sqlalchemy import create_engine
  engine = create_engine('mysql+pymysql://user:pass@localhost/db')
  df = pd.read_excel('data.xls')
  df.to_sql('table_name', engine, if_exists='replace', index=False)
  ```

### 用 LibreOffice 命令行批量转换（适合服务器）

```bash
# Linux/Mac
libreoffice --headless --convert-to csv *.xls

# Windows
"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to csv *.xls
```

## 5. 常见报错与解决

### 问题1：xlrd 读取报错 "Unsupported format, or corrupt file"

**报错信息**：`xlrd.biffh.XLRDError: Unsupported format, or corrupt file: Expected BOF record`

**原因**：
1. 文件实际上不是 XLS 格式（可能是 XLSX 改了后缀名，或 HTML/XML 伪装成 XLS）
2. 文件已损坏
3. xlrd 版本不兼容（xlrd 2.0+ 不再支持 .xls 格式）

**解决方法**：
1. 先确认文件真实格式（用文本编辑器打开看开头，如果是 `PK` 就是 ZIP/XLSX，如果是 `<html` 就是 HTML）
2. 安装旧版 xlrd：`pip install xlrd==1.2.0`
3. 如果实际是 XLSX 文件，改用 openpyxl 读取：
   ```python
   df = pd.read_excel('data.xls', engine='openpyxl')  # 注意：实际是 XLSX 格式
   ```
4. 如果是 HTML 表格导出的假 XLS，用 pandas 读取 HTML：
   ```python
   dfs = pd.read_html('data.xls')  # 读取 HTML 表格
   df = dfs[0]  # 第一个表格
   ```

---

### 问题2：读取后数据类型混乱，数字变成字符串

**问题描述**：Excel 中的数值列读取后变成了 object（字符串）类型，无法进行数值计算。

**原因**：
1. 列中混合了数字和文本（某些单元格格式是文本）
2. 数字前面有空格或不可见字符
3. 空值被表示为特殊字符而非真正的空单元格

**解决方法**：
1. 读取时强制转换类型：
   ```python
   df = pd.read_excel('data.xls', dtype={'amount': float, 'id': str})
   ```
2. 读取后手动转换：
   ```python
   df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # 错误值转为 NaN
   ```
3. 去除空格后再转换：
   ```python
   df['amount'] = df['amount'].astype(str).str.strip()
   df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
   ```
4. 用 `converters` 参数在读取时处理：
   ```python
   df = pd.read_excel('data.xls', converters={'amount': lambda x: float(x) if x else 0})
   ```

---

### 问题3：日期格式读取后变成数字（如 44231.523）

**问题描述**：Excel 中的日期列读取后变成了类似 44231.523 这样的浮点数。

**原因**：Excel 将日期存储为序列号（从 1900 年 1 月 1 日开始计数的天数），小数部分是时间。pandas 有时无法自动识别为日期类型。

**解决方法**：
1. 读取时指定日期列：
   ```python
   df = pd.read_excel('data.xls', parse_dates=['create_date', 'update_time'])
   ```
2. 读取后转换 Excel 序列号：
   ```python
   df['create_date'] = pd.to_datetime(df['create_date'], unit='D', origin='1899-12-30')
   # 注意：origin 用 1899-12-30 是因为 Excel 有个闰年 Bug（认为 1900 年是闰年）
   ```
3. 如果日期是文本格式的数字，先转数值再转日期：
   ```python
   df['date'] = pd.to_numeric(df['date'], errors='coerce')
   df['date'] = pd.to_datetime(df['date'], unit='D', origin='1899-12-30')
   ```

---

### 问题4：合并单元格导致数据错位

**问题描述**：Excel 中有合并单元格，读取后只有第一个单元格有值，其他都是空值。

**原因**：合并单元格在 Excel 中只有左上角的单元格保存值，其他单元格是空的。pandas 读取时会如实反映这种情况。

**解决方法**：
1. 向前填充（向下填充空值）：
   ```python
   df['category'] = df['category'].ffill()  # 用前一个非空值填充
   ```
2. 如果是多层表头，手动处理：
   ```python
   # 读取前几行作为表头
   df = pd.read_excel('data.xls', header=[0, 1])  # 前两行作为多级表头
   # 或者跳过前几行
   df = pd.read_excel('data.xls', skiprows=2)
   ```
3. 使用 openpyxl 直接操作合并单元格信息：
   ```python
   from openpyxl import load_workbook
   wb = load_workbook('data.xlsx')
   ws = wb.active
   # 遍历合并单元格并填充值
   for merged_range in ws.merged_cells.ranges:
       top_left_value = ws.cell(merged_range.min_row, merged_range.min_col).value
       for row in range(merged_range.min_row, merged_range.max_row + 1):
           for col in range(merged_range.min_col, merged_range.max_col + 1):
               ws.cell(row, col).value = top_left_value
   ```

---

## 💡 小知识

XLS 格式有个著名的"闰年 Bug"：Excel 认为 1900 年是闰年（实际上不是），所以它的日期序列号从 1900-01-01 开始算第 1 天，但 1900-02-29 这个不存在的日期也被计入了。这就是为什么用 Python 转换 Excel 日期时，origin 要设为 `1899-12-30` 而不是 `1899-12-31`——因为 Excel 多算了一天（那个不存在的 2 月 29 日）。

另外，xlrd 库从 2.0 版本开始不再支持 .xls 格式，只支持 .xlsx。这是因为维护者认为二进制格式太老旧且存在安全风险。如果你需要处理 XLS 文件，记得安装 `xlrd==1.2.0`，或者考虑先把文件转换成 XLSX 格式再处理。

## 🔗 相关链接

- [xlrd 官方文档](https://xlrd.readthedocs.io/)
- [xlwt 官方文档](https://xlwt.readthedocs.io/)
- [openpyxl 官方文档](https://openpyxl.readthedocs.io/)
- [Pandas read_excel 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- [LibreOffice 官网](https://www.libreoffice.org/)
- [DBeaver 数据库工具](https://dbeaver.io/)

# .mat 文件后缀详解

## 1. 文件定义 & 用途

MAT 文件是 MATLAB（Matrix Laboratory，矩阵实验室）软件的二进制数据文件格式，用于存储变量、矩阵、数组、结构体等数据。它是科学计算和工程领域最常用的数据交换格式之一，几乎所有数值计算软件都支持读取和写入 MAT 文件。

MAT 文件的核心特点：
- **MATLAB 原生格式**：MathWorks 公司 MATLAB 软件的标准数据格式
- **多类型存储**：可以存储矩阵、数组、结构体、单元数组、字符串、函数句柄等多种数据类型
- **二进制格式**：二进制存储，体积小、读写速度快
- **跨平台兼容**：Windows/Mac/Linux 都能读写
- **多语言支持**：Python、R、C/C++、Java 等主流语言都有读写 MAT 文件的库
- **版本演进**：有 v4、v6、v7、v7.3 等多个版本，新版本支持更大文件和更多特性

## 2. 适用场景

- **科学计算**：存储和交换 MATLAB/Octave 计算的数据和结果
- **工程仿真**：保存仿真数据、实验结果、模型参数
- **数据分析**：在不同软件之间传递数据（MATLAB ↔ Python ↔ R）
- **机器学习**：存储训练数据、模型参数、预测结果
- **信号/图像处理**：保存信号数据、图像矩阵、处理结果
- **学术研究**：科研数据的保存和共享

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | Octave、Python（scipy.io）、R（R.matlab） | MATLAB |
| Mac | Octave、Python、R | MATLAB |
| Linux | Octave、Python、R、GNU Octave | MATLAB |
| 在线 | MATLAB Online、Octave Online | - |

**新手推荐：**
- **专业使用**：MATLAB（行业标准，付费）
- **免费替代**：GNU Octave（语法几乎和 MATLAB 一致）
- **Python 用户**：使用 scipy.io.loadmat / savemat

## 4. 如何编辑、如何导出

### MAT 文件的基本操作

**使用 MATLAB：**
```matlab
% 保存变量到 .mat 文件
save('data.mat', 'x', 'y', 'z');   % 保存变量 x, y, z
save('data.mat');                  % 保存当前工作区所有变量

% 加载 .mat 文件
load('data.mat');                  % 加载所有变量
load('data.mat', 'x');             % 只加载变量 x
```

**使用 GNU Octave（免费开源）：**
```matlab
% Octave 的语法和 MATLAB 几乎一致
save data.mat x y z;               % 保存变量
load data.mat;                     % 加载变量
```

### 用 Python 读写 MAT 文件

```python
import numpy as np
from scipy.io import loadmat, savemat

# 读取 .mat 文件
data = loadmat('data.mat')
print(data.keys())         # 查看所有变量名
x = data['x']              # 获取变量 x

# 保存为 .mat 文件
x = np.array([1, 2, 3])
y = np.array([[1, 2], [3, 4]])
savemat('output.mat', {'x': x, 'y': y})
```

### 用 R 读写 MAT 文件

```r
# 安装包
install.packages("R.matlab")

# 加载包
library(R.matlab)

# 读取 .mat 文件
data <- readMat("data.mat")
print(names(data))

# 保存为 .mat 文件
x <- matrix(1:9, nrow = 3)
writeMat("output.mat", x = x)
```

### MAT 文件版本选择

| 版本 | 特点 | 适用场景 |
|------|------|----------|
| v4 | 最老，只支持二维矩阵 | 兼容最老的软件 |
| v6 | 支持多维数组、结构体、单元数组 | 兼容 MATLAB 5-6 |
| v7 | 支持数据压缩（默认） | 大多数场景推荐 |
| v7.3 | 基于 HDF5，支持 >2GB 大文件 | 大数据集、超大型矩阵 |

**MATLAB 中指定版本：**
```matlab
save('data.mat', '-v7.3');    % 保存为 v7.3 格式（HDF5 基础）
save('data.mat', '-v7');      % 保存为 v7 格式（默认）
save('data.mat', '-v6');      % 保存为 v6 格式（兼容老版本）
```

## 5. 常见报错与解决

### 问题 1：MAT 文件太大，打开很慢或内存不够

**原因：** 文件包含大型矩阵或大量数据，超出内存容量。

**解决方法：**
1. 使用 v7.3 格式（基于 HDF5），支持部分读取（不用全部加载进内存）
2. MATLAB 中使用 matfile 函数部分加载：
   ```matlab
   m = matfile('bigdata.mat');
   subset = m.largeMatrix(1:100, 1:100);  % 只读取部分数据
   ```
3. Python 中使用 h5py 读取 v7.3 格式的 MAT 文件
4. 考虑将数据分割成多个小文件
5. 增加系统内存或使用更高配置的计算机

### 问题 2：Python 读取 MAT 文件报错，提示"版本不支持"

**原因：** scipy.io.loadmat 不支持 v7.3 版本的 MAT 文件（因为 v7.3 是 HDF5 格式）。

**解决方法：**
1. **v7.3 格式**：使用 h5py 库读取
   ```python
   import h5py
   with h5py.File('data.mat', 'r') as f:
       x = f['x'][:]
   ```
2. **v7 及更早格式**：使用 scipy.io
   ```python
   from scipy.io import loadmat
   data = loadmat('data.mat')
   ```
3. 在 MATLAB 中重新保存为 v7 格式：`save('data_v7.mat', '-v7')`

### 问题 3：MAT 文件在不同软件间读取后数据类型变了

**原因：** 不同软件对 MAT 数据类型的映射不同。

**解决方法：**
1. 这是正常现象，数据内容通常是正确的，只是类型表示不同
2. Python 中读取的矩阵默认是 numpy 数组
3. 结构体在 Python 中变成字典，在 R 中变成列表
4. 读取后检查数据形状和内容是否正确
5. 保存时注意保持数据类型一致（如用单精度还是双精度）

### 问题 4：MAT 文件损坏，无法读取

**原因：** 保存过程中断电、磁盘错误或传输损坏。

**解决方法：**
1. 如果有备份，恢复备份
2. MATLAB 中尝试部分加载，看能否挽救部分数据
3. v7.3 格式的文件可以用 HDF5 工具尝试修复
4. 重要数据建议多份备份，保存完成后验证文件完整性
5. 保存后立即用 load 验证一下文件能否正常打开

---

## 💡 小知识

MAT 文件的历史和 MATLAB 一样悠久。MATLAB 最早诞生于 1970 年代末到 1980 年代初，由 Cleve Moler 开发。最初它只是一个方便学生使用 LINPACK 和 EISPACK 数学库的"外壳程序"，没想到后来发展成了科学计算领域的行业标准。

MAT 文件的设计目标很明确——让用户能够方便地保存和加载工作区中的所有变量。在 MATLAB 中，你输入一个 `save` 命令，当前内存里的所有矩阵、数组、结构体就都存到 .mat 文件里了；下次 `load` 一下，一切恢复原状。这种"工作区快照"的设计非常实用，深受科研人员喜爱。

有趣的是，虽然 MAT 文件是 MATLAB 的"私有"格式，但它却成了科学计算领域的"通用货币"——几乎所有数值计算软件都支持读写 MAT 文件。Python、R、Octave、Julia、Scilab……你能想到的科学计算语言，几乎都有读写 MAT 文件的库。为什么？因为 MATLAB 在学术界和工程界太普及了，大家都用它，其他软件想被用户接受，首先就得能读取 MATLAB 的数据格式。

MAT 文件的版本演进也很有意思。早期的 v4 格式只能存二维矩阵，后来的 v6 加入了多维数组和结构体，v7 加入了数据压缩，v7.3 更是直接用 HDF5 作为底层格式，支持 2GB 以上的大文件。每一次版本升级，都反映了科学计算需求的增长——从简单的矩阵运算，到复杂的数据分析，再到今天的大数据和机器学习。

## 🔗 相关链接

- [MATLAB 官方网站](https://www.mathworks.com/products/matlab.html)
- [GNU Octave 官方网站](https://www.gnu.org/software/octave/)
- [scipy.io 文档](https://docs.scipy.org/doc/scipy/reference/io.html)
- [HDF5 官方网站](https://www.hdfgroup.org/solutions/hdf5/)
- [.m MATLAB 脚本格式详解](./m.md)
- [.h5 HDF5 数据格式详解](./h5.md)
- [.r R 语言脚本详解](../13-高级编程与脚本/r.md)

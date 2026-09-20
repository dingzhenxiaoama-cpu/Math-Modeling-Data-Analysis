# Pandas 函数与数据操作整理

来源：[pandas_learning.py](pandas_learning.py)。包含正在执行的代码、`#` 注释中的代码，以及三引号包围的代码。三引号内容实际上是字符串，本笔记按停用的学习示例一并统计。

按名称去重，共整理 **21 项函数、类构造器和对象方法**，另列出 **6 项属性或索引器**，以及筛选、赋值和运算语法。示例中的 `pd` 来自 `import pandas as pd`。以下只介绍原文件涉及的用法，不是完整 API 参数表。

## 1. 函数与方法总览

| 序号 | 名称 | 作用 | 原文件中的用法 |
| --- | --- | --- | --- |
| 1 | `pd.Series()` | 创建带索引的一维数据 | `pd.Series([1, 3, 5, np.nan, 6, 8])` |
| 2 | `pd.DataFrame()` | 创建带行、列标签的二维表 | `pd.DataFrame(..., index=df3, columns=list('ABCD'))` |
| 3 | `pd.Timestamp()` | 创建单个日期时间值 | `pd.Timestamp('20130102')` |
| 4 | `pd.Categorical()` | 创建分类数据 | `pd.Categorical(['text', 'train', 'text', 'train'])` |
| 5 | `pd.date_range()` | 生成等间隔日期时间索引 | `pd.date_range('20130101', periods=6)` |
| 6 | `df.head()` | 查看前几行，默认 5 行 | `df.head()` |
| 7 | `df.tail()` | 查看后几行，默认 5 行 | `df.tail()` |
| 8 | `df.sort_index()` | 按行标签或列标签排序 | `df.sort_index(axis=1, ascending=False)` |
| 9 | `df.sort_values()` | 按指定列的数值或内容排序 | `df.sort_values(by='B')` |
| 10 | `df.copy()` | 复制数据对象 | `df3 = df.copy()` |
| 11 | `Series.isin()` | 判断每个元素是否属于给定集合 | `df3['E'].isin(['two', 'four'])` |
| 12 | `df.reindex()` | 按指定行、列标签重新对齐数据 | `df.reindex(index=..., columns=...)` |
| 13 | `df.dropna()` | 删除包含缺失值的行或列 | `df1.dropna(how='any')` |
| 14 | `df.fillna()` | 填充缺失值 | `df1.fillna(value=5)` |
| 15 | `pd.isna()` | 判断数据是否为缺失值 | `pd.isna(df1)` |
| 16 | `df.eq()` | 逐元素判断等于 | `df1.eq(df2)` |
| 17 | `df.ne()` | 逐元素判断不等于 | `df1.ne(df2)` |
| 18 | `df.gt()` | 逐元素判断大于 | `df1.gt(df2)` |
| 19 | `df.lt()` | 逐元素判断小于 | `df1.lt(df2)` |
| 20 | `df.ge()` | 逐元素判断大于或等于 | `df1.ge(df2)` |
| 21 | `df.le()` | 逐元素判断小于或等于 | `df1.le(df2)` |

严格来说，`Series`、`DataFrame`、`Timestamp`、`Categorical` 是类，这里把创建对象的调用也纳入学习清单。

## 2. 创建数据

### 2.1 `pd.Series()`：一维带标签数据

常用形式：`pd.Series(data, index=None, dtype=None)`。

```python
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

c = pd.Series(1, index=list(range(4)), dtype='float32')
print(c)
```

- `data`：数据，可以是列表、数组或标量。
- `index`：索引标签；省略时通常使用从 0 开始的整数索引。
- `dtype`：数据类型，如 `float32`。
- 第二个例子把标量 `1` 扩展到 4 个索引位置，得到 4 个浮点数 `1.0`。
- `np.nan` 是 NumPy 提供的缺失值标记，pandas 可以识别它。

### 2.2 `pd.DataFrame()`：二维表格

常用形式：`pd.DataFrame(data, index=None, columns=None)`。

```python
df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['text', 'train', 'text', 'train']),
    'F': 'foo'
})
print(df2)
```

字典的键是列名，值是各列的数据。这里数组和 Series 确定了 4 行，`A`、`B`、`F` 中的标量会填充到每一行。不同列可以具有不同数据类型；Series 数据会按索引标签对齐。

```python
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(
    np.random.randn(6, 4),
    index=dates,
    columns=list('ABCD')
)
print(df)
```

这里创建 6 行 4 列的数据表。`index` 提供 6 个行标签，`columns` 提供 4 个列标签。`index=6` 不合法；需要默认数字索引时，可以省略 `index` 或使用 `index=range(6)`。

依据：[DataFrame 官方文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)。

### 2.3 `pd.Timestamp()`：单个日期时间

```python
timestamp = pd.Timestamp('20130102')
print(timestamp)  # 2013-01-02 00:00:00
```

将日期字符串转换为 pandas 的日期时间标量。它代表一个时间点；原代码用它为 `B` 列提供同一个日期。

### 2.4 `pd.Categorical()`：分类数据

```python
category = pd.Categorical(['text', 'train', 'text', 'train'])
print(category)
```

把数据表示为有限类别及其编码。这里共有 `text` 和 `train` 两种类别，适合类别重复出现的字段。默认类别无序，不能据此认为类别具有大小等级。

### 2.5 `pd.date_range()`：日期序列

```python
dates = pd.date_range('20130101', periods=6)
print(dates)
```

`start` 是起点，`periods` 是生成数量；此例默认按天生成，返回 `DatetimeIndex`，包含 2013-01-01 至 2013-01-06。原脚本把这个结果命名为 `df3`，但它此时并不是 DataFrame。

## 3. 查看数据与标签

以下示例使用第 2.2 节创建的 `df`，其行标签为 6 个日期，列标签为 `A`、`B`、`C`、`D`。

| 写法 | 含义 | 是否带括号 |
| --- | --- | --- |
| `df.head()` | 返回前 5 行；`df.head(2)` 返回前 2 行 | 是，方法 |
| `df.tail()` | 返回后 5 行；`df.tail(2)` 返回后 2 行 | 是，方法 |
| `df.index` | 返回行标签，本例为日期索引 | 否，属性 |
| `df.columns` | 返回列标签，本例为 A、B、C、D | 否，属性 |

原文件的 `df.columns` 出现在空值处理示例中，也属于本次整理范围。

## 4. 排序

### 4.1 `df.sort_index()`：按标签排序

```python
print(df.sort_index(axis=1, ascending=False))
```

- `axis=0`：按行标签排序，也是默认设置。
- `axis=1`：按列标签排序。
- `ascending=True`：升序；`False`：降序。

原示例把列顺序从 `A、B、C、D` 改成 `D、C、B、A`，不是按单元格数值排序。

### 4.2 `df.sort_values()`：按数据值排序

```python
print(df.sort_values(by='B'))
```

`by='B'` 表示用 B 列作为排序依据。默认升序，并移动整行，保持同一行各列数据的对应关系。

这两个方法默认返回排序结果，不直接修改 `df`；需要保留结果时可以赋值给变量。

## 5. 选择数据：方括号与索引器

这些操作虽然不是普通函数调用，但在原文件中大量出现，因此单独整理。示例假设行、列标签唯一，日期按升序排列。

### 5.1 `df[...]`：选择列或切片选行

| 原代码 | 作用 |
| --- | --- |
| `df['A']` | 选择 A 列，返回 Series |
| `df[1:3]` | 按行位置选择第 2、3 行，不含位置 3 |
| `df['2013-01-02':'2013-01-05']` | 对本例日期索引切片，包含 1 月 2 日至 1 月 5 日 |

### 5.2 `loc`、`iloc`、`at`、`iat`

| 索引器 | 依据 | 用途 | 切片规则 |
| --- | --- | --- | --- |
| `df.loc[...]` | 标签 | 选择行、列或单个值 | 本例标签切片包含起止标签 |
| `df.iloc[...]` | 从 0 开始的位置 | 选择行、列或单个值 | 包含起点，不含终点 |
| `df.at[...]` | 行、列标签 | 快速读取或设置单个值 | 不用于范围切片 |
| `df.iat[...]` | 行、列位置 | 快速读取或设置单个值 | 不用于范围切片 |

它们使用方括号 `[]`，不能写成 `df.loc(...)` 这样的函数调用。

原文件所有相关示例：

```python
print(df.loc['2013-01-02'])                 # 选择该日期的一行
print(df.loc[:, ['A', 'B']])               # 所有行，只取 A、B 两列
print(df.loc['2013-01-02':'2013-01-05', ['A', 'B']])
print(df.loc['2013-01-02', 'A'])            # 指定日期的 A 列值
print(df.at['2013-01-02', 'A'])             # 读取同一个单元格

print(df.iloc[3])                          # 第 4 行
print(df.iloc[3:5, 0:2])                   # 第 4、5 行，第 1、2 列
print(df.iloc[[1, 2, 4], [0, 2]])           # 第 2、3、5 行，第 1、3 列
print(df.iloc[1, 1])                       # 第 2 行、第 2 列
print(df.iat[1, 1])                        # 读取同一个单元格
```

原注释把 `df.iloc[3:5, 0:2]` 解释成“第 2-4 行”，应改为“第 4、5 行”。

依据：[pandas 索引与选择](https://pandas.pydata.org/docs/user_guide/indexing.html)。

## 6. 筛选与复制

### 6.1 布尔筛选

```python
print(df[df['B'] > 0])  # 保留 B 列大于 0 的整行
print(df[df > 0])       # 保持表格形状，不大于 0 的位置变为缺失值
```

第一个条件是一维布尔 Series，用来筛选行；第二个条件是二维布尔 DataFrame，用来筛选单元格。此处 `df` 是纯数值表；添加字符串列后，直接对整表执行 `df > 0` 可能报类型错误。

### 6.2 `df.copy()`：创建副本

```python
df3 = df.copy()
df3['E'] = ['one', 'two', 'three', 'four', 'five', 'six']
```

默认 `deep=True`。对本例的数值表，修改副本中的数值或添加列不会修改原表。若单元格存放列表等可变 Python 对象，默认复制不等于递归复制这些内部对象。

### 6.3 `Series.isin()`：集合成员判断

```python
print(df3['E'].isin(['two', 'four']))
print(df3[df3['E'].isin(['two', 'four'])])
```

第一行返回与 E 列索引相同的布尔 Series：值为 `two` 或 `four` 的位置是 `True`。第二行利用这个结果保留对应整行。

## 7. 赋值操作

| 原代码 | 作用 |
| --- | --- |
| `df.at['2013-01-02', 'A'] = 0` | 按标签把指定单元格设为 0 |
| `df.iat[0, 2] = 1` | 按位置把第 1 行、第 3 列设为 1 |
| `df['G'] = [1, 2, 3, 4, 5, 6]` | 新建或覆盖 G 列；列表长度须与行数一致 |
| `df3[df3 < 0] = 0` | 将数值表中小于 0 的元素改为 0 |
| `df1.loc[起始标签:结束标签, 'E'] = 1` | 将指定标签范围内的 E 列设为 1 |

这里的赋值会修改等号左边的数据对象。`df3[df3 < 0] = 0` 对应原赋值段中刚执行 `df3 = df.copy()` 得到的数值副本，不应直接用于含字符串 E 列的筛选示例副本。

## 8. 重新对齐与缺失值处理

### 8.1 `df.reindex()`：按新标签对齐

常用形式：`df.reindex(index=新行标签, columns=新列标签)`。

它按标签匹配保留已有数据，并按给定标签顺序排列；新标签在原表中不存在时，相应位置默认产生缺失值。

原文件写的是：

```python
# 原文件的停用示例，存在问题，不直接运行
# df1 = df.reindex(index=s[0:4], columns=list(df.columns + ['E']))
# df1.loc[d[0]:d[1], 'E'] = 1
```

这里有三点需要修正：

1. `s[0:4]` 的值是 `1、3、5、NaN`，不能用来保留原表的前四个日期。`reindex` 按标签匹配，不是按行位置选取。
2. `df.columns + ['E']` 不是追加 E 列。在当前本机环境中，原写法报错 `ValueError: Lengths of operands do not match: 4 != 1`。追加应写成 `list(df.columns) + ['E']`，先转为 Python 列表，再连接列表。
3. `d` 在文件中未定义，执行 `d[0]` 会报 `NameError`。

下面是对应的可运行写法，独立建立示例数据，避免原文件复用 `df3` 名称造成混淆：

```python
import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df1 = df.reindex(index=dates[:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
```

此时 `df1` 有 4 行 5 列，A 至 D 列保留原值，E 列前两行为 `1`，后两行为 `NaN`。

依据：[reindex 官方文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html)。

### 8.2 `df.dropna()`：删除含缺失值的行或列

```python
print(df1.dropna(how='any'))
```

默认 `axis=0`，按行删除。`how='any'` 表示只要一行中有任意缺失值就删除该行；`how='all'` 表示整行都缺失才删除。设置 `axis=1` 时改为按列删除。

在上面的修正示例中，返回结果仅保留前两行。

### 8.3 `df.fillna()`：填充缺失值

```python
print(df1.fillna(value=5))
```

将缺失位置填为 `5`，已有的非缺失值保持原样。原示例的 `dropna()` 和 `fillna()` 都默认返回新结果，不直接修改 `df1`；需要保存时写 `df1 = df1.fillna(value=5)`。

### 8.4 `pd.isna()`：判断缺失值

```python
print(pd.isna(df1))
```

缺失位置返回 `True`，非缺失位置返回 `False`。输入本例 DataFrame 时，返回同形状的布尔 DataFrame；它只检测缺失值，不删除或填充数据。

依据：[pandas 缺失值处理](https://pandas.pydata.org/docs/user_guide/missing_data.html)。

## 9. 算术运算：按行列标签对齐

原文件使用以下两个表：

```python
df1 = pd.DataFrame(np.random.randn(2, 5))
df2 = pd.DataFrame(np.random.randn(3, 4))
```

| 写法 | 含义 |
| --- | --- |
| `df1 + df2` | 对齐后逐元素相加 |
| `df1 - df2` | 对齐后逐元素相减 |
| `df1 * df2` | 对齐后逐元素相乘，不是矩阵乘法 |
| `df1 / df2` | 对齐后逐元素相除 |

两表运算按行标签和列标签对齐。本例结果有 3 行 5 列，公共区域是行 `0、1` 与列 `0、1、2、3` 的交叉部分；行 `2` 或列 `4` 缺少另一张表对应的数据，所以结果为 `NaN`。

上述写法是运算符语法，不在 21 项命名调用中重复计数。随机数每次运行可能不同，但标签对齐规则不变。

## 10. 比较方法：`eq`、`ne`、`gt`、`lt`、`ge`、`le`

| 方法 | 比较含义 | 原代码 | 返回内容 |
| --- | --- | --- | --- |
| `eq()` | 等于 | `df1.eq(df2)` | 各位置是否相等 |
| `ne()` | 不等于 | `df1.ne(df2)` | 各位置是否不等 |
| `gt()` | 大于 | `df1.gt(df2)` | 左值是否大于右值 |
| `lt()` | 小于 | `df1.lt(df2)` | 左值是否小于右值 |
| `ge()` | 大于等于 | `df1.ge(df2)` | 左值是否大于或等于右值 |
| `le()` | 小于等于 | `df1.le(df2)` | 左值是否小于或等于右值 |

这些调用逐元素比较，返回布尔 DataFrame，不是用一个布尔值判断两张表是否整体相同。两表标签不一致时会按标签并集对齐，本例结果仍为 3 行 5 列。

本例为普通浮点数数据：对齐产生 `NaN` 的位置，`ne()` 返回 `True`，其余五种比较返回 `False`。不能把 `NaN` 当作普通数值来判断大小或相等。

虽然比较含义对应 `==`、`!=`、`>`、`<`、`>=`、`<=`，但不能在标签不一致时直接互换：两张 DataFrame 使用这些比较运算符通常要求行列标签一致，原文件的方法调用可以处理标签并集对齐。

依据：[DataFrame.eq 官方文档及其相关比较方法](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html)。

## 11. 原文件出现但不属于 pandas 的内容

| 内容 | 所属 | 作用 |
| --- | --- | --- |
| `np.array()` | NumPy | 创建数组，例如 4 个整数 3 |
| `np.random.randn()` | NumPy | 生成标准正态分布随机数数组 |
| `np.nan` | NumPy | 浮点缺失值标记，不是函数 |
| `print()` | Python 内置函数 | 输出结果 |
| `list()` | Python 内置类型构造器 | 转为列表，例如 `list('ABCD')` |
| `range()` | Python 内置类型构造器 | 创建整数范围，例如 `range(4)` |
| `[3] * 4` | Python 列表操作 | 把列表重复 4 次，得到 `[3, 3, 3, 3]` |

## 12. 运行原示例时的注意事项

- 三引号内的示例不会执行。单独启用选择、筛选等段落前，需要先执行创建 `df` 的代码。
- 原文件重复使用 `df1`、`df2`、`df3` 变量名。例如 `df3` 先表示日期索引，后来又表示表格副本；前后段落一起启用时要确认当前类型。
- `df3[df3['E'].isin(['two', 'four'])]`、`df1.dropna(...)` 等裸表达式在普通 `.py` 脚本中不会自动显示结果，查看时需要 `print(...)`。
- `sort_index()`、`sort_values()`、`reindex()`、`dropna()`、`fillna()` 在本文默认调用方式下都返回结果；不要把调用本身误认为已更新原变量。
- 学习脚本应使用 `pandas_learning.py` 等名称，避免命名为 `pandas.py` 导致导入冲突。

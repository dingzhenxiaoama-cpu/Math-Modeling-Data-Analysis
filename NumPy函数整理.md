# NumPy 函数与数组操作整理

来源：本文件夹中的 [`.vscode/NumPy.py`](.vscode/NumPy.py)。包含正在执行的代码、`#` 注释中的调用，以及三引号包围的代码。三引号内容在 Python 中是字符串，这里按学习笔记中的“停用代码”一并整理。

说明依据 NumPy、Python 官方文档核实；示例使用原脚本中的数据或简化数据。以下是常用调用形式，不是包含所有高级参数的完整签名。各节示例先执行 `import numpy as np`；同一节内按顺序运行。

## 1. 覆盖清单

| 类别 | 原文件中出现的内容 |
| --- | --- |
| 数组创建 | `np.array()` |
| 副本、视图、重塑 | `a.copy()`、`a.view()`、`a.reshape()` |
| 遍历 | `np.nditer()`、`np.ndenumerate()` |
| 连接、堆叠 | `np.concatenate()`、`np.stack()`、`np.hstack()`、`np.vstack()`、`np.dstack()` |
| 拆分 | `np.array_split()` |
| 搜索、排序 | `np.where()`、`np.searchsorted()`、`np.sort()` |
| Python 函数、方法 | `print()`、`type()`、列表的 `append()` |
| 属性（不加括号） | `np.__version__`、`a.ndim`、`a.shape`、`a.base` |
| 语法及运算 | 整数索引、切片、布尔索引、逐元素比较、取余；注释中提到的长度概念 `len` |

## 2. `np.array()`：创建数组

常用形式：`np.array(object, dtype=None)`。`object` 是标量、列表或嵌套列表；`dtype` 指定元素类型，省略时自动推断。返回 `ndarray`。

```python
import numpy as np

a = np.array(1)                         # 0 维，shape 为 ()
b = np.array([1, 2, 3])                 # 1 维，shape 为 (3,)
c = np.array([[1, 2, 3], [1, 2, 3]])     # 2 维，shape 为 (2, 3)
d = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])               # 2 维，shape 为 (3, 3)
e = np.array([1, 2, 3], dtype=float)     # [1. 2. 3.]
```

三行数据仍然是二维数组；维数由嵌套层级决定。普通数值矩阵的各行长度应一致。多个行列表需要放在同一个外层列表中，不能把第二行当作第二个位置参数传入，因为第二个参数是 `dtype`。

依据：[numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)。

## 3. 数组属性：版本、维数、形状、数据来源

属性用 `对象.属性` 读取，不写 `()`。

| 属性 | 作用 | 例子 |
| --- | --- | --- |
| `np.__version__` | 当前导入的 NumPy 的版本字符串 | `print(np.__version__)` |
| `a.ndim` | 数组的轴数，即维数 | 二维数组为 `2` |
| `a.shape` | 各轴长度组成的元组 | 2 行 3 列为 `(2, 3)` |
| `a.base` | 数组所依赖的底层对象；自有数据的数组通常为 `None` | 视图可能引用原数组或更底层的对象 |

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)   # 2
print(a.shape)  # (2, 3)
print(a.base)   # None：这个数组自己拥有数据
```

`base is None` 不表示“没有数据”，返回一个底层对象也不表示“才有数据”。此外，不能仅凭 `b.base is a` 为假就断言二者没有共享内存，因为 `base` 可能指向更早的底层对象。

依据：[ndim](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html)、[shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html)、[base](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html)。

## 4. 整数索引与切片

索引从 `0` 开始；二维数组用 `a[行索引, 列索引]`。负索引从末尾计数。

```python
d = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(d[2, 2])  # 3：第三行第三列

b = np.array([1, 2, 3])
print(b[0:2:1]) # [1 2]
print(b[::-1])  # [3 2 1]
```

切片为 `a[start:stop:step]`，包含起点、不包含终点，默认步长为 `1`，步长不能为 `0`。正步长时，省略边界通常表示从开头取到末尾；负步长时默认边界相应反向，不能统一理解为“永远默认 0 和长度”。

NumPy 基本切片得到的是视图；修改切片中的元素会影响原数据。这里的索引和切片是语法，不是函数。

依据：[NumPy 索引说明](https://numpy.org/doc/stable/user/basics.indexing.html)。

## 5. `a.copy()`：复制数组数据

常用形式：`a.copy()`，返回独立的数据副本。对于脚本中的普通数值数组，修改副本元素不会修改原数组，反之亦然。

```python
a = np.array([0, 1, 2, 3, 4, 5])
b = a.copy()
a[0] = 99
print(a)       # [99  1  2  3  4  5]
print(b)       # [0 1 2 3 4 5]
print(b.base)  # None
```

“复制到寄存器”不是这个方法的含义。它复制数组的数据缓冲区。补充边界：若元素类型为 `object`，复制的对象引用仍可指向同一个 Python 对象，不等于递归深复制。

依据：[ndarray.copy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html)。

## 6. `a.view()`：创建共享数据的视图

常用形式：`a.view()`。返回一个新的数组对象，但与原数组共享底层数据；在这个示例中，任一方修改元素都会反映在另一方。

```python
a = np.array([0, 1, 2, 3, 4, 5])
c = a.view()
a[0] = 99
print(c)            # [99  1  2  3  4  5]
print(c.base is a)  # True：针对这个直接创建的示例
```

视图本身有形状、类型等信息，也能访问数据，只是不另复制这一份底层数据。这里讨论的是元素赋值；把变量 `a` 重新绑定到另一个数组，不会让已有视图自动改为引用新数组。

依据：[ndarray.view](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html)、[副本与视图](https://numpy.org/doc/stable/user/basics.copies.html)。

## 7. `a.reshape()`：改变形状

常用形式：`a.reshape(新形状)`，或 `a.reshape(轴0长度, 轴1长度, ...)`。返回重塑后的数组，原数组的形状不会因此原地改变。

```python
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
b = a.reshape(4, 3)
c = a.reshape(2, 3, 2)
d = c.reshape(-1)
print(b.shape)  # (4, 3)
print(c.shape)  # (2, 3, 2)
print(d)        # [ 1  2  3  4  5  6  7  8  9 10 11 12]
```

新旧形状的元素总数必须相同，例如 `4 * 3 = 12`。最多有一个维度写成 `-1`，由元素数自动推算；`reshape(-1)` 就是推算一维长度。默认 `order='C'`，最后一个索引变化最快。

纠正原注释：“reshape 后是视图”不总成立。能共享原数据时返回视图，需要重新整理数据时可能复制。

依据：[reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)。

## 8. `np.nditer()`：逐元素迭代

常用形式：`np.nditer(a)`。创建多维数组迭代器，遍历元素，而普通 `for row in 二维数组` 遍历的是行。

```python
arr = np.array([[1, 2], [3, 4], [5, 6]])
for x in np.nditer(arr):
    print(x)  # 依次打印 1、2、3、4、5、6
```

默认按适合内存布局的 `order='K'` 遍历；若明确要求按行的索引顺序，可写 `np.nditer(arr, order='C')`。默认元素操作数只读，循环变量通常是零维数组，不能把上述写法直接当作修改元素的循环。

依据：[nditer](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html)。

## 9. `np.ndenumerate()`：同时获取索引与值

常用形式：`np.ndenumerate(a)`。返回迭代器，每次产生 `(索引元组, 元素值)`。

```python
arr = np.array([[1, 2], [3, 4]])
for index, value in np.ndenumerate(arr):
    print(index, value)
# (0, 0) 1
# (0, 1) 2
# (1, 0) 3
# (1, 1) 4
```

原代码 `for y in np.ndenumerate(arr): print(y)` 也正确，只是把索引和值组成的一整对内容一起打印。

依据：[ndenumerate](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html)。

## 10. `np.concatenate()`：沿已有轴连接

常用形式：`np.concatenate((a, b), axis=0)`。返回连接后的数组，不新增维度；除了连接轴，其他轴的长度必须一致。

```python
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(np.concatenate((arr1, arr2), axis=0))
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print(np.concatenate((arr1, arr2), axis=1))
# [[1 2 5 6]
#  [3 4 7 8]]
```

对二维数组，`axis=0` 是增加行数、上下连接；`axis=1` 是增加列数、左右连接。默认 `axis=0`。`axis=None` 则先展平再连接。

依据：[concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)。

## 11. `np.stack()`：新增一个轴来堆叠

常用形式：`np.stack((a, b), axis=0)`。所有输入形状必须相同；返回数组比每个输入多一维。`axis` 指新轴在结果中的位置。

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.stack((a, b), axis=0))
# [[1 2 3]
#  [4 5 6]]，shape 为 (2, 3)
print(np.stack((a, b), axis=1))
# [[1 4]
#  [2 5]
#  [3 6]]，shape 为 (3, 2)
```

二维输入的轴位置可以这样理解：

```python
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
s0 = np.stack((arr1, arr2), axis=0)
s1 = np.stack((arr1, arr2), axis=1)
print(s0[0])       # [[1 2], [3 4]]：第一份完整数组
print(s1[:, 0, :]) # [[1 2], [3 4]]：第一份完整数组
```

本例两种结果的形状都为 `(2, 2, 2)`，但元素布局不同。若每个输入形状为 `(2, 3)`，两个输入使用 `axis=0/1/2` 的结果分别为 `(2, 2, 3)`、`(2, 2, 3)`、`(2, 3, 2)`；前两者形状也可能相同，仍应看新轴位置。不能把高维 `stack` 固定记成“按行”或“按列”。

依据：[stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html)。

## 12. `np.hstack()`：水平连接

常用形式：`np.hstack((a, b))`。二维及更高维输入沿 `axis=1` 连接；一维输入沿 `axis=0` 连接。非连接轴的长度要匹配，返回连接后的数组。

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.hstack((a, b)))
# [[1 2 5 6]
#  [3 4 7 8]]
print(np.hstack((np.array([1, 2]), np.array([3, 4]))))
# [1 2 3 4]
```

原注释“按行堆叠”容易混淆；对于二维数组，记成“左右拼接、增加列数”。

依据：[hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html)。

## 13. `np.vstack()`：垂直连接

常用形式：`np.vstack((a, b))`。一维输入先变成一行，再沿 `axis=0` 连接；结果至少二维。除第 0 轴外，其他轴长度需一致。

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))
# [[1 2 3]
#  [4 5 6]]
```

对于原文件的两个 `(2, 2)` 数组，结果为 `(4, 2)`。记成“上下拼接、增加行数”，避免原注释“按列堆叠”的歧义。

依据：[vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html)。

## 14. `np.dstack()`：沿第三个轴连接

常用形式：`np.dstack((a, b))`，返回至少三维的数组。它先把一维 `(N,)` 输入变为 `(1, N, 1)`，二维 `(M, N)` 输入变为 `(M, N, 1)`，再沿 `axis=2` 连接。其他轴长度需一致。

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
r = np.dstack((a, b))
print(r)
# [[[1 5]
#   [2 6]]
#  [[3 7]
#   [4 8]]]
print(r.shape)  # (2, 2, 2)
```

对于三维输入，连接的是已有第三轴，并不总是再新增维度。

依据：[dstack](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html)。

## 15. 连接与堆叠对照

设 `a`、`b` 都是 `(2, 2)` 的二维数组：

| 调用 | 结果形状 | 作用 |
| --- | --- | --- |
| `np.concatenate((a, b), axis=0)` | `(4, 2)` | 上下连接 |
| `np.concatenate((a, b), axis=1)` | `(2, 4)` | 左右连接 |
| `np.stack((a, b), axis=0)` | `(2, 2, 2)` | 新增第 0 轴 |
| `np.stack((a, b), axis=1)` | `(2, 2, 2)` | 新增第 1 轴；布局与上一行不同 |
| `np.hstack((a, b))` | `(2, 4)` | 水平连接 |
| `np.vstack((a, b))` | `(4, 2)` | 垂直连接 |
| `np.dstack((a, b))` | `(2, 2, 2)` | 本例补第三轴后沿第三轴连接 |

## 16. `np.array_split()`：拆分数组

常用形式：`np.array_split(ary, indices_or_sections, axis=0)`。第二个参数可为正整数份数，也可为切分位置列表。返回由子数组组成的 Python 列表，普通数组的这些子数组共享原数组的数据。

```python
arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.array_split(arr, 3)
print(parts[0])  # [1 2]
print(parts[1])  # [3 4]
print(parts[2])  # [5 6]

print(np.array_split(arr, 4))
# [array([1, 2]), array([3, 4]), array([5]), array([6])]
print(np.array_split(arr, [2, 5]))
# [array([1, 2]), array([3, 4, 5]), array([6])]
```

不能整除时，前面的部分会多分到一个元素。原文件的 `np.array_split(arr, 3, axis=1)` 会出错，因为一维 `arr` 没有第 1 轴。按列拆分要先有二维数组，例如：

```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
columns = np.array_split(arr2, 3, axis=1)
print(columns[0])  # [[1], [4]]，shape 为 (2, 1)
```

依据：[array_split](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html)。

## 17. `np.where()`：查询条件成立的位置，或按条件选值

原文件使用 `np.where(condition)`：返回索引数组构成的元组，每个维度对应一个索引数组。

```python
arr = np.array([1, 2, 3, 4, 4])
x = np.where(arr == 2)
y = np.where(arr % 2 == 0)
print(x)     # (array([1]),)
print(y)     # (array([1, 3, 4]),)
print(y[0])  # [1 3 4]
```

这里得到的是位置，不是元素值。末尾逗号表示这是一个单元素元组。另一种常用形式是 `np.where(condition, x, y)`：条件真时取 `x`，否则取 `y`，三者需要能广播到共同形状。

```python
print(np.where(arr % 2 == 0, arr, 0))  # [0 2 0 4 4]
```

依据：[where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)。

## 18. `np.searchsorted()`：查询保持升序的插入位置

常用形式：`np.searchsorted(a, v, side='left')`。`a` 是已按升序排列的一维数组；返回插入位置，不会真的插入或修改数组。`v` 为单值时返回整数，为数组时返回对应位置数组。

```python
arr = np.array([1, 2, 3, 4, 4])
print(np.searchsorted(arr, 3))                # 2
print(np.searchsorted(arr, 3, side='right'))  # 3
print(np.searchsorted(arr, 4, side='left'))   # 3
print(np.searchsorted(arr, 4, side='right'))  # 5
print(np.searchsorted(arr, [0, 5]))           # [0 5]
```

`left` 放在已有相等元素之前，`right` 放在已有相等元素之后。一般内部位置 `i` 满足：

| 参数 | 条件 |
| --- | --- |
| `side='left'` | `a[i-1] < v <= a[i]` |
| `side='right'` | `a[i-1] <= v < a[i]` |

边界位置可为 `0` 或数组长度，此时不应真的访问不存在的邻居。原注释“左开右闭/左闭右开”可对应上述不等式，但不足以说明插入位置的含义。未排序输入需先排序，或提供合法的 `sorter` 排序索引。

依据：[searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html)。

## 19. `np.sort()`：返回排序后的数组

常用形式：`np.sort(a, axis=-1)`。对普通数值按升序排序，返回副本，不原地修改 `a`。默认沿最后一轴排序；二维时相当于每行分别排序，`axis=0` 则每列分别排序，`axis=None` 先展平。

```python
arr = np.array([1, 5, 7, 2, 3, 8, 4, 5, 8])
result = np.sort(arr)
print(result)  # [1 2 3 4 5 5 7 8 8]
print(arr)     # [1 5 7 2 3 8 4 5 8]，保持原顺序
```

依据：[sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)。

## 20. 布尔索引、比较与取余

一维数组可用等长布尔列表或布尔数组筛选，`True` 保留、`False` 排除。读取 `arr[mask]` 返回选中数据的副本。

```python
arr = np.array([1, 2, 3, 4, 5, 6])
mask = [True, False, True, True, False, True]
print(arr[mask])  # [1 3 4 6]

arr1 = np.array([12, 44, 66, 34, 72, 77, 55, 44])
mask1 = arr1 > 62
mask2 = arr1 % 2 == 0
print(arr1[mask1])  # [66 72 77]
print(arr1[mask2])  # [12 44 66 34 72 44]
```

`>`、`==` 对数组逐元素比较，返回布尔数组；`%` 是逐元素取余。因此 `arr1 % 2 == 0` 表示筛选偶数。原代码中 `filiter` 拼写虽不常见，但作为自定义变量名合法；保持引用一致即可。

依据：[布尔索引](https://numpy.org/doc/stable/user/basics.indexing.html#boolean-array-indexing)。

## 21. Python 自带的函数和方法

这些调用也出现在脚本中，但不是 NumPy 的函数。

### `print()`：输出对象

`print(*objects, sep=' ', end='\n')` 把对象输出到终端；默认对象之间用空格，末尾换行，返回 `None`。

```python
arr = np.array([1, 2, 3])
print(arr, arr.shape)  # [1 2 3] (3,)
```

### `type()`：查看对象类型

脚本使用单参数形式 `type(object)`，返回类型对象。

```python
arr = np.array([1, 2, 3])
print(type(arr))  # <class 'numpy.ndarray'>
```

### `list.append()`：向列表末尾追加一个元素

`列表.append(value)` 原地修改列表，返回 `None`。原文件用于逐个生成筛选条件，它不是 `np.append()`。

```python
arr1 = np.array([12, 44, 66, 34, 72, 77, 55, 44])
filter_arr = []
for i in arr1:
    if i > 62:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
print(arr1[filter_arr])  # [66 72 77]
```

### 注释中的 `len`：长度概念

原文件只在切片注释中提到 `len`，没有实际调用。`len(a)` 返回容器长度；对非零维 NumPy 数组，返回第 0 轴长度，而非所有元素的总数。例如 `len(np.array([[1, 2, 3], [4, 5, 6]]))` 为 `2`。零维数组不能使用 `len()`。

依据：[Python 内置函数](https://docs.python.org/3/library/functions.html)、[列表 append](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)。

## 22. 原代码注释与使用问题汇总

| 原写法或理解 | 核实后的说明 |
| --- | --- |
| “副本是 copy 到寄存器” | 副本复制数组数据，不表示复制到 CPU 寄存器 |
| “视图没有数据” | 视图共享底层数据，自身仍是可访问数据的数组对象 |
| “base 只有能返回值的才有数据” | `None` 常表示自有数据；其他值是底层对象引用 |
| “reshape 后是视图” | 尽可能返回视图，必要时会复制 |
| `concatenate` 默认“沿列连接” | 准确写为沿 `axis=0`，二维时上下连接、增加行数 |
| `hstack` / `vstack` 的行列注释 | 二维时分别是左右拼接 / 上下拼接 |
| 一维 `arr` 使用 `array_split(..., axis=1)` | 轴不存在，需改用 `axis=0` 或二维数据 |
| `searchsorted` 只记开闭区间 | 应理解为相等元素之前或之后的插入位置 |
| 三行数组就是三维 | 三行矩阵仍是二维，例如形状 `(3, 3)` |

这些修正记录在笔记中；原 Python 文件未作修改。

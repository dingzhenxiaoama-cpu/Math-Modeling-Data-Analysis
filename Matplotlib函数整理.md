# Matplotlib 函数与绘图用法整理

来源：[matplotlid_learning.py](matplotlid_learning.py)。覆盖执行中的代码、`#` 注释调用，以及三引号中的停用代码。文件名虽写作 `matplotlid_learning.py`，实际导入的绘图库是 `matplotlib`。

内容依据 Matplotlib、NumPy 官方文档核实。下面列出常用调用形式和原脚本涉及的参数，不穷举所有高级参数。各示例独立练习时，先执行以下导入；一个绘图示例中的代码按顺序运行。

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as ny
```

`plt` 和 `ny` 是自定义别名；本文件的 `ny.array()` 与常见写法 `np.array()` 是同一个 NumPy 函数。

## 1. 覆盖清单

| 分类 | 原脚本中出现的内容 |
| --- | --- |
| 子图和文字 | `plt.subplot()`、`plt.title()`、`plt.xlabel()`、`plt.ylabel()`、`plt.suptitle()` |
| 线图、散点图 | `plt.plot()`、`plt.scatter()` |
| 柱状图、直方图、饼图 | `plt.bar()`、`plt.barh()`、`plt.hist()`、`plt.pie()` |
| 辅助设置、显示 | `plt.grid()`、`plt.colorbar()`、`plt.legend()`、`plt.show()` |
| 全局配置（不是函数） | `matplotlib.rcParams['font.sans-serif']` |
| 本脚本使用的 NumPy 函数 | `ny.array()`、`ny.random.normal()` |

`pyplot` 会操作“当前图”和“当前坐标区”。一张 Figure 可以包含多个 Axes（坐标区/子图）；大多数 `plt` 调用影响当前 Axes，`suptitle` 设置整张 Figure 的标题。依据：[pyplot 官方说明](https://matplotlib.org/stable/api/pyplot_summary.html)。

## 2. `matplotlib.rcParams`：设置全局默认样式

这是配置对象，不是函数。脚本中的赋值设置无衬线字体候选列表：

```python
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
```

默认字体族使用 `sans-serif` 时，会按候选列表尝试字体。`KaiTi` 是楷体字体名；是否能生效取决于系统是否安装该字体，以及字体是否包含所需字符。建议在绘图前设置，它影响当前 Python 进程的默认绘图配置，不等于永久修改系统字体。

依据：[rcParams 与样式配置](https://matplotlib.org/stable/users/explain/customizing.html)。

## 3. `ny.array()`：为绘图准备数组

常用形式：`ny.array(object, dtype=None)`，将列表等数据转换为 NumPy 数组，返回 `ndarray`。`dtype` 可指定元素类型。

```python
xpoints = ny.array([1, 2, 6, 10])
ypoints = ny.array([10, 5, 4, 6])
categories = ny.array(['A', 'B', 'C', 'D'])
```

数组可保存数值或字符串。绘图函数通常也接受 Python 列表，所以并非每次绘图都必须先转成 NumPy 数组。

依据：[numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)。

## 4. `plt.subplot()`：创建或选择子图

常用形式：`plt.subplot(nrows, ncols, index)`，在当前 Figure 的网格中创建或选中一个 Axes，返回该 Axes，并将其设为当前坐标区。

| 参数 | 含义 |
| --- | --- |
| `nrows` | 网格行数 |
| `ncols` | 网格列数 |
| `index` | 位置编号，从 `1` 开始，先从左到右，再从上到下 |

```python
plt.subplot(1, 2, 1)  # 1 行 2 列，选中左图
plt.plot([1, 2, 3], [2, 4, 6])
plt.title('Left')
plt.subplot(1, 2, 2)  # 选中右图
plt.plot([1, 2, 3], [6, 4, 2])
plt.title('Right')
plt.show()
```

这里的位置编号从 `1` 开始，与 NumPy 索引从 `0` 开始不同。

依据：[subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)。

## 5. `plt.plot()`：画折线或点标记

常用形式：`plt.plot(x, y, fmt, **kwargs)`，其中 `fmt` 可省略。返回 `Line2D` 对象组成的列表。一维输入中，`x` 与 `y` 长度应一致；只传 `y` 时，横坐标默认为 `0, 1, ...`。

```python
xpoints = ny.array([1, 2, 6, 10])
ypoints = ny.array([10, 5, 4, 6])
plt.plot(xpoints, ypoints, 'o:r')
plt.show()
```

原代码 `'o:r'` 的含义是：`o` 为圆形标记，`:` 为点线，`r` 为红色。它不包含线宽信息。常用关键字：

| 参数 | 含义 | 示例 |
| --- | --- | --- |
| `color` | 颜色 | `'red'` |
| `linestyle` | 线型 | `'-'`、`'--'`、`':'`、`'-.'` |
| `marker` | 点标记 | `'o'` |
| `linewidth` | 线宽，单位为 point | `2` |
| `label` | 图例项文字 | `'Group A'` |

原停用代码 `plt.plot(x2,y2,color = red,linestyle = : )` 不能直接运行：`:` 应写成字符串，`red` 不加引号会被当作变量名。正确示例：

```python
x2 = ny.array([1, 2, 3, 4, 5])
y2 = ny.array([2, 6, 7, 10, 1])
plt.plot(x2, y2, color='red', linestyle=':', linewidth=2)
plt.show()
```

依据：[plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)。

## 6. `plt.title()`：设置当前子图标题

常用形式：`plt.title(label, fontsize=..., loc='center')`。`label` 是标题文字；`fontsize` 控制字号；`loc` 可为 `'left'`、`'center'`、`'right'`。返回标题的 `Text` 对象。

```python
plt.plot([1, 2, 3], [2, 5, 4])
plt.title('函数图像', fontsize=14)
plt.show()
```

使用多个子图时，先 `subplot(...)` 选中目标子图，再设置标题。

依据：[title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)。

## 7. `plt.xlabel()`、`plt.ylabel()`：坐标轴名称

`plt.xlabel(xlabel, labelpad=..., fontsize=...)` 设置当前子图的横轴标签；`plt.ylabel(ylabel, labelpad=..., fontsize=...)` 设置纵轴标签。均返回 `Text` 对象。`labelpad` 是标签与坐标轴区域的间距，单位为 point。

```python
plt.plot([1, 2, 3], [2, 5, 4])
plt.xlabel('时间 / s')
plt.ylabel('速度 / m/s')
plt.show()
```

这两个函数设置的是轴名称，并不会修改数据或直接设置刻度值。

依据：[xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)、[ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)。

## 8. `plt.grid()`：控制网格

常用形式：`plt.grid(visible=None, which='major', axis='both', **kwargs)`。

| 参数 | 作用 |
| --- | --- |
| `visible=True/False` | 明确开启或关闭网格 |
| `which` | `'major'` 主刻度网格、`'minor'` 次刻度网格、`'both'` 两者 |
| `axis` | `'x'`、`'y'`、`'both'` |
| `color`、`linestyle`、`linewidth` | 网格线颜色、线型、宽度 |

```python
plt.plot([1, 2, 3], [2, 5, 4])
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.show()
```

原文件的空参数 `plt.grid()` 是切换网格显示状态，连续调用可能又关掉网格。希望明确开启时用 `plt.grid(True)`。返回值为 `None`。

依据：[grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)。

## 9. `plt.suptitle()`：整张图的总标题

常用形式：`plt.suptitle(t, fontsize=..., x=0.5, y=0.98)`。`t` 是文字，`x`、`y` 是相对 Figure 的位置坐标，返回 `Text` 对象。

```python
plt.subplot(1, 2, 1)
plt.plot([1, 2], [2, 3])
plt.title('A')
plt.subplot(1, 2, 2)
plt.plot([1, 2], [3, 2])
plt.title('B')
plt.suptitle('两组数据对比')
plt.show()
```

`title` 属于当前子图，`suptitle` 属于整张图。

依据：[suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html)。

## 10. `plt.scatter()`：绘制散点图

常用形式：`plt.scatter(x, y, s=None, c=None, cmap=None, alpha=None)`。返回 `PathCollection`，可交给 `colorbar` 使用。

| 参数 | 含义 |
| --- | --- |
| `x`、`y` | 点的横纵坐标，点数应一致 |
| `s` | 标记大小，单位为 points²；不是半径 |
| `c` | 颜色，或需要映射成颜色的数值 |
| `cmap` | 数值到颜色的映射方案，例如 `'viridis'` |
| `alpha` | 透明度，`0` 透明、`1` 不透明 |

原文件 `x`、`y` 都有 13 个元素，而 `colors` 只有 11 个数值，取消注释运行时会报长度不匹配。若每个点对应一个颜色数值，应有 13 个：

```python
x = ny.array([1, 2, 5, 11, 9, 6, 3, 5, 2, 5, 3, 6, 8])
y = ny.array([20, 40, 50, 6, 80, 40, 67, 89, 94, 57, 28, 79, 55])
colors = ny.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
points = plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar(points)
plt.show()
```

若只要单一颜色，用 `plt.scatter(x, y, color='red')` 即可，此时不需要数值颜色映射。

依据：[scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)。

## 11. `plt.colorbar()`：添加颜色与数值的对照条

常用形式：`plt.colorbar(mappable=None, orientation='vertical', label=...)`。`mappable` 可传入散点图返回的对象；省略时尝试使用当前可映射对象。返回 `Colorbar`。

```python
points = plt.scatter([1, 2, 3], [4, 6, 5], c=[10, 20, 30], cmap='viridis')
plt.colorbar(points, label='数值')
plt.show()
```

它说明颜色对应的数值范围，不是类别图例。通常先画使用数值颜色映射的图，再添加颜色条；明确传入 `points` 可以避免多个图对象时关联错误。

依据：[colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html)。

## 12. `plt.bar()`：竖直柱状图

常用形式：`plt.bar(x, height, width=0.8, bottom=0, color=...)`，返回 `BarContainer`。

| 参数 | 含义 |
| --- | --- |
| `x` | 横轴位置或类别 |
| `height` | 每根柱的高度，即数据值 |
| `width` | 柱子的横向宽度 |
| `bottom` | 柱子的纵向起点 |
| `color` | 单一颜色或颜色序列 |

```python
x = ny.array(['A', 'B', 'C', 'D'])
y = ny.array([9, 1, 10, 4])
plt.bar(x, y, width=0.6, color='blue')
plt.show()
```

依据：[bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)。

## 13. `plt.barh()`：水平柱状图

常用形式：`plt.barh(y, width, height=0.8, left=0, color=...)`，返回 `BarContainer`。

| 参数 | 含义 |
| --- | --- |
| `y` | 纵轴位置或类别 |
| `width` | 每根水平柱的长度，即数据值 |
| `height` | 柱子的纵向厚度 |
| `left` | 柱子的横向起点 |

```python
categories = ny.array(['A', 'B', 'C', 'D'])
values = ny.array([9, 1, 10, 4])
plt.barh(categories, values, height=0.6, color='green')
plt.show()
```

原文件 `plt.barh(x, y)` 的变量名合法：第一个实参虽然名叫 `x`，仍传给函数的纵向位置参数。原注释的 `heigh` 应为 `height`。在同一坐标区连续调用 `bar` 和 `barh` 会叠加图形，不会自动分成两张图；要对比可先用 `subplot` 分别选中两个子图。

依据：[barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html)。

## 14. `ny.random.normal()`：生成正态分布样本

这是 NumPy 的函数。常用形式：`ny.random.normal(loc=0.0, scale=1.0, size=None)`。

| 参数 | 含义 |
| --- | --- |
| `loc` | 分布均值 |
| `scale` | 分布标准差，必须非负 |
| `size` | 样本数量或输出形状，如 `250`、`(10, 25)` |

```python
x = ny.random.normal(170, 10, 250)
```

这里生成 250 个样本，所设分布均值为 170、标准差为 10、方差为 100。原注释把 `10` 说成方差，需要纠正。有限随机样本的实际均值与标准差不保证恰好等于设定值；未固定随机状态时每次结果通常不同。

有 `size` 时返回相应形状数组；标量参数且 `size=None` 时返回一个随机数。官方建议新项目使用 `Generator` 的方法，但这里保留并解释原脚本的调用形式。

依据：[numpy.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)。

## 15. `plt.hist()`：统计并绘制直方图

常用形式：`plt.hist(x, bins=..., density=False, color=...)`。先按区间分组计数，再画出分布；单组数据返回 `(n, bins, patches)`，分别是各组统计值、区间边界、图形对象集合。

| 参数 | 含义 |
| --- | --- |
| `x` | 原始样本数据 |
| `bins` | 分组数量或边界序列；未指定时遵循配置，默认配置为 10 组 |
| `density=False` | 默认画频数；设为 `True` 时画概率密度 |
| `color` | 颜色 |

```python
x = ny.random.normal(170, 10, 250)
n, edges, patches = plt.hist(x, bins=15, color='blue')
plt.xlabel('数值')
plt.ylabel('频数')
plt.show()
```

柱状图 `bar` 通常展示各类别已有的数值，`hist` 则对原始样本进行分箱统计。`density=True` 归一化的是总面积，不是要求各柱高度之和为 1。

依据：[hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)。

## 16. `plt.pie()`：绘制饼图

常用形式：`plt.pie(x, labels=..., colors=..., startangle=0, explode=None, shadow=False, autopct=None)`。输入为一维非负数值，总和应大于零；默认将数值归一化成占比，所以不要求它们本来就加起来等于 100。

| 参数 | 含义 |
| --- | --- |
| `x` | 各扇区对应的数值 |
| `labels` | 扇区名称，数量与数据一致 |
| `colors` | 扇区颜色序列；不足时循环使用 |
| `startangle` | 从正 x 轴逆时针旋转的起始角，单位为度 |
| `explode` | 各扇区偏移量，占圆半径的比例，数量与数据一致 |
| `shadow` | 是否显示阴影 |
| `autopct` | 百分比格式，例如 `'%1.1f%%'`；这是补充参数，原脚本未用 |

```python
y = ny.array([35, 25, 25, 15])
mylabels = ['A', 'B', 'C', 'D']
mycolors = ['red', 'blue', 'pink', 'green']
myexplode = [0, 0.1, 0, 0]
plt.pie(y, labels=mylabels, colors=mycolors,
        startangle=90, explode=myexplode, shadow=True)
plt.legend(title='four alpha:')
plt.show()
```

`startangle=90` 让第一块从正上方开始，默认逆时针排列。`explode` 中第二项 `0.1` 表示第二块向外偏移半径的 10%。默认返回 `(wedges, texts)`；提供 `autopct` 时再多返回百分比文字列表 `autotexts`。

依据：[pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html)。

## 17. `plt.legend()`：显示图例

常用形式：`plt.legend(title=..., loc='best')`，返回 `Legend` 对象。通常根据当前坐标区中图形对象的标签生成图例。

```python
plt.plot([1, 2, 3], [2, 4, 6], label='Group A')
plt.legend(title='Groups', loc='upper left')
plt.show()
```

`title` 是图例标题，不是整张图的标题；`loc` 控制图例位置。没有可用标签时，单独调用 `legend()` 不会自动理解每组数据的含义。原饼图已经通过 `labels=mylabels` 为扇区设置名称，因此 `plt.legend(title='four alpha:')` 可以利用这些标签。

依据：[legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)。

## 18. `plt.show()`：显示已创建的图形

常用形式：`plt.show(block=None)`。显示所有打开的 Figure，返回 `None`。普通非交互脚本中通常会阻塞，直到图形窗口关闭；Notebook 或 IDE 的行为取决于绘图后端和交互模式。

```python
plt.plot([1, 2, 3], [2, 4, 6])
plt.title('Example')
plt.show()
```

一般放在数据绘制、标题、标签等设置完成后。它负责显示，不负责保存图片。

依据：[show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)。

## 19. 原代码中需要注意的问题

| 原代码或注释 | 准确说明或改法 |
| --- | --- |
| `'o:r'` 旁注为颜色、线型、线宽 | 实际是圆形标记、点线、红色；线宽另用 `linewidth` |
| `color = red, linestyle = :` | 应为 `color='red', linestyle=':'` |
| 散点图中 13 个点、11 个颜色数值 | 每点一个映射数值时，颜色数组长度必须为 13 |
| `plt.grid()` 只注为网格 | 空调用是切换；明确开启用 `plt.grid(True)` |
| `barh` 注释写 `heigh` | 正确参数是 `height`，控制水平柱厚度 |
| `normal(170,10,250)` 注释写方差 10 | 标准差 10，方差 100 |
| 连续调用 `bar`、`barh` | 在当前坐标区叠加；分开展示需分别选中子图 |
| 设置 `KaiTi` 就一定显示楷体 | 还要求系统有对应字体且覆盖所需字符 |

三引号里的语法错误不会作为 Python 代码执行；取消三引号启用对应片段后才会暴露。以上问题已在本笔记的示例中修正，原 Python 文件未作修改。

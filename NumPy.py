import numpy as np

'''
#print(np.__version__)
a = np.array(1)
b = np.array([1,2,3])
c = np.array([[1,2,3],
             [1,2,3]])
d = np.array([[1,2,3],
             [1,2,3],
             [1,2,3]])
'''

#ndim检查维度
'''
print(a)
print(a.ndim)
print(b)
print(b.ndim)
print(c)
print(c.ndim)
#索引（0开始）
print(d[2,2])
#数据裁切[start:end:step](默认分别为0，len，1)
print(b[0:2:1])
#print(type(arr))
'''

#副本与视图(副本是copy到寄存器，视图是指针)(副本有数据，视图没有数据)
'''
a = np.array([0,1,2,3,4,5])
b = a.copy()
c = a.view()
a[0] = 99
print(a)
print(b)
print(c)
print(a.base)#检查数据，只有能返回值的才有数据
print(b.base)
print(c.base)
'''

#数组重塑,reshape后是视图
'''
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape(4,3)#4行3列
c = a.reshape(2,3,2)
d = c.reshape(-1)#用-1展平数组，变成1D
print(a)
print(b)
print(c)#三维
print(d)
'''

#使用nditer迭代数组
'''
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
for x in np.nditer(arr):
    print(x)
for y in np.ndenumerate(arr):#增加索引
    print(y)
'''

#数组的连接
'''
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr3 = np.concatenate((arr1,arr2))#沿列连接
print(arr3,arr3.shape)
arr4 = np.concatenate((arr1,arr2),axis=1)
print(arr4,arr4.shape)
arr5 = np.stack((arr1,arr2),axis=0)#按行堆叠新的维度
print(arr5,arr5.shape)
arr6 = np.stack((arr1,arr2),axis=1)#按列堆叠新的维度
print(arr6,arr6.shape)
arr7 = np.hstack((arr1,arr2))#按行堆叠
print(arr7,arr7.shape)
arr8 = np.vstack((arr1,arr2))#按列堆叠
print(arr8,arr8.shape)
arr9 = np.dstack((arr1,arr2))#按深度堆叠
print(arr9,arr9.shape)
'''

#拆分数组
'''
arr = np.array([1,2,3,4,5,6])
new_arr = np.array_split(arr,3)
print(new_arr)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])
arr2 = np.array_split(arr,3,axis=1)
print(arr2)
'''

#数组搜索
'''
arr = np.array([1,2,3,4,4])
x = np.where(arr==2)
y = np.where(arr%2==0)
z = np.searchsorted(arr,3)#左开右闭
w = np.searchsorted(arr,3,side = 'right')#左闭右开
print(x)
print(y)
print(z)
print(w)
'''

#数组排序
'''
arr = np.array([1,5,7,2,3,8,4,5,8])
print(np.sort(arr))
'''

#数组过滤
arr = np.array([1,2,3,4,5,6])
x = [True,False,True,True,False,True]
print(arr[x])

arr1 = np.array([12,44,66,34,72,77,55,44])
filiter_arr = []
for i in arr1:
    if i > 62:
        filiter_arr.append(True)
    else:
        filiter_arr.append(False)
newarr = arr1[filiter_arr]

print(filiter_arr)
print(newarr)
print(np.sort(newarr))

filiter = arr1 > 62
arr3 = arr1[filiter]
filiter2 = arr1 % 2 == 0
arr4 = arr1[filiter2]
print(arr3)
print(filiter)
print(arr4)
print(filiter2)
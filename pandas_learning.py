import numpy as np
import pandas as pd

'''
s = pd.Series([1,3,5,np.nan,6,8])
df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index = list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype = 'int32'),
                    'E':pd.Categorical(['text','train','text','train']),
                    'F':'foo'})
#print(df2)

df3 = pd.date_range('20130101',periods=6)
#print(df3)

df = pd.DataFrame(np.random.randn(6,4),index = df3 ,columns= list('ABCD'))
#print(df)
'''

#查照数据
'''
print(df.head())
print(df.tail())
print(df.index)
'''

#排序
'''
print(df.sort_index( axis = 1 , ascending = False))#axis 按照第x维排序，ascending = True升序
print(df.sort_values(by = 'B'))#B列按值开始从小到大排序
'''

#选择数据
'''
print(df['A'])#选择单列
print(df[1:3])#对行切片
print(df['2013-01-02':'2013-01-05'])#按索引切片
print(df.loc['2013-01-02'])#按标签选择
print(df.loc[ :, ['A','B']])#取出多个列
print(df.loc['2013-01-02':'2013-01-05',['A','B']])#用标签切片
print(df.loc['2013-01-02','A'])#取出特定行列的元素
print(df.at['2013-01-02','A'])#取出特定行列的元素(快速)
#按照位置取
print(df.iloc[3])#取出第4行数据
print(df.iloc[3:5,0:2])#取出第2-4行，1-2列的元素
print(df.iloc[[1,2,4],[0,2]])#取出第二行，第三行，第五行，第一列。第三列元素
print(df.iloc[1,1])#提取特定坐标
print(df.iat[1,1])#快速提取特定坐标
'''

#筛选
'''
print(df[df['B']>0])
print(df[df>0])
df3 = df.copy()
df3['E'] = ['one','two','three','four','five','six']
print(df3)
df3[df3['E'].isin(['two','four'])]
'''

#赋值
'''
df.at['2013-01-02','A'] = 0#按标签赋值
print(df)
df.iat[0,2] = 1#按坐标赋值
print(df)
df['G']=[1,2,3,4,5,6]#给数组赋值
print(df)
df3 = df.copy()
df3[df3<0] = 0
print(df3)
'''

#空值
'''
df1 = df.reindex(index = s[0:4],columns=list(df.columns+['E']))
df1.loc[d[0]:d[1],'E']=1
print(df1)
df1.dropna(how='any')
df1.fillna(value=5)
pd.isna(df1)
'''

#算数运算
df1 = pd.DataFrame(np.random.randn(2,5))
df2 = pd.DataFrame(np.random.randn(3,4))
print("df1 + df2 \n",df1+df2)
print("df1 - df2 \n",df1 - df2)
print("df1 * df2 \n",df1 * df2)
print("df1 / df2 \n",df1 / df2)

print("df1 等于 df2 \n",df1.eq(df2))
print("df1 不等于 df2 \n",df1.ne(df2))
print("df1 大于 df2 \n",df1.gt(df2))
print("df1 小于 df2 \n",df1.lt(df2))
print("df1 大于等于 df2 \n",df1.ge(df2))
print("df1 小于等于 df2 \n",df1.le(df2))
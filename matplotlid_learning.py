import matplotlib
import matplotlib.pyplot as plt
import numpy as ny
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']#设置字体

'''
xpoints = ny.array([1,2,6,10])
ypoints = ny.array([10,5,4,6])

plt.subplot(1,2,1)#多图，一行两列,第三个数是索引
plt.plot(xpoints,ypoints, 'o:r')#(color linestyle linewidth)

plt.title("函数图像")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()#网格

x2 = ny.array([1,2,3,4,5])
y2 = ny.array([2,6,7,10,1])

plt.subplot(1,2,2)
plt.plot(x2,y2,color = red,linestyle = : )
plt.title("函数图像2")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()

plt.suptitle("NB")#整张图大标题
'''

'''
x = ny.array([1,2,5,11,9,6,3,5,2,5,3,6,8])
y = ny.array([20,40,50,6,80,40,67,89,94,57,28,79,55])
colors = ny.array([0,10,20,30,40,50,60,70,80,90,100])

plt.scatter( x , y , c = colors , cmap='viridis')
plt.colorbar()#颜色图
#plt.scatter(x,y)#散点图
plt.show()
'''

'''
#柱状图
x = ny.array(["A","B","C","D"])
y = ny.array([9,1,10,4])
plt.bar(x,y)#竖直柱状图 color = "颜色" ，width = k
plt.barh(x,y)#水平柱状图 heigh = k 
plt.show()
'''

'''
#直方图
x = ny.random.normal(170,10,250)#创造均值为170，方差为10，250个数据
plt.hist(x)#直方图
plt.show()
'''

#饼图
y = ny.array([35,25,25,15])
mylabels = (["A","B","C","D"])
mycolors = (["red","blue","pink","green"])
myexplode = ([0,0.1,0,0])

plt.pie(y , labels = mylabels , colors = mycolors , startangle = 90 , explode = myexplode , shadow = True)#标签，颜色，起始角度,突出,阴影
plt.legend(title = "four alpha:")#图例
plt.show()
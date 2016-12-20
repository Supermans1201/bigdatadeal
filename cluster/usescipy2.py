# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
###cluster.py
#导入相应的包
import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import numpy as np
import matplotlib.pylab as plt
name='srm1_d2_0'
import pandas as pd
data = pd.read_csv(name+'.csv',sep=',',encoding='gbk')
datalist= data.values.tolist()

points = data.as_matrix()

#生成待聚类的数据点,这里生成了20个点,每个点4维:

#1. 层次聚类
#生成点与点之间的距离矩阵,这里用的欧氏距离:
disMat = sch.distance.pdist(points,'euclidean')
#进行层次聚类:
Z=sch.linkage(disMat,method='average')
#将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
P=sch.dendrogram(Z)
plt.savefig(name+'plot_dendrogram.png')
#根据linkage matrix Z得到聚类结果:
cluster= sch.fcluster(Z, t=1)

print "Original cluster by hierarchy clustering:\n",cluster

#2. k-means聚类
#将原始数据做归一化处理
data=whiten(points)

#使用kmeans函数进行聚类,输入第一维为数据,第二维为聚类个数k.
#有些时候我们可能不知道最终究竟聚成多少类,一个办法是用层次聚类的结果进行初始化.当然也可以直接输入某个数值.
#k-means最后输出的结果其实是两维的,第一维是聚类中心,第二维是损失distortion,我们在这里只取第一维,所以最后有个[0]
centroid=kmeans(data,max(cluster))[0]

#使用vq函数根据聚类中心对所有数据进行分类,vq的输出也是两维的,[0]表示的是所有数据的label
label=vq(data,centroid)[0]

g={}
for l in label:
    g[l]=g.get(l,0)+1
print g
i=0
for dl in datalist:
    dl.append(label[i])
    i+=1

print datalist
import  numpy
numpy.savetxt(name+'new1.csv',label, delimiter = ',')
print "Final clustering by k-means:\n",label


centroid=kmeans(data,7)[0]

#使用vq函数根据聚类中心对所有数据进行分类,vq的输出也是两维的,[0]表示的是所有数据的label
label=vq(data,centroid)[0]

g={}
for l in label:
    g[l]=g.get(l,0)+1
print g
i=0
for dl in datalist:
    dl.append(label[i])
    i+=1

print datalist
import  numpy
numpy.savetxt(name+'new.csv',label, delimiter = ',')
print "Final clustering by k-means:\n",label


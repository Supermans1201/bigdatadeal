# -*- coding: utf-8 -*-
from numpy import array
from numpy.random import normal, randint
#列表
data = [1, 2, 3]
print data
#数组
data = array([1, 2, 3])
print data
#正态分布
data = normal(0, 10, size=10)
print data
#均匀分布
data2 = randint(0, 10, size=10)
print data2
print data.__class__

#中心位置
from numpy import mean, median
#均值
print '均值',mean(data)
#中位数
print '中位数',median(data)

from scipy.stats import mode
#众数
print  '众数'
print mode(data)

#发散程度
from numpy import mean, ptp, var, std
#极差
print '极差'
print ptp(data)
#方差
print '方差'
print var(data)
#标准差
print '标准差'
print std(data)
#变异系数
print '变异系数'
print mean(data) / std(data)

#偏差程度
from numpy import mean, std

#计算第一个值的z-分数
print 'z-s', (data[0]-mean(data)) / std(data)

from numpy import array, cov, corrcoef

data = array([data, data2])

#计算两组数的协方差
#参数bias=1表示结果需要除以N，否则只计算了分子部分
#返回结果为矩阵，第i行第j列的数据表示第i组数与第j组数的协方差。对角线为方差
print 'cov'
print cov(data, bias=1)

#计算两组数的相关系数
#返回结果为矩阵，第i行第j列的数据表示第i组数与第j组数的相关系数。对角线为1
print 'corr'
print corrcoef(data)

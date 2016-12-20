# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from matplotlib import pyplot
#显示中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
rootdir='F:/bigdata/hraw/0/png'
#绘制柱状图
import os
def draw(grades, xl='test', yl='Frequency', t='for the test',rootdir=rootdir):

    gradeGroup = {}
    #对每一类成绩进行频数统计
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1

    labels = sort(gradeGroup.keys())
    length=len(labels)

    #创建柱状图
    #第一个参数为柱的横坐标
    #第二个参数为柱的高度
    #参数align为柱的对齐方式，以第一个参数为参考标准
    pyplot.bar(range(length), [gradeGroup.get(label, 0) for label in labels], align='center')

    #设置柱的文字说明
    #第一个参数为文字说明的横坐标
    #第二个参数为文字说明的内容
    pyplot.xticks(range(length), [label  for label in labels])

    #设置横坐标的文字说明
    pyplot.xlabel(xl)
    #设置纵坐标的文字说明
    pyplot.ylabel(yl)
    #设置标题
    pyplot.title(t)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test2png.png', dpi=100)
    #绘图
    # pyplot.show()
    pyplot.savefig(os.path.join(rootdir, t + '_bar.png'))
    pyplot.close()

    pyplot.pie([gradeGroup.get(label, 0) for label in labels], labels=labels, autopct='%1.1f%%',shadow = False,startangle = 90,pctdistance = 0.6)
    pyplot.title(t)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test2png.png', dpi=100)
    pyplot.savefig(os.path.join(rootdir, t + '_pie.png'))
    pyplot.close()

grades=['上海','江苏','上海','辽宁','北京','上海','辽宁','辽宁','江西','江西','辽宁','重庆']
draw(grades)

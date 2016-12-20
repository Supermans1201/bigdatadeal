
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
name='srm1_d2_4'
new0='new'
new1='new1'


def drawcsv():
    from printpng import draw
    import pandas as pd
    data = pd.read_csv(name+new0+'.csv',sep=',',encoding='gbk')
    datalist= data.values.tolist()
    g=[dl[0] for dl in datalist]
    draw(g,xl=name,t=name+new0,rootdir='F:/bigdata/pydeal/cluster/png')

    data = pd.read_csv(name+new1+'.csv',sep=',',encoding='gbk')
    datalist= data.values.tolist()
    g=[dl[0] for dl in datalist]
    draw(g,xl=name,t=name+new1,rootdir='F:/bigdata/pydeal/cluster/png')

drawcsv()

# coding="utf-8"
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd

rawexcel = "F:/bigdata/dealed/dealed_num.xlsx"
data = pd.read_excel(rawexcel)
print data
d1=data.corr()
print d1
print "\n"


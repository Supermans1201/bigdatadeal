# coding="utf-8"
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#supplier base infomation
sbi=xlrd.open_workbook("F:/bigdata/dealed/dealed.xlsx")

print sbi.__class__

def getinfo(book):
    sheets=book.sheets()
    for table in sheets:
        print table.name,"(",table.nrows,",",table.ncols,")"
        dealtable(table)
    return ""
from printpng import draw
def dealtable(table):
    ncols=table.ncols
    nrows=table.nrows

    for j in range(1,ncols):
        result=[]
        name=table.cell(0,j).value
        print name
        for i in range (2,nrows):
            result.append(table.cell(i,j).value)
        draw(result,xl=name,t=name,rootdir='F:/bigdata/dealed/png')
        print result
if __name__=="__main__":
    getinfo(sbi)



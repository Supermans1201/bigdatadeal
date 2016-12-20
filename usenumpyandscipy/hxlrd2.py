# coding="utf-8"
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#supplier base infomation
sbi=xlrd.open_workbook("F:\\bigdata\\raw\\sbi.xlsx")
#supplier relationship management
# srm=xlrd.open_workbook("F:\\bigdata\\raw\\srm.xlsx")

# rd='F:/bigdata/hraw/0/png'
# srm =xlrd.open_workbook("F:/bigdata/hraw/0/srm0.xlsx")

# rd='F:/bigdata/hraw/1/png'
# srm =xlrd.open_workbook("F:/bigdata/hraw/1/srm1.xlsx")

rd='F:/bigdata/hraw/1/png'
srm =xlrd.open_workbook("F:/bigdata/hraw/1/srm1.xlsx")

print sbi.__class__

def getinfo(book):
    sheets=book.sheets()
    for table in sheets:
        print table.name,"(",table.nrows,",",table.ncols,")"
        dealtable(table)
    return ""
def dealtable(table):
    ncols=table.ncols
    print ncols
    nrows=table.nrows
    print nrows
    for j in range(ncols):
        result=[]
        for i in range(2,nrows):
            if table.cell(i,j).value=='':
                result.append('NULL')
            else:
                result.append(table.cell(i,j).value)

        xl=table.cell(1,j).value
        tl=table.name+xl
        import printpng as p
        p.draw(result, xl=xl, yl='Frequency', t=tl,rootdir=rd)

if __name__=="__main__":
    getinfo(srm)
    # print "srm"
    # getinfo(srm)


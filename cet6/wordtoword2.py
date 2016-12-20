# coding="utf-8"
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlsxwriter
import os
root= "F:/bigdata/pydeal/cet6"
rawsuffix=".xls"
name="word"
#supplier base infomation
sbi=xlrd.open_workbook(os.path.join(root,name+rawsuffix))


def getinfo(book):
    sheets=book.sheets()
    for table in sheets:
        print table.name,"(",table.nrows,",",table.ncols,")"


        wtexcel(table)
    return ""

def wtexcel(table):
     w=xlsxwriter.Workbook("word2.xls")
     sheet= w.add_worksheet("cet6")
     t=0
     s=0
     for i in range(table.nrows):
         for j in range(table.ncols):
             if not table.cell(i,j).value =="":
                 sheet.write(t,s,table.cell(i,j).value)
                 s=s+1
                 if s==2:
                     s=0
                     t=t+1
     w.close()
     print "123"
if __name__=="__main__":
    getinfo(sbi)

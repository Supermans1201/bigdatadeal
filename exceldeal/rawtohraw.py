# coding="utf-8"
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlsxwriter
import os
root= "F:/bigdata/raw"
root2="F:/bigdata/hraw"
rawsuffix=".xlsx"
suffix=".xlsx"
name="srm"
#supplier base infomation
sbi=xlrd.open_workbook(os.path.join(root,name+rawsuffix))

def dealtable(table):
    list0=[]
    list1=[]
    list2=[]
    list3=[]
    ncols=table.ncols
    for i in range(ncols):
        x=len(set(table.col_values(i)))
        y=len(table.col_values(i))
        score= float(x)/y
        if x<=3:
            list0.append(i)
        elif score<0.05:
            list1.append(i)
        elif score>0.98:
            list2.append(i)
        else:
            list3.append(i)
    dirt={'0':list0,'1':list1,'2':list2,'3':list3}
    return dirt
def getinfo(book):
    sheets=book.sheets()
    # every table

    dirs=['0','1','2','3']

    for s in dirs:
        p=os.path.join(root2,s)
        if not os.path.exists(p):
            os.makedirs(p)
        print os.path.join(p,name+s+suffix)
        w=xlsxwriter.Workbook(os.path.join(p,name+s+suffix))

        for table in sheets:
            print table.name,"(",table.nrows,",",table.ncols,")"
            #{'0':list0,'1':list1,'2':list2,'3':list3}
            dirt=dealtable(table)
            sheet= w.add_worksheet(table.name)
            wtexcel(table,sheet,dirt[s])
        w.close

    return ""

def wtexcel(table,sheet,dirt=[]):
    t=0
    for i in dirt:
        for j in range(table.nrows):
            sheet.write(j,t,table.cell(j,i).value)
        t=t+1
if __name__=="__main__":
    getinfo(sbi)

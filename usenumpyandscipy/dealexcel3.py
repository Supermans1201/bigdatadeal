# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd
#supplier relationship management
srm =xlrd.open_workbook("F:/bigdata/hraw/1/srm1.xlsx")
root ="F:/bigdata/hraw/1/"
name='srm1_d2'
suffix='.xlsx'


def getinfo(book):
    sheets=book.sheets()
    w=xlsxwriter.Workbook(os.path.join(root,name+suffix))

    for table in sheets:
        print table.name,"(",table.nrows,",",table.ncols,")"

        sheet= w.add_worksheet(table.name)
        dealtable(table,sheet)
    w.close()
    return ""
import os
import  xlsxwriter
def dealtable(table,sheet):
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
                result.append((table.cell(i,j).value))
        Group = {}
        for g in result:
            Group[g] = Group.get(g, 0) + 1
        tup=[]
        tup.append(len(Group.keys()))
        print 'keys : ',len(Group.keys())
        r=0
        n=0

        for k in Group.keys():
            if not k == 'NULL':
                r+=Group.get(k)
            else:
                n+=Group.get(k)
        tup.append(r)
        tup.append(n)
        print r,
        print n,
        score=float (n)/(r+n)
        print score,":",
        tup.append(score)
        import getType
        # [key，r，n,f]
        # 0，1，3
        t = getType.type(tup)

        # for g in result:
        #     Group[g] = float(Group[g])/(float(r)/len(Group.keys()))
        for i in range(2):
            sheet.write(i,j,(table.cell(i,j).value))
        for i in range(2,nrows):
            if t==0:
                if table.cell(i,j).value =='':
                     sheet.write(i,j,Group[getRondow(Group)])
                else:
                    sheet.write(i,j,Group[table.cell(i,j).value])
            elif t==1:
                if table.cell(i,j).value =='':
                     sheet.write(i,j,n)
                else:
                    sheet.write(i,j,(Group[table.cell(i,j).value]))
            elif t==2:
               if table.cell(i,j).value =='':
                     sheet.write(i,j,Group[getMax(Group)])
               else:
                    sheet.write(i,j,Group[(table.cell(i,j).value)])
            elif t==3:
                if table.cell(i,j).value =='':
                     sheet.write(i,j,n)
                else:
                     sheet.write(i,j,r)
            else:
                sheet.write(i,j,-1)
import random
def getRondow(Group={}):
    r=0
    for k in Group.keys():
            if not k == 'NULL':
                r+=Group.get(k)
    t=random.randint(0,r)
    for k in Group.keys():
        t=t-Group.get(k)
        if t<=0:
            return k
def getMax(Group={}):
    r=0
    for k in Group.keys():
            if not k == 'NULL':
                r+=Group.get(k)
    t=0
    x=Group.keys()[0]
    for k in Group.keys():
        if t<Group.get(k):
            x=k
            t=Group.get(k)
    return x



if __name__=="__main__":
    getinfo(srm)



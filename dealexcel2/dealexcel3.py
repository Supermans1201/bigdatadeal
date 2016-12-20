# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd
#supplier relationship management
srm =xlrd.open_workbook("F:/bigdata/dealed/dealed.xlsx")
root ="F:/bigdata/dealed/"
name='dealed_num'
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
            result.append((table.cell(i,j).value))

        Group = {}
        for g in result:
            Group[g] = Group.get(g, 0) + 1

        print 'keys : ',len(Group.keys())
        # n=0
        # for g in Group.keys():
        #     n+=Group.get(g)
        # for g in result:
        #     Group[g] = float(Group[g])/(float(n))
        for g in result:
            print  float (Group[g])/400
        base={}
        basenum=0
        for g in Group.keys():
            base[g]=basenum
            basenum+=3
        import random

        for i in range(2):
            sheet.write(i,j,(table.cell(i,j).value))
        for i in range(2,nrows):
             print 'b',base[table.cell(i,j).value]
             print (float(Group[table.cell(i,j).value])/400)
             print random.random()
             sheet.write(i,j,base[table.cell(i,j).value]+(float(Group[table.cell(i,j).value])/400)*random.random())
        basenum=0
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



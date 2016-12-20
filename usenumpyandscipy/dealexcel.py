# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd
#supplier relationship management
srm =xlrd.open_workbook("F:/bigdata/hraw/1/srm1.xlsx")
root ="F:/bigdata/hraw/1/"
name='srm1_d'
suffix='.xlsx'

ci=[];
def getinfo(book):
    sheets=book.sheets()
    w=xlsxwriter.Workbook(os.path.join(root,name+suffix))

    for table in sheets:
        print table.name,"(",table.nrows,",",table.ncols,")"

        sheet= w.add_worksheet(table.name)
        dealtable(table,sheet)
    w.close()
    print ci
    return ""
import csv
def savecsv():

    csvfile = file('null.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['o', 't','f'])
    d= [(key[0],key[2],key[3]) for key in ci]
    writer.writerows(d)
    csvfile.close()
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
                result.append(str(table.cell(i,j).value))

        xl=table.cell(1,j).value
        tl=table.name+xl
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
        print score
        tup.append(score)
        ci.append(tup)
        # for g in result:
        #     Group[g] = float(Group[g])/(float(r)/len(Group.keys()))
        # for i in range(2):
        #     sheet.write(i,j,(table.cell(i,j).value))
        # for i in range(2,nrows):
        #     sheet.write(i,j,Group.get(str(table.cell(i,j).value)))

if __name__=="__main__":
    getinfo(srm)
    # print "srm"
    # getinfo(srm)
    savecsv()


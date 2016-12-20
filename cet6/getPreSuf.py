# coding="utf-8"
import xlrd
import xlutils
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlsxwriter
import os
root= "F:/bigdata/pydeal/cet6"
rawsuffix=".xls"
pname="prefixes"
#supplier base infomation
prepath =os.path.join(root,pname+rawsuffix)
sname="suffixes"
sufpath=os.path.join(root,sname+rawsuffix)

import re

def getPre(word):
    excel=xlrd.open_workbook(prepath)
    sheets=excel.sheets()
    list=[]
    for sheet in sheets:
        nrow=sheet.nrows
        ncol=sheet.ncols
        for j in range(ncol):
            for i in range(nrow):
                s=sheet.cell(i,j).value
                if re.match(s,word,re.I):
                    list.append(s)
    temp=""
    for l in list:
        if len(temp)<len(l):
            temp=l

    return temp

def getSuf(word):
    excel=xlrd.open_workbook(sufpath)
    sheets=excel.sheets()
    list=[]
    for sheet in sheets:
        nrow=sheet.nrows
        ncol=sheet.ncols
        for j in range(ncol):
            for i in range(nrow):
                s=sheet.cell(i,j).value

                if re.search(s+'$',word,re.I):
                    list.append(s)

    temp=""
    for l in list:
        if len(temp)<len(l):
            temp=l
    return temp
if __name__=="__main__":
    word='weqwer'
    print getPre(word) , "-", "*", "-",getSuf(word)

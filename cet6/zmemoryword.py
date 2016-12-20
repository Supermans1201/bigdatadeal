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
name="word2"

sheetid=2
#supplier base infomation
path =os.path.join(root,name+rawsuffix)

from xlutils.copy import *
def set(excel,row,col=3,t='true'):
    wexcel = xlutils.copy.copy(excel)
    word = wexcel.get_sheet(sheetid)
    word.write(row, col, t)
    wexcel.save(path)
import random
def getword():
    s=">>start"
    print s
    r=-1
    while not s=='exit':
        rexcel=xlrd.open_workbook(path)
        rsheet=rexcel.sheet_by_index(sheetid)

        nrow=rsheet.nrows
        ncol=rsheet.ncols
        r=r+1
        # r=random.randint(1080, 1100)
        word=rsheet.cell(r,0).value
        print ">",word
        raw_input()
        import getPreSuf

        pre=getPreSuf.getPre(word)
        suf=getPreSuf.getSuf(word)
        print pre,word[int(len(pre)):int(len(word)-len(suf))],suf
        print ">",rsheet.cell(r,1).value
        for c in range(ncol):
            if rsheet.cell(r,c).value=='':
                break
        if c<2:
            c=2
        s = raw_input(">")
        if s=="y":
            set(rexcel,r,col=c,t=s)
        if s=="h":
            set(rexcel,r,col=c,t=s)
        if s=="n":
            set(rexcel,r,col=c,t=s)
if __name__=="__main__":
    getword()

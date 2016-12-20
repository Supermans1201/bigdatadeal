# coding="utf-8"
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#supplier base infomation
sbi=xlrd.open_workbook("F:\\bigdata\\raw\\sbi.xlsx")
#supplier relationship management
srm=xlrd.open_workbook("F:\\bigdata\\raw\\srm.xlsx")

print sbi.__class__

def getinfo(book):
    sheets=book.sheets()
    for table in sheets:
        print table.name,"(",table.nrows,",",table.ncols,")"
        dirt2=dealtable(table)
        for d in dirt2['0.05']:
            print d

    return ""
def dealtable(table):
    ncols=table.ncols
    list0=[]
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    dirt={"0":list0,"95":list1,"0.05":list2,"0.3":list3,"else":list4}
    for i in range(ncols):
       # print set(table.col_values(i))
        if len(set(table.col_values(i)))==2:
            pass
            # print "no value"
        else:
            x=len(set(table.col_values(i)))
            y=len(table.col_values(i))
            # print float(x)/y
            if float(x)/y>95:
                pass
                # print "key value"
            elif float(x)/y<0.05:
                dirt['0.05'].append(i)
            elif float(x)/y<0.3:
                pass
            else:
                pass


    return dirt
if __name__=="__main__":
    getinfo(sbi)
    print "srm"
    getinfo(srm)


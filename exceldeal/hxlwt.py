import xlwt

w=xlwt.Workbook()
sheet= w.add_sheet("helloworld")
style = xlwt.easyxf('font: bold 1')
sheet.write(0,0,"hello",style)

w.save("F:/bigdata/hraw/helloworld.xls")

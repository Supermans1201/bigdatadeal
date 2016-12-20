import xlsxwriter
with xlsxwriter.Workbook("F:/bigdata/hraw/helloworld.xlsx") as w:
    sheet= w.add_worksheet("helloworld1")
    w.close()
    w.add_worksheet("helloworld2")
    sheet.write(0,0,"hello")




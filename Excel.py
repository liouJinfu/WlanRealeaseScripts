# --*-- coding: UTF-8 --*--
import subprocess,xml.etree.ElementTree as EI
import re
import sys

import xlrd,xlwt,os
def travelXML(element):
    if len(element) > 0:
        for child in element:
            print(child.tag, '----', child.attrib)
            travelXML(child)
def excelRd():
    workbook = xlrd.open_workbook(r'test.xls',formatting_info=True)

    sheet_names= workbook.sheet_names()
    ###0. empty（空的）,1 string（text）, 2 number, 3 date, 4 boolean, 5 error， 6 blank（空白表格）单元格类型
    for sheet_name in sheet_names:
        everySheet = workbook.sheet_by_name(sheet_name)
        rows = everySheet.row_values(3)
        print(sheet_name, rows) # 获取第四行内容
        cols = everySheet.col_values(1) # 获取第二列内容
        print(rows)
        print(cols)
        print(everySheet.cell(1, 0).value.encode('utf-8'))#获取sheet中第2行第1列的值并转码为utf-8格式
        print(everySheet.cell_type(1, 0))  # 返回单元格中的数据类型
        print(everySheet.cell_value(1, 0))  #返回单元格中的数据
        print(everySheet.col(1, 0, 10))#返回该列中所有的单元格对象组成的列表
        print(everySheet.col_types(1, 0, 10))#返回该列中所有的单元格对象组成的列表
        print(everySheet.merged_cells)##merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),\
        # 其中[row,row_range)包括row,不包括row_range,col也是一样，即(1, 3, 4, 5)的含义是：第1到2行（不包括3）\
        # 合并，(7, 8, 2, 5)的含义是：第2到4列合并。

        ##获取所有的merge的单元格内容
        merge =[]
        for (rlow, rhigh, clow, chigh) in everySheet.merged_cells:
            merge.append([rlow, clow])
        for index in merge:
            print(everySheet.cell_value(index[0], index[1]))
def write_conten(titles, kvalus):
    os.chdir(r"D:\scripts\WlanRealeaseScripts")
    file = xlwt.Workbook()
    table = file.add_sheet("log_info",cell_overwrite_ok=False)
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = "Times New Roman"
    font.bold =True
    style.font = font
    for index in range(0, len(titles)):
        table.write(0, index, titles[index], style)
    for index in range(0, len(kvalus)):
        for index2 in range(0, len(titles)):
            table.write(index+1, index2, kvalus[index].get(titles[index2]))
    file.save("svnlog.xls")

def excelWt():
    file=xlwt.Workbook()
    table = file.add_sheet("mysheet",cell_overwrite_ok=True)
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.bold = True
    style.font = font  # 为样式设置字体
    table.write(0, 0, 'some bold Times text', style)  # 使用样式
    file.save('test2.xls')
if __name__ == '__main__':
    _PATH=r"D:\MyTestSvn\proj\branches\branch1"
    os.chdir(_PATH)
    cmd = r'svn log -r 4:HEAD -v --xml'
    pro = subprocess.Popen(cmd,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    try:
        outs, errs=pro.communicate()
    except Exception:
        print(outs,errs)
    print(outs, errs)
    # os.chdir(r'D:\scripts\WlanLibRelease')
    # FILE = open(r"test1.xml", 'w+')
    # FILE.write(str(outs, 'utf-8'))
    # FILE.close()

    try:

        root=EI.fromstring(outs)
    except Exception as E:
        print("parse test1.xml fail!")
        sys.exit()
    contens = []
    pattern =re.compile(r'(.*).c')
    # commit_attrs = root.findall('logentry/path')
    for item in root.iter('logentry'):
        entry_info={x.tag:x.text  for x in item.getchildren()}
        titles = [x.tag for x in list(item)]
        # write_title(titles)
        print(entry_info)
        for e in item.findall('paths/path'):
            print(e.attrib, e.text)
            entry_info['paths'] = entry_info['paths'] + '\n'+e.text
            if(None != re.match(pattern, e.text)):
                print("find the same :", e.text)
        contens.append(entry_info)
    write_conten(titles, contens)
    # print("root type:", type(root))
    # print(root.tag, "----", root.attrib)
    # #遍历root的下一层
    # for child in root:
    #     print ("遍历root的下一层", child.tag, "----", child.attrib)
    #     captionList = child.findall("author")  # 在当前指定目录下遍历
    #     print(len(captionList))
    #     for caption in captionList:
    #         print(caption.tag, "----", caption.attrib, "----", caption.text)
    #     # 使用下标访问
    # print(root[0].text)
    # # print(root[1][1][0].text)
    #
    # # 根据标签名查找root下的所有标签
    # captionList = root.findall("logentry")  # 在当前指定目录下遍历
    # print(len(captionList))
    # for caption in captionList:
    #     print(caption.tag, "----", caption.attrib, "----", caption.text)
    #
    # print(20 * "*")
    # # 遍历xml文件
    # # travelXML(root)
    # print(20 * "*")


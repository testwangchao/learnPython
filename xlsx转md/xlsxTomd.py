#coding:utf-8
'''
xlsx to md
'''
import xlrd
import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
def OpenFile(fileName):
    #打开xlsx文件
    with xlrd.open_workbook(fileName) as file:
        #选择表
        firstTable = file.sheet_by_index(0)
        #输出的md文件位置
        with open("C:\\Users\\wangchao88\\Desktop\\test.md",'w+') as file2:
            file2.write("|编号|项目名称 |测试标题|操作步骤|预置条件|预期输出|" +
                        '\n' +
                        "|---|--------|------ |--------|--------|--------|"+
                        '\n')
            for i in range(1,firstTable.nrows):
                j = 0
                while j < firstTable.ncols:
                    writeFile = firstTable.cell(i,j).value
                    if isinstance(writeFile,float):
                        file2.write('|'+str(writeFile)+'|')
                    elif '\n' in writeFile:
                        for k in writeFile.split('\n'):
                            file2.write(k+'<br>')
                        file2.write('|')
                    else:
                        file2.write(writeFile+'|')
                    j += 1
                file2.write('\n')
        file2.close()
OpenFile("C:\\Users\\wangchao88\\Desktop\\test.xlsx")
import pandas as pd
import csv
import xlwt
import xlrd
import openpyxl as op


#  使用第三方库pandas将xlsx文件转csv文件
def xlsx_to_csv_pd(name):
    data_xls = pd.read_excel('{}.xlsx'.format(name), index_col=0)
    data_xls.to_csv('{}.txt'.format(name), sep=',', index=False, encoding='utf-8')


#  csv文件转换成xlsx文件
def csv_to_xlsx():
    with open('1.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1

        workbook.save('1.xlsx')  # 保存Excel


#  使用pandas将csv文件转成xlsx文件
def csv_to_xlsx_pd():
    csv = pd.read_csv('1.csv', encoding='utf-8')
    csv.to_excel('1.xlsx', sheet_name='data')


def wz_kj_txt():
    file_write = open('zzzz.txt', "w", encoding="utf-8")
    with open('wz_kj.txt', 'r', encoding='utf-8')as f:
        n = 1
        for i in f:
            data = str(n) + ',' + i
            file_write.write(data)
            n += 1


def txt_write(xlsxname, txtname):
    with open(txtname, mode="w+", encoding="utf-8") as f:
        # 打开指定文件
        xlsx_file = xlsxname
        book = xlrd.open_workbook(xlsx_file)
        # 通过sheet索引获得sheet对象
        sheet01 = book.sheet_by_index(0)
        cellvalue = ''
        # 获得指定索引的sheet名
        # sheet1_name = book.sheet_names()[0]
        # print(sheet1_name)
        # 通过sheet名字获得sheet对象
        # sheet1 = book.sheet_by_name(sheet1_name)
        # 获得行数和列数
        # 总行数
        nrows = sheet01.nrows
        # 总列数
        ncols = sheet01.ncols
        # 遍历打印表中的内容
        for i in range(nrows):
            for j in range(ncols):
                cellvalue = sheet01.cell_value(i, j)
                # 强制转换数字格式
                celltype = sheet01.cell_type(i, j)
                if celltype == 2:
                    cellvalue = str(cellvalue)
                f.write(str(cellvalue) + ",")
            f.write('\n')


def strs(row):
    """
    :返回一行数据
    """
    try:
        values = ""
        for i in range(len(row)):
            if i == len(row) - 1:
                values = values + str(row[i])
            else:
                #使用“，”逗号作为分隔符
                values = values + str(row[i]) + ","
        return values
    except:
        raise


def xls_txt(xls_name):
    """
    :excel文件转换为txt文件
    :param xls_name excel 文件名称
    :param txt_name txt   文件名称
    """
    n = 25807
    try:
        data = xlrd.open_workbook("{}.xlsx".format(xls_name))
        sqlfile = open("{}.txt".format(xls_name), "a", encoding='utf-8')
        table = data.sheets()[0]  # 表头
        nrows = table.nrows  # 行数
        # 如果不需跳过表头，则将下一行中1改为0
        for ronum in range(0, nrows):
            print(ronum)
            n += 1
            row = table.row_values(ronum)
            # num = 0
            # for i in row:
            #     if isinstance (i,float) == True:
            #         i = int(i)
            #         row[num] = str(i)
            #     num += 1
            # if row[6] == 'taobao':
            #     row[6] = '1'
            # elif row[6] == 'tmall':
            #     row[6] = '2'
            # elif row[6] == 'jd':
            #     row[6] = '3'
            # elif row[6] == 'smt':
            #     row[6] = '4'
            # row[1] = '2021'
            row[0] = str(int(row[0]))
            # row[1] = str(int(row[1]))
            # row[2] = str(int(row[2]))
            # row[4] = str(int(row[4]))
            # row[5] = str(int(row[5]))
            # row[6] = str(int(row[6]))
            # row[7] = str(int(row[7]))
            # row[9] = str(int(row[9]))
            # row[8] = str(int(row[8]))
            # row[10] = str(int(row[10]))
            # row[12] = str(int(row[12]))
            # row[13] = str(int(row[13]))
            # # row[3] = row[3]
            # if isinstance(row[4], str) == True:
            #     row[4] = row[4]
            # elif isinstance(row[4], int) == False:
            #     row[4] = str(int(row[4]))
            #
            # # row[5] = str(int(row[5] * 10000))
            # row[6] = str(int(row[6]))
            # row[8] = str(int(row[8])) if len(str(row[8])) > 0 else row[8]
            # row.insert(0, ronum + 1)
            # # row[6] = str(int(row[6]))
            # row[8] = str(int(row[8]))
            # if row[9] == 0.0:
            #     row[9] = str(int(row[9]))
            # row[10] = str(int(row[10]))
            # row[11] = str(int(row[11]))
            # row[0] = str(int(row[0]))
            # row[1] = str(int(row[1]))
            values = strs(row) + '\n'  # 条用函数，将行数据拼接成字符串
            sqlfile.writelines(values)  # 将字符串写入新文件
        sqlfile.close()  # 关闭写入的文件
    except Exception as e:
        print(e)

def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['序号', '酒店', '价格']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]["id"], data[j]["name"], data[j]["price"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


# "-------------数据用例-------------"
testData = [
    {"id": 1, "name": "立智", "price": 100},
    {"id": 2, "name": "维纳", "price": 200},
    {"id": 3, "name": "如家", "price": 300},
]
fileName = '测试.xlsx'
xw_toExcel(testData, fileName)



def pd_toExcel(data, fileName):  # pandas库储存数据到excel
    ids = []
    names = []
    prices = []
    for i in range(len(data)):
        ids.append(data[i]["id"])
        names.append(data[i]["name"])
        prices.append(data[i]["price"])

    dfData = {  # 用字典设置DataFrame所需数据
        '序号': ids,
        '酒店': names,
        '价格': prices
    }
    df = pd.DataFrame(dfData)  # 创建DataFrame
    df.to_excel(fileName, index=False)  # 存表，去除原始索引列（0,1,2...）


if __name__ == '__main__':
    # name = 'dm_county_general_kj'
    # xlsx_to_csv_pd(name)
    # wz_kj_txt()
    # xlsx_name = 'all_jd_goodsinfo_daima_终极'
    # xls_txt(xlsx_name)
    testData = [
        {"id": 1, "name": "立智", "price": 100},
        {"id": 2, "name": "维纳", "price": 200},
        {"id": 3, "name": "如家", "price": 300},
    ]
    # testData = {"id": 1, "name": "立智", "price": 100}
    fileName = '测试2.xlsx'
    pd_toExcel(testData, fileName)




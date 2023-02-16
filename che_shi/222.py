import os
import pandas as pd
import xlrd


def xls_txt():
    """
    :excel文件转换为txt文件
    :param xls_name excel 文件名称
    :param txt_name txt   文件名称
    """
    n = 25807
    data_xlsx_dict = {}
    data = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\工作簿1222.xlsx")
    # sqlfile = open("{}.txt".format(xls_name), "a", encoding='utf-8')
    table = data.sheets()[0]  # 表头
    nrows = table.nrows  # 行数
    # 如果不需跳过表头，则将下一行中1改为0
    for ronum in range(1, nrows):
        print(ronum)
        n += 1
        row = table.row_values(ronum)
        row[0] = str(int(row[0]))
        row[1] = str(int(row[1]))
        row[2] = str(row[2])
        row[3] = str(row[2])
        row[4] = str(int(row[4]))
        row[5] = str(row[5])
        row[6] = str(row[6])
        row[7] = str(int(row[7]))
        row[9] = str(int(row[9]))
        row[8] = str(int(row[8]))
        lac = row[0]
        ci = row[1]
        lac_ci = str(lac) + str(ci)
        data_xlsx_dict[lac_ci] = row
    path = 'D:\影刀\\0921'
    datanames = os.listdir(path)
    list = ['14.log', '15.log', '16.log']
    data_data_list = []
    for path_name in datanames:
        for i in list:
            new_path = path + '\\' + path_name + '\\' + i
            with open(new_path, 'r', encoding='utf-8') as f:
                for data in f:
                    new_data = data.split('|')
                    lac_3 = new_data[3]
                    ci_4 = new_data[4]
                    lac_3_ci_4 = lac_3 + ci_4
                    data_data = data_xlsx_dict.get(lac_3_ci_4)
                    if data_data != None:
                        with open(r'latest_road_info.txt', 'a', encoding='utf-8') as w:
                            w.write(','.join(data_data) + '\n')
                            w.flush()
                            w.close()
    # pd_toExcel(data_data_list, 'latest_road_info.xlsx')
        # values = strs(row) + '\n'  # 条用函数，将行数据拼接成字符串
        # sqlfile.writelines(values)  # 将字符串写入新文件
    # sqlfile.close()  # 关闭写入的文件


if __name__ == '__main__':
    xls_txt()


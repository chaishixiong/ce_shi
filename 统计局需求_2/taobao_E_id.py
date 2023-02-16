import xlrd


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


def xls_txt(xls_name, data_list, e_daima):
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
            n += 1
            row = table.row_values(ronum)
            row[0] = str(int(row[0]))
            str_data = row[1]
            for data in data_list:
                if data in str_data:
                    row[2] = e_daima
                    values = strs(row) + '\n'  # 条用函数，将行数据拼接成字符串
                    sqlfile.writelines(values)  # 将字符串写入新文件
                    sqlfile.close()  # 关闭写入的文件
                    break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    e_daima = 'E301'
    data_list = ['成人用品']
    xlsx_name = '淘宝'
    xls_txt(xlsx_name, data_list, e_daima)


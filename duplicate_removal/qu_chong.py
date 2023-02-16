# -*- coding: UTF-8 -*-
'''
@Author ：Jason
pandas 数据处理,在之前的数据结构基础上升级
'''
from pandas import DataFrame,Series
import pandas as pd


class DataProcessing(object):
    def __init__(self):
        self.data = {
            "age": Series([18, 85, 64, 85, 86]),
            "name": Series(["Jason", "John", "Jerry", "John", "John"])
        }

    def dataClean(self):
        # 5.1 数据清洗:去重 + 缺失值处理

        df = DataFrame(data=self.data)
        print(df)
        '''
           age   name
        0   26  Jason
        1   85   John
        2   64  Jerry
        3   85   John
        4   85   John
        '''
        print(df.duplicated()) #False代表不重复，True 重复
        '''
        0    False
        1    False
        2    False
        3     True
        4     True
        dtype: bool
        '''
        print(df.duplicated("name")) #name重复情况
        '''
        0    False
        1    False
        2    False
        3     True
        4     True
        dtype: bool
        '''
        print(df.drop_duplicates("age")) #去除重复数据
        '''
           age   name
        0   18  Jason
        1   85   John
        2   64  Jerry
        '''
        #缺失值之前处理过，这里初略
        '''
        df.isnull() 缺失True,不缺失为False
        df.notnull() 和上面相反
        df.dropna()  去除缺失行，如果删除列的话，加参数axis=1，参数how="all",全却删除，any有缺就删除
        df.fillna()  填充。df.fillna(value="",method="") value指定值替换缺失值，
                                method参数 pad,前一个替换，bfill，后一个替换，mean()平均值替换
                                df.fillna(df.mean()["填补列名":"计算均值的列名"])，
                                df.fillna({"列名1":值1,"列名2":"值2"}) 不同列不同填充
        df["列或列"].str.strip() 去除空格,和字符用法一致               
        '''

    # 5.2 数据抽取
    def extractionData(self):
        df = pd.read_excel("./FIle/lemon.xlsx",sheet_name="student")
        name = df["name"].str.slice(0,1)  #  抽取名字中的姓,用法字符串切片....
        # print(name) #0  黄 1  华 2  毛 Name: name, dtype: object

        #  5.2.1 重置索引 将name变为索引
        df1 = DataFrame(self.data).set_index("name")
        print(df1)
        '''
               age
        name      
        Jason   18
        John    85
        Jerry   64
        John    85
        John    85
        '''
        #  5.2.3 抽取name = "John"
        print(df1.ix["John"])
        '''
              age
        name     
        John   85
        John   85
        John   85
        '''
    # 5.3 插入记录
    def insertData(self):
        df = pd.DataFrame({
            "a": [1, 2, 3],
            "b": ["a", "b", "c"],
            "c": ["A", "B", "C"]
        })
        line = pd.DataFrame({df.columns[0]:"--",df.columns[1]:"--",df.columns[2]:"--"},index=[1,2,3])
        print(line)
        #  抽取df的index = 1,2,3的行赋值为  "--"
    # 5.4 修改记录:单值替换 和 整行整列替换

    def changeData(self):
        df = DataFrame(self.data)
        df2 = df.replace("Jason","ABC") #  单值替换 为ABC
        print(df2)
        df3 = df.replace(["Jason","John"],["A","b"]) #  A替换Jason,b替换John
        df["age"] = [1,2,3,4,5]
        print(df) #  整列替换  为[1,2,3,4,5]
    # 5.5 交换  行和列

    def changeRowCol(self):
        df = DataFrame(self.data)
        print(df)
        print(df.reindex([1,0,2,3,4])) # 1,2行互换,其他不换
        # print(df.reindex(columns = ["name","age"])) #name 和 age列互换

    # 5.6 排名索引
    def sortIndex(self):
        df0 =  {"China":[9,7,10],"Japan":[6,8,7],"America":[9,5,8]}
        df = DataFrame(df0,index=["a","c","d"])
        # print(df.sort_index(ascending=False)) #默认index升序,False降序
        # print(df.sort_index(by=["China","Japan"])) #by指定列，可以一列也可以多列,但是只有第一列生效

    # 5.7 数据合并 append,concat 数组合并

    #  merge(df1,df2,left_on=index,right_on=index),类似于Excel中的VLOOKUP和sql的多表连接
    def mergeData(self):
        df1 = DataFrame(self.data)
        df2 = DataFrame({
            "name":[4,5,6,7],
            "age":[1,2,3,4]
        })
        df = pd.concat([df1,df2],ignore_index=True)
        # print(df) #合并起来,index自动顺延
        # print(df1.append(df2,ignore_index=True))

        df3 = df2["name"] + df2["age"]
        # print(df3) #变成索引 + 5,7,9,11

        df4 = DataFrame({
            "name":["Jason","John"],
            "age":[18,19]
        })
        df5 = DataFrame({
            "name":["Jason","John"],
            "Phone":[1234567,9897769]
        })
        df6 = pd.merge(df4,df5,left_on="name",right_on="name") #理解为左右连接
        print(df6)


if __name__ == "__main__":
    DP = DataProcessing()
    DP.dataClean()

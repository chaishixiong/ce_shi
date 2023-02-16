# with open(r'a.txt', 'r', encoding='utf-8')as f:
#     for i in f:
#         d = i.strip('\n') + ',' + '2206458909647'
#         print(d)


# -*- coding: UTF-8 -*-
def test():
    books = ('程序员修炼之道', '构建之法', '代码大全', 'TCP/IP协议详解')

    # TODO(you): 此处请为reading进行正确的赋值
    reading = (book for book in books if len(book) <= 4)
    print("太长的书就不看了，只读短的：")
    for book in reading:
        print(" ->《{}》".format(book))

    print("可是发现书的名字短，内容也可能很长啊！")


if __name__ == '__main__':
    test()




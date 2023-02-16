# # coding=utf-8
#
# import sys, re, os
#
#
# def getDictList(dict):
#     regx = 'b.csv'
#     with open(dict) as f:
#         data = f.read()
#         return re.findall(regx, data)
#
#
# def rmdp(dictList):
#     return list(set(dictList))
#
#
# def fileSave(dictRmdp, out):
#     with open(out, 'a') as f:
#         for line in dictRmdp:
#             f.write(line + '\n')
#
#
# def main():
#     try:
#         dict = sys.argv[1].strip()
#         out = sys.argv[2].strip()
#         dictList = getDictList(dict)
#         dictRmdp = rmdp(dictList)
#         fileSave(dictRmdp, out)
#     except Exception as e:
#         print('error:', e)
#         me = os.path.basename(__file__)
#         print('usage: %s <input> <output>' % me)
#         print('example: %s dict.txt dict_rmdp.txt' % me)
#         exit()
from collections import defaultdict
s = (('544732228602', '2590418492', '8'), ('612736543127', '2590418492', '195'), ('611630153925', '2590418492', '227'), ('568660087709', '2590418492', '8'), ('575932108781', '2590418492', '6'), ('582251506678', '2590418492', '0'), ('592901983354', '2590418492', '22'), ('568789854525', '2590418492', '0'), ('616910032251', '2590418492', '54'), ('619011239468', '2590418492', '4'))
result = defaultdict(set)
for i in s:
    data = result.get('2590418492', [])
    print(data)



# if __name__ == '__main__':
#     main()

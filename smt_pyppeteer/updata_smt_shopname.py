# b_name = {}
# with open(r"C:\Users\Administrator\Desktop\tb\smt_shop_name_合并.txt_去重.txt", "r", encoding="utf-8") as f_f:
#     b_num = 0
#     for i_i in f_f:
#         b_num += 1
#         if b_num % 1000000 == 0:
#             print(b_num)
#         data = i_i.strip().split(",")
#         b_name[data[0]] = data
#
#
# file_write = open(r"C:\Users\Administrator\Desktop\tb\smt_shopinfo_202106_new.txt", "w", encoding="utf-8")
# with open(r"C:\Users\Administrator\Desktop\tb\smt_shopinfo_202106.txt", "r", encoding="utf-8") as f:
#     num = 0
#     for i in f:
#         try:
#             num += 1
#             data = i.strip().split(",")
#             goods_id = data[0]
#             shop_name = b_name.get(goods_id)
#             if shop_name == None:
#                 file_write.write(",".join(data) + "\n")
#                 print(1)
#                 # pass
#             else:
#                 # 淘宝天猫信用信息更新
#                 data[2] = shop_name[2]  # shop_hpl
#                 # data[27] = shop_name[2]  # describe_rate
#                 file_write.write(",".join(data)+"\n")
#             if num % 1000000 == 0:
#                 print(num)
#                 file_write.flush()
#         except Exception as e:
#             print(e)





# import socket,re
#
#
# def get_ip():
#     addrs = socket.getaddrinfo(socket.gethostname(), "")
#     match = re.search("'192.168.(\d+.\d+)'", str(addrs))
#     ip_num = "0.000"
#     if match:
#         ip_num = match.group(1)
#         print(ip_num)
#     return ip_num
#
#
# get_ip()
import re

aaa = 'seller=A30VUVZNLKIC4U">NY Discounts</a>   </td>   <td class="comparison_sim_items_column comparable_item0">    <a class="a-spacing-top-small a-link-normal" target="_self" href="/-/zh/gp/help/seller/at-a-glance.html/ref=psdc_165797011_s1_B088B3BJ4F?ie=UTF8'

aaaa = re.search(r'seller=(.*?)(">|&amp)', aaa).group(0)
aaaaaaaaaaa = re.search(r'seller=(.*?)(">|&amp)', aaa).group(1)
print(aaaa)
print(aaaaaaaaaaa)




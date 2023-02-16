'''
202106四-家装家饰及家具-天猫京东
'''
goods_id = '''
592616144
67645171
57301625
71841570
117264779
114670429
66755689
57301501
448572928
73217434
'''
tt = '202002'
str_id = goods_id.strip('\n')
list_id = str_id.split('\n')
id_list = []
for id in list_id:
    sql_txt = "select shop_id,goods_id,sales_month,discount_price,sales_month*discount_price as 销售额 from tmall_goodsmobile_{} where shop_id = '{}' order by  sales_month*discount_price desc limit 10".format(tt, id)
    # sql_txt = "select shop_id,goods_id,realcomment,price,realcomment*price as 销售额 from jd_goodsinfo_{} where shop_id = '{}' order by  realcomment*price desc limit 10".format(
    #     tt, id)
    id_list.append(sql_txt)
sql_all = '''select * FROM(
({})
union all
({})
union all
({})
union all
({})
union all
({})
union all
({})
union all
({})
union all
({})
union all
({})
union all
({})) a '''.format(id_list[0], id_list[1], id_list[2], id_list[3], id_list[4], id_list[5], id_list[6], id_list[7], id_list[8], id_list[9])
print(sql_all)





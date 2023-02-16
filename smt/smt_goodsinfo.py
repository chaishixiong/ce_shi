def goodsinfo():
    goods_data_dict = dict()
    new_goods = open("X:\数据库\速卖通\smt_goodsid_order_new.txt", "w", encoding="utf-8")
    with open("X:\数据库\速卖通\smt_goodsid_order-data_合并.txt", "r", encoding="utf-8") as goods_data:
        for data in goods_data:
            data_list = data.strip().split(',')
            if len(data_list) > 4:
                goods_id = data_list[3]
                goods_data_dict[goods_id] = 1
    with open("X:\数据库\速卖通\\202211\smt_goodsinfo_202211[店铺id,卖家id,商品数目,商品id,销量,商品价格,商品价格_较高值,产品url,评分,商品名称,评论数量,媒体id,图片链接,标签].txt", "r", encoding="utf-8") as goods_data_old:
        for data_old in goods_data_old:
            data_list_old = data_old.strip().split(',')
            if len(data_list_old) > 4:
                goods_id_old = data_list_old[3]
                data_old_n = goods_data_dict.get(goods_id_old)
                if data_old_n == None:
                    new_goods.write(data_old)
                    new_goods.flush()
    new_goods.close()


if __name__ == '__main__':
    goodsinfo()


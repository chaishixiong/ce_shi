from lxml import etree
import re
with open(r'amazon_shopinfo.txt', 'r', encoding='utf-8') as f:
    response = f.read()
    text_html = etree.HTML(response)
    html = ''
    postcode = ''
    postcode_list = text_html.xpath('//div[@class="a-row a-spacing-none indent-left"]/span/text()')
    if len(postcode_list) > 1:
        for i in postcode_list:
            p = re.match(r"\d+$", i)
            html += i
            if p != None:
                postcode = str(i)
        print(html)
        print(postcode)










def updata_amazon_shop_id():
    shop_data = {}
    with open(r"C:\Users\Administrator\Desktop\data\shopinfo.txt", "r", encoding="utf-8") as f_f:
        for i_i in f_f:
            id_i = i_i.strip('\n').split(',')
            shop_data[id_i[0]] = id_i[1]

    file_write = open(r"C:\Users\Administrator\Desktop\data\amazonus_shopinfo_202112_sales_new.txt", "a", encoding="utf-8")
    with open(r"C:\Users\Administrator\Desktop\data\amazonus_shopinfo_202112_sales.txt", "r", encoding="utf-8") as f:
        for i in f:
            i = i.strip('\n').split(',')
            shop_id = i[0]
            company = shop_data.get(shop_id)
            if company != None:
                i[3] = company
                file_write.write(",".join(i) + "\n")
            else:
                file_write.write(",".join(i) + "\n")
        file_write.close()



updata_amazon_shop_id()






import requests
from lxml import etree
import re
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_pool


class TaobaoGoodsAll(object):
    def __init__(self):
        self.session_227_tb = DataBaseSession(tb_pool)
        self.id_id = ''

    def goods_resques(self, shop_id, pag):
        url = 'https://shop{}.taobao.com/i/asynSearch.htm?_ksTS=1618216498569_351&callback=jsonp352&mid=w-23295354947-0&wid=23295354947&path=/category.htm&spm=a1z10.1-b-s.w5001-23295377977.6.2059782don1Eg5&search=y&orderType=hotsell_desc&scene=taobao_shop&pageNo={}'.format(shop_id, pag)
        goods_headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "authority": "shop100062373.taobao.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "cookie":"t=f1fa1ccef6aac303323bc6cc85df8529; thw=cn; enc=VHva0IGMkrL3FuQL1k22a9xjcOZVvIp7NgXX9djazYqpuHEE%2Fu39MmsMnaaHo72BCxMWCgRjAYAeUMTAbFewsQ%3D%3D; cookie2=14413d78b0e4a059473cda8c5e3f9d39; _tb_token_=e37ea15effb5d; _samesite_flag_=true; cna=FASBGyJdJx8CAdpKMN2vfUtF; sgcookie=E10015J199UOqz3IhGnhQiKAIHupZ146ZKYySoIC2RE20syTGzMf%2FPX8athcaCt%2BetFIWAcPzIIR%2BQBDvImxBknx9bQgd8PpHn5uaSn3rHsaZjCnfzDRMz6UVTnApt5ZKi93; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&id2=UUkO1%2BLahLblCw%3D%3D&vt3=F8dCv4fSAAYBdmSeafk%3D&nk2=F5RMHK6PLjrWyQ%3D%3D; csg=ba022f22; lgc=tb95487286; cancelledSubSites=empty; dnk=tb95487286; skt=e011df82f6f29d59; existShop=MTY2MjM2MDgzMg%3D%3D; uc4=id4=0%40U2uCuLZXEe%2Fl8gAXJJUSjYiNmDXP&nk4=0%40FY4HWUiuhU2ELf%2BnMxGJkb29%2BEqZ; tracknick=tb95487286; _cc_=W5iHLLyFfA%3D%3D; linezing_session=TFFcYOFWJu73cCd3GxE5DhDr_16623631842969fL5_2; mt=ci=65_1; ariaDefaultTheme=default; ariaFixed=true; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie14=UoeyDHGcNESGDw%3D%3D&cookie21=WqG3DMC9Fbk9noNn3aVF&pas=0&existShop=false; xlly_s=1; _m_h5_tk=c01d66052311eba550a1ffb5e384536d_1662537611673; _m_h5_tk_enc=56b68ba6b9a6bae4e31f637d26ca5a67; tfstk=czTcBRZgZnSb34FuSn_j7MFA6dTcZjaNKF8WzjQWqZpMepLPitqzYa6tZtDI3l1..; l=eBIrvOunTNr4_hADBOfwourza77tbIRAguPzaNbMiOCPO35w5SI1B6ktrUYeCnGVh6zMR3z1UrspBeYBqn4xIghne5DDwKMmn; isg=BN_f6nvowI4SssSSTh_SNN1JbjNpRDPmSXdpUXEsbA7VAP-CeRZ6Nl3SxpB-mAte; ariaStatus=true; ariaReadtype=1; ariaoldFixedStatus=false"
        }
        r = requests.get(url, headers=goods_headers)
        # print(r.text)
        return r

    def goods_list(self, goods_data):
        html_data = etree.HTML(goods_data.text)
        goods_id_list = html_data.xpath("/html/body/div[1]/div[3]/div/dl/@data-id")
        return goods_id_list

    def writer_goods(self, data_data):
        with open(r'taobao_goods_seed.txt', 'a', encoding='utf-8') as w:
            w.write(data_data + '\n')
            w.flush()
            w.close()

    def re_shopid_sellerid(self, goods_id):
        goodsid = re.search(r'[\d]+', str(goods_id)).group(0)
        data_data = goodsid + ',' + self.seller_id
        self.writer_goods(data_data)

    def run_spider_tb(self):
        sql = 'select shop_id,seller_id from taobao_shopinfo_202208_add_new_shop'
        sql_data = self.session_227_tb.query_tuple_data(sql)
        for shop_data in sql_data:
            shop_id = shop_data[0]
            self.seller_id = shop_data[1]
            pag = 1
            while True:
                if self.seller_id == '2200811705209':
                    self.id_id = '2200811705209'
                    break
                if self.id_id == '2200811705209':
                    goods_data = self.goods_resques(shop_id, pag)
                    goods_id_list = self.goods_list(goods_data)
                    print(shop_id + '------' + str(len(goods_id_list)))
                    if len(goods_id_list) == 0:
                        break
                    for goods_id in goods_id_list:
                        self.re_shopid_sellerid(goods_id)
                    pag += 1
                else:
                    break


def run_tb_goods_spider():
    run = TaobaoGoodsAll()
    run.run_spider_tb()


if __name__ == '__main__':
    run_tb_goods_spider()




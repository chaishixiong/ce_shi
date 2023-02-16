import requests
from lxml import etree
import re
import time
from 统计局需求_2.sql_pool.dbpool import kuajing_227_pool
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession


def request_youbian(data):
    yb_id = data[0]
    url = 'https://www.youbianku.com/{}'.format(yb_id)
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "cookie": "__yjs_duid=1_57d8f6212632629bb57f8d9c79abaae81635476326399; _ga=GA1.2.2124734861.1635476330; __gads=ID=a8c812dfb3a9bd01-2282ca46efcc00f8:T=1635476328:RT=1635476328:S=ALNI_MYi9r8kNmA10aL-n1AeVILkvNtHRg; __utma=188475552.2124734861.1635476330.1635480464.1635750003.2; __utmz=188475552.1635750003.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; BMAP_SECKEY2=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b45f459cf1f0308166dbc02025f0b0ab5e88716497b66b5e09a5d430c8e7eccad2d6a8f6b32cc80d704d69e0c704f5bf36856f71552676b057bc4e4d160471ebfb2f2706cb8d737425e3c3fdf56b4a335a80127d2f0f37a9ae39053ac4f1bc1cdd7f30f06443555044c32fd125e1adc5fe449a9e3312d6ae40c1d835c17840e76bf4f2c40f35b050ca841ee1744231b8abe693b76a1013176a96ba7e00fe61023913937f7a5693e41bed473a6ca3f18548b; SECKEY_ABVK=H74A7WL91yZ8MgHOXWvLE1Wl4JuSXJA+C25mOhXj9h8%3D; BMAP_SECKEY=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b45f459cf1f0308166dbc02025f0b0ab5e88716497b66b5e09a5d430c8e7eccad2d6a8f6b32cc80d704d69e0c704f5bf3687e686e925cae97021f2b8efcc5579dfbe7a7f0258d7ec2dc7bfad71a60d602c7d76be5b5071e21bb30435999cb6540850a5b24895a4581d32c0720dd753cb68feb9650616785604ab0b27853fb5c7e15e0281d08f399d5b055988a9b09ce6f80c54448022932a358ff0e40f31761918cb934519861102316594efa5822a2bbbb; BAIDU_SSP_lcr=https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=21002492_28_hao_pg&wd=%E9%82%AE%E7%BC%96%E6%9F%A5%E8%AF%A2&fenlei=256&rsv_pq=acd96c0b00039c95&rsv_t=e7cbDy9Gpl4cnIMBoZk8RNLygL4fn%2FO8a37AIMSD9ba1rS%2FxFUaiipRQ0XYH94R5LL8WZOK1DDfu&rqlang=cn&rsv_enter=1&rsv_dl=ts_1&rsv_sug3=9&rsv_sug1=9&rsv_sug7=101&rsv_sug2=1&rsv_btype=i&prefixsug=%25E9%2582%25AE%25E7%25BC%2596&rsp=1&inputT=4098&rsv_sug4=5288&rsv_sug=2; Hm_lvt_855d4c8eddca4a78f37ebe6b005dbd95=1637825532,1638164250,1639363605,1639468459; Hm_lpvt_855d4c8eddca4a78f37ebe6b005dbd95=1639468459; _gid=GA1.2.21195202.1639468459; _gat_gtag_UA_241337_11=1"
    }
    time.sleep(2)
    r = requests.get(url=url, headers=headers)
    try:
        if r.status_code == 200:
            html_txt = r.text
            html_t = etree.HTML(html_txt)
            province = html_t.xpath('//*[@class="unified-content"]/div/span[2]/a/span/text()')[0]
            city = html_t.xpath('//*[@class="unified-content"]/div/span[3]/a/span/text()')[0]
            all_address_list = html_t.xpath('//*[@id="separate"]/text()')
            county = ''
            for all_address in all_address_list:
                county = re.search('{}(.*)'.format(city), all_address).group(1)
                if len(county) > 0:
                    break
            data_list = (yb_id, str(province), str(city), str(county))
            print(data_list)
            return data_list
        else:
            province = ''
            city = ''
            county = ''
            data_list = (yb_id, province, city, county)
            return tuple(data_list)
    except Exception as e:
        print(yb_id)
        province = ''
        city = ''
        county = ''
        data_list = (yb_id, province, city, county)
        return tuple(data_list)


if __name__ == '__main__':
    session_228 = DataBaseSession(kuajing_227_pool)
    with open(r'albbgj_id.txt', "r", encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            data_list = request_youbian(data)
            insertion_sql = "insert into alibabagj_postcode_id (postcode_id, province, city, county) VALUES (%s,%s,%s,%s)"
            session_228.insertion_data(insertion_sql, data_list)























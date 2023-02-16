import requests
import re, json


def headers_todict(header_str):
    header = header_str.split("\n")
    headers = {}
    for cookie in header:
        if ":" in cookie:
            cookie_split = cookie.split(":", 1)
            name = cookie_split[0].strip()
            values = cookie_split[1].strip()
            headers[name] = values
        else:
            headers[cookie] = ""
    return headers

pinyin = 'Beijing'
city_id = '1'
url = 'https://m.ctrip.com/restapi/soa2/16709/HotelSearch'
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json;charset=UTF-8",
    "p": "67350836008",
    "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Referer": "https://hotels.ctrip.com/hotels/listPage?cityename=北京&city=1"
    }
data = '''{"meta":{"fgt":"","hotelId":"","priceToleranceData":"","priceToleranceDataValidationCode":"","mpRoom":[],"hotelUniqueKey":"","shoppingid":""},"seqid":"","deduplication":[],"filterCondition":{"star":[],"rate":"","rateCount":[],"priceRange":{"lowPrice":0,"highPrice":-1},"priceType":"","breakfast":[],"payType":[],"bedType":[],"bookPolicy":[],"bookable":[],"discount":[],"zone":[],"landmark":[],"metro":[],"airportTrainstation":[],"location":[],"cityId":[],"amenty":[],"promotion":[],"category":[],"feature":[],"brand":[],"popularFilters":[]},"searchCondition":{"sortType":"1","adult":1,"child":0,"age":"","pageNo":"1","optionType":"","optionId":"","lat":0,"destination":"","keyword":"","cityName":"北京","lng":0,"cityId":"1","checkIn":"入住时间","checkOut":"离店时间","roomNum":1,"mapType":"gd","travelPurpose":0,"countryId":1,"url":"https://hotels.ctrip.com/hotels/listPage?cityename=北京&city=1","pageSize":20,"timeOffset":28800,"radius":0,"directSearch":0},"queryTag":"NORMAL","genk":true,"genKeyParam":"a=0,b=入住时间,c=离店时间,d=zh-cn,e=2","webpSupport":true,"platform":"online","pageID":"102002","head":{"Version":"","userRegion":"CN","Locale":"zh-CN","LocaleController":"zh-CN","TimeZone":"8","Currency":"CNY","PageId":"102002","webpSupport":true,"userIP":"","P":"","ticket":"","clientID":"","Union":{"AllianceID":"","SID":"","Ouid":""},"HotelExtension":{"group":"CTRIP","hasAidInUrl":false,"Qid":"","hotelUuidKey":"","hotelUuid":""}}}'''

r = requests.post(url=url, headers=headers, body=data)
data_str = r.content.decode()
print(data_str)


import requests
from fake_useragent import UserAgent

location = r'C:\Users\Administrator\Desktop\测试\taobao\fake_useragent_0.1.11.json'
ua = UserAgent(path=location)
user_agent = ua.chrome
url = 'https://shop94.taobao.com'
header = {
    'user-agent': user_agent
}
r = requests.get(url, headers=header)
data_html = r.text
print(data_html)
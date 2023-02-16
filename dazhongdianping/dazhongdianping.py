import requests


def run_da():
	url = 'https://www.dianping.com/quzhou/ch10'
	headers = {
				'Accept': 'text/html,application/xhtml+xml,application/xmlq=0.9,image/webp,image/apng,*/*q=0.8,application/signed-exchangev=b3',
				'Accept-Encoding': 'gzip, deflate',
				'Cookie': 'navCtgScroll=100; _lxsdk=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; _lxsdk_cuid=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; switchcityflashtoast=1; _hc.v=ce0d9b7c-277f-582f-7204-2d40c1c9a9cc.1614744421; s_ViewType=10; _tr.u=KmpIrpU4VFRQEB9E; _dp.ac.v=28882ee0-66fa-400f-a218-97da5a749b5b; ctu=2a2d9a661eb30bb6d36de26436e1fdf1857c55c22c0f2809953c81468300ca3a; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1619679169; source=m_browser_test_33; PHOENIX_ID=0a48873f-1791c776a08-610f; info="{\"query_id\":\"9dce19f9-c2a9-4884-99c4-0fe41c38b073\",\"ab_id\":\"exp000095_a\"}"; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3713187639; uamo=18779340395; cityid=106; cy=106; cye=quzhou; fspop=test; pvhistory="6L+U5ZuePjo8L3F1emhvdS9jaCU3Qj46PDE2MjAzNzcxNDUyMTVdX1s="; m_flash2=1; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A11%7Cindex%3AA%3A3%7CshopList%3AA%3A5%7Cmap%3AA%3A1%7Cmyinfo%3AA%3A1; thirdtoken=e9214815-06a0-41d9-a0ef-2ed692fff555; _thirdu.c=35551c46e88dbc3a47a53c2e949b3cbd; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1619677706,1619681417,1619753965,1620379992; aburl=1; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1620380041; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1620640617; _lxsdk_s=17955b15b65-97b-196-418%7C%7C103',
				'Host': 'www.dianping.com',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
			}
	response = requests.get(url=url, headers=headers)
	print(response.status_code)
	print(response.content.decode())
	
run_da()
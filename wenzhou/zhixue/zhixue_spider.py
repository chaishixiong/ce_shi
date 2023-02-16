import requests
import re
import time
import json


class ZhiXue(object):
    def __init__(self):
        pass

    def request(self):
        url = 'https://www.zhixue.com/paperfresh/api/question/show/knowledge/getTopics?_=1646123468898&pageIndex=1&knowledgeSelectType=0&knowledgeType=0&knowledgeId=&level=0&gradeCode=&sectionCode=&difficultyCode=&paperTypeCode=&topicFromCode=&areas=&year=&sortField=default&sortDirection=true&keyWord=%20&knowledgeTag=01&keywordSearchField=topic&excludePapers=&isRelatedPapers=true'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'Cookie': 'JSESSIONID=2E24957A934203B4400BCCC0BD3C2362; deviceId=9313E596-B2BA-428A-B352-CB0A9892729D; loginUserName=tch3855385; SSO_CUSTOM_LOGOUT_URL="https://www.zhixue.com/login.html"; tlsysSessionId=2993ff8b-1f59-47fb-bbc8-bb3a1fe76dd2; isJump=true; JSESSIONID=09FBDB80BCE5F8BE18BAA1B646BD621B; ui=1500000100024840723; CartTotalCount=0'
        }
        r = requests.get(url=url, headers=headers)
        return r

    def dict_data(self, data_dict):
        data_list = data_dict.get('result').get('pager').get('list')
        if len(data_list) > 0:
            for data_d in data_list:
                originalStruct = data_d.get('originalStruct')
                title = originalStruct.get('contentHtml')  # 题目
                analysis = originalStruct.get('analysisHtml')  # 解析
                answerImg_url = originalStruct.get('analysisHtml')  # 答案图片url
                analysis_url = originalStruct.get('analysisHtml')  # 解析图片url
                difficulty = data_d.get('difficulty')
                difficulty_name = difficulty.get('name')  # 难易程度
                print(data_d)
        pass

    def run_spider(self):
        data_text = self.request()
        data_dict = json.loads(data_text.text)
        self.dict_data(data_dict)


def run_zhixue():
    run = ZhiXue()
    run.run_spider()


if __name__ == "__main__":
    # run_zhixue()

    for i in range(1, 10, 3):
        print(i)




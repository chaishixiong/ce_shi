import requests
import re
import os
import json
import time
'''
单选，多选，解答题
'''


class JiKe(object):
    def __init__(self):
        self.os_path = 'F:\极课网\数学\函数概念与基本初等函数\单选'
        self.timu = ''
        self.timu_all_list = ['题目', '答案', '解析']

    def request(self):
        url = 'https://exam.fclassroom.com/ark/ocean/api/list_item?school_id=2012288&aid=3449'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "content-type": "application/json",
            "token": "null",
            "cookie": "x-jupiter-uuid=16481950221555324; s_v_web_id=verify_l164rg0y_Rwytf69U_SOWI_47ze_9x8I_TFktTmtXjMdo; passport_csrf_token=1ee29bfaa5958f65595e86764c318583; passport_csrf_token_default=1ee29bfaa5958f65595e86764c318583; _tea_utm_cache_2018=undefined; n_mh=68kQnpaUz3XZTSY57tndYpoJEyA_8sTFxagX-ti5bko; odin_tt=de80a918bfe1e68746e95cbaa7e1411a5abae7f56e43db1e8b80c5c9b8ef818cd3681d097eb02078f2af9c80501b060f9635daead0b88b183ea4741220479a31; sid_guard=05924b4ef70b72e33efd727889bdf1b8%7C1648447364%7C5184000%7CFri%2C+27-May-2022+06%3A02%3A44+GMT; uid_tt=578448f2e1e5e86aec7dc1e88e0f2fc6; uid_tt_ss=578448f2e1e5e86aec7dc1e88e0f2fc6; sid_tt=05924b4ef70b72e33efd727889bdf1b8; sessionid=05924b4ef70b72e33efd727889bdf1b8; sessionid_ss=05924b4ef70b72e33efd727889bdf1b8; sid_ucp_v1=1.0.0-KDdiNzMwYWRhN2MzMTA2MTE1ZGU3MTE5ODM2MmU3ZjA1M2Y2YzBmMDcKHwiTwtDL543WBhCEn4WSBhj5GiAMMMKwno8GOAJA7wcaAmxmIiAwNTkyNGI0ZWY3MGI3MmUzM2VmZDcyNzg4OWJkZjFiOA; ssid_ucp_v1=1.0.0-KDdiNzMwYWRhN2MzMTA2MTE1ZGU3MTE5ODM2MmU3ZjA1M2Y2YzBmMDcKHwiTwtDL543WBhCEn4WSBhj5GiAMMMKwno8GOAJA7wcaAmxmIiAwNTkyNGI0ZWY3MGI3MmUzM2VmZDcyNzg4OWJkZjFiOA; ttwid=1%7CJgrCEiroWKUPggoeYl50F34xjYrhVCFW6us71aAGlP0%7C1648449156%7Cdd96578440eb52b583a98e42fa27bc46cfabddfbc67b6247c360e0c47acf08c8",
        }
        body = {"department":3,"subject":2,"teaching_type":2,"tree_ids":["200880"],"point_ids":["10464211"],"item_banks":[1],"item_types":[32],"item_categories":[],"difficulties":[],"exam_types":[],"years":[],"provinces":[],"page":1,"per_page":20,"sort":0,"use_search_strategy":False}
        r = requests.post(url=url, headers=headers,data=json.dumps(body))
        return r

    def png_request(self, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "content-type": "application/json",
            "token": "null",
            "cookie": "x-jupiter-uuid=16461996866683508; s_v_web_id=verify_l094sh8r_gXYuEwqq_Faaw_4Jsj_95CH_t1l1c8E9nDiH; passport_csrf_token_default=0deaf9decfe8854a94bf23ed6b25156a; passport_csrf_token=0deaf9decfe8854a94bf23ed6b25156a; _tea_utm_cache_2018=undefined; n_mh=zm8AOnUPFMIlRCXj1C3hq4vdcxt9YqILJnlaIK7YdDg; sid_guard=a2ca1d33234f97b84f11c587d8c22261^%^7C1646200788^%^7C5184000^%^7CSun^%^2C+01-May-2022+05^%^3A59^%^3A48+GMT; uid_tt=855ee497cd550589257fe510a2f73d93; uid_tt_ss=855ee497cd550589257fe510a2f73d93; sid_tt=a2ca1d33234f97b84f11c587d8c22261; sessionid=a2ca1d33234f97b84f11c587d8c22261; sessionid_ss=a2ca1d33234f97b84f11c587d8c22261; sid_ucp_v1=1.0.0-KDA5ZDc4YzgxZDhkNjcwNzg0NDkzMTI4ZWMxZGI1NGY5ZThhZDQ2MzAKHwiTwtDL543WBhDUj_yQBhj5GiAMMMKwno8GOAJA7wcaAmxmIiBhMmNhMWQzMzIzNGY5N2I4NGYxMWM1ODdkOGMyMjI2MQ; ssid_ucp_v1=1.0.0-KDA5ZDc4YzgxZDhkNjcwNzg0NDkzMTI4ZWMxZGI1NGY5ZThhZDQ2MzAKHwiTwtDL543WBhDUj_yQBhj5GiAMMMKwno8GOAJA7wcaAmxmIiBhMmNhMWQzMzIzNGY5N2I4NGYxMWM1ODdkOGMyMjI2MQ; odin_tt=f9df85be5bc99bb7cb6bf1558c1b09e88c98b270d6754e31b1b1539ddbb1a81e6094ab498c6dc93db0d9dfc46735fa5276f1e067400e7fc855df39dd1ee07d44; ttwid=1^%^7CGPdnpcMsWqbXf4A_NBNSBz0I0EYi7_By9gXvYelRP20^%^7C1646205764^%^7Cfd175d4e9f520268c9949f18715b44a72baa84b2bc0987d99c2570ba7923990d",
        }
        r = requests.get(url=url, headers=headers)
        return r

    def dict_data(self, data_dict):
        item = dict()
        item['question_types'] = ''
        data_all = data_dict.get('matrix_item')
        struct_question = data_all.get('struct_question')  # 题
        title_name = struct_question.get('content')  # 题目名字
        item['title_name'] = title_name
        hint = struct_question.get('hint')  # 解析
        item['hint'] = hint
        questions_list = struct_question.get('questions')  # 问题列表
        options = struct_question.get('options')
        difficulty_des = data_all.get('difficulty_des')  # 难易程度
        item['difficulty_des'] = difficulty_des
        content_list = []
        answer_res_list_list = []
        if len(questions_list) > 0:
            for questions in questions_list:
                content = questions.get('content')  # 问题
                content_list.append(content)
                answer_res_list = questions.get('answers')
                for answer in answer_res_list:
                    answer_res = answer.get('answer_res')[0]  # 答案
                    answer_res_list_list.append(answer_res)
            item['content_list'] = content_list
            item['answer_res_list'] = answer_res_list_list
        elif len(options) > 0:
            item['question_types'] = '选择题'
            answers_list = struct_question.get('answers')[0]
            answers_dict = answers_list.get('answer_res')   # 选择答案
            options_list = options[0]
            option_values_list = options_list.get('option_values')
            for answers in answers_dict:
                answer_res_list_list.append(answers)
            item['answer_res_list'] = answer_res_list_list
            for option_values_dict in option_values_list:
                options_key = option_values_dict.get('key')
                options_values = option_values_dict.get('value')
                options_all = options_key + '.  ' + options_values
                content_list.append(options_all)
            item['content_list'] = content_list
        return item

    def with_open(self, path_pp, write, attribute):
        with open(path_pp, attribute) as f:
            f.write(write)
            f.close()

    def data_cleans_html(self, item_dict):
        for timu_title in self.timu_all_list:
            timu_find = self.timu + '\{}'.format(timu_title)  # 创建第n题文件
            self.os_path_path(timu_find)
        title_name = item_dict['title_name']  # 题
        hint = item_dict['hint']  # 解析
        condition = 0
        difficulty_des = item_dict['difficulty_des']  # 难易程度
        difficulty_title = '题目难易程度：{}'.format(difficulty_des) + '\n'


        title_data, title_url_list = self.re_data(title_name, condition)
        png_num = 0
        aaa = 0
        for title_url in title_url_list:
            aaa += 1
            respons = self.png_request(title_url + 'png')
            self.with_open(self.timu + '\题目\{}.png'.format(aaa), respons.content, 'wb')

        #  写入题目难易程度
        self.with_open(self.timu + '\题目\题目.txt', difficulty_title, 'a')
        #  写入题目
        self.with_open(self.timu + '\题目\题目.txt', title_data + '\n', 'a')
        print(title_data)
        hint_data, hint_url_list = self.re_data(hint, condition)
        for hint_url in hint_url_list:
            png_num += 1
            respons = self.png_request(hint_url + 'png')
            self.with_open(self.timu + '\解析\{}.png'.format(png_num), respons.content, 'wb')
        # 写入解析
        self.with_open(self.timu + '\解析\解析.txt', hint_data, 'a')
        if item_dict['question_types'] == '选择题':
            content_list = item_dict.get('content_list')  # 选项列表
            answer_res_list = item_dict['answer_res_list']  # 答案列表

            for content in content_list:
                aaa += 1
                # 写入题目
                if 'http' in content:
                    pngurl = re.search(r"src=\"(.*?)png", content).group(1)
                    png_name = content[0]
                    respons = self.png_request(pngurl + 'png')
                    self.with_open(self.timu + '\题目\{}.png'.format(png_name), respons.content, 'wb')
                else:
                    self.with_open(self.timu + '\题目\题目.txt', content + '\n', 'a')
            self.with_open(self.timu + '\答案\答案.txt', answer_res_list[0] + '\n', 'a')
        else:
            print()

    def re_data(self, data, condition):
        cleans_data = re.sub(r"(<br.*?/>)", '', data)
        cleans_data = re.sub(r"(<img.*?>)", '{png}', cleans_data)
        if condition > 0:
            cleans_data_two = re.sub(r"(<answer.*?answer>)", '', cleans_data)
        else:
            cleans_data_two = re.sub(r"(<answer.*?answer>)", '(  )', cleans_data)
        # png_url_list = re.findall(r"src=\"(.*?)\" />|src=\"(.*?)!content", data)
        png_url_list = re.findall(r"src=\"(.*?)png", data)
        return cleans_data_two, png_url_list

    def os_path_path(self, path_path):
        folder = os.path.exists(path_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("---  new folder...  ---")
        else:
            print("文件已存在")
        return path_path

    def run_spider(self):
        for i in range(1, 501):
            folio_pag_name = self.os_path + '\第{}页'.format(i)
            path_path = self.os_path_path(folio_pag_name)
            data_text = self.request()
            time.sleep(1)
            data_dict = json.loads(data_text.text)
            data_list = data_dict.get('data').get('items')
            n = 0
            if len(data_list) > 0:
                for data_d in data_list:
                    n += 1
                    self.timu = path_path + '\第{}题'.format(n)  # 创建第n题文件
                    self.os_path_path(self.timu)
                    item_dict = self.dict_data(data_d)
                    self.data_cleans_html(item_dict)


def run_jike():
    run = JiKe()
    run.run_spider()


if __name__ == "__main__":
    run_jike()
    #  | >.* ? < | >.*.




import requests
import re
import os
import json
'''
单选，多选，解答题
'''


class JiKe(object):
    def __init__(self):
        self.os_path = 'F:\极课网\数学\函数概念与基本初等函数'
        self.timu = ''
        self.timu_all_list = ['题目', '答案', '解析']

    def request(self):
        url = 'https://exam.fclassroom.com/ark/ocean/api/list_item?school_id=2012288&aid=3449'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "content-type": "application/json",
            "token": "null",
            "cookie": "x-jupiter-uuid=16461996866683508; s_v_web_id=verify_l094sh8r_gXYuEwqq_Faaw_4Jsj_95CH_t1l1c8E9nDiH; passport_csrf_token_default=0deaf9decfe8854a94bf23ed6b25156a; passport_csrf_token=0deaf9decfe8854a94bf23ed6b25156a; _tea_utm_cache_2018=undefined; n_mh=zm8AOnUPFMIlRCXj1C3hq4vdcxt9YqILJnlaIK7YdDg; sid_guard=a2ca1d33234f97b84f11c587d8c22261^%^7C1646200788^%^7C5184000^%^7CSun^%^2C+01-May-2022+05^%^3A59^%^3A48+GMT; uid_tt=855ee497cd550589257fe510a2f73d93; uid_tt_ss=855ee497cd550589257fe510a2f73d93; sid_tt=a2ca1d33234f97b84f11c587d8c22261; sessionid=a2ca1d33234f97b84f11c587d8c22261; sessionid_ss=a2ca1d33234f97b84f11c587d8c22261; sid_ucp_v1=1.0.0-KDA5ZDc4YzgxZDhkNjcwNzg0NDkzMTI4ZWMxZGI1NGY5ZThhZDQ2MzAKHwiTwtDL543WBhDUj_yQBhj5GiAMMMKwno8GOAJA7wcaAmxmIiBhMmNhMWQzMzIzNGY5N2I4NGYxMWM1ODdkOGMyMjI2MQ; ssid_ucp_v1=1.0.0-KDA5ZDc4YzgxZDhkNjcwNzg0NDkzMTI4ZWMxZGI1NGY5ZThhZDQ2MzAKHwiTwtDL543WBhDUj_yQBhj5GiAMMMKwno8GOAJA7wcaAmxmIiBhMmNhMWQzMzIzNGY5N2I4NGYxMWM1ODdkOGMyMjI2MQ; odin_tt=f9df85be5bc99bb7cb6bf1558c1b09e88c98b270d6754e31b1b1539ddbb1a81e6094ab498c6dc93db0d9dfc46735fa5276f1e067400e7fc855df39dd1ee07d44; ttwid=1^%^7CGPdnpcMsWqbXf4A_NBNSBz0I0EYi7_By9gXvYelRP20^%^7C1646205764^%^7Cfd175d4e9f520268c9949f18715b44a72baa84b2bc0987d99c2570ba7923990d",
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
                    print(answer_res)
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
        #  写入题目难易程度
        self.with_open(self.timu + '\题目\题目.txt', difficulty_title, 'a')
        #  写入题目
        self.with_open(self.timu + '\题目\题目.txt', title_data, 'a')
        hint_data, hint_url_list = self.re_data(hint, condition)
        # 写入解析
        self.with_open(self.timu + '\解析\解析.txt', hint_data, 'a')
        if item_dict['question_types'] == '选择题':
            content_list = item_dict.get('content_list')  # 选项列表
            answer_res_list = item_dict['answer_res_list']  # 答案列表
            for content in content_list:
                # 写入题目
                self.with_open(self.timu + '\题目\题目.txt', content + '\n', 'a')
            self.with_open(self.timu + '\答案\案.txt', answer_res_list[0] + '\n', 'a')
        else:
            condition = 1
            content_list = item_dict.get('content_list')  # 问题列表
            answer_res_list = item_dict['answer_res_list']  # 答案列表
            j_x = 0
            for content, answer_res in zip(content_list, answer_res_list):
                j_x += 1
                png_num = 0
                content_data, content_url_list = self.re_data(content, condition)
                answer_res_data, answer_res_list = self.re_data(answer_res, condition)
                # 写入题目
                self.with_open(self.timu + '\题目\题目（{}）.txt'.format(j_x), content_data + '\n', 'a')
                for content_url in content_url_list:
                    png_num += 0
                    respons = self.png_request(content_url)
                    self.with_open(self.timu + '\题目\题目（{}）{}.png'.format(j_x, png_num), respons.content, 'wb')
                # 写入解析
                self.with_open(self.timu + '\解析\解析（{}）.txt'.format(j_x), answer_res_data + '\n', 'a')
                print()

    def re_data(self, data, condition):
        cleans_data = re.sub(r"(<img.*?/>)", '{png}', data)
        if condition > 0:
            cleans_data_two = re.sub(r"(<answer.*?answer>)", '', cleans_data)
        else:
            cleans_data_two = re.sub(r"(<answer.*?answer>)", '(  )', cleans_data)
        png_url_list = re.findall(r"src=\"(.*?)/>", data)
        print(cleans_data_two)
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
        for i in range(1, 21):
            folio_pag_name = self.os_path + '\第{}页'.format(i)
            path_path = self.os_path_path(folio_pag_name)
            data_text = self.request()
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
    data = '若<img class="latex" data-tex="m%3D0" style="width:6.298ex; height:2.176ex; vertical-align: -0.338ex;" src="https://qb-oss.bytededu.cn/latex/e6753e61990bc639ae1869683cb421b7.png" />，求<img class="latex" data-tex="%5Ccomplement+_%7BR%7DB" style="width:4.403ex; height:2.843ex; vertical-align: -0.671ex;" src="https://qb-oss.bytededu.cn/latex/7adc6809ceb795e9797bc5b0ee5d06da.png" />；<answer id="0"></answer>'
    run.re_data(data)


if __name__ == "__main__":
    run_jike()
    #  | >.* ? < | >.*.




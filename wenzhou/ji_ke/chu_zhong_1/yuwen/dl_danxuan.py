import requests
import re
import os
import hashlib
import json
import time
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import life_227_pool
from wenzhou.ji_ke.chu_zhong.settings import tree_ids_dict_shuxue, cookies, tree_ids_dict_dili
'''
单选，多选，解答题
'''


class JiKeYuWen(object):
    def __init__(self):
        self.life_227 = DataBaseSession(life_227_pool)
        self.os_path = 'F:/极课网/数学/'
        self.tree_ids_dict = tree_ids_dict_dili
        self.tree_ids = ''

    def request(self, page):
        url = 'https://exam.fclassroom.com/ark/ocean/api/list_item?school_id=2012288&aid=3449'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "content-type": "application/json",
            "token": "null",
            "cookie": cookies,
        }
        body = {
              "page": page,
              "per_page": 100,
              "teaching_type": 1,
              "item_banks": [
                1
              ],
              "sort": 0,
              "item_types": [],
              "item_categories": [],
              "difficulties": [],
              "exam_types": [],
              "years": [],
              "provinces": [],
              "use_search_strategy": False,
              "point_ids": [
                11191783
              ],
              "tree_ids": [
                self.tree_ids
              ],
              "department": 2,
              "subject": 7
            }
        r = requests.post(url=url, headers=headers, data=json.dumps(body))
        return r

    def png_request(self, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "content-type": "application/json",
            "token": "null",
        }
        r = requests.get(url=url, headers=headers)
        return r

    def dict_data(self, data_dict):
        self.item = dict()
        self.item['question_types'] = ''
        data_all = data_dict.get('matrix_item')
        self.item['item_id'] = data_all['item_id']  # 题目ID
        self.item['subject_des'] = data_all['subject_des']  # 学科
        self.item['grade_des'] = data_all['grade_des']  # 年级
        self.item['item_type_des'] = data_dict['item_type_des']  # 题型
        self.item['difficulty_des'] = data_all['difficulty_des']  # 题目难度
        struct_question = data_all.get('struct_question')
        title_name = struct_question.get('content')  # 题目
        title_name_data = self.question_stem(title_name)
        self.item['title_name'] = title_name_data
        hint = struct_question.get('hint')  # 解析
        questions_list = struct_question.get('questions')
        if len(questions_list) > 0:
            for questions_ in questions_list:
                self.for_questions(questions_)
        else:
            answers_list = struct_question.get('answers')
            answer_res = answers_list[0].get('answer_res')[0]  # 答案
            uid = answers_list[0].get('uid')
            self.question_answer(uid, answer_res)
            options_list = struct_question.get('options')
            if len(options_list) > 0:
                for options_l in options_list:
                    option_values_list = options_l.get('option_values')
                    self.option_values(uid, option_values_list)
        self.item['knowledge'] = data_all.get('points')  # 知识点
        self.item['tags'] = data_all.get('tags')  # 年-省-市
        self.item['hint'] = hint
        return self.item

    def for_questions(self, question_all):
        try:
            questions_list = question_all.get('questions')
            if len(questions_list) > 0:
                for questions in questions_list:
                    self.for_questions(questions)
            else:
                title_name = question_all.get('content')
                title_name_data = self.question_stem(title_name)  # 题干
                answers_list = question_all.get('answers')
                answer_res = answers_list[0].get('answer_res')[0]  # 答案
                uid = answers_list[0].get('uid')
                self.question_answer(uid, answer_res)
                options_list = question_all.get('options')[0]
                option_values_list = options_list.get('option_values')
                self.option_values(uid, option_values_list)
                qb_title_2_data = [uid, title_name_data, self.item['item_id']]
                insertion_sql = "replace into qb_title_2 (title_id, content, pid) VALUES (%s,%s,%s)"
                self.life_227.insertion_data(insertion_sql, qb_title_2_data)
                # print('二级题干', qb_title_2_data)
        except Exception as e:
            print(e)

    # 年-省-市
    def year_tags(self):
        title_id = self.item['item_id']  # 题目id
        content = self.item['title_name']  # 题目内容
        subject = self.item['subject_des']  # 科目
        type = self.item['item_type_des']  # 题型
        grade = self.tree_ids_dict[self.tree_ids]  # 年级
        difficulty_value = self.item['difficulty_des']  # 难易度
        sch_year = ''
        province = ''
        city = ''
        year_tags_list = self.item['tags']
        for dict in year_tags_list:
            if dict.get('key') == 'year':
                sch_year = dict.get('value')
            elif dict.get('key') == 'province_des':
                province = dict.get('value')
            elif dict.get('key') == 'city_des':
                city = dict.get('value')
        all_qb_title = [title_id, content, subject, type, difficulty_value, grade, sch_year, province, city]
        insertion_sql = "replace into qb_title (title_id, content, subject, type, difficulty_value, grade, sch_year, province, city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.life_227.insertion_data(insertion_sql, all_qb_title)
        print('题干', all_qb_title)

    #  题干
    def question_stem(self, title_name):
        data, picture_list = self.re_data(title_name)
        if len(picture_list) > 0:
            data_list = data.split('png')
            n = 0
            data_data = ''
            for d in data_list:
                data_data += d
                if n != len(data_list) - 1:
                    pic_url = picture_list[n]
                    pict_name = self.get_md5(pic_url)
                    data_data += pict_name
                    self.with_open(pic_url, pict_name)
                n += 1
            return data_data
        else:
            return data

    #  知识点
    def question_knowledge(self):
        title_id = self.item['item_id']
        knowledge_list = self.item['knowledge']
        for knowledge in knowledge_list:
            point_id = knowledge.get('point_id')
            name = knowledge.get('name')
            qb_knowledge_sql = "replace into qb_knowledge (pid, content) VALUES (%s,%s)"
            qb_title_knowledge_sql = 'insert into qb_title_knowledge (title_id, knowledge_id) VALUES (%s,%s)'
            qb_knowledge_list = [point_id, name]
            qb_title_knowledge_list = [title_id, point_id]
            self.life_227.insertion_data(qb_knowledge_sql, qb_knowledge_list)
            self.life_227.insertion_data(qb_title_knowledge_sql, qb_title_knowledge_list)
            # print('知识点, 知识点id', qb_knowledge_list, qb_title_knowledge_list)

    #  选项
    def option_values(self, title_id, option_values_list):
        for option_values in option_values_list:
            key = option_values.get('key')
            value = option_values.get('value')
            data, picture_list = self.re_data(value)
            if len(picture_list) > 0:
                data_list_list = data.split('png')
                n = 0
                value_str = ''
                for v_d in data_list_list:
                    value_str += v_d
                    if n != len(data_list_list) - 1:
                        pic_url = picture_list[n]
                        pic_name = self.get_md5(pic_url)
                        value_str += pic_name
                        self.with_open(pic_url, pic_name)
                    n += 1
            else:
                value_str = data
            key_value = [title_id, key, value_str]
            insertion_sql = "insert into qb_title_option (title_id, option_title, option_content) VALUES (%s,%s,%s)"
            self.life_227.insertion_data(insertion_sql, key_value)
            # print('选项', key_value)

    #  解析
    def question_analysis(self):
        try:
            hint_str = self.item['hint']
            title_id = self.item['item_id']
            hint_data, hint_picture_list = self.re_data(hint_str)
            if len(hint_picture_list) > 0:
                data_list = hint_data.split('png')
                n = 0
                hint_data_data = ''
                for d in data_list:
                    hint_data_data += d
                    if n != len(data_list) - 1:
                        pic_url = hint_picture_list[n]
                        pict_name = self.get_md5(pic_url)
                        hint_data_data += pict_name
                        self.with_open(pic_url, pict_name)
                    n += 1
                hint_data_all = hint_data_data
            else:
                hint_data_all = hint_data
            all_data = [title_id, hint_data_all]
            insertion_sql = "insert into qb_analysis (title_id, content) VALUES (%s,%s)"
            self.life_227.insertion_data(insertion_sql, all_data)
            # print('解析', all_data)
        except Exception as e:
            print(e)

    #  答案
    def question_answer(self, id, answer_res):
        question_answer_list = [id, answer_res]
        question_answer_sql = "replace into qb_answer (title_id, content) VALUES (%s,%s)"
        self.life_227.insertion_data(question_answer_sql, question_answer_list)
        # print('答案', question_answer_list)

    def with_open(self, title_url, name_md5):
        respons = self.png_request(title_url)
        geshi = title_url[-3:]
        write = respons.content
        with open(self.os_path + '{}.{}'.format(name_md5, geshi), 'wb') as f:
            f.write(write)
            f.close()

    def get_md5(self, s):
        md = hashlib.md5()
        md.update(s.encode('utf-8'))
        a = md.hexdigest()
        return a

    def re_data(self, data):
        png_url_list = []
        cleans_data_1 = re.sub(r"(<br.*?/>)", '', data.strip(' '))
        cleans_data_2 = re.sub(r"(<br>)", '', cleans_data_1)
        cleans_data_3 = re.sub(r"(<img.*?>)", '{png}', cleans_data_2)
        cleans_data_4 = re.sub(r'(<uline.*?000">)|(<uline.*?000;">)', '___', cleans_data_3)
        cleans_data_5 = re.sub(r"(</uline>)", '___', cleans_data_4)
        cleans_data_6 = re.sub(r"(\u3000)", ' ', cleans_data_5)
        cleans_data_7 = re.sub(r'<div(.*?)(right">|right;">)', '    ', cleans_data_6)
        cleans_data_8 = re.sub(r"(</div>)", '  ', cleans_data_7)
        cleans_data_9 = re.sub(r"(&nbsp;|<sup>|</sup>)", '', cleans_data_8)
        cleans_data_10 = re.sub(r'<div(.*?)(center">|center" >|center;">)', '', cleans_data_9)
        cleans_data_11 = re.sub(r'(<upoint>|</span>|</rt>)(.*?)(<span>|1em;">|</upoint>)', '', cleans_data_10)
        cleans_data_two = re.sub(r"(<answer.*?answer>)", '', cleans_data_11)
        png_re_url_list = re.findall(r"src=\"(.*?)(png|jpg|jpeg)", data)
        data_list = cleans_data_two.split('png')
        for png_url in png_re_url_list:
            pagurl = png_url[0] + png_url[1]
            png_url_list.append(pagurl)
        if '{png}' not in cleans_data_two and len(png_re_url_list) > 0:
            cleans_data_two += '{png}'
        elif len(data_list) == len(png_url_list):
            cleans_data_two += '{png}'
        return cleans_data_two, png_url_list

    def run_spider(self):
        for self.tree_ids in self.tree_ids_dict.keys():
            if self.tree_ids == '200654':
                page = 0
            # elif self.tree_ids == '201128':
            #     page = 101
            # elif self.tree_ids == '200666':
            #     page = 101
            # elif self.tree_ids == '201293':
            #     page = 101
            # elif self.tree_ids == '200667':
            #     page = 28
            # elif self.tree_ids == '201301':
            #     page = 42
            else:
                page = 0
            while True:
                data_text = self.request(page)
                print(self.tree_ids_dict[self.tree_ids] + '第：' + str(page) + '页')
                data_dict = json.loads(data_text.text)
                data_list = data_dict.get('data')
                if data_dict['code'] == 400 and data_list == None:
                    break
                total_count = data_list.get('total_count')
                if data_dict['code'] == 200 and total_count == 0:
                    break
                item_list = data_list.get('items')
                if len(item_list) > 0:
                    for data_d in item_list:
                        try:
                            self.dict_data(data_d)
                            self.question_knowledge()
                            self.question_analysis()
                            self.year_tags()
                        except Exception as e:
                            print(e)
                page += 1


def run_yuwen_danxuan():
    run = JiKeYuWen()
    run.run_spider()


if __name__ == "__main__":
    run_yuwen_danxuan()








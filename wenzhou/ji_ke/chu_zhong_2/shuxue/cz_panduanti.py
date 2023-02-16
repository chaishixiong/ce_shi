import requests
import re
import os
import hashlib
import json
from wenzhou.ji_ke.gao_zhong.cz_settengs import s_x_point_id_list
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import life_227_pool
from wenzhou.ji_ke.chu_zhong.settings import tree_ids_dict_shuxue, cookies
'''
单选，多选，解答题
'''


class JiKe(object):
    def __init__(self):
        self.life_227 = DataBaseSession(life_227_pool)
        self.os_path = 'F:/极课网/生物/'
        self.point_id_dict = s_x_point_id_list
        self.point_id = ''

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
          "item_types": [
            39
          ],
          "item_categories": [],
          "difficulties": [],
          "exam_types": [],
          "years": [],
          "provinces": [],
          "use_search_strategy": False,
          "point_ids": [
              self.point_id
          ],
          "tree_ids": [
              200480
          ],
          "department": 2,
          "subject": 2
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
            answer_answer = self.answer_res(struct_question)
            self.question_answer(self.item['item_id'], answer_answer)

        self.item['knowledge'] = data_all.get('points')  # 知识点
        self.item['tags'] = data_all.get('tags')  # 年-省-市
        self.item['hint'] = hint
        return self.item

    def for_questions(self, question_all):
        questions_list = question_all.get('questions')
        if len(questions_list) > 0:
            for questions in questions_list:
                self.for_questions(questions)
        else:
            title_name = question_all.get('content')
            title_name_data = self.question_stem(title_name)  # 题干
            answers_list = question_all.get('answers')
            answer_res = self.answer_res(question_all)  # 答案
            uid = answers_list[0].get('uid')
            self.question_answer(uid, answer_res)
            qb_title_2_data = [uid, title_name_data, self.item['item_id']]
            insertion_sql = "replace into qb_title_2 (title_id, content, pid) VALUES (%s,%s,%s)"
            self.life_227.insertion_data(insertion_sql, qb_title_2_data)
            # print('二级题干', qb_title_2_data)

    def answer_res(self, answers):
        answers_dict = answers['answers']
        answers_res_list = answers_dict[0].get('answer_res')
        answer_res_data = answers_res_list[0]
        if answer_res_data == '1':
            answer = '√'
        elif answer_res_data == '0':
            answer = '×'
        else:
            answer = ''
        return answer

    # 年-省-市
    def year_tags(self):
        title_id = self.item['item_id']  # 题目id
        content = self.item['title_name']  # 题目内容
        subject = self.item['subject_des']  # 科目
        type = self.item['item_type_des']  # 题型
        grade = self.item['grade_des']  # 年级
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
    def question_stem(self, question_stem_data):
        data = self.re_picture(question_stem_data)
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

    #  题目
    def question_data(self):
        title_id = self.item['item_id']
        option_values_list = self.item['option_values_list']
        for option_values in option_values_list:
            key = option_values.get('key')
            value = option_values.get('value')
            value_str = self.re_picture(value)
            key_value = [title_id, key, value_str]
            insertion_sql = "insert into qb_title_option (title_id, option_title, option_content) VALUES (%s,%s,%s)"
            self.life_227.insertion_data(insertion_sql, key_value)
            # print('选项', key_value)

    #  解析
    def question_analysis(self):
        hint_str = self.item['hint']
        title_id = self.item['item_id']
        hint_data_all = self.re_picture(hint_str)
        all_data = [title_id, hint_data_all]
        insertion_sql = "insert into qb_analysis (title_id, content) VALUES (%s,%s)"
        self.life_227.insertion_data(insertion_sql, all_data)
        # print('解析', all_data)

    #  答案
    def question_answer(self, id, answer_res):
        question_answer_list = [id, answer_res]
        question_answer_sql = "replace into qb_answer (title_id, content) VALUES (%s,%s)"
        self.life_227.insertion_data(question_answer_sql, question_answer_list)
        # print('答案', question_answer_list)

    def re_picture(self, data_data):
        self.picture_url = data_data
        picture_url_list = re.findall(r'://(.*?)(.png|.jpg|.gif)', data_data)
        if len(picture_url_list) > 0:
            for tuple_pic in picture_url_list:
                pic_url = tuple_pic[0]
                pic_gs = tuple_pic[1]
                picture_url = 'https://' + pic_url + pic_gs
                md5_data = self.get_md5(picture_url)
                self.picture_url = self.picture_url.replace(picture_url, md5_data)
                self.with_open(picture_url, md5_data)
        return self.picture_url

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
        cleans_data_1 = re.sub(r"(<br.*?/>)", '', data)
        cleans_data_2 = re.sub(r"(<br>)", '', cleans_data_1)
        cleans_data_3 = re.sub(r"(<img.*?>)", '{png}', cleans_data_2)
        cleans_data_two = re.sub(r"(<answer.*?answer>)", '', cleans_data_3)
        png_re_url_list = re.findall(r"src=\"(.*?)(png|jpg|jpeg)", data)
        for png_url in png_re_url_list:
            pagurl = png_url[0] + png_url[1]
            png_url_list.append(pagurl)
        data_list = cleans_data_two.split('png')
        if len(data_list) == len(png_url_list):
            cleans_data_two += '{png}'
        return cleans_data_two, png_url_list

    def run_spider(self):
        for self.point_id in self.point_id_dict.keys():
            page = 0
            while True:
                data_text = self.request(page)
                print(self.point_id_dict[self.point_id] + '第：' + str(page) + '页')
                data_dict = json.loads(data_text.text)
                data_list = data_dict.get('data')
                total_count = data_list.get('total_count')
                if data_dict['code'] == 400 and data_list == None:
                    break
                elif data_dict['code'] == 200 and total_count == 0:
                    break
                item_list = data_list.get('items')
                if len(item_list) > 0:
                    for data_d in item_list:
                        self. dict_data(data_d)
                        self.question_knowledge()
                        self.question_analysis()
                        self.year_tags()
                page += 1


def run_jike():
    run = JiKe()
    run.run_spider()


if __name__ == "__main__":
    run_jike()








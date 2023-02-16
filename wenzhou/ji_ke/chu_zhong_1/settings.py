import re


shuxue_tree_ids = ['200654', '201128', '200666', '201293', '200667', '201301']  # 年纪
shuxue_point_ids = []  # 章节
shuxue_item_types = []  # 题型
shuxue_difficulties = []  # 难度
shuxue_exam_types = []  # 类型
shuxue_provinces = []  # 省份
shuxue_years = []  # 年份

tree_ids_dict_shuxue = {
    '200654': '初中数学七年级上册',
    '201128': '初中数学七年级下册',
    '200666': '初中数学八年级上册',
    '201293': '初中数学八年级下册',
    '200667': '初中数学九年级上册',
    '201301': '初中数学九年级下册',
}

tree_ids_dict_huaxue = {
    '200671': '初中数学九年级上册',
    '200700': '初中数学九年级下册',
}

tree_ids_dict_dili = {
    '202560': '初中数学七年级上册',
    '202561': '初中数学七年级下册',
    '202562': '初中数学八年级上册',
    '202563': '初中数学八年级下册',
}
tree_ids_dict_other = {
    '202560': '初中数学七年级上册',
}


cookies = 's_v_web_id=verify_l7snhfp1_hH2lEGeJ_Qy5B_4uKX_BX6d_INtM1L3E1gSh; passport_csrf_token=009068cea24bf5255b60b6a037197042; passport_csrf_token_default=009068cea24bf5255b60b6a037197042; n_mh=68kQnpaUz3XZTSY57tndYpoJEyA_8sTFxagX-ti5bko; odin_tt=ab0983b3a8c4cd18ddb54dfce4fdc37af69acd1e2ac80bc27f64de3253b99f411686947d99df1a1d63399710398dcdf362b8ec125f5154d778647b557dfa8f9d; sid_guard=07336414d9d82f62c160dcbe25c46d0a%7C1663314487%7C5184000%7CTue%2C+15-Nov-2022+07%3A48%3A07+GMT; uid_tt=7fd1a70730fa0afc1e037181f2940a3d; uid_tt_ss=7fd1a70730fa0afc1e037181f2940a3d; sid_tt=07336414d9d82f62c160dcbe25c46d0a; sessionid=07336414d9d82f62c160dcbe25c46d0a; sessionid_ss=07336414d9d82f62c160dcbe25c46d0a; sid_ucp_v1=1.0.0-KDdjM2MxNmE0NzVhYTMyYTJlMjc4YTFiZmU3MmU1ZDU4MWE4M2Q5MDQKHwiTwtDL543WBhC31JCZBhj5GiAMMMKwno8GOAJA7wcaAmxmIiAwNzMzNjQxNGQ5ZDgyZjYyYzE2MGRjYmUyNWM0NmQwYQ; ssid_ucp_v1=1.0.0-KDdjM2MxNmE0NzVhYTMyYTJlMjc4YTFiZmU3MmU1ZDU4MWE4M2Q5MDQKHwiTwtDL543WBhC31JCZBhj5GiAMMMKwno8GOAJA7wcaAmxmIiAwNzMzNjQxNGQ5ZDgyZjYyYzE2MGRjYmUyNWM0NmQwYQ; x-jupiter-uuid=16655716817959364; ttwid=1%7CskdjwFaJmmsutTEyKU5QDEioErv98UueIC9H1VGxZeA%7C1665709392%7C286c48deb35a565d6e243e06edc49d85de7be9af7a4749ecc0f6cc4b410d8917'


def re_data(data):
    png_url_list = []
    cleans_data_1 = re.sub(r"(<br.*?/>)", '', data.strip(' '))
    cleans_data_2 = re.sub(r"(<br>)", '', cleans_data_1)
    cleans_data_3 = re.sub(r"(<img.*?>)", '{png}', cleans_data_2)
    cleans_data_4 = re.sub(r'(<uline.*?000">)|(<uline.*?000;">)', '___', cleans_data_3)
    cleans_data_5 = re.sub(r"(</uline>)", '___', cleans_data_4)
    cleans_data_6 = re.sub(r"(\u3000)", ' ', cleans_data_5)
    cleans_data_7 = re.sub(r'<div(.*?)(right">|right;">)', '    ', cleans_data_6)
    cleans_data_8 = re.sub(r"(</div>)", '  ', cleans_data_7)
    cleans_data_9 = re.sub(r"(&nbsp;|<sup>|</sup>|<span>|</span>)", '', cleans_data_8)
    cleans_data_10 = re.sub(r'<div(.*?)(center">|center" >|center;">|<b>|</b>)', '', cleans_data_9)
    cleans_data_11 = re.sub(r'(<upoint>|</span>|</rt>)(.*?)(<span>|1em;">|</upoint>)', '', cleans_data_10)
    cleans_data_two = re.sub(r"(<answer.*?answer>)", '___', cleans_data_11)
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


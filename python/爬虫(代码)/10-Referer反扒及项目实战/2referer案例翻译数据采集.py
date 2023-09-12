"""
要采集翻译数据   在采集完一页以后
在抓取后面 2  3  4  5页的参数做对比    看参数变化的规律能不能通过代码实现
如果不能通过循环之类的常见处理方法   就要考虑js逆向(后面会讲)

第一页
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=0&bkn=&r=0.9911

第二页
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=1&bkn=&r=0.9911

第三页
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=2&bkn=&r=0.1985
第四页
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=3&bkn=&r=0.5107
第五页
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=4&bkn=&r=0.4194

发现 page 是变化
发现不能按规律生成的参数  可以尝试删除一部分发送请求     看能不能获取
不能在考虑JS逆向(后面会讲)
"""

import  requests
from jsonpath import jsonpath
import  json

# for i in range(5):
#     url = f"https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page={i}&bkn=&r=0.4194"
#     # 请求头 里面是键值对  值前面不要加空格
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
#         "cookie":"RK=B6t1BsgNfN; ptcz=a4b0c3645b4488c8897dc4cfe1c82b41d0abc9430540b3d166aa842536a70ed2; eas_sid=p186r7k8w6z7K8H8b9V5M0w4q8; uin_cookie=o1308826174; ied_qq=o1308826174; LOLWebSet_AreaBindInfo_1308826174=%257B%2522areaid%2522%253A%25225%2522%252C%2522areaname%2522%253A%2522%25E7%258F%25AD%25E5%25BE%25B7%25E5%25B0%2594%25E5%259F%258E%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221308826174%2522%252C%2522rolename%2522%253A%2522%25E6%2588%2591%25E7%2588%25B1%25E5%25BE%25AE12%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1308826174%257C5%257C1308826174*%257C%257C%257C%257C%2525E6%252588%252591%2525E7%252588%2525B1%2525E5%2525BE%2525AE12*%257C%257C%257C1678678931%257C%2522%252C%2522md5str%2522%253A%2522D50FC9B994803469848BD46C85BEEE73%2522%252C%2522roleareaid%2522%253A%25225%2522%252C%2522sPartition%2522%253A%25225%2522%257D; uin=o1308826174; pac_uid=1_1308826174;",
#         "referer": "https://ke.qq.com/course/292490?tuin=d4c97e25"
#     }
#     # 发送请求
#     response = requests.get(url=url, headers=headers)
#     # 获取文本
#     str_data = response.content.decode()
#     # print(str_data)
#     # 数据转换 进行数据清洗   str >> dict    <?>
#     dict_data = json.loads(str_data)
#     nick_name = jsonpath(dict_data, "$..nick_name")
#     first_comment = jsonpath(dict_data, "$..first_comment")
#     data_list = []
#     with open(f"评论{i+1}.json", "w", encoding="utf-8") as file1:
#         for data in zip(nick_name, first_comment):
#             comment_data = {
#                 "nickname": data[0],
#                 "comment": data[1],
#             }
#             data_list.append(comment_data)
#         # list >> str
#         datas = json.dumps(data_list, ensure_ascii=False, indent=2)
#         file1.write(datas)

#把所有数据保存到一个文件  文件写入只能执行一次 json
with open("all评论.json","w",encoding="utf-8")as file1:
    data_list = []
    for i in range(5):
        url = f"https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page={i}&bkn=&r=0.4194"
        # 请求头 里面是键值对  值前面不要加空格
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "cookie":"RK=B6t1BsgNfN; ptcz=a4b0c3645b4488c8897dc4cfe1c82b41d0abc9430540b3d166aa842536a70ed2; eas_sid=p186r7k8w6z7K8H8b9V5M0w4q8; uin_cookie=o1308826174; ied_qq=o1308826174; LOLWebSet_AreaBindInfo_1308826174=%257B%2522areaid%2522%253A%25225%2522%252C%2522areaname%2522%253A%2522%25E7%258F%25AD%25E5%25BE%25B7%25E5%25B0%2594%25E5%259F%258E%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221308826174%2522%252C%2522rolename%2522%253A%2522%25E6%2588%2591%25E7%2588%25B1%25E5%25BE%25AE12%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1308826174%257C5%257C1308826174*%257C%257C%257C%257C%2525E6%252588%252591%2525E7%252588%2525B1%2525E5%2525BE%2525AE12*%257C%257C%257C1678678931%257C%2522%252C%2522md5str%2522%253A%2522D50FC9B994803469848BD46C85BEEE73%2522%252C%2522roleareaid%2522%253A%25225%2522%252C%2522sPartition%2522%253A%25225%2522%257D; uin=o1308826174; pac_uid=1_1308826174;",
            "referer": "https://ke.qq.com/course/292490?tuin=d4c97e25"
        }
        # 发送请求
        response = requests.get(url=url, headers=headers)
        # 获取文本
        str_data = response.content.decode()
        # print(str_data)
        # 数据转换 进行数据清洗   str >> dict    <?>
        dict_data = json.loads(str_data)
        nick_name = jsonpath(dict_data, "$..nick_name")
        first_comment = jsonpath(dict_data, "$..first_comment")
        for data in zip(nick_name, first_comment):
            comment_data = {
                "nickname": data[0],
                "comment": data[1],
            }
            data_list.append(comment_data)
    # list >> str
    datas = json.dumps(data_list, ensure_ascii=False, indent=2)
    file1.write(datas)
"""
目标：抓取腾讯课程评论数据
流程：
    网址：https://ke.qq.com/course/292490?tuin=d4c97e25#term_id=100346594
    目的：抓取腾讯课程评论数据
    采集字段： 评论人  详情评论数据
    保存到json文件

准备工具：
明确数据类型
    json类型   jsonpath/re
确认数据字段的位置
    都在一个数据包
"""

"""
抓包流程：
1. 打开开发者工具  f12
2. 刷新网页以后  最上面的是最先生成的数据包
3. 如何在网页上(看到了自己要采集的数据以后)   再去抓包  不然就做生成数据包的操作(点击用户评论)
4. 发现是异步加载(网页没有刷新)的数据包  可以通过   数据包的筛选标签  fetch/xhr
"""
import  requests
from jsonpath import jsonpath
import  json

#评论接口
url ="https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=2&bkn=&r=0.3282"
# 请求头 里面是键值对  值前面不要加空格
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "referer": "https://ke.qq.com/course/292490?tuin=d4c97e25"

}
#发送请求
response = requests.get(url=url, headers=headers)
#获取文本
str_data = response.content.decode()
#print(str_data)
#数据转换 进行数据清洗   str >> dict    <?>
dict_data = json.loads(str_data)
nick_name = jsonpath(dict_data,"$..nick_name")
first_comment = jsonpath(dict_data,"$..first_comment")
print(nick_name)
print(first_comment)
print(len(nick_name))
print(len(first_comment))

data_list = []
with open("评论1.json", "w", encoding="utf-8") as file1:
    for data in zip(nick_name, first_comment):
        comment_data = {
            "nickname":data[0],
            "comment": data[1],
        }
        data_list.append(comment_data)
    # list >> str
    datas = json.dumps(data_list, ensure_ascii=False, indent=2)
    file1.write(datas)

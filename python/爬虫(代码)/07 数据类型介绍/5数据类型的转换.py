"""
如何构建好能用 jsonpath 提前数据的数据   !=str
需要使用到的模块
json 是python自带的模块  不用下载
        从网页上采集下来的数据，不论是html还是json都是str类型
需要把str类型转换成json(dict)
通过 json.loads(str_data)  result_type >>> dict
"""
import  json
import  re
import  requests

# 1. 抓包： 包含：1. 车辆款式  2. 价格区间  指导价格
url = "https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc"

# 请求头
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 请求的参数
# 可以通过 ctrl+R进行替换; \n
data = {
    "sort_new": "hot_desc",
    "city_name": "成都",
    "limit": "30",
    "page": "5",
}
# 2.发送请求  获取响应
response =  requests.post(url=url, headers=headers, data=data)
res_data =  response.content.decode()
# print(res_data)
#
# print(type(res_data))
# str > dict/json操作
json_data = json.loads(res_data)
# print(json_data)
# print(type(json_data))


# dict >> str 进行写入 ensure_asciii=Fasle 代表不对中文进行转码
str_data = json.dumps(json_data)
print(str_data)
print(type(str_data))
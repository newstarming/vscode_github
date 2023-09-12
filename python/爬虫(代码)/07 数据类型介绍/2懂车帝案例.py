"""
同步加载数据包和异步加载数据包在请求方法上有没有区别？
猜想？
答案：  没有区别   都是通过request库的get或post方法 进行请求
目的： 采集懂车帝的车辆列表信息
    url:https://www.dongchedi.com/auto/library/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
    字段： 1. 车辆款式  2. 价格区间  指导价格
"""

"""
1. 抓包  包含：1. 车辆款式  2. 价格区间  指导价格
    tips: 需要根据实际需求在 response 里面搜索你需要的内容，如果全部都有就确认数据包，如果直接部分字段，就换数据包抓取
    tips: 抓取异步加载的数据包  可以通过  Fetch/Xhr 搜索数据包的标签来筛选
    Fetch/xmL/http/requests
2. 发送请求   获取响应
3. 清洗数据
4. 保存到txt文件

"""
import  requests
import  re
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
print(res_data)
# 请求到了数据还要验证一下数据内容  1. 车辆款式 2.价格
# 如何发现网页的数据和数据包的数据有差别  一切以数据包内容为准

#3. 数据清洗  使用正则模块

#findall(): 参数1 正则表达式   参数2 需要被匹配的字符串
#  123456789  4和7中间是  56   4是前标杆  7是后标杆

#1. 车辆的款式
outter_name = re.findall('outter_name":"(.*?)","pre_price"', res_data)
print(outter_name)
#1. 价格
pre_price = re.findall('official_price":"(.*?)","outter_name"', res_data)
print(pre_price)
# 4. 保存到 txt文件
print(len(outter_name))
print(len(pre_price))


# '捷豹XEL' , '29.98万'
#  需要使用组合数据的函数  zip  拉链函数
with open("懂车帝.txt", "w", encoding="utf-8") as file1:
    for car in zip(outter_name,pre_price):
        print(car)
        file1.write(str(car)+"\n")




"""
作业  采集翻页的数据(采集5页) 自己练习抓取异步加载的数据包  对比每个数据包的参数  构建好以后分布发送请求保存到不同的txt文件
代码截图发给我  
重点： 要自己手动构建正则匹配字符串保存

提交：192516521@qq.com
"""
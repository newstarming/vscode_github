"""
目的：https://bj.lianjia.com/ershoufang/dongcheng/pg1/
采集该网站下面的指定字段
1. 标题名
2. 标价
3. 平方价格
4. 户型
5. 房屋大小

流程
1. 抓取包含了数据的数据包  确认数据类型 html 请求方法Get
2. 获取数据以后需要进行数据转换    str>> element  xpath提取数据的对象是element对象
3. 再进行数据的清洗
4. 数据的保存
"""
import  requests
import  json
"""
采集数据：在网页返回数据到控制台后， 先查看内容里面有没有你要的数据再写语法
"""

"""
需要使用 lxml 模块
pip install lxml 加源
导入模块 
from lxml import etree
"""
from lxml import etree
url = "https://bj.lianjia.com/ershoufang/dongcheng/pg1/"
#请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Cookie":"lianjia_uuid=70e02a31-b685-4ed5-8263-44a242ccae23; _smt_uid=645b8bb6.853630f; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221880599bf688a6-021d2d718eb36d-c4e7526-2073600-1880599bf69cdc%22%2C%22%24device_id%22%3A%221880599bf688a6-021d2d718eb36d-c4e7526-2073600-1880599bf69cdc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.509358956.1683721144; _gid=GA1.2.2083956186.1683721144; lianjia_ssid=23e4879b-a047-e557-169a-06074d00ec21; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1683721142,1683726876; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1683726876; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiM2U0ODY4YzRjYjZkOGE3NjdhNDgyMDA4ZTJjMDQzZjAwNDgyMWE5NjBmZDMyZTQwYmJhM2RlODZhNDYzNjk5ZmI4ZDliZjkwYjViMmNkNzU3YjEzYTY2ZDQ1MzNkNTBlYTgxN2NkYjJjMjFiZGRkOWNlYWVjNTZmNjhkZGNhNjFkZDgwN2Q1ZGUzNWQ3NTJiNGNlNDE0NzU0MWFlMzA1NmVhYzgyMTU0YzEyZTZiNmEzZjQ1YjBiNjhmZjdkNWIyNmNkYzZkNDY3YWM3YzJjYTcwOGQwMTM0Mjk2Zjc3YTBlOGI3NzVmNDRhNDU4NzllNDNiYjRlNWFhMmM0MzZjZlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI1NDZhMjIzNFwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvZG9uZ2NoZW5nL3BnMS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=="
}

#发送请求
response = requests.get(url=url, headers=headers)
res_data = response.content.decode()
print(res_data)
print(type(res_data))
# 通过etree 模块里面的HTML方法， 把str类型数据转换成element类型数据
html = etree.HTML(res_data)

print(type(html))
print(html)

"""
1. 标题名
2. 标价
3. 平方价格
4. 户型
5. 房屋大小
"""
# 1. 标题名
# 通过html对象的xpath方法提前网页数据  参数一个单引号的字符串  里面就是语法
titles = html.xpath('//div[@class="info clear"]/div[1]/a/text()')
print(titles)
#2. 标价
prices = html.xpath('//div[@class="info clear"]/div[6]/div[1]/span/text()')
print(prices)
#3. 平方价格
peace_price = html.xpath('//div[@class="info clear"]/div[6]/div[2]/span/text()')
print(peace_price)
#4. 户型 #5. 房屋大小
public_data = html.xpath('//div[@class="info clear"]/div[3]/div[1]/text()')
print(public_data)
huxing_list = []
house_size_list = []

for data in public_data:
    # data.split(" | ") 切割字符串方法
    #2室1厅 | 62.62平米 | 南 北 | 精装 | 中楼层(共5层) | 1960年建 | 板楼
    hx_data = data.split(" | ")[0]
    huxing_list.append(hx_data)
    house_size = data.split(" | ")[1]
    house_size_list.append(house_size)
print(huxing_list)
print(house_size_list)
print(len(titles))
print(len(prices))
print(len(peace_price))
print(len(huxing_list))
print(len(house_size_list))

"""
 把所有的数据写入到一个列表， 再跳出循环对列表数据进行转换， list > str 再写入文件
"""
data_list = []
with  open("链家.json", "w", encoding="utf-8") as file1:
    for i  in zip(titles,prices,peace_price,huxing_list,house_size_list):
        item = {
            "title":i[0],
            "price":i[1],
            "peace_price":i[2],
            "huxing":i[3],
            "house_size":i[4]
        }
        data_list.append(item)
    #跳出循环写入文件
    json.dump(data_list,file1,ensure_ascii=False)
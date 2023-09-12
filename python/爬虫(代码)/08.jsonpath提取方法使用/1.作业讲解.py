"""
作业 采集翻页数据(采集5页) 自己练习抓取异步加载的数据包  对比每个数据包的参数 构建好以后分别发送请求
保存为不同的txt文件
懂车帝作业： 异步+翻页(URL+POST)

**重点**：在于要自己手动构建正则匹配字符串保存

目的: 采集翻页的汽车数据    已知结论 能采集单页的数据！
翻页？   更古不变的道理  抓取翻页数据的重点 ？
        找请求每一页数据的参数   找不同！ 找规律  看python能不能模仿

做项目 得先完成再完美(最省力法则)      先把实质性目的完成  再考虑优化代码

第一步 找参数
第一页url https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc
第一页的参数
country: 0
sort_new: hot_desc
city_name: 成都
limit: 30
page: 1

第二页url https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc
第二页的参数
country: 0
sort_new: hot_desc
city_name: 成都
limit: 30
page: 2

第三页url https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc
第三页的参数
country: 0
sort_new: hot_desc
city_name: 成都
limit: 30
page: 3

第四页url https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc
第四页的参数
country: 0
sort_new: hot_desc
city_name: 成都
limit: 30
page: 4

发现每一页的参数中 page字段在变化 每次以加一的形式递增

如何快速找到提供数据的URL地址：
    网页一般数据都是以异步的方式提供： XHR/Fetch
    根据找的数据类型看请求方法的名字： 列表-->select_series_v2
    看请求方法+URL+携带的参数
"""
import requests
import re
import json
url="https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc"

# 请求头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
# 发送请求
# 文件操作参数w 代表如果再次对文件进行写入 会进行覆盖  因此要进行数据追加得用a  append追加和写入
with open("懂车帝3.json", "w", encoding="utf-8")as file1:
    for i in range(1):
        print(i)
        data={
            "country": "0",
            "sort_new": "hot_desc",
            "city_name": "成都",
            "limit": "30",
            "page": i+1
        }
        response=requests.post(url=url,headers=headers,data=data)
        res_data=response.content.decode()
        print(res_data)
    #     复盘清洗数据操作 重点
    #     具体字段   指导价格
    #     1.车辆款式  注意点   正则表达式外面的用单引号  里面用双引号
        car_style=re.findall('"outter_name":"(.*?)","pre_price":',res_data)
        print(car_style)
    # #     2价格区间
        prices=re.findall('"official_price":"(.*?)","outter_name',res_data)
        print(prices)
        print(len(car_style))
        print(len(prices))
        for i in zip(car_style,prices):
            item={
                "style":i[0],
                "price":i[1]
            }
            # write 只能写入字符串 或者在文件操作方式传入wb时能写入字节 其他都不能写入
            # 字典转字符串    dumps列表转字符串,ensure_ascii=False代表不对中文进行编码
            print(item)
            str_data=json.dumps(item,ensure_ascii=False)
            file1.write(str_data+",\n")

"""
优化代码：
1. 先完成功能（最省力的方法）
2. 看循环的代码(把多次变1次)
法则：减少做的事情，改善工作方式

"""

"""
问：如何采集二级目录数据?
需要分清二级目录url和翻页url
    二级目录就是每一页的item(项目)里面的详细数据 
    翻页url就是每一页的数据
    翻页的url对应的响应内容包含二级目录url   

https://www.dongchedi.com/auto/series/4865
https://www.dongchedi.com/auto/series/4857
https://www.dongchedi.com/auto/series/5288
https://www.dongchedi.com/auto/series/649
要想采集二级目录数据  车辆价格  就得在一级目录的响应内容找二级目录的url或者关键性参数
1.写一个正则 匹配每一辆车的 concern_id 然后和 https://www.dongchedi.com/auto/series/拼接得到二级目录url
2.向二级目录url发送请求得到二级目录响应内容！
"""









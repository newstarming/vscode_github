"""
目的 到目标网址采集对应的贴吧数据保存到本地!
url:https://tieba.baidu.com/f?ie=utf-8&kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&fr=search

流程
1.确认数据包
2.发送请求 获取响应
3.暂时不需要清洗 直接保存数据

href="./../视频/可惜没如果.png"  
"""
import requests
# 1.确认数据包  根据数据包的response标签里面 有你要的关键字进行数据包的确认!    因为有"英雄联盟吧"所以确认了数据包
url="https://tieba.baidu.com/f?ie=utf-8&kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&fr=search"

# 请求头
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 发送请求
response=requests.get(url=url,headers=headers)
# 以字符形式保存
response_data=response.content.decode()  #response.text 交换使用
with open("英雄联盟.html","w",encoding="utf-8")as file1:
    file1.write(response_data)
















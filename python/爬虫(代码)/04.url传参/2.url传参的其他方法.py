"""
如果需要传递多个参数使用字符串拼接就不是很好维系代码

制作一个规范的传递参数的程序
通过输入不同的内容采集不同的数据保存到html文件

步骤
1.写input操作
2.拿网址进行参数拼接  或者通过params参数传递
3.发送请求 获取响应
4.保存数据
"""
import requests
import random
def crawl_data1():
    word=input("请输入要采集的关键字:")
    url="https://search.bilibili.com/all?keyword="+word
    ua_pool = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    ]
    ua=random.choice(ua_pool)
    headers={
        "user-agent":ua
    }
    response=requests.get(url=url,headers=headers)
    response_data=response.content.decode()
    print(response_data)
    with open(f"{word}.html","w",encoding="utf-8")as file1:
        file1.write(response_data)

# 使用get方法的规范的参数进行传递    关键字 params
def crawl_data2():
    word = input("请输入要采集的关键字:")
    url = "https://search.bilibili.com/all?"
    ua_pool = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    ]
    ua = random.choice(ua_pool)
    headers = {
        "user-agent": ua
    }
    # https://search.bilibili.com/all?keyword=%E6%B7%84%E5%8D%9A%E7%83%A7%E7%83%A4&from_source=webtop_search&spm_id_from=333.1007&search_source=5
    # 构建形式是 {键:值}   ==== 对应的是url后面的键值对    :号等于=号   &号等于,逗号
    params={
        "keyword": word,
        "from_source":"webtop_search",
        "spm_id_from": "333.1007",
        "search_source":"5"
    }
    # 这里使用params以后  get方法会自动讲参数镶嵌到主页url后面发送请求
    response=requests.get(url=url,headers=headers,params=params)
    response_data=response.content.decode()
    print(response_data)
    with open(f"{word}.html","w",encoding="utf-8")as file1:
        file1.write(response_data)
crawl_data2()





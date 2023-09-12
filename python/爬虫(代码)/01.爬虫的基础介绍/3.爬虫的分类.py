"""
1.通用爬虫
    什么是通用爬虫 ? 什么数据都进行爬取的爬虫
    百度就是一个通用爬虫(搜索引擎)!

2.聚焦爬虫
    是我们要深入学习的知识点
    针对性的对单一网站进行采集的爬虫,  针对这个网页的 png  mp4 mp3  ts
    2.1累积式爬虫   从开始到结束一直进行爬取  中间做到去重操作(一次性的，内存释放以后，程序结束以后再次运行会重复采集)
            是在内存条里面读取是否采集了当前的数据来进行判断
            (这里的文件，数据会随着程序，线程的结束 消失掉)
    2.2增量式爬虫   从开始到结束一直进行爬取  中间做到去重操作(非一次性的，会读取本地的文件，看文件是否存在
    if 文件存在:
        不爬取
    else
        爬取)
            是在硬盘(机械硬盘，固态硬盘)里面去读取的数据来进行判断
            (这里的文件，数据不会随着程序，线程的结束消失掉)

"""
# 2.1累积式爬虫
def crawl_data():
    list1=[]
    print("获取链接")
    url="https:xxxx"
    list1.append(url)
    list1.append(url)
    list1.append(url)
    print(list1)
#     去重操作
    datas=set(list1)
    print(datas)
    for data in datas:
        print(f"采集{data}")
crawl_data()



# 2.2增量式爬虫
import os

def crawl_data():
    list1=[]
    print("获取链接")
    url="https:xxxx"
    list1.append(url)
    list1.append(url)
    list1.append(url)
    print(list1)
#     去重操作
    if not os.path.exists("雪中悍刀行.txt"):
            print(f"采集")
crawl_data()




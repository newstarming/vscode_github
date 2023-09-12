
#作业1： 采集翻页的贴吧数据  采集5页
    #提示：  pn字段在变化   循环    字符串拼接/params传参

#作业2： 使用面向对象改写， 采集翻页贴吧数据的代码


#第一个作业
#
#
"""
#第一页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&ie=utf-8&pn=0
# 记录：0~50 [)
#第二页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&ie=utf-8&pn=50
# 记录：50~100  [)
#第三页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&ie=utf-8&pn=100
#第四页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&ie=utf-8&pn=150
#采集不同页数的贴吧数据，更改的参数就是pn字段，
"""

import  requests
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
# }
# kw = input("请输入要采集的贴吧数据关键字：")
# for i in range(5):
#     #format
#     url = f"https://tieba.baidu.com/f?kw={kw}&ie=utf-8&pn={i*50}"
#     response = requests.get(url=url,headers=headers)
#     with open(f"{kw}{i+1}.html","w",encoding="utf-8") as file1:
#         file1.write(response.content.decode())

"""
#第二个作业
使用面向对象改写采集贴吧数据案例？

为什么要用面向对象？ 它是一种编程思想，能更好的使程序员与程序员直接进行对接
面向对象可以理解为一个类  手机
有属性   变量      颜色|尺寸|
有方法   实现功能的函数   手机功能：打电话 发短信
调用？ 要通过类实例化对象，通过对象调用类里面的方法   以实现采集数据的效果
"""

class Tieba(object):
    def __init__(self):
        #实例属性  想当于变量
        self.url = "https://tieba.baidu.com/f?"
        # 请求头
        self.headers = {
           "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
        }
        # 声明实例方法

    # 1. 声明发送请求的方法
    def crawl_data(self, params,kw,i):
        response = requests.get(url=self.url, headers=self.headers, params=params)
        datas = response.content.decode()
        self.save_data(datas, kw,i)

    # 2. 声明保存数据的方法
    def save_data(self, datas,kw,i):
        with open(f"{kw}{i + 1}.html", "w", encoding="utf-8") as file1:
            file1.write(datas)
        print(f"{kw}第{i+1}页的贴吧数据已经采集完毕")

    #  调用主程序的方法
    def run(self):
        #方法与方法直接调用需要加 self.方法名()
        #https://tieba.baidu.com/f?kw=林俊杰&ie=utf-8&pn=150
        kw = "林俊杰"
        # 0 1 2 3 4
        for i in range(5):
            params = {
                "kw": kw,
                "ie": "utf-8",
                "pn": i*50,
            }
            print(params)
            self.crawl_data(params,kw,i)

#实现功能
# 类实例化对象   通过类实例化对象调用方法
tieba = Tieba()  #构造方法，定义了参数，类实例化就需要传入参数，反之则不传
tieba.run()


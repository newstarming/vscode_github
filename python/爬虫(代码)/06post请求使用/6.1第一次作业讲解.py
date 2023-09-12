"""
作业
作业1 采集翻页的贴吧数据   采集5页的
        提示  pn字段在变化   循环  字符串拼接/params传参

作业2 使用面向对象改写  采集翻页贴吧数据的代码
        实例属性  静态的 headers url
        实例方法  发送请求的   保存数据的方法
通过类实例化对象  通过对象调用 类里面的方法 完成数据采集

2304-第一次作业-xxx(真名)
把自己写的代码复制给我
发送到 192516521@qq.com
下周一之前交       周三讲解

第一个作业 :
第一页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E5%98%89%E5%B0%94&ie=utf-8&pn=0
第二页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E5%98%89%E5%B0%94&ie=utf-8&pn=50
第三页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E5%98%89%E5%B0%94&ie=utf-8&pn=100
第四页url:https://tieba.baidu.com/f?kw=%E7%8E%8B%E5%98%89%E5%B0%94&ie=utf-8&pn=150
要采集不同页数的贴吧数据  要更改的参数就是pn字段   变更的规律是 以50递增
"""
# 第一页贴吧的url
import requests
headers={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
kw=input("请输入要采集的贴吧数据关键字:")
for i in range(5):
    url=f"https://tieba.baidu.com/f?kw={kw}&ie=utf-8&pn={i*50}"
    #url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}".format(kw, i * 50)
    #url = "https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s" % (kw,i*50)  #有花括号时，就用这种
    response=requests.get(url=url,headers=headers)
    # with open 打开文件(连着用)
    with open(f"{kw}{i+1}.html","w",encoding="utf-8")as file1:
        file1.write(response.content.decode())
"""
使用面向对象改写采集贴吧数据案例？
为什么要用面向对象？
它是一种编程思想   能更好的使程序员与程序员之间做对接
面向对象可以理解成一个类 
有属性  变量
有方法  实现功能的"函数" 

怎么改写？
根据需求 
采集翻页贴吧数据
实例属性 变量 静态的东西  url headers
实例方法 发送请求  清洗数据  保存数据的方法！
调用？
需要通过类实例化对象，通过对象调用类里面的方法  实现采集数据的效果！ 

按 ctrl+alt+l

"""
# 模块是属于全局变量 不用写入类里面
import requests


# 基类  对顶层的类
#self 实例
#cls  类
class Tieba(object):
    #     实例属性是写在构造方法里面的
    def __init__(self):
        # 实例属性  相当于变量
        self.url = "https://tieba.baidu.com/f?"
        # 请求头
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    # 声明实例方法
    # 声明发送请求的方法
    def crawl_data(self, params, kw, i):
        response = requests.get(url=self.url, headers=self.headers, params=params)
        datas = response.content.decode()
        #   调用保存数据的方法
        self.save_data(datas, kw, i)

    # 声明保存数据的方法
    def save_data(self, datas, kw, i):
        # 需要有一个文件名参数  林俊杰
        with open(f"{kw}{i + 1}.html", "w", encoding="utf-8")as file1:
            file1.write(datas)
        print(f"{kw}第{i + 1}页的贴吧数据已经采集完毕！")

    #   调用主程序的方法
    def run(self):
        # 方法与方法直接按调用需要加self.方法名()
        # https://tieba.baidu.com/f?kw=林俊杰&ie=utf-8&pn=0
        kw = "林俊杰"
        # 0 1 2 3 4
        for i in range(5):
            params = {
                "kw": kw,
                "ie": "utf-8",
                "pn": i * 50}
            print(params)
            self.crawl_data(params, kw, i)


# 实现功能
# 通过类实例化对象   通过对象调用类里面的方法
tieba = Tieba()
tieba.run()

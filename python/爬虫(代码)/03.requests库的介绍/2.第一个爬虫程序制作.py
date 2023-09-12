"""
目的:通过requests模块向一个网页发送请求 并且将网页对应的数据保存到本地为一个html文件?
爬虫流程
    1.确认url
    2.向url发送请求 获取响应
    3.对数据进行清洗
    4.保存数据
打勾选择行以后  按 F11 取消也是按F11

Request URL: https://www.baidu.com/
Request Method: GET

ctrl+alt +l 是格式化代码的意思
"""
import requests
def crawl_baidu():
    # 1.确认url
    # url是资源定位符/链接 /数据包
    url="https://www.baidu.com/"
    # 通过requests的get方法向这个url发送请求.服务器返回对应的响应内容   默认响应变量叫response
    # 通过关键字参数传参
    # 可以把get()看成调用函数的意思  橙色的url就代表指定get函数的url形参 后面的白色url是实参
    response=requests.get(url=url)
    # response=requests.get(url)
    print(response) #<Response [200]> 本次请求响应码是200 表示请求成功!
    # 我要的是网页文本 保存到HTML文件     html是什么一个文件后缀:作用表示网页骨架(包含了链接,文本)
    # 获取文本方式1   response.text返回的是str类型的数据
    # data=response.text
    # print(data)
    # <class 'str'>
    # print(type(data))
    print(response.encoding) #ISO-8859-1
    # 强制的把响应的编码形式改成和py文件同样兼容的 utf-8
    response.encoding="utf-8"
    # response.text是把响应内容以文本str形式进行返回
    data=response.text
    print(response.encoding)
    print(data)
    # 但凡涉及str类型的数据写入 必须在open()里面加指定编码参数
    # with open()是操作文件的函数    参数1:文件名 ,参数2:文件操作方式(a,w,wb,ab,r+,w+) 参数3:编码utf-8
    # w代表对文件覆盖式写入 再次运行就会覆盖掉之前保存的内容
    with open("百度.html","w",encoding="utf-8")as file1:
        file1.write(data)

    # 1.为什么采集下来的html文件和实际的baidu主页的内容所展示的不一样？
    # 由于我们仅仅是采集的整个网页的部分数据 所以展示又出入是正常的!
    # 2.在html文件点击谷歌浏览器报错 不能打开html文件 是因为没有指定清楚谷歌浏览器的位置
    # 看视频操作  通过Everything软件查 chrome.exe  再到pycharm设置

"""
小tips 
网页组成是由 .html  .css  .js  

html 负责网页的骨架(文本:链接:) 爬虫主要爬取的就是html文件 
css  负责网页的排版(起美化效果)    
js   负责监听用户动作  点击某某标签以后反馈用户的文件


"""
#
# 第二种获取文本保存的方法
def crawlbaidu2():
    # 1.确认url
    # url是资源定位符/链接 /数据包
    url = "https://www.baidu.com/"
    # 通过requests的get方法向这个url发送请求.服务器返回对应的响应内容   默认响应变量叫response
    # 通过关键字参数传参
    # 可以把get()看成调用函数的意思  橙色的url就代表指定get函数的url形参 后面的白色url是实参
    response = requests.get(url=url)
#     获取文本类型数据   response.content.decode()>>type(str)
#     response.content是将数据以字节形式进行返回>>>type>>bytes  如果在后面加了decode()方法就是对字节进行解码
#     response.content.decode()默认是以utf-8进行解码  不用手动更改解码方式!
    response_data=response.content.decode()
    print(response_data)
    print(type(response_data))  #<class 'str'>
    with open("百度2.html","w",encoding="utf-8")as file1:
        # file1.write只支持str或者bytes类型的数据
        file1.write(response_data)
# crawlbaidu2()

#
# 第三种获取数据保存到本地的方法  通过字节写入
def crawlbaidu3():
    # 1.确认url
    # url是资源定位符/链接 /数据包
    url = "https://www.baidu.com/"
    # 通过requests的get方法向这个url发送请求.服务器返回对应的响应内容   默认响应变量叫response
    # 通过关键字参数传参
    # 可以把get()看成调用函数的意思  橙色的url就代表指定get函数的url形参 后面的白色url是实参
    response = requests.get(url=url)
    # response.content 将数据包对应的内容以字节形式进行返回    如果需要得到字符就需要通过decode方法进行bytes>str
    response_data = response.content
    print(response_data)
    print(type(response_data)) #<class 'bytes'>
    # 通过with open生成一个文件 百度3.html 文件写入方式 wb ==write bytes
    # 如果使用字节形式就行写入 就不需要加编码！  encoding="utf-8"  重点!
    with open("百度3.html","wb")as file1:
        # write方法可以写入str或者 bytes
        file1.write(response_data)

crawlbaidu3()
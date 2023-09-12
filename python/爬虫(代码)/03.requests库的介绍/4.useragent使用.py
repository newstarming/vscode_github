"""

useragent是什么？
是用户代理
useragent有什么用？
代表请求这个数据包的基本信息有哪些 身份是什么
是一个字段
作用: 用于服务端反扒的
if user.User-Agent == python-requests/2.28.2:
    反扒!
所以需要在进行数据采集的时候把useragent带到请求头里面发送请求    反反爬措施!

useragent怎么用？ 怎么反反爬?
通过构建键值对的形式放在字典里面  然后通过在requests的get方法里面传递参数进行身份确认!

复制数据包的 requests headers 下面的 User-Agent :xxxxx


User-Agent:

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
"""

import requests
# 默认加请求头都用headers变量
# 这是一个字典!   需要有键值对!
# "User-Agent" 是键
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" 是值
# 而且   不要在useragent对应的值里面加空格!  大忌!

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
url="https://www.baidu.com"
# 通过requests的get方法 向"https://www.baidu.com"发送请求，在发送请求的同时携带了请求头信息 里面就表明了我的User-Agent是"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" 而不是之前的 'python-requests/2.28.2'
response=requests.get(url=url,headers=headers)

response_data=response.content.decode()
print(response.request.headers)
# {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
print(response_data)
print(type(response_data)) #<class 'str'>

with open("百度4.html","w",encoding="utf-8")as file1:
    file1.write(response_data)










"""
# 目的： 为了实时的获取cookie
# 流程
#1. 通过request库的session对象向服务器发送请求(method=post) 获取cookie保存到session对象里面
#2. 再通过session对象向包含了个人信息数据的数据发送请求(method=get) 获取书架数据 不需要手动构建cookie

"""

import  requests

#通过requests库的session类实例化一个session1的对象
session1 = requests.session()
#提交账号密码的数据包  登录的数据包
url = "https://www.kkkkkkkkk.com/user/user/login.html"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

data = {
    "username":"winner192",
    "password":"winner192516521",
}
# 这里不需要用response接受   这里的目标是获取cookie  不是为了获取数据
# 执行下面的代码， cookie就会存储到session1对象里面
session1.post(url=url, headers=headers,data=data)
#2. 再通过session对象向包含了个人信息数据的数据发送请求(method=get) 获取书架数据 不需要手动构建cookie
book_url = "https://www.kkkkkkkkk.com/user/bookshelf/index.html"
# 目的 获取书架的数据，所以使用response接受
response = session1.get(url=book_url, headers=headers)
#datas =  response.content.decode()[1:-1].replace(r"\n", "").replace(r"\t","").replace(r"\r","").replace("\\","")
datas =  response.content.decode()[1:-1].replace(r"\n", "").replace(r"\t","").replace(r"\r","").replace("\\","")
print(datas)
# 取索引1号位字符串
print(response.content.decode().index("1",1))
# 4.保存
with open('shujia.html','w',encoding="utf-8") as f:
    f.write(datas)


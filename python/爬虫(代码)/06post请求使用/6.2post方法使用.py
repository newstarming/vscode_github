"""
# post 方法和get方法都是http请求？ 它们在发送请求时的区别是什么？
http请求方法： post  get
post特点： 形式为表单传参； 安全 传输的数据更多
"""
import  requests
url = "https://www.kkkkkkkkk.com/user/user/login.html"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
#x-requested-with: "XMLHttpRequest"  是一个反反爬的字段，和ua cookie一样
data = {
    "username":"winner192",
    "password":"winner192516521",
}
# 发送post请求， 必须要传入data参数  data参数就在  数据包的payload里面， 如果payload没有  就在headers标签的最下面

response = requests.post(url=url,headers=headers,data=data)
print(response.content.decode())




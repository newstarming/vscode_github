"""
业务场景：  以高频速度采集网页数据(会暴露自己的IP) 会被反扒(不返回数据，或者返回假数据)  会有警告 请求失败 异常从你的IP发出
Ip: 计算机的身份信息
查看： cmd >> ipconfig  查看自己ip    ifconfig >> linux  ipaddr

反扒以后就不能采集数据了吗？
可以视情况采集，通过刷新网页查看其网页的响应速度
如果反馈好  可以使用代理IP发送请求， 获取对应的响应内容

192.168.0.1  >>> （数据） 1000次/s  >>>>> 192.168.0.1 >>> 反扒
192.168.0.1  >>>（代理ip）192.168.1.45 >>>（数据） >>>> （代理ip）192.168.1.45 >>>> 192.168.0.1
代理ip是什么？  也是一个IP地址
作用：帮我们发送请求，获取数据，从而不暴露我们自己的IP
注意点：代理IP也是IP，如果同一个代理IP发送请求次数多， 频率高 也是会被反扒的，  需要使用不同的IP发送请求(代理池)
"""

"""
ip的分类
    匿名ip  >>>   服务器是知道我们使用了代理的IP
    高匿ip  >>>   服务器是不知道我们使用了代理的IP
写爬虫程序的时候，如何构建？
先声明一个键值对
proxies = {
    http: http://ip:port
}
proxies = {
    http: http://117.114.149.66:55443,
    https:http://117.114.149.66:55443
}
"""
import  requests

url = "https://www.baidu.com/"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
#声明 代理IP参数   类型字典
proxies = {
    "http":"http://113.121.44.248:15759",
    "https":"http://113.121.44.248:15759",
}
response = requests.get(url=url, headers=headers, proxies=proxies)
res_data = response.content.decode()
print(res_data)

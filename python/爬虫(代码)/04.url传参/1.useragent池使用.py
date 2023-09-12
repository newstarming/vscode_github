"""
1.什么是useragent池
是保存了多个不同的useragent的容器(列表，元祖，集合)
useragent:用户代理
池:列表   []
2.他有什么用？
使用同一个ua向服务器发送请求会不会被反扒?
会  如何解决？
就需要使用useragent池构建不同的ua发送请求
服务器反扒机制!
requests >>> server
user1.useragent.sum=0
if user1.useragent.sum==100:
    反扒!  不返回数据  或者返回假数据  或者部分数据
if user1.requests.headers=="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    user1.useragent.sum+=1
根据机制 可以得出如果使用不同的ua(更改ua的参数信息)(type==str)发送请求 就不会被反扒
不要乱更改参数


每个同学的开发者工具里面的数据包的ua都是一样的
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
"""

# 3.怎么用?
# 第一种方法   通过修改不同浏览器版本 生成不同的ua
import os
import random
import tempfile

ua_pool=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
]

# 随机生成 0 - 4之间的随机数
# index=random.randint(0,4)
# ua=ua_pool[index]
# headers={
#     "user-agent":ua
# }
# print(headers)
# 第二种直接生成随机ua的方法
# 调用random的choice传入列表  直接返回列表里面的随机值! ua
# ua=random.choice(ua_pool)
# headers={
#     "User-Agent":ua
# }
# print(headers)
"""
headers={
    "user-agent":ua
} 
和
headers={
    "User-Agent":ua
}
都可以使用
"""

#第三种生成ua的方法  通过模块
# fake-useragent模块
# 随机生成不同类型ua的模块(操作系统不同 linux windows 安卓 mac)
# 下载 pip install fake-useragent 加源
# ectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x041A9640>: Failed to establish a new connection: [
# Errno 11001] getaddrinfo failed')': /fake-useragent/
# 下载出现以上问题网络问题,解决方法  把site-packages.rar 解压到自己的 python安装目录的 lib文件夹的site-packages文件夹下面

# 导入 使用FakeUserAgent生成ua是需要联网的 但是是访问国外的服务器得到ua 就会有网路问题 就会报错
# 解决方法 就是把 生成ua的json文件保存到本地  让FakeUserAgent去本地的json文件获取ua  不用向国外服务器请求ua，就不用担心网络问题
# 怎么操作？
# 首先 执行打印DB的代码得到一个路径  C:\Users\admin\AppData\Local\Temp\fake_useragent_0.1.11.json
__version__ = '0.1.11'
DB = os.path.join(
    tempfile.gettempdir(),
    'fake_useragent_{version}.json'.format(
        version=__version__,
    ),
)
# print(DB)

# C:\Users\admin\AppData\Local\Temp\fake_useragent_0.1.11.json
from fake_useragent import FakeUserAgent
# 通过FakeUserAgent类的random方法随机进行网络请求 生成一个ua
useragent=FakeUserAgent().random
# print(useragent)
headers={
    "User-Agent":useragent
}
print(headers)

"""
Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36
Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36

通过这个命令更新pip    
python -m pip install --upgrade pip


"""















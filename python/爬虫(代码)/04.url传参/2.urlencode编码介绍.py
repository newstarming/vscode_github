"""
https://www.baidu.com/s?wd=%E5%8D%A1%E5%AE%B4
为什么从到寒兰复制到本地的url里面的中文 "卡宴" 会变成 “%E5%8D%A1%E5%AE%B4” 这个样子的密文呢？
在复制的时候 浏览器会对中文"卡宴"进行urlencode编码    "卡宴" >>urlencode >>“%E5%8D%A1%E5%AE%B4
为什么会进行urlcode编码?
有什么用呢？
方便其他软件进行链接解析从而方便进行页面访问!
2020版本的pycharm才能按住ctrl点击链接进行访问     不是2020版本pycharm的同学找我获取
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%8D%A1%E5%AE%B4&oq=%25E5%258D%25A1%25E5%25AE%25B4&rsv_pq=bbca88be0007b403&rsv_t=3c59gxYadTE0FPEt59x04GDSTpk3Qh4FYXUdqCdZGwIKfr2ibZBMVsA5glc&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t


如果使用中文构建url发送请求能不能成功呢？
能成功！  无论是经过了urlencode编码或者没有经过的链接都能进行页面的访问

无论是经过了urlencode编码或者没有经过的链接都能进行页面的访问

"""
from urllib.parse import quote,unquote
# quote urlencode编码
# unquote urlencode解码

word="卡宴"
encodeurldata=quote(word)
print(encodeurldata)
# %E5%8D%A1%E5%AE%B4
# %E5%8D%A1%E5%AE%B4
# 解码
decodeurldata=unquote(encodeurldata)
print(decodeurldata)









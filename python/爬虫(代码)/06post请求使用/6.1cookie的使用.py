"""
1. cookie是什么？ 作用
    饼干 是request  header 里面的字段  和ua  一样
  有什么用？
  让服务器确认你的信息， 从而让服务器能给到你对应的数据
  怎么生成的？
  第一次浏览器和服务器建立连接后，服务器会给浏览器发送一个字段(cookie) 浏览器就会存储cookie
  浏览器有了cookie  那么再次请求对应的网页时，就不用重新输入账号密码和服务器建立连接
"""
import  requests
def crawl_book():
    url="https://www.kkkkkkkkk.com/user/bookshelf/index.html"
    # 请求头
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        "cookie":"lf___forward__=%2F; Hm_lvt_bd48ecec99527fc609704be7dcf3fe88=1682406862,1682515608; lf_user_auth=think%3A%7B%22uid%22%3A%22772%22%2C%22username%22%3A%22winner%22%7D; lf_user_auth_sign=f4ed6424b7bd3e52dd5c5fbf187b574967a5e17e; lf_user_recommend=1682515659; Hm_lpvt_bd48ecec99527fc609704be7dcf3fe88=1682515660"
    }
    #发送请求
    response =  requests.get(url=url, headers= headers)
    datas = response.content.decode()
    print(datas)
crawl_book()

"""
# 出现问题  采集过程中携带了ua 但是依然没有采集到对应的我的书架数据
原因： cookie没携带  cookie过期  cookie错误
"""

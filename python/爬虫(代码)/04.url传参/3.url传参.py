"""
1.什么是url传参?
向百度查询"保时捷"的过程中    在输入框输入"保时捷"的操作就叫做url传参
 什么是请求参数?
 保时捷 ......
2.它和爬虫有什么关系？
如果我要采集保时捷卡宴的主页数据
需要向以下链接发送请求
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=卡宴&oq=%25E5%258D%25A1%25E5%25AE%25B4&rsv_pq=bbca88be0007b403&rsv_t=3c59gxYadTE0FPEt59x04GDSTpk3Qh4FYXUdqCdZGwIKfr2ibZBMVsA5glc&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t
如果我要采集法拉利的主页数据
需要向以下链接发送请求
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=法拉利&oq=%25E5%258D%25A1%25E5%25AE%25B4&rsv_pq=b7478d6900078fb5&rsv_t=6f29CDt5H%2F9fl4TK9xm%2BNJkjmEoK9bwSBFGwG8YZXwto%2FQ9syZ65XlcRxaY&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=8&rsv_sug7=100&bs=%E5%8D%A1%E5%AE%B4
学习url传参的目的就是为了可以通过传递不同参数(使用大部分url参数相同的url)发送请求获取对应的响应

3.如何构建请求参数?
    3.1 需要确认传递参数的位置以及参数传递的形式！
        {key:value}
        https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=卡宴&oq=%25E5%258D%25A1%25E5%25AE%25B4&rsv_pq=bbca88be0007b403&rsv_t=3c59gxYadTE0FPEt59x04GDSTpk3Qh4FYXUdqCdZGwIKfr2ibZBMVsA5glc&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t
        https://www.baidu.com/s?
        ?前面是服务器的主页位置  https://www.baidu.com/s?
        ?后面是参数信息  ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=卡宴&oq=%25E5%258D%25A1%25E5%25AE%25B4&rsv_pq=bbca88be0007b403&rsv_t=3c59gxYadTE0FPEt59x04GDSTpk3Qh4FYXUdqCdZGwIKfr2ibZBMVsA5glc&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t
        在url里面传递参数形式  键=值&键=值
    3.2 构建以及传递参数只需要确认关键性参数进行传递即可！
        怎么确认关键性参数?
            爬虫初期 都建议根据以上参数构建规则  一步步删减url参数 不断进行访问 来甄别关键性参数！  关键性参数数量不一定
            第一次url
                https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%8D%A1%E5%AE%B4&oq=%25E5%258D%25A1%25E5%25AE%25B4&rsv_pq=bbca88be0007b403&rsv_t=3c59gxYadTE0FPEt59x04GDSTpk3Qh4FYXUdqCdZGwIKfr2ibZBMVsA5glc&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t
            第二次url
                https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%8D%A1%E5%AE%B4&oq=%25E5%258D%25A1%25E5%25AE%25B4&rsv_pq=bbca88be0007b403
            第三次url
                https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%8D%A1%E5%AE%B4
            第四次url  如果发现删减url不能访问原来的响应内容  说明关键性参数被删减掉了
                https://www.baidu.com/s?ie=utf-8&f=8
            https://www.baidu.com/s?wd=%E5%8D%A1%E5%AE%B4
"""

# 写一个能根据不同参数采集不同内容的程序并且将响应内容保存到本地为html文件!
# https://search.bilibili.com/all?keyword=%E6%B7%84%E5%8D%9A%E7%83%A7%E7%83%A4&from_source=webtop_search&spm_id_from=333.1007&search_source=5
import requests
# 卡宴   法拉利   兰博基尼  ........
keyword=input("请输入要采集的内容关键字:")
url=f"https://search.bilibili.com/all?keyword="+keyword
# url=f"https://search.bilibili.com/all?keyword={keyword}"
print(url)

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

response=requests.get(url=url,headers=headers)
response_data=response.content.decode()
print(response_data)

with open(f"{keyword}.html","w",encoding="utf-8")as file1:
    file1.write(response_data)










"""

目的使用一个程序采集多页贴吧数据保存到本地

结论性知识点: 要采集翻页的数据  都是在url对应的参数上面做手脚!
get  params     或者通过直接在url后面进行参数修改  生成不同的url 采集不同页数的数据！
总结 要采集不同的内容 就得有不同的url对应的参数

流程
抓取不同的页数的贴吧url做参数对比   关键点!翻页重点!
第一页 https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=0
第二页 https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=50
第三页 https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=100
第四页 https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=150
第五页 https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=200

# page num == pn
得出结论 如果我要采集不同页数的响应 就需要更改pn的值 每次递增50
"""
import requests
# 0 1 2 3 4
for i in range(3):
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    url = f"https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn={i * 50}"
    print(url)
    # 发送请求
    response = requests.get(url=url, headers=headers)
    # 以字符形式保存
    response_data = response.content.decode()  # response.text 交换使用
    # 文件写入方式的w 代表覆盖原本文件的数据!
    # 1 2 3 4....
    with open(f"英雄联盟{i + 1}.html", "w", encoding="utf-8")as file1:
        file1.write(response_data)

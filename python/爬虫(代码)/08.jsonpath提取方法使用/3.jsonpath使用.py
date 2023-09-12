"""
jsonpath 是提取json格式数据的模块    这里使用的是jsonpath模块里面的方法
主要针对  list 或者 dict类型数据进行跨界点匹配数据的操作！

优点/缺点 可以对数据进行跨界点匹配

重点语法介绍
$ 根节点       从哪个节点开始匹配
. 取子节点      节点与节点之间的过渡
* 代表选择全部的意思 取列表里面数据的时候可以使用
.. 和$配合使用 代表无论在哪个节点  都能匹配到对应的数据

练习
需要匹配所有的书的标题和价格  一共有四条数据

"title": "Sayings of the Century",
"price": 8.95


需要使用jsonpath
1.下载
pip install jsonpath 加源下载
2.使用
从jsonpath模块里面使用jsonpath方法
"""
from jsonpath import jsonpath
import json
word = """
{"store": {
    "book": [
        {"category": "reference",
         "author": "Nigel Rees",
         "title": "Sayings of the Century",
         "price": 8.95
         },
        {"category": "fiction",
         "author": "Evelyn Waugh",
         "title": "Sword of Honour",
         "price": 12.99
         },
        {"category": "fiction",
         "author": "Herman Melville",
         "title": "Moby Dick",
         "isbn": "0-553-21311-3",
         "price": 8.99
         },
        {"category": "fiction",
         "author": "J. R. R. Tolkien",
         "title": "The Lord of the Rings",
         "isbn": "0-395-19395-8",
         "price": 22.99
    ],
    "bicycle": {
        "color": "red",
        "price": 19.95
    }
}
}"""

# 标题
# 使用jsonpath方法 参数1 对象(dict/list) ,参数2 匹配的语法
dict_data=json.loads(word)
print(type(dict_data))
# titles = jsonpath(dict_data,"$..title")
# print(titles)
#
# # 价格
# prices=jsonpath(dict_data,"$..price")
# print(prices)

# 解决jsonpath跨界点匹配的缺点
# 指定清楚该数据的父节点
# $..book[*] 代表我要匹配book节点下的列表里面的所有数据
prices=jsonpath(dict_data,"$..book[*].name.a")
print(prices)
if prices == False:
    prices = jsonpath(dict_data, "$..book[3].price")
    print(prices)

# jsonpath提取数据的机制
# jsonpath提取到数据返回包含数据的列表  没有匹配到数据返回false











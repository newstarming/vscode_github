"""
爬虫需要采集的文本数据类型有2种
1. 结构化数据
    json(结构化数据的基本类型)
    如何鉴别一个数据包里面的内容是一个json类型的数据呢？
    要查看响应内容确认url, 如果perview 和response 里面都有响应内容且preview里面的内容可以规整的展开，就是json格式数据
    json格式数据提取？  有专门的数据清洗方法， jsonpath方法（跨节点匹配数据的方法），在使用该方法之前需要进行数据类型转化 str >> jsonpath(模块) 能提前的数据类型
    也可以用re匹配json格式的数据
    保存：json数据的数据类型只能是一个字符串或者一个列表或者一个字典

2. 非结构式数据
    html （非结构化数据基本类型）
    如何鉴别一个数据包里面的内容是一个html类型的数据？
    打开response标签，前面有html标签的响应内容存在，  就是html数据
    html  lxml（模块） xpath (lxml模块下方法)  str >> element对象 xpath(element对象)>>>结果！！
    也可以用re匹配html格式的数据

"""


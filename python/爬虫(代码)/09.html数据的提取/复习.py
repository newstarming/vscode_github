"""
1. load loads dump dumps 的区别
文件  ====> Python
load 是在读取json数据时，  直接对json（文件对象） 进行操作将数据转换str 成字典类型dict操作
loads 是对字符串str 数据类型进行操作  将str转换到dict的操作

总： py ===》 文件
dumps 是将(dict字典)转换成(str字符串)的方法
dump  是将(dict字典数据)和(file文件对象) 直接传入其中并保存json文件的方法

2. jsonpath 提前语法掌握
答： 重点掌握万能匹配方式  jsonpath(data, "$..节点")
3. jsonapth提取不同节点  但有相同键名的数据时  应该如何处理才能达到数据的精准提前？
答：  方法===> 表明该键名的父节点  并写入jsonpath语法   即确认坐标
"""


"""

1. 如何使用代理IP发送请求？
2. 超文本标记语言的文本数据分为几种？
3. 属性数据和文本数据都各用什么方式进行提取？
4. xpath 提取数据失败的处理 重点
快代理平台==> 免费代理获取
https://www.kuaidaili.com/free/

案例：https://bj.lianjia.com/ershoufang/dongcheng/pg1/

爬取作业: https://xa.58.com/ershoufang/    
字段数据：
标题
1.标题名 2.标价   3.平方价格  4.户型 5.房屋大小
爬取十页数据

"""
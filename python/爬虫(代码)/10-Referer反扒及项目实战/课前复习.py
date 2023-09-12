"""
1. 如何使用代理IP发送请求？
答： 通过构建proxies(字段) 类型的参数构建在发送get或post请求方法里面
2. 超文本标记语言的文本数据分为几种？
答： 2种  属性数据  文本数据
3. 使用xpath提前数据之前要做哪些操作？
答： 需要通过etree.HTML() 把str类型转换成element对象

4. 属性数据和文本数据分别要用什么方式去提取？
答：  属性 @   文本 text()

5. xpath提前数据失败的处理方法？ 重点！
答： 1. 打印整体响应内容看数据是否存在，不然即使语法写对也匹配不到数据
    2. 有数据时  检查自己的语法是否写错   重新构建xpath语法进行数据提取
"""

"""
1. 认识referer反扒
    https://ke.qq.com/course/292490?tuin=d4c97e25#term_id=100346594
2. 跟项目 听细节
    https://shareae.com/after-effects-project
"""
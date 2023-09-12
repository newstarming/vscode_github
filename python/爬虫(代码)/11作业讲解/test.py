"""
主题：作业讲解

第四次作业
小作业  根据下面需求  完成代码的编写
1. 图片视频保存要以该主题的id作为文本名保存
2. 图片视频保存到不同的文件夹
3. 可以自己指定页数爬取
注： 因为此网页响应速度比较慢， 所以只需要看到代码实现部分即可


第三作业
爬取  https://sh.58.com/ershoufang/链接的 字段数据
标题
1. 标题名 2. 标价  3. 平方价格 4. 户型 5. 房屋大小
爬取十页的数据
保存为十个json格式文件

1. 巩固提前字符串的语法
2. xpath匹配数据的重点讲解

特殊字段
"""
# import  re
# #响应数据
# link = "https://videohive.net/item/promo-reel/45423014"
# print(link)
# id = re.findall('tem/promo-reel/(.*)',link)
# print(id)
# data = link.split("/")[-1]
# print(data)

import  os
# 每次运行时 检查是否存在这个文件夹  或者文的方法 判断
#os.mkdir("视频")
# 传递路径  xxx/xx/文件夹 or xxx/xx/xxxx/index.html 文件
#  返回的是bool值  如果 文件路径存在 返回真True  如果不存在就返回False
# flug = os.path.exists("./视频123")
# print(flug)

# if not os.path.exists("./视频"):
#     os.mkdir("./视频")
# if not os.path.exists("./图片"):
#     os.mkdir("./图片")
start_num   =  int(input("请输入采集的起始页："))
end_num = int(input("请输入采集的结束页："))
for i in range(start_num, end_num+1):
    print(i)




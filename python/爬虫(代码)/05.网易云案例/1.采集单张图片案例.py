"""
目的:通过开发者工具区定位要采集的资源(png(图片格式)) 找url，并且把它保存到本地为一张能正常看的图片

本节课的重点     "抓包"
1.抓url
2.向url发送请求 获取响应
3.(采集的资源是图片) 不用进行清洗(根据不同的数据类型制定不同的业务逻辑,直接保存到本地即可！)


1.抓url
定位方法1:在network里面使用全类型搜索数据包的形式抓取!
定位方法2:通过类型筛选  根据要采集的数据类型 选择不同的类型标签(png mp3) 比如png就可以选择img的数据包分类
定位方法3:通过资源定位标签(开发者工具左上角的箭头)和Element标签(网页源代码)配合定位网页元素!



tips1:要抓数据包，就得做抓数据包的操作！
tips2:抓取图片类型的数据包  需要查看preview标签里面的内容确认url
tips3:图片视频音频的字节不能通过decode进行解码！   文本的字节才可以通过decode方法解码
tips4:图片视频音频类型数据只能通过字节类型写入方式进行写入！  不能通过字符写入方式进行写入! 规则，机制
"""

import requests
# 图片链接
url="https://p3.music.126.net/73zBA6FM8UkOXfx-cXyQDw==/18725782534645765.jpg?param=200y200"

# 请求头
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 2.向url发送请求 获取响应
response=requests.get(url=url,headers=headers)
print(response.content)
# 图片视频音频的字节不能通过decode进行解码！   文本的字节才可以通过decode方法解码
# 这是规则!机制！
# print(response.content.decode())
# 图片视频音频类型数据只能通过字节类型写入方式进行写入！  不能通过字符写入方式进行写入! 规则，机制
# 写入字节类型数据 不能指定encoding="utf-8"参数    规则，机制
bytes_data=response.content
# png jpg是图片文件后缀!  你要明确你采集的内容是什么再用对应的文件后缀进行保存!
with open("白天鹅.png","wb")as file1:
    file1.write(bytes_data)











"""
目的 采集网易云的单个mv并且保存到本地   mv  music video /   mp4  ts  flv  枚举的文件后缀

重点：抓包!
流程
1.根据要采集的内容抓去对应的视频我换数据包
2.发送请求
3.获取响应 并且保存到本地(因为采集的是视频 所以不需要清洗直接保存)

抓包tips1 可以通过MP4 flv或者url里面有某视频文件后缀的字符串  进行抓取!
抓包tips2 通过数据包的size大小 进行定位  158M
抓包tips3  可以通过(media)筛选标签来进行定位!
如果发现暂停了视频，重新刷新网页重新播放视频 依然没有数据包出现
    可能是数据包已经把缓存存到浏览器了  所以没有数据包  是读取的本地缓存
    解决方法:点击中间没有加载出来的部分!   让浏览器请求未请求下来的数据!

tips 音视频图片的请求方法 基本都是get方法请求来的
"""
import requests
url="https://vodkgeyttp8.vod.126.net/cloudmusic/ICAiMDAwIGAwICAgISIiJA==/mv/375130/fab51440788fca8cdfcf2726b7328947.mp4?wsSecret=49eae2d2ac25ead11d6d3846b9b76574&wsTime=1682342207"
# 请求头
headers={
     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 发送请求  获取响应
response=requests.get(url=url,headers=headers)
# 获取的是字节类型的数据
# 音视频图片不能通过content.decode进行解码
bytes_data=response.content
# 写入字节不能指定编码！
# ./代表当前路径的文件    重点!
# ../代表网上找一级目录
# /视频  代表我切换到了视频文件夹下面去!
# /可惜没如果.mp4 代表我把数据写到了(/视频)文件夹里面去
with open("./../视频/可惜没如果.mp4","wb")as file1:
    file1.write(bytes_data)

# 绝对路径指定  从怕盘符开始指定
with open(r"D:\六星教育\2304期\2304期python\05.网易云案例\视频\可惜没如果.mp4","wb")as file1:
    file1.write(bytes_data)
"""
爬取的爬取速度 取决于网速和硬盘写入速度,数据的大小  不能控制!
不要拿pycharm打开MP3 或者 摸MP4的文件!    因为pycharm是编辑器不是播放器!

怎么指定路径保存
保存到视频文件夹,进行路径指定
        1.相对路径指定
        2.绝对路径指定
"""
















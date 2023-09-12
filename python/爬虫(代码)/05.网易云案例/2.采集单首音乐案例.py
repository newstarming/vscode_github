"""
# 如何指定路径 ?  支线任务
目的:采集网易云能播放的一首歌曲 保存到本地    音乐的文件后缀 mp3 m4a mp4

重点  在于抓包！
流程
1.使用开发者工具定位一首歌曲 (音频mp3数据包)
2.发送请求 获取响应内容
3.根据你实际要采集的数据 决定业务逻辑  （这里采集的是音频  不需要进行清洗(直接保存到本地！)）


1.抓包tips1 抓包之前先进行数据包的清空(前提:知道数据包还没有生成出来)
2.抓包tips2  抓取音频数据  不能通过preview数据包标签来进行筛选! 因为看不到声音


抓包方法1:通过关键字筛选:    mp4 m4a 等等一系列的关键字筛选!
发现可疑的数据包 就把该数据包完整的url放到导航栏访问！ 如果是直接播放音乐 那么就抓到了对应的数据包!
    https://m801.music.126.net/20230424211136/7fc9506cd3347020a3e3caca1cf8fd31/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/17224485019/4b36/a241/7711/ab99b8c8f61f334f6f6c63a28fb85ce5.m4a
    https://m801.music.126.net/20230424211136/7fc9506cd3347020a3e3caca1cf8fd31/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/17224485019/4b36/a241/7711/ab99b8c8f61f334f6f6c63a28fb85ce5.m4a
抓包方法2:通过数据类型筛选抓取  音频类型数据包可以通过 media(多媒体:音频,视频)筛选标签进行筛选!  能起到60%作用
抓包方法3:可以根据数据响应内容的大小size进行筛选      34Mb ~ 2M
"""

import requests
# 音频url
url="https://m801.music.126.net/20230424211136/7fc9506cd3347020a3e3caca1cf8fd31/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/17224485019/4b36/a241/7711/ab99b8c8f61f334f6f6c63a28fb85ce5.m4a"
# 请求头
headers={
     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 发送请求
response=requests.get(url=url,headers=headers)
# 音视频图片只能以字节形式进行保存!
bytes_data=response.content
# 我现在没弄懂file是是什么意思 file1是文件的对象名
with open("海阔天空.mp3","wb")as file1:
        file1.write(bytes_data)
# 注意注意  不要在pycharm打开音视频文件 mp3 mp4 >因为pycharm是编辑器不是播放器 不能读取mp3 mp4
# 仅仅只能查看图片!   pycharm机制!
# 可以单机MP3文件  右键>>show explore 在资源管理器打开!   用windows自带的播放器播放!
# Music Video  文件后缀属于mp4   音频文件格式有很多   只是枚举几个!
# with open 可以指定文件目录吗? 可以!
# 指定文件夹写入方法得用追加吧？  不用  直接在with open的第一个参数指定路径
# 爬腾讯视频可以吗? 能抓到数据包都可以
# 意思说那些腾讯vip可以试看的，都可以爬到吧？ 看到了的出现数据包了的 都是可以的采集的！


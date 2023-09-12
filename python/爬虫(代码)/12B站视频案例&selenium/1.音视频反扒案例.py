"""
目的： 采集B站的视频  保存到本地 让大家认识音视频反扒的机制  以及对应得到反反扒的措施
网址： https://www.bilibili.com/
项目背景
使用传统的音视频抓包方式去抓取数据包   会出现 media 定位不到的数据包的 情况
如何直接把抓到的数据包赋值到导航栏打开 会返回 403   就检查请求头参数的出入   在pycharm构建请求协议(referer) 验证猜想
tips  如果数据包在response里面是乱码情况  就一定是一个音频或者是一个视频多媒体数据包
tips    mp4文件可以保存音频数据
"""

import  requests

url="https://cn-sccd-ct-01-19.bilivideo.com/upgcxcode/48/71/1131537148/1131537148_nb3-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1684335157&gen=playurlv2&os=bcache&oi=0&trid=0000bd5f6a0264ca4da3b63540780e3d02bcu&mid=492342119&platform=pc&upsig=d0406b27ffad042dd7941de3666137a4&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=62619&bvc=vod&nettype=0&orderid=0,3&buvid=A6C90F98-73DE-4FF7-8E3E-2818A9B1D1A816178infoc&build=0&agrr=0&bw=10406&logo=80000000"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "referer":"https://www.bilibili.com/video/BV1po4y1F7nV/?spm_id_from=333.1007.tianma.1-2-2.click&vd_source=324de56fba761bf7b21ba31b8631021e"
}

response = requests.get(url=url, headers=headers)
#视频直接保存
bytes_date =response.content
with open("3.mp3","wb") as file1:
    file1.write(bytes_date)
print("采集完毕")

url = "https://cn-sccd-ct-01-19.bilivideo.com/upgcxcode/48/71/1131537148/1131537148-1-100113.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1684335780&gen=playurlv2&os=bcache&oi=0&trid=0000fd2e02ec53764e30af0211801b5175e4u&mid=492342119&platform=pc&upsig=287f1c1451eb97afebb318b44549a3eb&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=62619&bvc=vod&nettype=0&orderid=0,3&buvid=A6C90F98-73DE-4FF7-8E3E-2818A9B1D1A816178infoc&build=0&agrr=0&bw=101926&logo=80000000"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "referer":"https://www.bilibili.com/video/BV1po4y1F7nV/?spm_id_from=333.1007.tianma.1-2-2.click&vd_source=324de56fba761bf7b21ba31b8631021e"
}

response = requests.get(url=url, headers=headers)
#视频直接保存
bytes_date =response.content
with open("4.mp4","wb") as file1:
    file1.write(bytes_date)
print("采集完毕")

import  os
os.system("ffmpeg -i 3.mp3 -i 4.mp4 -c copy new123.mp4")
#'ffmpeg' �����ڲ����ⲿ���Ҳ���ǿ����еĳ���
#���������ļ���
# 配置了环境变量 但是未重启 pycharm

"""
若network 抓取的音频数据 不能正常播放  可在主页的response 里面搜索 video  audio 获取地址连接进行数据提取
video  视频
audio   音频
video  url = https://cn-sccd-ct-01-19.bilivideo.com/upgcxcode/48/71/1131537148/1131537148-1-100113.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1684335780&gen=playurlv2&os=bcache&oi=0&trid=0000fd2e02ec53764e30af0211801b5175e4u&mid=492342119&platform=pc&upsig=287f1c1451eb97afebb318b44549a3eb&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=62619&bvc=vod&nettype=0&orderid=0,3&buvid=A6C90F98-73DE-4FF7-8E3E-2818A9B1D1A816178infoc&build=0&agrr=0&bw=101926&logo=80000000
"""
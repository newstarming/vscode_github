"""
目的： 采集B站视频  保存到本地
要求： 通过输入主页连接就能将视频(有声音的视频)保存到本地
步骤：
1. 获取主页链接以后，向主页发送请求
2. 匹配音视频URL
3. f分别向音视频发送请求  保存到本地
4.  通过ffmpeg合成
5.  删除纯音频纯视频的文件
"""
import  os
import  re
import  requests
def crawl_data():
    #1. 获取主页链接以后，向主页发送请求
    url = input("请输入要采集的视频主页链接：")
    #匹配音视频URL
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "cookie":"uvid3=A6C90F98-73DE-4FF7-8E3E-2818A9B1D1A816178infoc; b_nut=1675804316; i-wanna-go-back=-1; _uuid=D6A73622-A7101-AD9B-B1092-35FA17FF1410A18077infoc; nostalgia_conf=-1; rpdid=0zbfVGh1hS|7iw2KtOP|3xK|3w1PpvgN; DedeUserID=492342119; DedeUserID__ckMd5=7561573ea76933aa; b_ut=5; buvid4=2FB647DB-46F8-7CEA-E0E0-8E3CB29396AB16982-023020805-HNYvTHSPdBRoVfJ96dYuv5Ip702uhVGfBDrgZVYeg0xrnRF5o%2FFVOA%3D%3D; CURRENT_BLACKGAP=0; home_feed_column=5; LIVE_BUVID=AUTO1316791010102034; CURRENT_PID=b56121c0-c903-11ed-9d96-4954d996628e; header_theme_version=CLOSE; FEED_LIVE_VERSION=V8; browser_resolution=1920-937; fingerprint=94d3a8d88d33c23f383b8a14ed364328; buvid_fp_plain=undefined; buvid_fp=94d3a8d88d33c23f383b8a14ed364328; bsource=search_baidu; CURRENT_FNVAL=4048; bp_video_offset_492342119=796242501203656700; b_lsid=A395A5104_188298EACD7; SESSDATA=06e475ef%2C1699879125%2C1c0b7%2A51; bili_jct=690c8f6c4b0b8dbd9bb0271022f9efd0; sid=5d8ajvmx; innersign=1; PVID=1; CURRENT_QUALITY=0",
        "referer": "https://www.bilibili.com"
    }
    response = requests.get(url=url, headers=headers)
    str_data = response.content.decode()
    #print(str_data)
    video_url = re.findall('"video":\[\{"id":\d*,"baseUrl":"(.*?)"',str_data)[0]
    print(video_url)
    audio_url = re.findall('"audio":\[\{"id":30280,"baseUrl":"(.*?)"',str_data)[0]
    print(audio_url)
    title = re.findall('<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili</title>',str_data)[0]
    print(title)
    #用正则去匹配所有的中文
    title = re.findall('[\u4e00-\u9fa5]',title)
    print(title)
    newtitle = "".join(title) #拼接列表中的多个字符为1个字符串
    #3.分别向音视频发送请求  保存到本地
    video_res = requests.get(video_url,headers=headers)
    video_data = video_res.content
    with open(f"{newtitle}demo.mp4","wb") as file1:
        file1.write(video_data)

    audio_res = requests.get(audio_url, headers=headers)
    audio_data = audio_res.content
    with open(f"{newtitle}demo.mp3", "wb") as file2:
        file2.write(audio_data)
   # 4.通过ffmpeg合成
    os.system(f"ffmpeg -i {newtitle}demo.mp4 -i {newtitle}demo.mp3 -c copy {newtitle}.mp4")
   # 5.删除纯音频纯视频的文件
    os.remove(f"./{newtitle}demo.mp4")
    os.remove(f"./{newtitle}demo.mp3")

if __name__ == '__main__':
    crawl_data()

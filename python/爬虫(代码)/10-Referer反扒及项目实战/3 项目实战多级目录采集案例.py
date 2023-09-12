"""
链接：https://shareae.com/after-effects-project
目标：采集视频  图片 bytes
要求：
1. 无水印(采集多级目录里面的视频就可以达到这个效果)
2. 图片视频保存要以该主题id作为 文件名保存
3. 图片和视频保存到不同的文件夹 (mkdir)
4.可以自己指定页数爬取


流程：
1. 数据类型 bytes
2. 数据位置  在三级目录响应内容里
    1. 先像一级目录发送请求 获取二级目录URL
    2. 向二级目录的URL发送请求 获取三级目录的URL
    3. 向三级目录发送请求  获取图片 视频链接
    4. 再向图片 视频发送请求 保存数据
"""
# 先实现一个功能的类， 具体实现某件事情的方法  需要URL
import  requests
from  lxml import  etree
import  re
class Crawl_Data():
    def __init__(self):
        self.starturl = "https://shareae.com/after-effects-project"
        self.headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "referer":"https://shareae.com/after-effects-project/logo-stings/61150-videohive-white-logo-44452978.html"
        }
    #定义每个方法实现的具体功能
    def first_crawl(self):
        first_res = requests.get(url=self.starturl, headers=self.headers)
        res_data = first_res.content.decode()
        html = etree.HTML(res_data)
        second_url_list = html.xpath('//div[@id="dle-content"]/div/h2/a/@href')
        #获取所有二级目录URL 地址
        self.second_crawl(second_url_list)
    def second_crawl(self,second_url_list):
        # 取一个
        for second_url in second_url_list[0:1]:
            second_response = requests.get(url=second_url, headers=self.headers)
            #second_res  = second_response.content.decode()
            #html = etree.HTML(second_res)
            #html.xpath('//*[@id="dle-content"]/div/div[@class="buttondownload1"]/a/@href')[0]

            second_res = second_response.text
            third_url = re.findall('"(https://videohive.net/item/white-logo/\d*)"', second_res)[0]
            #保存第三级的URL地址
            self.third_crawl(third_url)
    #向第三季目录发送请求 获取 视频 图片链接
    def third_crawl(self,third_url):
        third_response =requests.get(url=third_url)
        third_res = third_response.content.decode()
        video_url = re.findall('js-video-player" href="(.*?)"',third_res)[0]
        print(video_url)
        png_url = re.findall('width="590" height="332" src="(.*?)"', third_res)[0].replace("amp;","")
        print(png_url)
        #https://videohive.img.customer.envatousercontent.com/files/440469875/Big_00055.jpg?auto=compress%2Cformat&amp;fit=crop&amp;crop=top&amp;max-h=8000&amp;max-w=590&amp;s=5f41bc0cc613b0064966c45f2768aa7b"

        #https://videohive.img.customer.envatousercontent.com/files/440469875/Big_00055.jpg?auto=compress%2Cformat&fit=crop&crop=top&max-h=8000&max-w=590&s=5f41bc0cc613b0064966c45f2768aa7b


        self.crawl_medid(video_url,png_url)
    def crawl_medid(self,video_url,png_url):
        print("正在采集视频")
        video_res = requests.get(video_url, headers=self.headers)
        with open("视频.mp4","wb")as file2:
            file2.write(video_res.content)
        print("正在采集图片")
        png_res = requests.get(png_url, headers=self.headers)
        with open("图片.png","wb")as file3:
            file3.write(png_res.content)

crawl = Crawl_Data()
crawl.first_crawl()

"""
把剩下3个需求给完成
2.  图片视频保存要以该主题的id作为文件名保存
https://videohive.net/item/white-logo/44452978.mp4
3. 图片视频保存到不同文件夹
4. 可以自己指定页数爬取

"""
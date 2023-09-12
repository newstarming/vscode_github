"""
链接：https://shareae.com/after-effects-project
目标：采集视频  图片 bytes
要求：
1. 无水印(采集多级目录里面的视频就可以达到这个效果)
2. 图片视频保存要以该主题id作为 文件名保存  45423014.mp4 45423014.png
#  三级目录  url 后面跟上的数字
# https://videohive.net/item/promo-reel/45423014
3. 图片视频 保存到不同的文件夹
4.可以自己指定页数爬取
"""
import requests
from  lxml import  etree
import  re
import  os
class Crawl_Data():
    def __init__(self):
        # https://shareae.com/page/1/
        #https://shareae.com/page/2/
        #https://shareae.com/after-effects-project/page/3/
        #https://shareae.com/after-effects-project/page/4/
        #https://shareae.com/after-effects-project/page/5/
        #self.startUrl = "https://shareae.com/after-effects-project/page/5/"
        self.headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "referer":"https://shareae.com/after-effects-presets/"
        }

        # 定义每个方法实现的具体功能
    def first_crawl(self,page):
            self.starturl = f"https://shareae.com/after-effects-project/page/{page}/"
            first_res = requests.get(url=self.starturl, headers=self.headers)
            res_data = first_res.content.decode()
            html = etree.HTML(res_data)
            second_url_list = html.xpath('//div[@id="dle-content"]/div/h2/a/@href')
            # 获取所有二级目录URL 地址
            self.second_crawl(second_url_list)
        # 获取三级目录的URL https://videohive.net/item/sketchme/24531615
    def second_crawl(self, second_url_list):
            #取一个
        for second_url in second_url_list[0:1]:
            second_response = requests.get(url=second_url, headers = self.headers)
            second_res = second_response.text
                #https://videohive.net/item/kinetic-typography-titles-20-ae/44527600
                #https://videohive.net/item/rgb-pixel-transitions-for-after-effects/44452835
            third_url = re.findall('"(https://videohive.net/item/.*?\d*)"', second_res)[0]
            self.third_crawl(third_url)
    def third_crawl(self, third_url):
            third_response = requests.get(url=third_url)
            third_res = third_response.content.decode()
            video_url = re.findall('js-video-player" href="(.*?)"', third_res)[0]
            print(video_url)
            png_url = re.findall('width="590" height="332" src="(.*?)"', third_res)[0].replace("amp;", "")
            media_id = third_url.split('/')[-1]
            print(media_id)
            self.crawl_medid(video_url, png_url,media_id)

    def crawl_medid(self, video_url, png_url,media_id):
            print("正在采集视频")
            video_res = requests.get(video_url, headers=self.headers)
            with open(f"./视频/{media_id}.mp4", "wb")as file2:
                file2.write(video_res.content)
            print("正在采集图片")
            png_res = requests.get(png_url, headers=self.headers)
            with open(f"./图片/{media_id}.png", "wb")as file3:
                file3.write(png_res.content)
    def create_dir(self):
            # 如何文件夹不存在即创建  else 不创建
            if not os.path.exists("./视频"):
                print("文件夹不存在 创建视频文件夹")
                os.mkdir("视频")
            if not os.path.exists("./图片"):
                print("文件夹不存在 创建图片文件夹")
                os.mkdir("图片")
    def run(self):
            self.create_dir()
            ## 先采集1也数据 做对比
            # 采集多余  start 1 end 4  range(1,5+1) 1 2 3 4 5
            start_num = int(input("请输入采集的起始页："))
            end_num = int(input("请输入采集的结束页："))
            for i in range(start_num, end_num + 1):
                self.first_crawl(i)

if  __name__ == '__main__':
    crawl = Crawl_Data()
    crawl.run()
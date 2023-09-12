"""
目的： 1.明确视频解析的原理  2.如何站在用户的角度去编写这个程序
案例： 通过输入视频主页链接就能播放视频的软件
会涉及播放源  可以产生一些特殊的资源
  {"name":"百域","url":"https://jx.618g.com/?url="},
     {"name":"爱豆","url":"https://jx.aidouer.net/?url="},
     {"name":"BL","url":"https://vip.bljiex.com/?v="},

编程步骤：
1. 根据输入的序号  查询出对应的播放源
2. 根据输入的播放源序号进下一个提示
3. 提示要观看的视频主页链接
4. 回车以后访问对应的特殊资源   >>>> next
    1. 看视频
    2.  退出
"""

import  re
import  webbrowser

def look_movie():
    yuan = """
     {"name":"百域","url":"https://jx.618g.com/?url="},  
     {"name":"爱豆","url":"https://jx.aidouer.net/?url="}, 
     {"name":"BL","url":"https://vip.bljiex.com/?v="},  
    """
    while True:
        #1. 根据输入的序号  查询出对应的播放源
        word = input("1.看视频\n2.退出\n请输入要执行的功能：")
        if word =="1":
            names = re.findall('"name":"(.*?)"', yuan)
            links  =re.findall('"url":"(.*?)"', yuan)
            for data in zip(names,links):
                print(f"有'{data[0]}'播放器")
            while True:
                try:
                    #2. 根据输入的播放源序号进下一个提示
                    index = int(input("输入播放源序号即可，例如：1,2: "))
                    if index <= len(links):
                        # 用户指定要用的源链接
                        link = links[index-1]# 1-1  2-1 3-1
                        # 3.提示要观看的视频主页链接  判断是否是一个链接 有 http html 字符
                        videl_link = input("请输入要观看的主页链接：")

                        #4. 回车以后访问对应的特殊资源
                        url = link +videl_link
                        print(url)
                        # new =1 新开一个浏览器窗口
                        # autoraise=True  浏览器对象自动激活  固定参数
                        # webbrowser.oepn()
                        webbrowser.open(url=url, new=1,autoraise=True)
                    else:
                        raise  Exception
                    break
                except Exception as r:
                    print("请输入数字符合：", r)
        elif word=="2":
            print("谢谢使用，拜拜")
            break
        else:
            print("程序员提醒，不要乱输入")
            print("根据提示输入")

if __name__ == '__main__':
    look_movie()
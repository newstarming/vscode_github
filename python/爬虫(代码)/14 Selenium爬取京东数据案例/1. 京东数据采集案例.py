"""
url = “https://search.jd.com/Search?keyword=%E5%9B%BE%E4%B9%A6&enc=utf-8&suggest=1.his.0.0&wq=&pvid=dde079363c0b4618adcce332229d7fb8”
目的：使用selenium 采集该网页下面的图书信息
字段：1. 书名  2. 价格 3. 评分 4. 书籍链接 5.店名

分析数据类型  str >>> page_source(element网页源代码) >>> html >>> lxml/re
数据字段位置  都在1个网页

document.documentElement.scrollTop=1000
出现问题   如果不往下滚动界面 就不能加载出剩下的数据  就会 导致返回的数据不完整
解决办法 调用driver的执行js代码的方法 滑动界面 让网页异步加载书籍数据  最后返回网页源代码  在进行调试

步骤：
1. 声明打开浏览器的函数
2. 需要写滑动界面的函数
3. 返回数据清洗数据的函数
4. 保存数据的函数
5. 关闭浏览器对象的函数
"""
from selenium import webdriver
import time
from lxml import etree
import  json
# 1. 声明打开浏览器的函数
def open_selenium():
    global driver
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://search.jd.com/Search?keyword=%E5%9B%BE%E4%B9%A6&enc=utf-8&suggest=1.his.0.0&wq=&pvid=dde079363c0b4618adcce332229d7fb8")
    driver.maximize_window()
    time.sleep(1)
    scroll_selenium()
#2.需要滑动界面的函数
def scroll_selenium():
    js_code="window.scrollBy(0,300)"
    for i in  range(10):
        driver.execute_script(js_code)
        time.sleep(0.3)
    #滑动完以后跳出循环调用清洗数据的方法
    clear_data()
#3. 返回数据清洗数据的函数
def clear_data():
    # 声明保存数据的列表
    datalist = []
    #获取网页源代码
    datas = driver.page_source
    #数据转换
    html = etree.HTML(datas)
    #有60个节点的列表
    nodes = html.xpath('//ul[@class="gl-warp clearfix"]/li')
    for node in nodes:
        # 1.  书名
        bookname = node.xpath('./div/div[3]/a/em/text()')
        # 2. 价格
        price = node.xpath('./div/div[2]/strong/i/text()')
        # 3. 评分
        score = node.xpath('./div/div[4]/strong/a/text()')
        if score == []:
            score =  node.xpath('./div/div[5]/strong/a/text()')
        # 4. 书籍链接
        booklink = node.xpath('./div/div[1]/a/@href')
        # 4. 店名
        shopname = node.xpath('./div/div[5]/a/@title')
        if shopname == []:
            shopname = node.xpath('./div/div[6]/i/@data-tips')
        item = {
            "bookname":bookname[0],
            "price":price[0],
            "score":score[0],
            "booklink":"https:"+booklink[0],
            "shopname":shopname[0],
        }
        datalist.append(item)
    save_data(datalist)
# 4. 保存数据的函数
def save_data(datalist):
    with open("图书.json","w", encoding="utf-8")as file1:
        strdata = json.dumps(datalist,ensure_ascii=False)
        file1.write(strdata)
    close_selenium()
#5关闭对象
def close_selenium():
    driver.close()
    driver.quit()

if __name__ == '__main__':
    open_selenium()
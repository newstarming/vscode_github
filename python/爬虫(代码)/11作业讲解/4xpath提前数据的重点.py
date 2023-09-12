"""
现在使用的是用一个xpath提取所有数据
title  title  title  title title  title  title  title title  title  title  title
price  price  price  price  price  price  price  price  price price  price  price
zip(title,price)
title  title  title  title title  title  title  title title  title
price  price  price  price  price  price        price  price price
"""

"""
爬取作业: https://xa.58.com/ershoufang/
字段数据：
标题
1.标题名 2.标价   3.平方价格  4.户型 5.房屋大小
爬取十页数据
"""
import requests
from lxml import etree
import  json
# 1. 发送请求
def crawl_data():
    url = "https://sh.58.com/ershoufang/"
    #请求头
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "cookie":"aQQ_ajkguid=F47D5096-46FE-4504-B6B2-EB8B4C2AEC54; sessid=21E200E2-B0D0-44FF-B079-C8314B3F7E5D; ajk-appVersion=; id58=pRGhm2Rbi+lSD7KzBzDgAg==; 58tj_uuid=b46ff179-fe55-45c1-a833-4a60d794f38c; als=0; 58home=cd; fzq_h=95ccf5d7d8991d8d28496b7eb082c184_1684243248320_9d050fdc16104d25a35d532b689448ea_47924972895294158965352949380214739794; new_uv=2; utm_source=; spm=; init_refer=; new_session=0; 58_ctid=483; is_58_pc=1; commontopbar_new_city_info=31%7C%E8%A5%BF%E5%AE%89%7Cxa; ctid=483"
    }
    response = requests.get(url=url, headers=headers)
    #验证数据是否可以拉到
    str_data = response.content.decode()
    #print(str_data)
    # 2 数据转换
    html = etree.HTML(str_data)
    nodes = html.xpath('//section[@class="list"]/div')
    print(nodes)
    datalist1 = []
    for node in nodes:
        # . 代表section[@class="list"]/div
        title = node.xpath('./a/div[2]/div[1]/div[1]/h3/text()')
        price = node.xpath('./a/div[2]/div[1]/p/span[1]/text()')
        if price == []:
            price.append("没有详细价格")
        liaojie = node.xpath('./a/div[2]/div[1]/div[2]/div/span[4]/text()')
        if liaojie == []:
            liaojie.append("他不了解")
        dict_data = {
            "title": title[0],
            "price": price[0],
            "liaojie": liaojie[0],
        }
        datalist1.append(dict_data)
    with open("58同城.json", "w", encoding="utf-8") as file1:
        str_datass = json.dumps(datalist1, ensure_ascii=False)
        file1.write(str_datass)
    #
    # # 1. 标题名
    # titles = html.xpath('//div[@class="property-content-detail"]/div[1]/h3/text()')
    # # 2. 标价
    # allprice = html.xpath('//div[@class="property-price"]/p/span[1]/text()')
    # # 3. 平方价格
    # piece_price = html.xpath('//div[@class="property-price"]/p[2]/text()')
    # # 4. 户型
    # huxingshi = html.xpath('//div[@class="property-content-info"]/p/span[1]/text()')
    # huxingting = html.xpath('//div[@class="property-content-info"]/p/span[3]/text()')
    # huxingwei = html.xpath('//div[@class="property-content-info"]/p/span[5]/text()')
    # new_huxinglist= []
    # for i in  zip(huxingshi,huxingting,huxingwei):
    #     str = i[0]+"室"+i[1]+"厅"+i[2]+"卫"
    #     new_huxinglist.append(str)
    # #5.  房间大小
    # homesize = html.xpath('//div[@class="property-content-info"]/p[2]/text()')
    # datalist=  []
    # with open("同城.json","w",encoding="utf-8") as file1:
    #     for data in zip(titles,allprice,piece_price,new_huxinglist,homesize):
    #         dict_data = {
    #             "titles":data[0],
    #             "allprice":data[1]+"万",
    #             "piece_price":data[2],
    #             "huxing":data[3],
    #             "homesize":data[4].replace("\n","").replace(" ",""),
    #         }
    #         datalist.append(dict_data)
    #         print(dict_data)
    #     str_datass = json.dumps(datalist, ensure_ascii=False)
    #     file1.write(str_datass)



if __name__ == '__main__':
    crawl_data()
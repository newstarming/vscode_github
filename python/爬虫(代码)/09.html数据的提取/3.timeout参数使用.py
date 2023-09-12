import  requests
import random
ip_list = ["101.4.60.50:80","183.221.50.92:8123","140.124.72.74:8088"]


url = "https://www.jd.com/"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

while True:
    try:
        ip = random.choice(ip_list)
        proxies = {
            "http": f"http://{ip}",
            "https": f"https://{ip}"
        }
        #timeout参数没有提示，要手打
        response = requests.get(url=url, headers=headers, proxies=proxies,timeout=3)
        print("清洗数据")
        break
    except:
        print("代理异常重新使用的代理！")


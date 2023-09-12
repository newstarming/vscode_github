import  requests
import random
ip_list = ["61.216.156.222:60808","112.14.47.6:52024","182.139.110.52:9000"]
ip  = random.choice(ip_list)
#f = format()
proxies = {
    "http":f"http://{ip}",
    "https":f"https://{ip}"
}
url = "https://www.jd.com/"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url=url,headers=headers, proxies=proxies)
res_data = response.content.decode()
print(res_data)


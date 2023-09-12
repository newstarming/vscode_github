"""
response常用的属性



"""
import requests
url = "https://www.baidu.com/"
response=requests.get(url=url)

# 查看响应码
code=response.status_code
print(code)
print(type(code)) #<class 'int'>
if code ==200:
    print("执行清洗数据的方法，函数")
else:
    print("请求失败!")
# 查看请求头信息   查看本次请求的身份
headers=response.request.headers
print(headers)
# User-Agent 用户请求身份   python-requests库版本 2.28.2
# {'User-Agent': 'python-requests/2.28.2',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*',
# 'Connection': 'keep-alive'}




















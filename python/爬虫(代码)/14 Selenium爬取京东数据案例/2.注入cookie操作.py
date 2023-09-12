"""
注入cookie目的:在于操作自己的用户数据

自动化测试工具访问网页是没有cookie的  需要进行用户操作 需要手动注入cookie
"""

from selenium import webdriver
import json
import time

driver=webdriver.Chrome(executable_path="./chromedriver.exe")
# 测试网址
driver.get("https://bilibili.com")
# 20
with open("cookie_dsa1.txt","r",encoding="utf-8")as file1:
    str_data=file1.read()
    listcookie=json.loads(str_data)
#     遍历列表里面的所有字典
    for cookie in listcookie:
        cookie_dict = {'domain': 'bilibili.com',
                       'name': cookie.get('name'),
                       'value': cookie.get('value'),
                       "expires": '', 'path': '/',
                       'httpOnly': False,
                       'HostOnly': False,
                       'Secure': False}
        # 循环往driver里面注入cookie
        driver.add_cookie(cookie_dict)
#    跳出循环刷新网页 查看注入结果
driver.refresh()
# 定位 点击 输入
time.sleep(5)
driver.close()
driver.quit()











"""
window.open("https://bilibili.com")
js   javasricpt 脚本代码
作用  在浏览器打开一个新窗口

目的：切换窗口
1. 打开多个窗口
2. 获取多个窗口
3. 切换多个窗口

"""
from selenium import webdriver
import time
#driver 绝对路径
driver = webdriver.Chrome(executable_path="D:\software\py_Project\2304\13.selenium元素定位\chromedriver.exe")
driver.get("https://www.biquqq.com/")
time.sleep(2)
#js   javasricpt 脚本代码
#作用  在浏览器打开一个新窗口
jscode = 'window.open("https://www.bilibili.com")'
#通过driver 执行js代码
driver.execute_script(jscode)
# 获取多个 窗口的列表 [win1,win2]
window_list = driver.window_handles
#通过索引类别进行切换
time.sleep(2)
driver.switch_to.window(window_list[0])
time.sleep(2)
print("窗口1的操作代码")
driver.switch_to.window(window_list[1])
time.sleep(2)
driver.close()
driver.quit()

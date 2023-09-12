"""
目的:通过selenium访问bilibili网站获取网页源代码 保存到本地
步骤:
    1.实例化浏览器对象
    2.通过浏览器对象打开网页
    3.增加时间延时 返回网页源代码
    4.关闭浏览器对象

D:/六星教育/2212期/2212期python/12.B站视频案例&selenium基本使用/3.selenium方法介绍.py:16: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver=webdriver.Chrome(executable_path="./chromedriver.exe")
  这个是警告 不影响我们程序的运行！
"""
import time
from selenium import webdriver
#     1.实例化浏览器对象
# 通过webdriver模块 的Chrome类 实例化浏览器对象driver  指定了驱动位置
driver=webdriver.Chrome(executable_path="./chromedriver.exe")
#     2.通过浏览器对象打开网页
driver.get("https://www.bilibili.com/")
#     3.增加时间延时 返回网页源代码
driver.maximize_window()
time.sleep(3)
driver.save_screenshot("哔哩哔哩.png")
# 返回网页源代码的方法
data=driver.page_source
print(data)

# 4.关闭浏览器对象窗口
driver.close()
# 退出浏览器
driver.quit()










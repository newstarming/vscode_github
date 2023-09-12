"""
无头模式即使用selenium发送请求时  不会打开界面会在后台运行 不影响最终程序执行结果

"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 设置无头对象
options=Options()
# 设置无头参数  让使用了该无头对象的driver对象 不展示其操作的界面
options.add_argument("--headless")
driver=webdriver.Chrome(executable_path="./chromedriver.exe",options=options)
driver.get("https://www.bilibili.com/")
#     3.增加时间延时 返回网页源代码
driver.maximize_window()
time.sleep(3)
driver.save_screenshot("哔哩哔哩.png")
# 返回网页源代码的方法
data=driver.page_source
print(data)
#     4.关闭浏览器对象
driver.close()
# 退出浏览器
driver.quit()











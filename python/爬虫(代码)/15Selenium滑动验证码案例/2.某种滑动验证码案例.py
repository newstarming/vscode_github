"""
目的： 滑动铁路的滑动验证码
流程：
1. 通过浏览器对象打开网页
2. 定位到账户密码标签 分别进行账户密码输入
3. 定位登录标签  点击登录
4. 给出时间的延迟，让滑动的表情弹出来
5. 定位可以滑动的标签
6. 对标签进行滑动

可能出现的问题？
1. 在使用selenium打开网页时，  会在顶部出现  “Chrome正在收到自动化的测试”  可能会被反扒

解决： 可以添加去除该标签的参数  消除该标签
     options=webdriver.ChromeOptions()
     #去除   “Chrome正在收到自动化的测试”
     options.add_wxperimental_option("excludeSwitchers","enable_automation")
     driver = webdriver.Chrome(executable_path=r"./chromedriver.exe", options=options)
2. 可能会出现网页返回的元素差异  导致元素定位失败
解决： 可以通过findElements 匹配元素的特征 进行元素匹配

3. 遇到环境检测  直接检测到你在使用自动化测试工具在调试网页
解决：  执行清楚wendriver身份的脚步 主动去访问网页
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# 动作链对象  支持点击 滑动操作
from selenium.webdriver import ActionChains
# 实例化一个参数对象 可以添加一定的反反爬参数
options = webdriver.ChromeOptions()
#去除 Chrome正在收到自动化的测试”
options.add_experimental_option('excludeSwitches',['enable_automation'])
#1. 通过浏览器对象打开网页
driver = webdriver.Chrome(executable_path="../14.selenium京东案例/代码/chromedriver.exe", options=options)
driver.get("https://kyfw.12306.cn/otn/resources/login.html")

#窗口最大化
driver.maximize_window()
time.sleep(3)
# 模拟真实用户进行操作
script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
driver.execute_script(script)
#2.定位到账户密码标签 分别进行账户密码输入
username = driver.find_element(By.XPATH, '//*[@id="J-userName"]')
username.send_keys("1234567289")
#密码
password = driver.find_element(By.XPATH, '//*[@id="J-password"]').send_keys("789456")
#3. 定位登录标签  点击登录
click1 = driver.find_element(By.XPATH,'//*[@id="J-login"]').click()
#4. 给出时间的延迟，让滑动的标签给弹出来
time.sleep(2)
#5. 定位可以滑动的标签
driver.find_elements()
actionChains = driver.find_elements(By.XPATH,'//*[@id="nc_1_n1z"]')
        #'//*[@id="nc_2_n1z"]'
print(actionChains)

if actionChains == []:
    print("上一个语法没有匹配到元素")
    actionChains = driver.find_elements(By.XPATH, '//*[@id="nc_1__bg"]')

print(actionChains)
#6. 对标签进行滑动
#动作链对象
action1 = ActionChains(driver)
#通过 click_and_hlod 点击并且不放手的方法
action1.click_and_hold(actionChains[0])

# move_by_offset 制定滑动的距离  根据实际的距离  给出不同的段数
#参数1  指定X轴的值 参数2  指定Y轴的值
action1.move_by_offset(80,-20).perform()
action1.move_by_offset(40,40).perform()
action1.move_by_offset(60,-30).perform()
action1.move_by_offset(40,-50).perform()
#可以通过release 方法 执行放手的操作
action1.move_by_offset(80,20).release().perform()
time.sleep(3)
driver.close()
driver.quit()

"""
显示等待概念： 在一定时间内， 如果加载出现元素则返回改元素 如果超出最大容忍时间抛出异常
目的  完善之前使用的time.sleep的项目
让网页的元素 加载出来即定位而且直接进行下一步的操作  不等待


"""

from selenium import  webdriver
from  selenium.webdriver.common.by import By
import  time
#导入显示等待类
from  selenium.webdriver.support.ui import  WebDriverWait
#导入预期效果条件文件 需要使用里面的函数
from  selenium.webdriver.support import expected_conditions
driver  =webdriver.Chrome(executable_path="./chromedriver.exe")
#1. 访问笔趣网
driver.get("https://www.biquqq.com/")
#r重新定义一个显示等待对象， WebDriverWait(参数1： driver对象 参数2：最大的容忍时间)
#如果后面通过这个显示等待对象定位元素最大时间超过5秒 抛出异常
wait_driver = WebDriverWait(driver, 5)
#定位账号
# until 直到
# 调用 expected_conditions 文件里面的presence_of_element_located(By.XPATH,"退出")
username = wait_driver.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="username"]')))
username.send_keys("jiuhaoyyds")
password = wait_driver.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
password.send_keys("qwe123")

login = wait_driver.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'int')))
login.click()
# 4. 需要加入至少4s的时间延迟， 让业务进行跳转到用户主页
#5. 点击我的书架  跳转  加1个2秒时间延迟
book = wait_driver.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/div[1]/div/div[3]/a[2]')))
book.click()
#6. 获取数据
datas = driver.page_source
print(datas)
#7. 清晰数据
#8. 关闭浏览器对象和窗口
driver.close()
driver.quit()


"""
iframe 标签切换
iframe 是什么？
是嵌套在网页源代码里面的一个标签(相当于一个窗口)
有什么用？
如果没有iframe标签的切换  是不能对iframe标签里面的元素进行操作

目的： 定位网易云歌单  并且进行点击
流程：
1. 打开163.com
2. 定位歌单的标签
3. 点击
<a title="予你情诗百首，余生你是我的所有" class="tit s-fc0" href="/playlist?id=2230318386" data-res-id="2230318386" data-res-type="13" data-res-action="log" data-res-data="recommendclick|1|alg_high_quality|user-playlist">
予你情诗百首，余生你是我的所有
</a>
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://music.163.com/")
time.sleep(2)
# 要发现iframe标签 就切换  标签   通过drvier.switch_to.iframe(参数：网页里面的iframe的id)方法
driver.switch_to.frame("g_iframe")
songlist = driver.find_element(By.XPATH, '//*[@id="discover-module"]/div[1]/div/div/div[1]/ul/li[1]/div/a')
songlist.click()
time.sleep(2)
driver.close()
driver.quit()
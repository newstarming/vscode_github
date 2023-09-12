"""
讲解定位元素的方法
    讲解三种
By.ID  By.XPATH  By.NAME  By.CLASS_NAME
目的是为了在网页上没有id  或其他元素时可以使用其他定位元素的方法定位元素

selenium 打开网页都是以无cookie的身份访问， 所以不能直接访问用户数据， 需要手动输入账号密码此案查看
目的： 访问笔趣阁  获取自己的书籍信息

流程：
1. 访问笔趣网
2. 定位账号密码并且输入
3. 定位登录按钮进行点击
4. 需要加入至少4s的时间延迟， 让业务进行跳转到用户主页
5. 点击我的书架  跳转  加1个2秒时间延迟
6. 获取数据
7. 保存数据

document.querySelector('.int')
寻找1个class等于 int的元数
class 在网页的标签里面可以有很多个相同
"""
from selenium import  webdriver
from  selenium.webdriver.common.by import By
import  time
driver  =webdriver.Chrome(executable_path="./chromedriver.exe")

#1. 访问笔趣网
driver.get("https://www.biquqq.com/")
time.sleep(1)
#2.定位账号密码并且输入 链式调用 定位到元素直接执行send_keys方法
driver.find_element(By.NAME, "username").send_keys("jiuhaoyyds")
driver.find_element(By.NAME, "password").send_keys("qwe123")
#3. 定位登录按钮进行点击  网页上面的 class属性 对应着  By.CLASS_NAME
driver.find_element(By.CLASS_NAME, "int").click()
# 4. 需要加入至少4s的时间延迟， 让业务进行跳转到用户主页
time.sleep(4)
#5. 点击我的书架  跳转  加1个2秒时间延迟
# 出现没有 id class   就用By.XPATH方法  定位
driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/div/div[3]/a[2]').click()
time.sleep(1)
#6. 获取数据
datas = driver.page_source
print(datas)
#7. 清晰数据
#8. 关闭浏览器对象和窗口
driver.close()
driver.quit()
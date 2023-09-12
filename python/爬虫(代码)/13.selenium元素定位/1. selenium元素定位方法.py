"""
目标： 通过selenium 访问百度输入关键字 访问对应的网页， 并且返回的数据保存到本地 为html文件
url = "https://www.baidu.com
流程
通过代码实现
1. 打开浏览器访问百度首页
2. 定位到输入的标签
3. 向输入标签键入关键字 input
4. 定位到点击百度一下的标签
5. 点击百度一下  >>> 返回数据
6. 保存数据
7. selenium 对象关闭

<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
input标签是前端输入标签
tips:
标签里面的id属性是当前整个网页里面唯一字段    selenium定位元素的重点

<input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">
    <input type="submit"  想当于  提交的按钮

document.querySelector("#su")  找到一个id等于su的元素  .是class

"""
from  selenium import webdriver
from  selenium.webdriver.common.by import  By
import  time

word = "python"
#生成浏览器对象
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
#1. 打开浏览器访问百度首页
driver.get("https://www.baidu.com")
time.sleep(2)
#2. 定位到输入的标签

# find_element 寻找网页元素的方法， 参数：1. 元素类型 参数2 元素的位置/元素具体的值  返回值element对象
#没有匹配到元素 报错
input = driver.find_element(By.ID,"kw")
print(input)
#3. 向输入标签键入关键字 input  仅限于input标签的元素才能调用send_keys方法
input.send_keys(word)
time.sleep(2)
#4. 定位到点击百度一下的标签
click_ = driver.find_element(By.ID,"su")
# 点击的标签  不能执行send_keys 标签
click_.click()  #点击以后还有发送请求的操作，  就会产生响应， 还是要加上时间延迟，  给服务器容错时间
time.sleep(2)
#6. 保存数据
str_data = driver.page_source
print(str_data)
with open(f'{word}.html',"w", encoding="utf-8")as  file1:
    file1.write(str_data)

#    7. selenium 对象关闭
driver.close()  #网页
driver.quit()  #浏览器对象


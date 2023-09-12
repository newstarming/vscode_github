
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# 更新 pip   //pip install pillow下载这个库 (裁剪图片的库)
from PIL import Image
# 第三方打码接口   imag1.png   需要自己注册账号密码 填入接口函数
from interface_w import chaojiyin
# 使用动作链类
from selenium.webdriver import ActionChains

def selenium111():
    driver=webdriver.Chrome(executable_path=r"./chromedriver.exe")
    driver.get("https://passport.bilibili.com/login?from_spm_id=333.337.top_bar.login_window")
    time.sleep(2)
    driver.maximize_window()
#     输入账号密码
    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys("123456465")
    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/input').send_keys("123456465")
    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]').click()
    time.sleep(2)
    driver.save_screenshot("哔哩哔哩.png")
    # 生成一个画布对象  裁剪验证码
    image_ws =Image.open("哔哩哔哩.png")
    # 根据坐标进行裁剪 返回裁剪对象
    captcha=image_ws.crop((792,257,1111,668))
    # 保存裁剪后的验证码
    captcha.save("imag2.png")
    # 验证码已经保存 就可以调用 识别验证码的接口
    # 190,166|55,60|83,146
    places=chaojiyin()
    print(places)
    #places = "190,166|55,60|83,146"
    # # [190,166,  55,60    ,83,146]
    places=places.split("|")
    print(places)
    # 屏幕最左边的距离到验证码的真实距离
    initialize_x = 792
    # 屏幕最上边的距离到验证码的真实距离
    initialize_y = 257
    for place in places:
        # 190,166
        x=int(place.split(",")[0])
        # 166
        y=int(place.split(",")[1])
    #     实例化动作链对象
        actionChains=ActionChains(driver)
        # 链式调用  click点击x y轴对应的数据  并且执行 perform
        #
        actionChains.move_by_offset(initialize_x+x,initialize_y+y).click().perform()
        initialize_x=0
        initialize_y=0
    #     点击的重点 点完以后 要回到原来的位置  不然要报错
        actionChains.move_by_offset(-(x ), -(y)).click().perform()
        time.sleep(3)
    driver.find_element(By.CLASS_NAME,'geetest_commit_tip').click()
    time.sleep(50)
    # # 写入cookie
    # cookies=driver.get_cookies()
    # str_data=json.dumps(cookies)
    # with open("cookielist.txt","w",encoding="utf-8")as file1:
    #     file1.write(str_data)
    # driver.close()
    # driver.quit()
if __name__ == '__main__':
    selenium111()

"""
我们先定位到屏幕最左边的和最上边的距离到验证码的真实距离，网站更新了，出了一个新机制(点击验证码以后再点击其他非验证码位置（验证码会消失）)，这个时候再通过坐标点击就会报错，但是在验证码上方白色区域点击验证码就不会消失 

那么我们就需要在点击第一次的时候从0,0  点到(x+打码的x,y+打码的y)以后 ，往后退到(x,y)的距离  就是验证码的白色区域内(即验证码左上角) ，然后再往下进行下一次点击  循环点击完即可

"""



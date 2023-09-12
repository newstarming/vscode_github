"""
涉及b站登录



1.获取cookie   必须登录到主页才能获取!
2.定位输入账户密码的标签 输入账号密码
3.点击登录 弹出验证码
4.截取网页（全屏）
4.裁剪出验证码   对接第三方打码平台   调用接口 返回坐标   x|y (按照文字顺序 返回坐标 )
5.按照距离进行点击
6.点击确定
7.登录网页    获取cookie保存到本地    以便注入

"""

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
    driver=webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://passport.bilibili.com/login?from_spm_id=333.337.top_bar.login_window")
    time.sleep(2)
    driver.maximize_window()
#     输入账号密码
    driver.find_element(By.XPATH,'//*[@id="login-username"]').send_keys("123456465")
    driver.find_element(By.XPATH,'//*[@id="login-passwd"]').send_keys("123456465")
    driver.find_element(By.XPATH,'//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
    time.sleep(2)
    driver.save_screenshot("哔哩哔哩.png")
    # 生成一个画布对象  裁剪验证码
    image_ws =Image.open("哔哩哔哩.png")
    # 根据坐标进行裁剪 返回裁剪对象
    captcha=image_ws.crop((1069,238,1335,541))
    # 保存裁剪后的验证码
    captcha.save("imag1.png")
    # 验证码已经保存 就可以调用 识别验证码的接口
    # 190,166|55,60|83,146
    places=chaojiyin()
    # [190,166,  55,60    ,83,146]
    places=places.split("|")
    print(places)
    for place in places:
        # 190,166
        # 190
        x=int(place.split(",")[0])
        # 166
        y=int(place.split(",")[1])
    #     实例化动作链对象
        actionChains=ActionChains(driver)
        # 链式调用  click点击x y轴对应的数据  并且执行 perform
        actionChains.move_by_offset(1067+x,238+y).click().perform()
    #     点击的重点 点完以后 要回到原来的位置  不然要报错
        actionChains.move_by_offset(-(1067 + x), -(238 + y)).click().perform()
        time.sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a/div').click()
    time.sleep(50)
    # 写入cookie
    cookies=driver.get_cookies()
    str_data=json.dumps(cookies)
    with open("cookielist.txt","w",encoding="utf-8")as file1:
        file1.write(str_data)
    driver.close()

    driver.quit()

if __name__ == '__main__':
    selenium111()











from selenium import webdriver
import time
from lxml import etree
import  json
from selenium.webdriver.common.by import By
# pip install pillow 下载剪辑图片的库
from PIL import Image
#第三方打码接口  需要自己注册账号密码  填入接口函数

from  interface_w import  chaojiyin
#使用动作链类
from  selenium.webdriver import  ActionChains

def selenium111():
    drvier = webdriver.Chrome(executable_path="./chromedriver.exe")
    drvier.get("https://passport.bilibili.com/login?from_spm_id=333.37.top_bar.login_window")
    time.sleep(2)
    drvier.maximize_window()
    #输入账户密码
    drvier.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys("123456")
    drvier.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/input').send_keys("123456")
    drvier.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]').click()
    time.sleep(2)
    drvier.save_screenshot("哔哩哔哩.png")
    #生成一个画布对象 裁剪验证码
    image_ws = Image.open("哔哩哔哩.png")
    #根据坐标进行裁剪  返回裁剪对象
    captcha = image_ws.crop((793,256,1111,668))
    captcha.save("image2.png")
if __name__ == '__main__':
    selenium111()
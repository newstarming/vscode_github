# 超级鹰
import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }


    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考    http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }

        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()



# 超级鹰网址  打码平台
# http://www.chaojiying.com/price.html

def chaojiyin():
    chaojiying = Chaojiying_Client('jiuhao999', 'qweqwe', '96001')
    # 这个是需要传递的验证码
    im = open('imag2.png', 'rb').read()
    #本地图片文件路径 来替换 数字验证码.jpg 有时WIN系统须要//
    # 9004是验证码类型
    data=chaojiying.PostPic(im, 9004)["pic_str"]   #索引取值
    print(data,type(data))
    return data

if __name__ == '__main__':
    chaojiyin()
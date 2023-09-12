"""
1目的采集lol 的英雄数据  练习jsonpath提取数据
具体字段  1英雄名  2技能  3皮肤信息

流程
1抓包
2发送请求
3清洗数据
4保存数据

"""
import requests
from jsonpath import jsonpath
import json

url="https://game.gtimg.cn/images/lol/act/img/js/hero/43.js?ts=2788786"

# 请求头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
# 发送请求
response=requests.get(url=url,headers=headers)
str_data=response.content.decode()

# 数据类型转换 str >>dict
dict_data=json.loads(str_data)
print(dict_data)

#  1英雄名
# 天启者
nick_name=jsonpath(dict_data,"$..hero.name")
# 卡尔玛
true_name=jsonpath(dict_data,"$..hero.title")
print(nick_name)
print(true_name)
#  2技能
spells=jsonpath(dict_data,"$..spells[*].name")

print(spells)
#  3皮肤信息
skins=jsonpath(dict_data,"$..skins[*].name")
print(skins)













"""
要点错误    如何处理索引超出范围的错误
third_url = re.findall('"(https://videohive.net/item/white-logo/\d*)"', second_res)[0]
IndexError: list index out of range
"""
# 0  1 2
# list1 = [1]
# print(list1[0])
# #print(list1[1])
# print(list1[2])
# 原因： 有数据的列表只有1条数据 索引为0  1  2
# 但是取值的时候超出了索引的范围  就报错
# 数据少了 or  索引太大

#third_url = re.findall('"(https://videohive.net/item/white-logo/\d*)"', second_ res)[0]
#re.findall() >>> 匹配的数据返回包含数据的列表  else  返回空列表
#second_res  没有数据  "(https://videohive.net/item/white-logo/\d*)" 写对了
#second_res  有数据  "(https://videohive.net/item/white-logo/\d*)" 写错了  返回的数据变化了  正则匹配 不在适用
## 返回空列表
# 如何排查？ 打印  被匹配的字符串


#dictd = {'融创98平精装三室，满二，随时可以看房','activity_title','piece_price','570','home_size','75.1㎡'}
dictd = {'融创98平精装三室，满二，随时可以看房':'activity_title',
         'piece_price':'570',
         'home_size':'75.1㎡',
         }

import  json
json.dumps(dictd,ensure_ascii=False)
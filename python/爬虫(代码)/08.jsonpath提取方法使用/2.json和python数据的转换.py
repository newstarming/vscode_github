"""
业务场景
有了json文件      保存到excel  .xlsx .xls .csv文件

先读取json文件 再通过openpyxl模块进行写入!
"""

import json
with open("懂车帝3.json","r",encoding="utf-8") as file1:
    # str_data=file1.read()
    # print(str_data)
    # print(type(str_data))

#   需要通过数据转换 str >> dict 数据清洗 再写入xlsx
#     list_data=json.loads(str_data)
#     print(list_data)
#     print(type(list_data))
# #     数据清洗   jsonpath 清洗
#   json.load方法 直接传入文件对象  将文件里面的内容(list)转换成对应的数据类型(list)
    print(type(file1))
    list_data2 = json.load(file1)
    print(list_data2)
    print(type(list_data2))
#   对清洗好的数据进行保存

with open("new懂车帝.json","w",encoding="utf-8")as file2:
    # 需要传递 list/dict类型数据,文件对象,ensure_ascii=False
    json.dump(list_data2,file2,ensure_ascii=True)













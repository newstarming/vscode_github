"""
为什么写了采集一张图片的程序以后  计算机会按照代码的意思帮我们采集图片呢？
难道计算机能看得懂代码吗？
计算机看不懂代码
计算机只能看得懂  0101001001001001 二进制形式的数据

因为这是python解释器的功能 会把代码转换成字节类型的数据,字节类型数会进行转换
1bytes =  8bit (计算机最小的存储单位)   1bit 0 1
进行转换以后 计算机会自动按照二进制形式 执行命令发送请求
返回的响应内容又是010101010101010   计算机就会自动解码  010101010101 >>> bytes   python就可以对字节进行转换，转换以后就能把响应内容展示到控制台
"""
#
print("采集数据")

# import requests
# url="https://img1.baidu.com/it/u=2551315007,1592529415&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1681837200&t=8dd1a9d1e7166ee9ff4801a71656eb96"
# response=requests.get(url)
# with open("机车.png","wb")as file1:
#     file1.write(response.content)

databytes=  b"c"
print(databytes.decode())



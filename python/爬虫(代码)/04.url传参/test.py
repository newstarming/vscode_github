
"""
1.同一个用户代理 useragent访问次数过多可能会被反扒，那么我们可以采取什么措施来反反爬？

2.有几种实现useragent池的方法？

3.为什么网页导航栏上面的url里面有像密文的数据？是加密了吗？

4.url传参有什么用？

5.url传参有几种方式？













上节课参考答案
1.通过python如何发送http请求需要用到什么库?什么方法?
答:requests 库   通过requests.get方法发送请求

2.发送带https的数据包 报ssl验证错误如何处理？
答:通过在get方法 里面 加上关键字verify=False   注意不是所有同学都会有验证

3.实操任务 如何保存html文件到本地？   （而且还要明确保存不同格式文件的保存方法 wb w,以及文件格式）
# 通过with open函数 分别以文件操作参数wb （和response.content配合使用） 和 字符写入形式w分别进行写入(和response.content.decode()配合使用)

4.为了防止反扒需要设置用户代理，那如何设置用户代理
通过构建headers字典  把user-agent作为键  浏览器代理作为值   并且把headers放在get方法里面命名关键字参数headers进行传参

"""












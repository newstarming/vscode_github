"""
1.urllib
2.requests
这两个都是可以发送http请求的库/模块 (都可以访问网页的数据)

为什么要学习requests而不学习urllib呢？
urllib是python2版本发送http请求的库
urllib已经封装到了requests库里面

requests > urllib

怎么使用？怎么下载库?
requests是第三方库 需要手动下载

(-i https://pypi.tuna.tsinghua.edu.cn/simple) 这个是下载源 清华下载源 作用:在这个网站去下载模块
讲解三种下载方法
通过命令下载   pip 是python下载第三方库的软件  pip.exe
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
1.Terminal(pycharm控制台) 输入以上命令
    pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
    可能出现的问题
    1.1 提示'pip' 不是内部或外部命令，也不是可运行的程序     全部点击确定以后  重新开一个cmd窗口 查询!
        产生问题的原因是没有配置pip的环境变量(看视频操作)
    1.2不知道自己python位置                          全部点击确定以后  重新开一个cmd窗口 查询!
        通过命令 cmd >>> where python >>>D:\python3.9\python.exe
    1.3 'where' 不是内部或外部命令，也不是可运行的程序
        C:\Windows\System32 配置这个路径的环境变量  全部点击确定以后  重新开一个cmd窗口 查询!

2.在cmd 下载
    win+r >>cmd >输入命令
        pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple

3.通过pycharm下载
    左上角 file>>settings>>解释器>> 点加号>>搜索要下载的模块 >>install package
如果一种方法出错了  就是用另外两种  目的就是为了下载模块

怎么看下载成功？
import requests
"""




















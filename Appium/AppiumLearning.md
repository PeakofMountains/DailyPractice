# 通过Appium连接手机(我使用的是Android手机)，访问手机的应用，对手机进行相应的操作

参考内容：[python爬虫23 | 手机，这次要让你上来自己动了。这就是 Appium+Python 的牛x之处](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484358&idx=1&sn=23e920d7a8d43dafd7607c8d30eeb946&scene=19#wechat_redirect),[python爬虫24 | 搞事情了，用 Appium 爬取你的微信朋友圈](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484386&idx=1&sn=7f0545f27f095f20d69deedfa9f606a1&scene=19#wechat_redirect)和[Appium 手机 App 自动化 + Python - 华为大哥带你入门](https://www.bilibili.com/video/BV1tE411n7rV?p=4)

#### 第一次尝试连接手机后用Appium打开手机的bilibili应用，搜索指定的内容，并在电脑的控制台中输出搜索出来的一页视频标题
代码见androidTest.py文件
### 准备工作：

#### 电脑端环境:
1. 安装node.js，因为Appium的使用需要它的协助  
2. 安装JDK，java环境，Android需要这个环境  
3. 安装Android SDK，它是Android强大的开发工具包
4. 安装Android虚拟机(可选如果你用你的真机也可以的用usb插入电脑就行)
5. 安装Appium
6. 安装Appium-Python-Client，它是python客户端，用来连接 Appium  
7. 安装Python  
具体的安装流程见[此篇文章](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484358&idx=1&sn=23e920d7a8d43dafd7607c8d30eeb946&scene=19#wechat_redirect),此处只记录我在安装过程中出现的错误问题及解决办法  
* 在计算机的环境变量中添加某个路径只是为了能在命令行中直接通过程序的名称对程序进行访问，在命令行进行执行而不用进入到指定的文件夹在运行程序
* 安装完node之后要在电脑-属性-高级-环境变量-系统变量处Path添加node.exe所在的文件夹路径，以便在控制台直接通过输入node名称就能运行
* 安装完JDK之后同样要在环境变量中设置路径Path
* 安装Android SDK，根据自己电脑的版本选择安装适合的版本，文件在GitHub上下载速度较慢，可以通过代理下载网站来加速，安装完毕后将安装文件位置文件夹内的tools和platform-tools两个文件夹的路径添加到环境变量中
* 我直接用真机进行测试所以没有安装Android虚拟机，用手机直接连接的电脑，在手机(我的是oppoR15)上进入关于手机，找到版本号连续点击输入账户密码后开启开发者模式，然后进入更多设置-开发者选项，
选择开启USB调试，下滑到底下有禁止权限监控选项，选择开启，否则手机会在电脑上搜索不到。在电脑上启动命令行，输入adb devices查看连接的设备，如果连接成功会出现设备名称(一段字符码)
* 安装Appium有三种方式：  
1. 通过在GitHub上下载对应的Appium.zip版本压缩包，下载完毕直接解压在指定文件夹  
2. 通过在Github上下载对应的Appium.exe安装程序，运行后指定安装在指定位置
3. 通过在命令行用`npm install -g appium`命令安装，这种方式直接下载安装，但是因为他的服务器在国外，因此速度很慢，很难成功。
此时需要切换国内源进行安装，输入`npm config get registry`可看到当前的npm镜像。输入`npm --registry https://registry.npm.taobao.org info underscore`,
回车之后会有字符串,输入 `npm registry=https://registry.npm.taobao.org/`斜杠不要丢掉不然不会成功,输入`appium install -g appium`,此时输入完成之后在cmd
里输入`appium`会显示appium版本信息.但是这种方式安装还是太慢。  
我采用的是第二种方法，只是还没找到在cmd中运行appium的方法  
* 安装Appium-Python-Client可以直接在命令行通过`pip install Appium-Python-Client`命令来安装，安装完毕后在npm的文件夹内找到这个文件所在的bin文件夹，将这个文件夹添加到环境变量的路径Path中
* 安装appium-doctor可以直接在命令行通过`npm install -g appium-doctor`进行安装，安装完毕后在命令行运行`appium-doctor`命令，如果出现这个样子就算安装成功且之前的Appium相关的安装配置成功![appium-doctor进行检测是否配置成功](https://mmbiz.qpic.cn/mmbiz_png/J2icnQspGlaI2CvG0TfHIElp0zbKciapWr8Jefg8EaVZCU14MtQqlR8QeAADNS59DONoQbiaMlNPT2eLb54MxMfVg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

### 执行过程：
1. 编写驱动程序
3. 计算机连接手机(需要做上面所说的连接配置)
2. 运行Appium开启Appium Server服务器
3. 运行驱动程序
* 在首次运行驱动程序的适合会向手机上安装几个软件(包括只能用于程序进行输入的专用输入法)
* 在程序执行完毕还不能实现将输入法自动切换回去的功能，还得自己手动切换回手机的输入法，否则手机无法进行输入。
* 运行的时候可能会出现"selenium.common.exceptions.NoSuchElementException: Message: An element could not be located on the page using the given search parameters."
错误提示，这是因为页面跳转是需要时间的，但是代码执行是很快的，这里没有找到元素，在获取id时，手机页面还没有进入到该页面，所以在页面上找不到元素(例如：应用启动之前的那段广告已经超过了自己代码规定的时间)，
通过在代码中加大允许等待的时间可以解决这个问题  

![](https://pic3.zhimg.com/50/v2-ac7a976b3b3353895d504c93466375ee_hd.jpg?source=1940ef5c)


上面的尝试例子是访问Bilibili软件，如果要访问其他的应用就会用到包名Package，对于获取应用包名根据应用是否已经安装在手机上有两种分类，这两种方法见[教程文章](http://www.python3.vip/tut/auto/appium/01/#%E6%9F%A5%E6%89%BE-%E5%BA%94%E7%94%A8-package-%E5%92%8C-activity)和[教程视频](https://www.bilibili.com/video/BV1tE411n7rV?p=6)  

要实现功能按键的点击等操作就必须定位到相关组件的位置，Appium提供了几种定位的方法，详细的使用见[教程文章](http://www.python3.vip/tut/auto/appium/02/)和[教程视频1](https://www.bilibili.com/video/BV1tE411n7rV?p=7)和[教程视频2](https://www.bilibili.com/video/BV1tE411n7rV?p=8)和[教程视频2](https://www.bilibili.com/video/BV1tE411n7rV?p=9)和[教程视频2](https://www.bilibili.com/video/BV1tE411n7rV?p=10)  





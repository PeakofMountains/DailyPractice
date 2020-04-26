# PythonSpider Learning  

![image](https://w.wallhaven.cc/full/zx/wallhaven-zx69yw.jpg)
### 感谢[中国大学mooc嵩天老师团队的课程](https://www.icourse163.org/learn/BIT-1001870001)  

爬虫一直是我想学的一项技能，一是出于好奇心，二是想通过这个实例练习自己的python，爬虫的学习是有趣的，各种各样的实例可以自己创新，实现花样的功能

下面是学习中总结的一些易错点和知识点

----------------------
### Python网络爬虫之规则

* URL格式错误，一般指URL格式不符合规范导致无法建立连接，通常会产生URLRequired错误。如果URL格式正确，可能触发Timeout类错误
* timeout的多种情况--参考自[这篇文章](https://blog.csdn.net/w365904/article/details/100115665)：  
    1. connectionRequestTimout：指从连接池获取连接的timeout
    2. connetionTimeout：指客户端和服务器建立连接的timeout，就是http请求的三个阶段，一：建立连接；二：数据传送；三，断开连接。超时后会ConnectionTimeOutException
    3. socketTimeout：指客户端从服务器读取数据的timeout，超出后会抛出SocketTimeOutException
* 数据推送（push model）一般指将数据发送出去的行为。在Requests库中，post()、put()、patch()都体现这种行为模式
* request()是其他所有函数的基础函数，完成所有功能，其它函数只是它的一种封装形式
* Requests库共有7个主要方法：request()、get()、head()、post()、put()、patch()、delete()，名字基本与HTTP的操作相同
* Requests库中，检查Response对象返回是否成功的状态属性是r.status_code，200表示连接成功，404表示失败
* Requests库中，代表从服务器返回HTTP协议头所推荐编码方式的属性的是 .encoding 它是从HTTP header中猜测获得的响应内容编码方式
* Requests库中，以下代表从服务器返回HTTP协议内容部分猜测获得编码方式的属性是.apparent_encoding，它是从内容中分析出的编码方式，一般作为备选编码方式
* DNS失败将造成网络连接错误，因此产生连接错误异常
* get()方法最常用的原因在于服务器端对push()、post()、patch()等数据推送的限制，试想，如果允许大家向服务器提交数据，将带来无穷无尽的安全隐患。因此，通过get()获取数据，服务器作为数据提供方而不是接收方，更为安全

---------------------
### Python网络爬虫之提取  

* requests是爬虫库，只用于获取页面，不对页面信息进行提取，re,BeautifulSoup,lxml库都能进行对信息的提取
* from bs4 import BeautifulSoup指从bs4库中引入一个元素（函数或类），这里BeautifulSoup是类
* 一个文档只对应一个标签树,一个HTML文档与BeautifulSoup对象等价
* 标签树上除了标签外，节点还可能是字符串（NavigableString）类型  
* `<a class ="title" href ="https://python123.io/ws/demo.html" > TEXT </ a >`中 `a` 是标签，`href`是属性
* a标签是HTML预定义标签，通过soup.a可以直接获取
* 自然语言理解一般针对语言文本，HTML等信息标记格式产生的文本需要采用信息提取方式获得语言文本，才使用自然语言理解方式进一步处理（如果有需要的话）
* bs4解析器是能够解释HTML或XML的一个第三方库，re是用来表达并匹配正则表达式的，不能够装载到bs4库中
* 遍历树一般没有"跳跃遍历",bs4库遍历标签树方法有上行遍历，下行遍历，平行遍历
* Beautiful Soup库不能够生成标签树，只能解析、遍历和维护

--------------------------
### Python网络爬虫之实战 
* 尽管正则表达式可用于自动化脚本，但不直接体现自动脚本的作用  
* 以下这些操作符是正则表达式中最常用  
  ![image](https://python123.io/images/c6/a1/711110dbd78fef741e9e766b062d.png)  
  ![image](https://python123.io/images/a3/2a/8134df73b14e5b93bd020695bde3.png)
* 字符串包括：普通字符串和原生字符串，原生字符串中没有转义符（\）
* re库和BeautifulSoup库，两者没关系，re库以字符串模式匹配与检索方式提取信息，与Beautiful Soup库不同

-----------------------

###  Python网络爬虫之框架

* 爬虫技术路线至少包含一个爬虫库和一个解析库，bs4和re都是解析库，因此只是bs4-re不能实现爬取信息功能
* Robots协议允许是爬虫能够实施的首要条件
* Scrapy具有5+2结构，其中，5个模块分别是：Engine、Spiders、Scheduler、Downloader和Item Pipelines
* Spiders模块给出了Scrapy爬虫最初始的请求
* Scrapy中使用REQUESTS表达URL，因此，URL不是其直接承载的元素
* Spider请求顺序：Spider->Engine->Scheduler，注意，Spider请求不直接到Downloader模块
* 在Scrapy框架中，Downloader爬取页面内容后路线：Downloader->Engine->Spiders路径
* Spiders->Engine再到下面两条路径之一
    * ->(ITEMS) Item Pipelines
    * ->(REQUESTS) Scheduler  
    根据不同类型的结果，有两个路径

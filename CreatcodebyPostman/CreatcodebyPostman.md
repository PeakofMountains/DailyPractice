我是从这篇[文章](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247485571&idx=1&sn=094517114b22a4684988008aecab2639&scene=19&token=464856977&lang=zh_CN#wechat_redirect)了解到的Postman
## 实现的功能：通过Postman软件的功能实现自动生成request请求代码，可以直接在程序中使用， 而且可以请求到Json格式的网页内容，大大简化了操作难度(新手友好)

当然这是Postman的一个应用，它的其他功能也很强大！


具体使用流程：

1. 打开要请求的网页，按F12进入开发者调试模式
2. 刷新网页
3. 选择Network菜单，选择下面的XHR栏，对应下面左边有多个文件
4. 逐一点击查看Response菜单，是否含有你想爬取的内容
5. 找到包含你想爬取的内容的文件时，可以点击Headers栏查看请求的相关信息，比如页数什么的
6. 关键一步：在文件上右击，选择Copy--Copy as cURL(bash)，点击
7. 打开Postman软件，选择Import--Raw Text，将刚才复制的内容粘贴到此处，点击continue
8. 点击蓝色的Send图标发送请求，可以看到你想爬取的内容所在的文件内容已经显示在下面的文本框中
9. 点击Send图标下面的Code，选择你需要的对应语言的请求
10. 点击Setting右边的Copy按键
11. 现在可以把请求粘贴到程序中直接使用了！
12. 那个代码中的respond就是html了，最后的print可以去掉(这个输出请求的内容的)

## 给力！！！
![image](https://pic4.zhimg.com/80/v2-3486923c83196c45cbb27ca12c811203_1440w.jpg)

### BOM浏览器对象模型

#### BOM概述
* BOM( Browser Object Model)即浏览器对象模型，把浏览器当成一个对象，它提供了独立于内容而与浏览器窗口进行交互的对象，其核心对象是window
  * window对象是浏览器中的顶级对象，是JS访问浏览器窗口的接口，是一个全局变量，在浏览器中定义的变量和方法都会成为window对象的属性和方法

* BOM由一系列对象组成，每个对象都提供了很多方法和属性

* BOM兼容性较差，缺乏标准，是由各自的浏览器厂商定义的

* DOM可以理解成网页页面部分，BOM可以理解成整个浏览器部分，DOM是BOM的下属，就像DOM中使用的document是BOM中的window对象的下属，其完整写法应该是window.document，但是在DOM中window是可以省略的
* **注意:window下的一个特殊属性window.name，因此变量不能定义为name**

#### window对象的常见事件

* 窗口加载事件

  * 用法：

    ```js
    // 窗口加载事件的两种使用方式
    window.onload = function () { };
    window.addEventListener('load', function () { });
    ```

  * window.onload是窗口(页面）加载事件,当文档内容完全加载完成会触发该事件(包括图像、脚本文件、CSS文件等),就调用的处理函数，***使用了此方法将script标签里的内容加上窗口加载事件，就能将script标签放在body前面甚至head中，都能起到body中元素创建完毕后再执行script中的JS代码的效果***

  * 注意∶

    1. 有了window.onload就可以把JS代码写到页面元素的上方，因为onload是等页面内容全部加载完毕，再去执行处理函数。
    2. window.onload传统注册事件方式只能写一次，如果有多个，会以最后一个window.onload为准。
    3. 如果使用addEventListener的注册方式则没有限制

  * DOMContentLoaded事件，与onload事件不同的是：其触发时，仅当DOM加载完成，不包括样式表，图片，flash等等。le9以上才支持，如果页面的图片很多的话，从用户访问到onload触发可能需要较长的时间，交互效果就不能实现，必然影响用户的体验，此时用DOMContentLoaded事件比较合适。用法：

    ```js
    document.addEventListener('DOMContentLoaded',function(){});
    ```

* 调整窗口大小事件

  window.onresize是调整窗口大小的加载事件，当触发时就调用的处理函数

  * **只要窗口大小发生像素变化，就会触发这个事件，我们经常利用这个事件完成响应式布局，如屏幕窗口变小的时候，隐藏部分盒子**
  * window.innerWidth属性是当前屏幕的宽度

#### 定时器

##### setTimeout定时器

回调函数，功能是在指定的延时后进行执行，语法，例：

```js
window.setTimeout(function(){},2000);
// 可以给定时器起名字，例：
var timer = setTimeout(function(){},2000);
// * 第一个参数是调用函数，也可以在这里写函数名，把函数的定义写在setTimeout函数之外
// * window可以省略，可以直接setTimeout(function(){},2000)这种形式调用
// * 第二个参数是函数执行的延时，单位是毫秒，也可以省略，省略表示0
```

##### clearTimeout清除定时器

取消指定定时器的触发，语法，例：

```js
var timer = setTimeout(funtion(){},2000);
window.clearTimeout(timer);
// window可省略，直接用clearTimeout(timer)的形式
// clearTimeout的参数timer是指定定时器的名字
```



##### setInterval循环定时

循环执行定时函数，每隔一次延时时间就调用一次回调函数，例：

```js
window.setInterval(function(){},2000);
// 可以给定时器起名字，例：
var timer = setInterval(function(){},2000);
// * 第一个参数是调用函数，也可以在这里写函数名，把函数的定义写在setTimeout函数之外
// * window可以省略，可以直接setInterval(function(){},2000)这种形式调用
// * 第二个参数是函数执行的延时，单位是毫秒，也可以省略，省略表示0
```



  * 倒计时案例：

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>倒计时的制作</title>
        <style>
            .timer {
                width: 400px;
                height: 70px;
                margin: 200px auto;
            }
    
            /* 数字块的颜色大小 */
            span {
                display: inline-block;
                /* width: 50px;
                height: 50px; */
                padding: 10px 10px;
                line-height: 50px;
                background-color: black;
                color: aliceblue;
                font-size: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    
    <body>
        <div class="timer">
            倒计时：
            <span class="day"></span>天
            <span class="hour"></span>时
            <span class="minute"></span>分
            <span class="second"></span>秒
        </div>
    
        <script>
            var day = document.querySelector('.day');
            var hour = document.querySelector('.hour');
            var minute = document.querySelector('.minute');
            var second = document.querySelector('.second');
    
            // 倒计时效果
            var inputTime = +new Date('2021-9-5 00:00:00');
            function countDown(time) {
                // 现在总的毫秒数
                var nowTime = +new Date();
                var times = (inputTime - nowTime) / 1000;
                // 倒计时天数
                var days = parseInt(times / 60 / 60 / 24);
                // 格式化操作
                day.innerHTML = days < 10 ? '0' + days : days;
                var hours = parseInt(times / 60 / 60 % 24);
                hour.innerHTML = hours < 10 ? '0' + hours : hours;
                var minutes = parseInt(times / 60 % 60);
                minute.innerHTML = minutes < 10 ? '0' + minutes : minutes;
                var seconds = parseInt(times % 60);
                second.innerHTML = seconds < 10 ? '0' + seconds : seconds;
                // return day + '天' + hours + '时' + minutes + '分' + seconds + '秒';
            }
            // 先执行一遍倒计时函数，避免刷新之后时间还停留在默认设置
            countDown();
            // 每个1s刷新一次倒计时
            setInterval(countDown, 1000);
        </script>
    </body>
    
    </html>
    ```

    

##### clearInterval清除定时器

清除setInterval定时器函数，例：

```js
var timer = setInterval(function(){},1000);
clearInterval(t);
```



##### this指向问题

* 全局作用域或一般函数中，this都指向window对象
* 方法调用中，谁调用了this，就指向谁
* 构造函数中，this指向构造函数的示例化对象

#### JS执行机制

JS原先是单线程，因此会造成因一个部分执行时间过长，导致后面的代码长时间不能执行，为解决此问题，利用多核CPU的计算能力，HTML5提出Web Worker标准，允许JS脚本创建多个线程，于是出现了同步和异步

* 同步：程序的执行顺序和任务的排列顺序一致
* 异步：同时做多件事

JS将所有任务分为同步任务和异步任务

同步任务：都在主线程上执行， 形成一个执行栈

异步任务：通过回调函数实现，一般而言包含一下三类：

* 普通事件，如click，resize等
* 资源加载，如load，error等
* 定时器，包含setInterval，setTimeout等

执行的具体过程：

1. 先执行执行栈中的同步任务
2. 将执行栈中的异步任务（回调函数），放入任务队列中
3. 当执行栈中的所有同步任务完成后，系统按照次序读取任务队列中的异步任务放在执行栈中开始执行

在这个过程中主线程不断地接受任务和执行任务，这个过程称为**事件循环**

#### location对象

window对象提供了一个location属性，用于获取或设置窗体地URL，可用于解析URL，因为这个属性返回的是一个对象，因此这个属性也称location对象

* URL：统一资源定位符（Uniform Resource Locator，URL）是互联网上标准资源地地址，互联网上每个资源都有唯一URL，其中包含信息指出文件地存储位置和浏览器应如何处理它

* URL一般语法格式

  ```html
  protocol://host[:port]/path/[?query]#fragment
  ```

  其中参数地含义：

  * protocol：所采用的通信协议，常用的由http，ftp，maito等
  * host：主机（域名），例：www.baidu.com
  * port：端口号，可省略，省略表示默认的端口号，http中默认端口号是80
  * path：路径，一般表示主机上的一个目录或 文件地址
  * ?query：参数，以键值对的形式通过&符号分隔
  * fragment：片段，#后面内容常见于链接、锚点

* 例：

  ```markdown
  http://www.itcast.cn/index.html?name=andy&age=18#link
  ```

  

* Location对象的属性：

  * location.href，获取URL和修改URL，利用此属性结合定时器可实现定时跳转页面的功能
  * location.host，获取主机（域名）
  * location.port，返回端口号，如果采用默认端口号，返回空字符串
  * location.pathname，返回路径
  * location.search，返回参数
  * location.hash，返回片段

* location对象的方法：

  * location.assign()，跟href一样能实现跳转页面（也成为重定向页面），同时它还能记录浏览历史，因此可以实现后退功能，用法，例：

    ```js
    location.assign('http://www.baidu.com');
    ```

  * location.replace()，功能和location.assign()一样，区别在于这个不记录历史，不能实现后退功能

  * location.reload()，重新加载页面，相当于刷新按钮或者按下F5的效果，如果其中参数为true，则表示强制刷新（相当于Ctrl+F5）

#### navigator对象

navigatior对象包含有关浏览器的信息，含有很多属性，常用的是userAgent属性，该属性可以返回由客户机发送浏览器的user-agent头部的值

下面前端代码可以判断用户使用哪个终端打开页面，实现跳转

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JS代码测试</title>
</head>

<body>


    <script>
        if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
            // 手机端
            window.location.href = "";
        } else {
            // 电脑端
            window.location.href = "";
        }
    </script>
</body>

</html>
```



#### history对象

* history.forward()方法，页面前进

* history.back()方法，页面后退，变成刚才浏览的页面

* history.go()方法，参数是前进的步数，例：

  ```js
  history.go(1);
  // 这个代码相当于history.forward()方法
  ```

  

2


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

* setTimeout回调函数，功能是在指定的延时后进行执行，语法，例：

```js
window.setTimeout(function(){},2000);
// 可以给定时器起名字，例：
var timer = setTimeout(function(){},2000);
// * 第一个参数是调用函数，也可以在这里写函数名，把函数的定义写在setTimeout函数之外
// * window可以省略，可以直接setTimeout(function(){},2000)这种形式调用
// * 第二个参数是函数执行的延时，单位是毫秒，也可以省略，省略表示0
```

  * clearTimeout清除定时器方法，取消指定定时器的触发，语法，例：

    ```js
    var timer = setTimeout(funtion(){},2000);
    window.clearTimeout(timer);
    // window可省略，直接用clearTimeout(timer)的形式
    // clearTimeout的参数timer是指定定时器的名字
    ```

    

  * setInterval循环执行定时函数，每隔一次延时时间就调用一次回调函数，例：

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

* clearInterval，清除setInterval定时器函数，例：

  ```js
  var timer = setInterval(function(){},1000);
  clearInterval(t);
  ```

  



#### JS执行机制

#### location对象

#### navigator对象

#### history对象


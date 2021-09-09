# PC端网页特效

## 元素偏移量offset系列

相关属性可以***动态***得到该元素的位置（偏移），大小等

* 获得元素距离带有定位的父元素的位置
* 获得元素自身大小（宽度高度）
* **注意：返回的数值都不带单位**

### 常用属性

* element.offsetParent，返回元素带有定位的父级元素，如果父级都没有定位，则返回body

* element.offsetTop，返回元素相对带有定位的父元素顶部的偏移，如果没有父元素就认为父元素是body
* element.offsetLeft，返回元素相对带有定位的父元素左边界的偏移，如果没有父元素就认为父元素是body
* element.offsetWidth，返回自身包括padding，边框，内容区的宽度，返回的数值是不带单位的
* element.offsetHeight，返回自身包含padding，边框，内容区的高度，返回的数值是不带单位的

### offset与style的区别

* offset可以得到任意样式表（内嵌式，行内式，链接式样式表都可以）中的样式值，style只能得到行内样式中的样式值
* offset系列获取的数值是没有单位的，通过style获取的是带有单位的字符串
* offsetWidth获取的是包含padding+border+width的大小，而style.width获取的只是width的大小
* offsetWidth等属性获取的值只有只读属性，不能进行修改赋值，但是style获取的值可以进行赋值修改
* 因此，想要获取元素大小，用offset更好，想修改元素大小，使用style更好

## 元素可视区client系列

client翻译过来就是客户端，我们使用client系列的相关属性来获取元素可视区的相关信息。

通过client系列的相关属性可以动态的得到该元素的边框大小、元素大小等。

### client系列属性：

* element.clientTop
  返回元素上边框的大小
* element.clientLeft
  返回元素左边框的大小
* element.clientWidth
  返回自身包括padding 、内容区的宽度，***不含边框，返回数值不带单位***
* element.clientHeight
  返回自身包括padding 、内容区的高度，***不含边框，返回数值不带单位***

### 立即执行函数

不需要调用，立马能够自己执行的函数

两种写法：

```js
// 第一种写法,方法名fn可省略，参数放在最后面的括号内
(function fn(){})(1);
// 第二种写法，方法名fn可省略，参数放在大括号后的括号内
(function fn(){}(1));
```

立即执行函数最大的作用就是独立创建了一个作用域，里面所有的变量都是局部变量不会有命名冲突的情况

### load事件与pageshow事件的区别

* 下面三种情况都会刷新页面都会触发load事件。
  1. a标签的超链接
  2. F5或者刷新按钮(强制刷新)
  3. 前进后退按钮
* 但是火狐中，有个特点，有个“往返缓存”，这个缓存中不仅保存着页面数据，还保存了DOM和JavaScript的状态;实际上是将整个页面都保存在了内存里。所以如果使用load事件，此时后退按钮不能刷新页面。
* 此时可以使用pageshow事件来触发。，这个事件在页面显示时触发，无论页面是否来自缓存。
* 在重新加载页面中，pageshow会在load事件触发后触发；根据事件对象中的persisted来判断是否是缓存中的页面触发的pageshow事件，注意这个事件给window添加。
* pageshow相对于load适用于更多的浏览器

## 元素滚动scroll系列

scroll翻译过来就是滚动的，我们使用scroll系列的相关属性可以动态的得到该元素的大小、滚动距离等，主要是和页面的滚动条有关。

### scroll属性

* element.scrollTop
  返回被卷去的上侧距离，返回数值不带单位
* element.scrollLeft
  返回被卷去的左侧距离，返回数值不带单位
* element.scrollWidth
  返回自身实际的宽度，不含边框，返回数值不带单位
* element.scrollHeight
  返回自身实际的高度，不含边框，返回数值不带单位
* 拿带有滚动条的文本框来理解，文本框中的文字超出了容器的大小，把超出部分用滚动条的形式显示，scrollTop就是滚动条向下拉到最低端时，文字内容向上隐藏的部分的高度，scrollLeft是滚动条向右拉到最右端时，文字内容向左隐藏的部分的高度，scrollWidth是整个文本内容的宽度，scrollHeight是整个文本内容的高度
* 页面被卷去的头部：可以通过window.pageYoffset获得
* 页面被卷去的左侧：可以通过window.pageXOffset获得

### scroll滚动事件

当滚动条发生变化时触发，一下例子IE9+支持,语法，例：

```js
// 调用方法1
element.addEventListener('scroll',function(){});
// 方法2
element.onscroll = function(){};
```

### 滚动条效果制作案例

```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>侧边栏返回顶部</title>
    <style>
        .w {
            width: 1200px;
            margin: 0px auto;
            text-align: center;
        }

        .scrollbar {
            position: absolute;
            right: 20px;
            top: 300px;
            width: 50px;
            height: 100px;
            background-color: aquamarine;
        }

        .backtop {
            display: none;
            width: 100%;
            height: 50%;
            background-color: greenyellow;
        }

        .header {
            height: 200px;
            background-color: burlywood;
        }

        .banner {
            height: 200px;
            background-color: chartreuse;
        }

        .main {
            height: 1800px;
            background-color: darkorange;
        }
    </style>
</head>

<body>
    <div class="scrollbar">
        <a href="#">
            <div class="backtop">返回顶部</div>
        </a>

    </div>
    <div class="header w">头部</div>
    <div class="banner w">banner区域</div>
    <div class="main w">主体部分</div>

    <script>
        var scrollbar = document.querySelector('.scrollbar');
        var banner = document.querySelector('.banner');
        var main = document.querySelector('.main');
        var backtop = document.querySelector('.backtop');
        var bannerTop = banner.offsetTop;
        var mainTop = main.offsetTop;
        var scrollbarTop = scrollbar.offsetTop - bannerTop;
        document.addEventListener('scroll', function () {
            // 滚动条设置
            if (window.pageYOffset > bannerTop) {
                scrollbar.style.position = 'fixed';
                scrollbar.style.top = scrollbarTop + 'px';
            } else {
                scrollbar.style.position = 'absolute';
                scrollbar.style.top = 300 + 'px';

            }
            // 页面滚动到main时显示返回顶部的模块
            if (window.pageYOffset > mainTop) {
                backtop.style.display = 'block';
            } else {
                backtop.style.display = 'none';
            }
        })
    </script>
</body>

</html>
```

## 三大系列的联系

### 三个属性的差异

* element.offsetWidth
  返回自身包括padding 、边框、内容区的宽度，返回数值不带单位
* element.clientWidth
  返回自身包括padding 、内容区的宽度，不含边框，返回数值不带单位
* element.scrollWidth
  返回自身实际的宽度，不含边框，返回数值不带单位

### 他们主要用法:

* offset系列经常用于获得元素位置offsetLeft、offsetTop 
* client经常用于获取元素大小clientWidth、clientHeight
* scroll经常用于获取滚动距离 scrollTop、scrollLeft
* **注意页面滚动的距离通过window.pageXoffset获得**

## 动画函数封装

### 简单的动画函数封装

例：

```js
var first = document.querySelector('.first');
var second = document.querySelector('.second');
// 简单的动画函数封装，传参
function animate(obj, position) {
    var timer = setInterval(function () {
        obj.style.left = obj.offsetLeft + 3 + 'px';
        // 移动到三百像素的位置停止
        if (obj.offsetLeft >= position) {
            clearInterval(timer);
        }
    }, 20)
    }
// 动画函数的调用
animate(first, 200);
animate(second, 300);
```

对上面代码的改进优化：

```js
var first = document.querySelector('.first');
var second = document.querySelector('.second');
function animate(obj, position) {
    // 首先进行清除定时器的操作，防止对象本身带着定时器，多个定时器引起bug
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        obj.style.left = obj.offsetLeft + 3 + 'px';
        // 移动到三百像素的位置停止
        if (obj.offsetLeft >= position) {
            clearInterval(obj.timer);
        }
    }, 20)
}
animate(first, 200);
animate(second, 300);
```

### 缓冲动画和线性动画的对比

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>缓冲动画与线性动画的差异</title>
    <style>
        .first {
            position: absolute;
            left: 0px;
            top: 0px;
            width: 100px;
            height: 100px;
            background-color: gold;
        }

        .second {
            position: absolute;
            left: 0px;
            top: 120px;
            width: 100px;
            height: 100px;
            background-color: greenyellow;
        }
    </style>
</head>

<body>
    <div class="first"></div>
    <div class="second"></div>
    <script>
        var first = document.querySelector('.first');
        var second = document.querySelector('.second');
        function animateCurve(obj, position) {
            // 首先进行清除定时器的操作，防止对象本身带着定时器，多个定时器引起bug
            clearInterval(obj.timer);
            obj.timer = setInterval(function () {
                // 缓冲动画的步长不是固定不变的，是根据目的点与当前位置进行计算，是动态改变的
                obj.style.left = obj.offsetLeft + Math.ceil((position - obj.offsetLeft) / 10) + 'px';
                // 移动到指定位置停止
                if (obj.offsetLeft >= position) {
                    clearInterval(obj.timer);
                }
            }, 30)
        }
        function animateLinear(obj, position) {
            // 首先进行清除定时器的操作，防止对象本身带着定时器，多个定时器引起bug
            clearInterval(obj.timer);
            obj.timer = setInterval(function () {
                obj.style.left = obj.offsetLeft + 5 + 'px';
                // 移动到指定像素的位置停止
                if (obj.offsetLeft >= position) {
                    obj.style.left = position+'px';
                    clearInterval(obj.timer);
                }
            }, 30)
        }
        animateLinear(first, 500);
        animateCurve(second, 500);

    </script>
</body>

</html>
```

### 缓冲动画实现两个位置移动案例

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>缓冲动画在两个物体间移动</title>
    <style>
        .first {
            display: block;
            position: absolute;
            left: 0px;
            top: 100px;
            width: 100px;
            height: 100px;
            background-color: gold;
        }
    </style>
</head>

<body>
    <span class="first"></span>
    <button class="go">前进</button>
    <button class="back">返回</button>
    <script>
        // 缓冲移动动画定义
        function animateCurve(obj, position) {
            // 首先进行清除定时器的操作，防止对象本身带着定时器，多个定时器引起bug
            clearInterval(obj.timer);
            obj.timer = setInterval(function () {
                var step = (position - obj.offsetLeft) / 10;
                step = step > 0 ? Math.ceil(step) : Math.floor(step);
                // 缓冲动画的步长不是固定不变的，是根据目的点与当前位置进行计算，是动态改变的
                obj.style.left = obj.offsetLeft + step + 'px';
                // 移动到指定位置停止
                if (obj.offsetLeft == position) {
                    clearInterval(obj.timer);
                }
            }, 15)
        }
        var first = document.querySelector('.first');
        var go = document.querySelector('.go');
        var back = document.querySelector('.back');

        go.addEventListener('click', function () {
            animateCurve(first, 500);
        });
        back.addEventListener('click', function () {
            animateCurve(first, 0);
        });

    </script>
</body>

</html>
```



### 回调函数的使用

回调函数名当作定时器的参数传进定时器，回调函数的调用放在定时器结束的位置，以函数名()的方式进行调用

## 常见网页特效案例

### 轮播图案例

#### 节流阀的使用

##### 目的

能防止轮播图点击切换的太快

##### 实现思路

利用回调函数，添加一个控制变量，负责锁住函数和解开函数，用在动画函数的定义中，能起到动画播放完毕才解锁下一个操作的作用


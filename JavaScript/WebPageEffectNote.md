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
```



## 动画函数封装

## 常见网页特效案例


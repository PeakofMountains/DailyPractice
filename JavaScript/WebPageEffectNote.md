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

## 元素滚动scroll系列

## 动画函数封装

## 常见网页特效案例


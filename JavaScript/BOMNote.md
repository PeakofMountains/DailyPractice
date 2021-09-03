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

    

#### 定时器
#### JS执行机制

#### location对象

#### navigator对象

#### history对象


### DOM

文档对象模型（Document Object Model，简称DOM），是W3C组织土建的处理HTML或XML的标准编程接口

W3C已经定义了一系列的DOM接口，通过这些DOM接口可以改变网络的内容、结构和样式

* DOM树
  * 文档：一个页面就是一个文档，DOM中使用document表示
  * 元素：页面中所有标签都是元素，DOM中使用element表示
  * 节点：网页中所有内容都是节点（标签、属性、文本、注释等），DOM中使用node表示
  * DOM把以上内容都看作对象

#### Web APIs 和 JS基础关联性

JS基础学习ECMAScript基础语法，为后面做铺垫，Web APIs是JS的应用，大量使用JS基础语法做交互效果

#### API

Application Programming Interface应用程序编程接口，简称API，是一些预先定义的函数，是给程序员提供的一种工具，一遍轻松完成功能

#### Web API

Web API 是浏览器提供的一套操作浏览器功能（BOM）和页面元素的API(DOM)

Web API一般都有输入和输出（函数的传参和返回值），Web API 很多都是函数方法

[MDN详细API](https://developer.mozilla.org/zh-CN/docs/Web/API)

#### DOM获取元素

* 由于JS是从上向下执行，因此script标签应该写在body标签的尾部

* 根据ID获取，使用getElementById()方法，返回匹配ID的元素，参数是大小写敏感的ID，返回的是一个元素对象，例：

  ```js
  var mytime = document.getElementById('time');
  ```

  

* 根据标签Tag获取某个元素(父元素)内部所有指定标签名的子元素，返回的是获取元素对象的集合，以伪数组的形式存储，因此可以通过 object[1] 的方式访问对象，注意父元素必须是单个对象(必须指明是哪一个元素对象).获取的时候不包括父元素自己。例：

  ```js
  var lis = document.getElementsByTagName('li');
  ```

  

* 可以根据类名获取，例：

  ```js
  var boxes = document.getElementsByClassName('box')
  ```

  

* 返回指定选择器的第一个对象，例：

  ```js
  // 注意选择器前需加对应符号
  var firstbox = document.querySelector('.box');
  var nav = document.querySelector('#nav');
  ```

  

* 返回指定选择器的所有元素对象集合，例：

  ```js
  var allbox = document.querySelectorAll('.box');
  ```

  

* 获取body元素，例：

  ```js
  var bodyEle = document.body;
  ```

  

* 获取html元素，例：

  ```js
  var htmlEle = document.documentElement;
  ```



#### 事件三要素

* 事件是有三部分组成：事件源、事件类型、事件处理程序，我们也称为事件三要素

  * 事件源：事件被触发的对象

  * 事件类型：如何触发，什么事件，比如鼠标点击(onclick)，还是鼠标经过，还是键盘按下

  * 事件处理程序：通过一个函数赋值的方式完成

  * 使用过程，例：

    ```html
    <body>    
        <!-- 使用ID获取元素 -->
        <button id="btn">button</button>
        <script>
            // 获取事件源
            var btn = document.getElementById('btn');
            // 绑定事件，添加事件处理程序
            btn.onclick = function () {
                alert('托尔');
            }
        </script>
    </body>
    ```

    

#### 鼠标事件

* click 鼠标点击左键触发
* mouseover 鼠标经过触发
* mouseenter鼠标经过触发，当鼠标移动到元素上时就会触发mouseenter事件，类似mouseover
  * ***它们两者之间的差别是：mouseover鼠标经过自身盒子会触发一次，经过子盒子还会触发一次。mouseenter只会经过自身盒子触发之所以这样，就是因为mouseenter不会冒泡***
* mouseout 鼠标离开触发
* mouseleave鼠标离开触发，类似mouseover和mouseenter的差别，mouseleave也是不会冒泡
* focus 获得鼠标焦点触发
* blur 失去鼠标焦点触发
* mousemove 鼠标移动触发
* mouseup 鼠标弹起触发
* mousedown 鼠标按下触发



#### 操作元素之改变元素内容

例：

```js
var div = document.querySelector('div');
div.innerText = 'changeText';
```



```js
var div = document.querySelector('div');
div.innerHTML = 'changeText';
```

这两种方式的区别：

* innerText不识别html标签，非标准，去除空格和换行
* innerHTML 识别html标签，是W3C标准，保留空格和换行的

这两个属性都是可以读写的，因此可以当作一个值使用，例：

```js
var text = div.innerHTML;
```

#### 操作元素之修改元素属性

例：

```js
var img = document.querySelector('img');
img.src = 'image/1.jpg';
img.title = 'Test';
```

#### 操作元素之表单属性修改

例：

```js
var btn = document.querySelector('button');
var input = document.querySelector('input');
btn.onclick = function(){
    // 修改输入框的显示内容
    input.value = '康娜';
    // 禁用按钮，这里使用了this用法，因为调用者是btn，因此this就代指的btn
    this.disable = true;    
}

```

示例：

```js
// 密码框的做法
// 1. 获取元素
var eye = document.getElementById('eye');
var pwd = document.getElementById('psw');
// 2.注册事件，定义处理程序
var flag = 0;
// flag = 0 表示为明文显示
eye.onclick = function () {
    if (flag == 0) {
        pwd.type = 'text';
        eye.src = 'image/open.jpg';
        flag = 1;
    }
    else {
        // 密码显示的时候将显示框类型调整为密码框
        pwd.type = 'password';
        eye.src = 'image/close.jpg';
        flag = 0;
    }
}
```

#### 操作元素之修改样式属性

例：

```js
// 方法1：利用.style方式
var div = document.querySelector('div');
div.style.width = '250px';
// style样式属性应该使用驼峰命名法，例如：fontSize、backgroundColor等
// 利用JS修改style样式操作，产生的是行内样式css权重比较高
```

```js
// 方法2：利用操作类名方式
// -------------在css中定义类-------------
.change {
    fontsize = 14px;
    color = skyblue;
}
// ------------在JS中修改类名-------------
var div = document.querySelector('div');
div.className = 'change';
// 适用于样式修改较多的情形
// 因为class是保留字，因此通过className来操作元素类名属性
// className会直接覆盖掉原来的类名
// 假如原来的div还有一个类名为first的类，此时想保留first类，希望他不被覆盖掉，则可以用下面的写法
div.className = 'first change';
```

#### 排他思想算法

```js
// 排他思想算法
// 获取按钮元素
var bnts = document.getElementsByTagName('button');
// btns得到的是伪数组
for (var i = 0; i < bnts.length; i++) {
    bnts[i].onclick = function () {
        // 先将所有的背景颜色设为空
        for (var i = 0; i < bnts.length; i++) {
            bnts[i].style.backgroundColor = '';
        }
        // 将当前背景颜色设为指定颜色
        this.style.backgroundColor = 'yellow';
    }
}
```



#### 全选框的设计

```js
// 全选框的设计
// 全选功能实现：复选框跟随全选按钮的checked属性
// 1. 获取元素,j_cbAll为全选按钮，j_tbs为复选框
var j_cbAll = document.getElementById('j_cbAll');
var j_tbs = document.getElementById('j_tb').getElementsByTagName('input');
// 2. 注册事件
j_cbAll.onclick = function () {
    for (var i = 0; i < j_tbs.length; i++) {
        j_tbs[i].checked = this.checked;
    }
}
// 给所有的复选框绑定事件
for (var i = 0; i < j_tbs.length; i++) {
    j_tbs[i].onclick = function () {
        // 设置标志变量控制全选按钮是否选中
        var flag = true;
        for (var i = 0; i < j_tbs.length; i++) {
            if (!j_tbs[i].checked) {
                flag = false;
                break;
            }
        }
        j_cbAll.checked = flag;
    }
}
```



#### 自定义属性的操作

* 得到属性值的方法：

  * element.属性 ，获取内置属性值（元素自带的属性值）

  * element.getAttribute('属性')，主要获取自定义属性的属性值（程序员自定义的属性）

* 修改属性值的方法：

  * element.属性 = '值'
  * element.setAttribute('属性'，'值');

#### H5新增的自定义属性的方法

* 规定自定义属性的名字必须是以`data-`开头的

* H5规定将所有以data-开头的自定义属性都放在dataset这样一个集合中，因此在访问的时候可以把自定义属性当成对象dataset的属性进行使用，例：

  

  ```html
  <body>
      <div data-index="1">我是康娜</div>
      <script>
          var div = document.querySelector('div');
          console.log(div.dataset.index);
      </script>
  </body>
  ```

  

* 如果自定义属性的名字是以data-开头，而且包含多个`-`连接的单词，则采用驼峰命名法进行使用，例：

  ```html
  <body>
      <div data-list-name="kangna">我是康娜</div>
      <script>
          var div = document.querySelector('div');
          console.log(div.dataset.listName);
      </script>
  </body>
  ```

  

#### 节点操作

* 原因：之前学到的用DOM提供的方法获取元素的方法逻辑性不强，繁琐，因此这里学习另一种操作元素的方法——节点操作，根据元素在元素树中的父子，兄弟节点关系获取元素，逻辑性强，但是兼容性较差

* 一般地，节点至少拥有nodeType(节点类型 ) 、nodeName (节点名称）和nodeValue (节点值)这三个基本属性。

  * 元素节点nodeType为1
  * 属性节点nodeType为2
  * 文本节点nodeType为3(文本节点包含文字、空格、换行等)
  * 我们在实际开发中，节点操作主要操作的是元素节点

* 父节点，例：

  ```js
  // 父节点操作,查找的是离元素最近的父亲节点，否则返回null
  var div = document.querySelector('div');
  console.log(div.parentNode);
  ```

  

* 子节点，例：

  ```js
  var div = document.querySelector('div');
  // 方法1
  console.log(div.childNodes);
  // 不提倡使用此方法，因为此方法返回指定节点的所有子节点的集合，包含元素节点、文本节点等
  // 如果只是想返回元素节点，就需要专门处理，设置一个函数，在其中对childNodes节点集合进行遍历
  // 用nodeType属性查看节点是否为元素节点，将元素节点返回
  
  // 方法2
  console.log(div.children);
  // 获取指定节点的所有子元素节点，也是实际开发中常用的
  ```

* 关于获取第一个子节点和最后一个子节点

  ```js
  var ol = document.queryselector('ol');
  // 1. firstchild第一个子节点不管是文本节点还是元素节点 
  console.log(ol.firstchild);
  console.log(ol.lastchild);
  // 2. firstElementchild返回第一个子元素节点
  console.log(ol.firstElementChild);
  console.log(ol.lastElementchild);
  // 3．实际开发的写法既没有兼容性问题又返回第一个子元素
  console.log(ol.children[0]);
  console.log(ol.children[ol.children.length - 1]);
  ```

  

* 兄弟节点，例：

  ```js
  // 兄弟节点操作
  var div = document.querySelector('div');
  // 1. 方法1, 得到下一个或前一个兄弟节点，包含元素节点或文本节点等
  console.log(div.nextSibling);
  console.log(div.previousSibling);
  // 2. 方法2，得到下一个或前一个兄弟元素节点，只包含元素节点
  console.log(div.nextElementSibling);
  console.log(div.previousElementSibling);
  ```

####  创建和添加元素节点

动态添加元素的方式分为两步：1. 创建元素 2. 将元素添加至指定位置，例：

```js
// 获取父元素
var ul = document.querySelector('ul');
// 动态创建和添加元素节点
var li = document.createElement('li');
// 将li插入到ul的子元素的末尾
ul.appendChild(li);
var newli = document.createElement('li');
// 将newli插入到ul第一个子元素的前面
ul.insertBefore(newli, ul.children[0]);
```



#### 删除节点

从父节点中删除指定子节点，例：

```js
// 从父节点中删除子节点
var fatherNode = document.querySelector('ul');
var sunNode = document.querySelectorAll('li');
// 从父节点出发删除子节点
// 1. 可以通过父节点获取子节点
fatherNode.removeChild(fatherNode.children[0]);
// 2. 可以通过直接元素获取的方式获取子节点
fatherNode.removeChild(sunNode[1]);
```

#### 拷贝节点

分为带着标签内容一起拷贝和只拷贝标签两种形式，例

```js
var ul = document.querySelector('ul');
// cloneNode()的参数为空或者为false时只拷贝标签，不拷贝标签中内容
var li1 = ul.children[0].cloneNode();
ul.appendChild(li1);
// cloneNode()的参数为true时拷贝标签的同时，也会将标签内容拷贝
var li2 = ul.children[0].cloneNode(true);
ul.appendChild(li2);
```

#### 动态生成表格案例

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>动态生成表格</title>

    <!-- css样式部分 -->
    <style>
        table {
            width: 500px;
            margin: 100px auto;
            border-collapse: collapse;
            text-align: center;
        }

        td,
        th {
            border: 1px solid #333;
        }

        thead tr {
            height: 40px;
            background-color: #ccc;
        }
    </style>
</head>

<body>
    <table cellspacing="0">
        <!-- 表头部分 -->
        <thead>
            <tr>
                <th>姓名</th>
                <th>科目</th>
                <th>成绩</th>
                <th>操作</th>
            </tr>
        </thead>
        <!-- 主体部分，数据内容 -->
        <tbody>

        </tbody>
    </table>
    <script>
        var data = [
            {
                name: '鸣人',
                subject: 'JavaScript',
                score: 100
            },
            {
                name: '佐助',
                subject: 'JavaScript',
                score: 99
            },
            {
                name: '小樱',
                subject: 'JavaScript',
                score: 98
            }
        ]
        var tbody = document.querySelector('tbody');
        for (var i = 0; i < data.length; i++) {
            // 根据人数创建行
            var tr = document.createElement('tr');
            tbody.appendChild(tr);
            // 在单元行中根据数据的属性个数创建数据单元格
            for (var k in data[i]) {
                var td = document.createElement('td');
                tr.appendChild(td);
                // 将内容赋值给单元格,data[i][k]得到属性值
                td.innerHTML = data[i][k];
            }
            // 在单元行中创建删除选项的单元格
            var td = document.createElement('td');
            // 将删除选项单元格进行规格化，这种形式比较固定，都是用来设置删除选项的统一格式
            td.innerHTML = '<a href = "javascript:;">删除</a>'
            tr.appendChild(td);
        }
        // 定义删除操作
        var a = document.querySelectorAll('a');
        for (var i = 0; i < a.length; i++) {
            a[i].onclick = function () {
                tbody.removeChild(this.parentNode.parentNode);
            }
        }
    </script>
</body>

</html>
```

#### 创建元素的三种方式

```js
// 创建元素的三种方式
// 1. 直接将内容写入页面的内容流，但是文档流执行完毕会导致页面全部重绘
document.write();
// 2. 将内容写入DOM节点，不会导致页面重绘，而且创建多个元素时效率较高（不要采取拼接字符串的形式，采取数组形式拼接），结构稍复杂
element.innerHTML
// 3. 创建多个元素效率稍低，但是结构清晰
document.createElement()
// 不同的浏览器下innerHTML方法总比createElement()f
```

#### 获取查询DOM元素方式

* DOM提供的API方法: getElementByld、getElementsByTagName  古老用法不太推荐
* H5提供的新方法:querySelector、querySelectorAll  提倡
* 利用节点操作获取元素∶父(parentNode)、子(children)、兄(previousElementSibling，
  nextElementSibling)  提倡

#### 注册事件

给元素添加事件，称为注册事件或者绑定事件。注册事件有两种方式︰传统方式和方法监听注册方式，

* 传统方式，例：

```js
var button = document.querySelector('button');
button.onclick = function(){}
```

​	特点∶注册事件的唯一性
​	**同一个元素同一个事件只能设置一个处理函数，最后注册的处理函数将会覆盖前面注册的处理函数**

* 方法监听注册方式addEventListener()

  * w3c标准推荐方法
  * addEventListener()它是一个方法
  * IE9之前的E不支持此方法，可使用attachEvent()代替
  * 特点:同一个元素同一个事件可以注册多个监听器，按注册顺序依次执行

  语法，例：

  ```js
  // 可以给同一个事件注册多个监听器，按注册顺序依次执行
  var button = document.querySelector('button');
  button.addEventListener('click', function () {
      alert('click1');
  })
  button.addEventListener('click', function () {
      alert('click2');
  })
  // addEventListener()函数的第一个参数是事件类型，要用引号引起来，第二个参数是处理函数，用function定义，第三个参数默认是false，有关DOM事件流
  ```

  

  #### 删除注册事件的两种方式

  传统方式和使用removeEventListener()方式，例：

  ```js
  // 删除事件
  var button = document.querySelector('button');
  // // 传统删除事件方式
  // button.onclick = function () {
  //     alert('传统删除方式');
  //     button.onclick = null;
  //     此种方式使得此注册函数只执行一遍
  // }
  
  // 用removeEventListener()函数删除方式
  button.addEventListener('click', fn);
  function fn() {
      alert('removeEventListener方式删除事件');
      button.removeEventListener('click', fn);
      // 此操作让注册函数只执行一次
  }
  ```

#### DOM事件流

事件流描述的是从页面中接收事件的顺序。
事件发生时会在元素节点之间按照特定的顺序传播，这个传播过程即DOM事件流。

DOM事件流分为3个阶段∶

1. 捕获阶段
2. 当前目标阶段
3. 冒泡阶段

* 事件冒泡∶IE最早提出，事件开始时由最具体的元素接收，然后逐级向上传播到到DOM最顶层节点的过程。
* 事件捕获∶网景最早提出，由DOM最顶层节点开始，然后逐级向下传播到到最具体的元素接收的过程。

**JS代码中只能执行捕获或者冒泡其中的一个阶段**

onclick()和attachEvent()只能捕获冒泡阶段

如果addEventListener()的第三个参数是 true，则处于捕获阶段，默认为false，捕获冒泡阶段，例：

```js
// father为父盒子，son为子盒子
var father = document.querySelector('.father');
var son = document.querySelector('.son');
// 第三个参数为true，则为捕获阶段，那多个监听函数的顺序就是father的监听函数先执行，再执行son的监听函数
// 第三个参数为默认false，则为冒泡阶段，那多个监听函数的顺序就是son的监听函数先执行，再执行father的监听函数
father.addEventListener('click', function () {
    alert('father');
}, true)
son.addEventListener('click', function () {
    alert('son');
}, true)
```

* 实际开发中我们很少使用事件捕获，我们更关注事件冒泡。
* 有些事件是没有冒泡的，比如onblur、onfocus、onmouseenter、onmouseleave
* 事件冒泡有时候会带来麻烦，有时候又会帮助很巧妙的做某些事件

#### 事件对象

官方解释：event对象代表事件的状态，比如键盘按键的状态、鼠标的位置、鼠标按钮的状态。
简单理解：事件发生后，跟事件相关的一系列信息数据的集合都放到这个对象里面，这个对象就是事件对象event ，它有很多属性和方法。例：

```js
var div = document.querySelector('div');
div.onclick = function(event){}
// 其中event就是事件对象
```

* event 就是一个事件对象写到我们侦听函数的小括号里面当形参来看

* 事件对象只有有了事件才会存在，它是系统给我们自动创建的，不需要我们传递参数

* 事件对象是我们事件的一系列相关数据的集合跟事件相关的，比如鼠标点击里面就包含了鼠标的相关信息，鼠标坐标啊，如果是键盘事件里面就包含的键盘事件的信息比如判断用户按下了那个键

* 这个事件对象我们可以自己命名比如event 、evt、e

* event.target返回触发事件的对象，与this是不同的，this返回的是绑定事件的对象，例：

  ```js
  // event.target与this的区别
  var ul = document.querySelector('ul');
  ul.addEventListener('click', function (e) {
      console.log(e.target);
      console.log(this);
  })
  // 点击li发现e.target输出的是li对象，this输出的是ul对象，因为触发响应的是li，监听器绑定的是ul
  ```

  

* event.type返回事件的类型，比如click等

* event.preventDefault();方法，阻止默认行为或事件，例：

  ```js
  // 阻止默认行为或事件
  var a = document.querySelector('a');
  a.addEventListener('click', function (e) {
      e.preventDefault();
  })
  ```

  

#### 阻止冒泡的两种方式

```js
// 阻止冒泡
a.addEventListener('click', function (e) {
    alert('a');
    // 冒泡过程会在此停止向上传播
    e.stopPropagation();
})
```

#### 事件委托

事件冒泡带来的有好处也有坏处，事件委托也称事件代理，在jQuery里成为事件委派

**原理：不是每个子节点单独设置事件监听器，而是事件监听器设置在其父节点上，然后利用冒泡原理影响设置每个子节点。以上案例:给ul注册点击事件，然后利用事件对象的target来找到当前点击的li，,因为点击li，事件会冒泡到ul上，ul有注册事件，就会触发事件监听器**

#### 鼠标事件

* 阻止右键菜单打开
* 阻止文本被选中

```js
var p = document.querySelector('p');
// 阻止选中后右键菜单的打开
p.addEventListener('contextmenu', function (e) {
    e.preventDefault();
})
// 阻止文本被选中
p.addEventListener('selectstart', function (e) {
    e.preventDefault();
})
```

* event对象代表事件的状态，跟事件相关的一系列信息的集合。现阶段我们主要是用鼠标事件对象MouseEvent和键盘事件对象KeyboardEvent。

  * e.clientX

    返回鼠标相对于浏览器窗口可视区的X坐标

  * e.clientY
    返回鼠标相对于浏览器窗口可视区的Y坐标

  * e.pagex
    返回鼠标相对于文档页面的X坐标IE9+支持

  * e.pageY
    返回鼠标相对于文档页面的Y坐标IE9+支持

  * e.screenX
    返回鼠标相对于电脑屏幕的X坐标

  * e.screenY
    返回鼠标相对于电脑屏幕的Y坐标

#### 键盘事件

* onkeyup 某个键被松开时触发

* onkeydown 某个键按下时触发，按下不松会一直触发

* onkeypress 某个键按下时触发，按下不松会一直触发，与onkeydown不同的是它不识别功能键，如ctrl，shift，箭头等

* keydown和keypress都绑定时先执行keydown后执行keypress

* 用法，例：

  ```js
  // 键盘事件
  // 用法1
  document.addEventListener('keyup', function () {
      console.log('keyup');
  })
  document.addEventListener('keydown', function () {
      console.log('keydown');
  })
  document.addEventListener('keypress', function () {
      console.log('keypress');
  })
  // 用法2
  document.onkeyup = function(){
      console.log('keyup');
  }
  ```

* keycode属性返回键对应的ASCII码值

* **注意:onkeydown和onkeyup 不区分字母大小写，onkeypress区分字母大小写。在我们实际开发中，我们更多的使用keydown和keyup，它能识别所有的键（包括功能键)keypress不识别功能键，但是keyCode属性能区分大小写，返回不同的ASCIl值**

* 使用示例：

  ```js
  // 实现按下s键光标定在输入框中的操作
  var search = document.querySelector('input');
  document.addEventListener('keyup', function (e) {
      // console.log(e.keyCode);
      if (e.keyCode === 83) {
          // 让搜索框获得焦点
          search.focus();
      }
  })
  ```

  ```js
  // 将输入的内容放大到另一个提示框
  var tip = document.querySelector('.tip');
  var input = document.querySelector('input');
  // 设置输入内容的时候tip框显示
  input.addEventListener('keyup', function () {
      if (this.value == '') {
          tip.style.display = 'none';
      } else {
          tip.style.display = 'block';
          tip.innerHTML = this.value;
      }
  })
  // 设置失去焦点时tip框隐藏,获得焦点时显示
  input.addEventListener('blur', function () {
      tip.style.display = 'none';
  })
  input.addEventListener('focus', function () {
    	// 这里的判断是为了解决获得焦点输入框没有内容时tip框的显示问题
      if (this.value == '') {
          tip.style.display = 'none';
      } else {
          tip.style.display = 'block';
      }
  })
  ```

  * **注意:keydown和keypress在文本框里面的特点∶他们两个事件触发的时候，文字还没有落入文本框中。
    keyup事件触发的时候，文字已经落入文本框里面了**
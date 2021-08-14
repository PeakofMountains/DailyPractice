## JavaScript学习笔记

#### JavaScript历史

* 是运行在客户端的脚本语言
* 不需要编译，运行时由js解释器逐行解释执行
* 现在可以基于Node.js技术进行服务器端编程，可用于前端，可用于后端
* 编程类语言

####  JavaScipt用途

* 表单动态验证(最初作用)
* 网页特效
* 服务端开发
* 桌面程序
* APP开发
* 物联网
* 游戏开发

#### JS执行过程

浏览器本身并不会执行JS代码，而是通过内置JavaScript引擎(解释器)来执行JS代码。S引擎执行代码时逐行解释每一句源码（转换为机器语言），然后由计算机去执行，所以JavaScript语言归为脚本语言，会逐行解释执行。

#### JS组成

* ECMAScript(JS语法)：ECMAScript规定了JS的编程语法和基础核心知识，是所有浏览器厂商共同遵守的一套JS语法工业标准。
* DOM(页面文档对象模型)：(Document Object Model，简称DOM)，是W3C组织推荐的处理可扩展标记语言的标准编程接口。通过DOM提供的接口可以对页面上的各种元素进行操作(大小、位置、颜色等)。
* BOM(浏览器对象模型)：BOM(Browser Object Model，简称BOM)是指浏览器对象模型，它提供了独立于内容的、可以与浏览器窗口进行互动的对象结构。通过BOM可以操作浏览器窗口，比如弹出框、控制浏览器跳转、获取分辨率等。

#### JS书写位置

* 行内式，直接写在html的body代码中

  * 可以将单行或少量JS代码写在HTML标签的事件属性中(以on开头的属性），如: onclick
  * 注意单双引号的使用:在HTML中我们推荐使用双引号,JS中我们推荐使用单引号
  * 可读性差，在html中编写JS大量代码时，不方便阅读;
  * 引号易错，引号多层嵌套匹配时，非常容易弄混;
  * 特殊情况下使用

* 内嵌式

* 外部式

  例：

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>JS写法测试</title>
      <!-- 内嵌式js -->
      <script>
          // alert('沙漠骆驼');
      </script>
      <!-- 外部js写法，引入外部js文件,test.js文件在同级目录下 -->
      <script src="test.js"></script>
      <!-- 引用外部js文件的script标签之间不能写代码 -->
  </head>
  
  <body>
      <!-- 行内式 -->
      <!-- <input type="button" value="唐伯虎" onclick="alert('秋香姐')"> -->
  </body>
  
  </html>
  ```

#### JS注释

* 单行注释，语法：`// 需要注释的单行内容`，快捷键`Ctrl` + `/`
* 多行注释，语法：`/* 需要注释的多行或单行内容 */`，默认是`Shift` + `Alt` + `A`，可以更改为`Ctrl` + `Shift` + `/`更好用

#### JS输入输出

* alert(msg)：浏览器弹出警示框

* prompt(info)：浏览器弹出输入框，用户可以输入，例：`prompt('请输入姓名');`

* console.log(msg)：浏览器控制台打印输出信息（按F12键后在菜单栏能找到console界面）

  #### JS变量

* 使用过程：

1. 声明变量，例：`var age;` ，其中var是一个JS关键字，用来声明变量( variable变量的意思)。使用该关键字声明变量后，计算机会自动为变量分配内存空间，不需要程序员管
2. 赋值，例：`age  = 20;` 

* 变量的初始化（声明变量并初始化），例：`var age = 20;`

* 不同类型的变量都是使用var关键字进行声明
* 字符和字符串都是用单引号引起来，数字不用

* 将输入内容保存在变量中，例：`var myname = prompt('请输入姓名');`

* 变量可以进行重新赋值，并且重新赋值可以使用不同的变量类型，例如把数字赋值给字符串变量，变量在赋值后就变为数字变量，不同的变量类型都属于一个统筹的变量，都是用var进行声明创建

* 可以同时声明多个变量，例：`var myname = 'name', age = 18;`

* 只声明不赋值时变量的值为undefined
* 不声明不赋值就使用变量就会报错
* JS变量的命名
  * 由字母( A-Z，a-z )、数字( 0-9 )、下划线( _ )、美元符号( $ )组成，如: usrAge, num01,_name
  * 严格区分大小写。var app;和var App;是两个变量
  * 不能以数字开头。18age是错误的
  * 不能是关键字、保留字。例如: var、for、while
  * 变量名必须有意义
  * 遵守驼峰命名法。首字母小写，后面单词的首字母需要大写。myFirstName
  * 推荐翻译网站:有道 爱词霸
  * 不要使用name作为变量名

#### 数据类型

* 在计算机中，不同的数据所需占用的存储空间是不同的，为了便于把数据分成所需内存大小不同的数据，充分利用存储空间，于是定义了不同的数据类型。

* 变量是用来存储值的所在处，它们有名字和数据类型。变量的数据类型决定了如何将代表这些值的位存储到计算机的内存中。

* JavaScript是一种弱类型或者说动态语言。这意味着不用提前声明变量的类型，在程序运行过程中，类型会被自动确定。

* 变量的数据类型时可以变化的。

* 分类：

  * 简单数据类型：

    * 数字型Number，包含整数、小数、不同进制的数，八进制表示以 0+数字 的形式表示，例：`var num = 011;`表示十进制的9，十六进制表示以 0x+数字 的形式表示，例：`var num = 0xa`表示十进制的10

      Number的最大值`Number.MAX_VALUE`,最小值`Number.MIN_VALUE`

      * 数字型的三个特殊值：
        * Infinity代表无穷大，大于任何数值
        * -Infinity代表无穷小，小于任何数值
        * NaN代表一个非数值
      * isNaN()函数用来判断变量是不是非数值

    * 字符串型String，推荐使用单引号

      * 转义字符和C语言一样，例`\n`换行，`\b`空格
    * length属性能获取字符串长度，例字符串str的长度就是`str.length`
      * 字符串的拼接，用 `+` 进行字符串连接，不管什么类型和字符串进行拼接都会转为字符串后拼接成字符串
    * 变量不要写道字符串中，变量与字符串通过加号相连的方式将变量值与字符串进行连接
      * 字符串的连接多用于输出功能上
    
  * 布尔型Boolean，值为true和false，true数字值为1，false数字值为0
    
  * 空值null
    
  * 未定义undefined
  
* 查看数据类型typeof，例：
  
  ```javascript
    var num = 8;
    console.log(typeof num);
  ```
  
* 数据类型转换
  
  使用表单、prompt获取过来的数据默认是字符串类型的，此时就不能直接简单的进行加法运算，而需要转换变量的数据类型。通俗来说，就是把一种数据类型的变量转换成另外一种数据类型。
  
  * 转换为字符串，例数字型num转换成字符串：`var str = num.toString();` 或` var str = String(num);` 或 `var str = num+''`的隐式转换效果
    * 转换为数字型，例字符串str转换为数字型：`var num = parseInt(str);`,取整转换，会去掉单位，`var num = parseFloat(str);`,浮点数转换，会去掉单位，`var num = Number(str);`进行强制转换，`var num = '12'-'11';`这种形式进行隐式转换，上述语句结果是数字型1，同样的隐式转换还可以用 `*` 和 `/` 
  
  * 转换为布尔型，使用Boolean()函数，例：`var bool = Boolean(12);`注意：**代表空、否定的值会被转换为false ,如"、0、NaN、null、undefined，其余值都转换为true**

#### 关键字

包括: break、case、catch、continue、default、delete、do、else、finally、for、function、if、in、instanceof、new、return、switch、this、throw、try、typeof、var、void、while、with等。

#### 保留字

包括: boolean、byte、char、class、const、debugger、double、enum、export、extends、fimal、 float、goto、implements、import、int、interface、long、mative、package、
private、protected、public、short、static、super、synchronized、throws、transient、volatile等。

#### JS运算符

常用运算符：

* 算术运算符
  * 不要直接判断两个浮点数是否相等
  * 与C语言的算术运算符相同
* 递增递减运算符
  * `++a`先加1后返回值
  * `a++`先返回值后加1
* 比较运算符
  * 与C语言基本相同
  * 使用 `==` 进行判断是否相等的时候会自动进行数据转换，因此`18=='18'`的值是true
  * 相比C语言多了全等比较符：`===`，利用全等运算符来比较要求两侧的值和数据类型完全一致，才会返回true，因此`18==='18'`的值是false
* 逻辑运算符
  * 与C语言相同，`&&`、`||`、`!`
  * **短路运算的原理︰当有多个表达式(值)时左边的表达式值可以确定结果时,就不再继续运算右边的表达式的值; **

* 赋值运算符
  * 与C语言相同，`=`，`+=`，`-=`，`*=`，`/=`，`%=`

运算符优先级

* 小括号>一元运算符>算数运算符>关系运算符>相等运算符>逻辑运算符>赋值运算符>逗号运算符
* 特别的算术运算符中先`*`，`/`，`%`后`+`，`-`
* 逻辑运算符先`&&`后`||`

#### 流程控制

* 顺序结构

* 分支结构

  * if分支，语法，例：

    ```javascript
    var a = 1;
    if (a==1){
        alert('a等于1');
    }
    ```

  * if-else分支，语法，例：

    ```javascript
    var a = 1;
    if (a==1){
        alert('a等于1');
    } else {
        alert('a不等于1');
    }
    ```

  * if-if else分支，语法，例：

    ```javascript
    var a = 1;
    if (a==1){
        alert('a等于1');
    } 
    else if(a==0) {
        alert('a等于0');
    }
    else {
        alert('a不等于1和0');
    }
    ```

  * 三元表达式 

    语法，条件表达式?表达式1:表达式2

    规则：如果条件表达式结果为真则返回表达式1的值，如果条件表达式结果为假则返回表达式2的值。

    例：`a>8?a-1:a+1`

  * switch分支

    * 语法，例：

      ```javascript
      switch(a) {
          case 1: console.log('a=1');break;
          case 2: console.log('a=2');break;
          case 3: console.log('a=3');break;
          default:console.log('a不等于1或2或3');
      }
      ```

* 循环结构

  * for(){}
  * while(){}
  * do{}while()
  * continue跳出当前次的循环
  * break跳出整个循环结构

  用法与C语言相同

#### 代码调试

* 浏览器中按F12--> sources -->找到需要调试的文件-->在程序的某一行设置断点Watch:监视，通过watch可以监视变量的值的变化，非常的常用。
* F11:程序单步执行，让程序一行一行的执行，这个时候，观察watch中变量的值的变化（按加号可以添加观察变量），也可以把鼠标放变量上。

#### 命名规范和语法格式

* 标识符命名规范
  * 变量一般名词
  * 函数一般动词
* 操作符规范
  * 一般左右留空格
* 单行注释规范
  * 注释号后一般敲一个空格

#### 数组

* 创建方式：
  1. 利用new关键字，例：`var arr = new Array();`，arr就是数组名
  2. 利用数组字面量，例：`var arr = [];`，arr是数组名，空数组
  3. 利用Array对象，例：`var arr = new Array(1,2);`，相当于 `var arr = [1,2];`，**但是注意像`var arr = new Array(2);`这种Array()中仅含有一个数字的写法是创建了一个长度为2的空数组** 
* 访问方式：
  * 索引，例：`arr[0]`，**注意索引号是从0开始计算的**
* 数组长度：
  * .length属性，例：`arr.length`就是获取数组arr的长度(元素的个数)

* 数组内可以放不同的数据类型，元素之间逗号分隔，例：`var arr = [1,'1',true，1.1];`

* 数组扩容
  * 修改length 给数组长度赋值，例：`arr.length = 5;`，当扩容后没有被赋值，则空余的空间元素就是undefined
  * 修改索引，给数组的元素赋值，例：`arr[4] = 1;`
  * **不要给数组名赋值，否则数组中元素全部没有了**

* 数组排序

  * 冒泡排序

    ```javascript
    // 升序冒泡
    var arr = [1, 4, 3, 2, 5];
            var temp;
    		// 这里比较次数应该比数组总长度小1
            for (var i = 0; i < arr.length - 1; i++) {
                for (var j = 0; j < arr.length - i - 1; j++) {
                    if (arr[j] > arr[j + 1]) {
                        temp = arr[j + 1];
                        arr[j + 1] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
    console.log(arr);
    ```

    

    ```javascript
    // 降序冒泡
    var arr = [1, 4, 3, 2, 5];
            var temp;
    		// 这里比较次数应该比数组总长度小1
            for (var i = 0; i < arr.length - 1; i++) {
                for (var j = 0; j < arr.length - i - 1; j++) {
                    if (arr[j] < arr[j + 1]) {
                        temp = arr[j + 1];
                        arr[j + 1] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
    console.log(arr);
    ```

    升序冒泡与降序冒泡的区别就是条件比较的大于号换成小于号

#### 函数

* 函数的声明和调用，语法，例：

  ```javascript
  // 函数的声明
  function sayHi(){
      console.log('Hi~~~');
  }
  // 函数的调用
  sayHi();
  ```
  
  



#### 函数返回值

*  return关键字
* JS中的函数返回值与其他语言不同的是：JS中的函数返回值可以返回一个数组
* 在函数中如果没有return语句或者没有执行return语句，则函数的返回值是undefined



#### JS中的arguments的使用

* 函数中的arguments中含有函数传进来的实参
* 只有函数才有arguments对象，而且是每个函数都内置了这个对象
* arguments对象在函数内可直接当作数组进行调用和访问
* arguments对象具有数组的length属性，通过arguments.length获得的长度是传入的实参的个数
* 按照索引的方式进行存储
* 它本身并不是真正的数组，没有真正数组的一些方法，如pop()，push()等



#### 声明函数的两种方式

```javascript
// 两种声明函数的方式，都能进行参数的传递
// 1. 用函数关键字function声明函数
function fn(aru1) {
    console.log(aru1);
}
// 第一种声明函数的调用方法
fn('第一种声明函数的方式');

// 2. 用定义变量函数表达式的方式声明函数（匿名函数）
var fun = function (aru2) {
    console.log(aru2);
}
// 第二种声明函数的调用方法
fun('第二种声明函数的方式');
// fun是变量名，不是函数名，其中存的是函数，不是值
```



#### 作用域

* **下面说的作用域均是在ECMAScript 6之前的规则**

* 局部作用域-局部变量-在函数内部起作用
* 全局作用域-全局变量-整个script标签或者单独的js文件中起作用

* 块级作用域

  * 现阶段JS中没有块级作用域，在ECMAScript 6 之后加入了块级作用域（将if(){}和for(){}形成的空间成为块级作用域），因此目前的JS中不考虑块级作用域的影响，因此可以在if语句块和for语句块的外面访问在其内部语句块中定义的变量，例：

    ```javascript
    if (3<5) {
        var num = 10;
    }
    console.log(num);
    // 这个输出的结果就是10，能访问到if语句块中的num变量，这是目前JS和java等语言的作用域的差异
    ```
    
    

  **注意区分这个块级作用域和局部作用域以及全局作用域，全局作用域中是不能访问局部作用域中定义的局部变量的**

  

* 作用域链

  在内部函数中访问变量会从内部作用域中逐层向外部作用域中进行查找，采用就近原则的方式，访问首先遇到的变量值作为此变量的值，例：

  ```javascript
  // 作用域链
  var num = 20;
  function fn() {
      var num = 10;
      function fun() {
          console.log(num);
          // 由于离此处调用的num最近的是fn函数定义的num = 10，因此最终的输出结果应该是10
      }
      fun();
  }
  fn();
  ```

  

#### JS引擎运行JS的步骤

预解析和代码执行

* 预解析：JS引擎将JS中所有的var变量声明和function函数声明提升到**当前作用域**的最前端
  * 提升变量的时候不进行变量的赋值操作
  * 提升函数的时候不进行函数的执行调用
* 代码执行：按照与解析后的顺序从上往下依次进行执行

举一个例子：

```javascript
// 预解析和代码执行顺序测试
function f1() {
    var a = b = c = 9;
    // 上面这条语句相当于var a = 9; b = 9; c = 9;
    // 因为b和c没有用var直接进行声明，因此b，c是全局变量
    // 所以函数外的全局作用域中可以调用b，c的值，但是a是局部变量因此在全局作用域中进行调用会报错
    console.log(a);
    console.log(b);
    console.log(c);
}
f1();
console.log(c);
console.log(b);
console.log(a);
// 执行结果：9 9 9 9 9 报错
```





#### 对象

组成：属性（名词），方法（动词）

其概念和其他编程语言中的对象相同

对象创建方式：

```js
// 创建对象的方式1
var man = {
    // 对象属性的定义，注意之间用逗号隔开，而不是分号，属性与属性值，方法名与方法体之间都是键值对的形式
    uname: '张三',
    age: 18,
    // 对象方法的定义
    sayHi: function () {
        console.log('Hi~~~');
    }
}
// 对象属性的调用
// 方法1
console.log(man.uname);
// 方法2
console.log(man['age']);
// 对象方法的调用
man.sayHi();
```



```js
// 创建对象的方式2
// 创建一个空的对象，再逐步往空的对象里添加属性和方法
var woman = new Object();
// 添加属性,属性与属性值之间用赋值号连接，不同属性和方法之间用分号分隔
woman.uname = '张三',
    woman.age = 18,
    // 对象方法的定义
    woman.sayHi = function () {
    console.log('Hi~~~');
}
// 对象属性的调用
// 方法1
console.log(woman.uname);
// 方法2
console.log(woman['age']);
// 对象方法的调用
woman.sayHi();

```



```js
// 创建对象的方式3
// 利用构造函数,构造函数的首字母大写
// 构造函数不需要return就能返回结果
function Man(uname, age) {
    this.uname = uname;
    this.age = age;
    this.sing = function (sang) {
        console.log(sang);
    }
}
// 调用构造函数创建对象，调用构造函数必须使用new关键字
var man1 = new Man('刘德华', 50)
// 创建好的对象可以使用其属性和方法
console.log(man1.uname);
console.log(man1.age);
man1.sing('歌曲');
```

**构造函数与对象的关系：构造函数，泛指某一大类，将一类事物的特征抽象出来，封装在构造函数中，类似java语言中的类，对象是具体的一个事物，可以通过构造函数实例化创建对象。**

#### 遍历对象中内容

* 利用 for in 循环，语法，例：

  ```js
  // 利用for in 循环遍历对象中内容
  // 对象创建
  var obj = {
      uname: '六花',
      age: 17,
      sex: 'woman'
  }
  // 遍历对象中的内容
  for (var k in obj) {
      // k输出的是对象中的变量或方法名
      console.log(k);
      // obj[k]输出的是变量值或方法体
      console.log(obj[k]);
  }
  ```





#### 内置对象

JS语言自带对象，供开发者使用，并提供了常用的或必要的功能（属性和方法），如Math，Array，String



#### 查文档

Mozilla开发者网络提供了有关开放网络技术（Open Web）的信息，包括HTML、CSS和万维网及HTML5应用的API

MDN：[官方网址](https://developer.mozilla.org/zh-CN/)



#### Math对象

不用new，可以直接使用

* 常用属性和方法：
  * Math.PI			// 圆周率

  * Math.floor()      // 向下取整

  * Math.ceil()       // 向上取整

  * Math.round()   // 四舍五入 就近取整，**.5特殊，它往大取，例如：Math.round(-1.5)的值是-1**

  * Math.abs()      // 绝对值

  * Math.max()     // 最大值

  * Math.min()      // 最小值

  * Math.random()// 返回一个[0,1]的浮点数

    * 得到两个数之间（包含这两个整数）的随机整数

      ```js
      // 得到两个整数之间（包含这两个整数）的随机整数
      function getRandomInt(min, max) {
          return Math.floor(Math.random() * (max - min + 1)) + min;
      }
      // 调用方式举例
      console.log(getRandomInt(1, 3));
      
      ```



#### Date日期对象

是一个构造函数，必须用new关键字创建一个对象实例

* 获取格式化日期，例：

```js
// 获取格式化日期
function getNowDate() {
    var date = new Date();
    var year = date.getFullYear();
    // date.getMonth()方法得到的月份是0~11月，因此应该将结果+1
    var month = date.getMonth() + 1;
    var dates = date.getDate();
    var day = date.getDay();
    // date.getDay()方法得到的第一天是星期日，因此我们利用数组将星期对应起来
    var days = ['星期日', '星期六', '星期五', '星期四', '星期三', '星期二', '星期一'];
    console.log('今天是：' + year + '年' + month + '月' + dates + '日  ' + days[day]);
}
getNowDate();
```

* 获取格式化时间，例：

```js
// 获取格式化时间
function getNowTime() {
    var date = new Date();
    var hour = date.getHours();
    // 为了让时间显示的格式相同，将小于10的数字前面加上0占位，例如8显示为08
    hour = hour < 10 ? '0' + hour : hour;
    var minutes = date.getMinutes();
    minutes = minutes < 10 ? '0' + minutes : minutes;
    var seconds = date.getSeconds();
    seconds = seconds < 10 ? '0' + seconds : seconds;
    var day = date.getDay();
    return hour + '时' + minutes + '分' + seconds + '秒  ';
}
console.log('现在是：' + getNowTime());
```



* 获取日期的总的毫秒形式

Date对象基于1970年1月1日（世界标准时间）经过的毫秒数

````js
// 距离1970-1-1的毫秒数
var date = new Date();
// 写法1
console.log(date.valueOf());
// 写法2
console.log(date.getTime());
// 简单写法：与上面的写法相同
var date1 = +new Date();
// 新写法，HTML5新增,不考虑兼容性
console.log(Date.now());
````

利用这个做出倒计时效果：

```js
// 倒计时效果
function countDown(time) {
    // 现在总的毫秒数
    var nowTime = +new Date();
    // 用户输入的时间总的毫秒数
    var inputTime = +new Date(time);
    var times = (inputTime - nowTime) / 1000;
    // 倒计时天数
    var day = parseInt(times / 60 / 60 / 24);
    // 格式化操作
    day = day < 10 ? '0' + day : day;
    var hours = parseInt(times / 60 / 60 % 24);
    hours = hours < 10 ? '0' + hours : hours;
    var minutes = parseInt(times / 60 % 60);
    minutes = minutes < 10 ? '0' + minutes : minutes;
    var seconds = parseInt(times % 60);
    seconds = seconds < 10 ? '0' + seconds : seconds;
    return day + '天' + hours + '时' + minutes + '分' + seconds + '秒';
}
console.log('倒计时： ' + countDown('2021-8-12 09:25:00'));
```



#### Aarry数组对象

#### 判读是否为数组

语法，例：

```js
// 判断是否为数组
// 方法1
var arr = [];
if (arr instanceof Array) {
    console.log('是数组');
}
else {
    console.log('不是数组');
}
// 方法2,HTML5新增，IE9以上版本支持
var arr = [];
if (Array.isArray(arr)) {
    console.log('是数组');
}
else {
    console.log('不是数组');
}

```



#### 添加和删除数组元素

* 方法，例：

```js
// 添加和删除数组元素

var arr = [1, 2, 3];
// 在结尾添加一个元素
arr.push(4);
// 在结尾添加多个元素
// push()方法返回值是新数组的长度
console.log(arr.push(5, '六花'));
console.log(arr);
// 在数组开头添加一个元素
arr.unshift(0);
// 在数组开头添加多个元素
arr.unshift('勇太', -1);
console.log(arr);
// 同样unshift()的返回值也是新数组的长度
// 删除数组最后一个元素
// pop()返回值是删除的那个元素
console.log(arr.pop());
console.log(arr);
// 删除第一个元素
// shift()返回值是删除的那个元素
console.log(arr.shift());
console.log(arr);
```

#### 数组翻转

```js
var arr = [1,2,3];
console.log(arr.reverse());
```

#### 数组排序（冒泡）

```js
var arr = [13,4,77,1,7];
arr.sort(function(a,b){
    // 升序冒泡
    return a - b;
})
console.log(arr);
```



```js
var arr = [13,4,77,1,7];
arr.sort(function(a,b){
    // 降序冒泡
    return b - a;
})
console.log(arr);
```

#### 数组索引查询

```js
// 数组索引查询
var arr = ['古河渚', '琴美', '汐', '杏', '汐'];
// arr.indexOf()方法返回从左往右第一个查找到的索引号，如果没有找到，返回-1
console.log(arr.indexOf('汐'));
// arr.indexOf()方法返回从右往左第一个查找到的索引号，如果没有找到，返回-1
console.log(arr.lastIndexOf('汐'));
```



#### 数组去重

```js
// 数组去重
function unique(arr) {
    var newarr = [];
    for (var i = 0; i < arr.length; i++) {
        if (newarr.indexOf(arr[i]) === -1) {
            newarr.push(arr[i]);
        }
    }
    return newarr;
}
// 测试
var arr = ['a', 1, 3, 1, 4, 'a', 'b'];
console.log(unique(arr));

```

#### 数组转换为字符串

```js
// 数组转换为字符串
var arr = ['古河渚', '琴美', '汐', '杏', '汐'];
// 1. toString()方法
console.log(arr.toString());
// 2. join(分隔符)方法，可以设置转换后的元素之间的连接符
var arr = ['古河渚', '琴美', '汐', '杏', '汐'];
// join()没有参数是默认逗号分隔
console.log(arr.join());
console.log(arr.join('-'));
console.log(arr.join('&'));
```

#### 数组连接

* concat()方法实现数组连接，返回新数组，不改变原数组的值

  ```js
  // 连接多个数组，不影响原数组
  var arr1 = ['六花'];
  var arr2 = ['勇太'];
  var arr = arr1.concat(arr2);
  console.log(arr);
  console.log(arr1);
  console.log(arr2);
  ```

#### 数组截取片段

* slice()方法实现数组截取，返回截取的新数组，不改变原数组的值

  ```js
  // slice()方法截取数组，参数slice(begin,end);截取的是[begin,end),左闭右开，取不到end索引的值
  // 同样返回截取的新数组，不改变原数组的值
  var arr = ['六花', '勇太', '森大人'];
  console.log(arr.slice(0, 2));
  console.log(arr);
  
  ```

#### 数组删除片段

* splice()方法删除数组指定片段

  ```js
  // splice()方法删除数组指定片段
  var arr = ['六花', '勇太', '森大人'];
  // splice(start,length)函数，第一个参数是删除起始的索引，第二个参数是删除片段的长度
  console.log(arr.splice(0, 2));
  // splice()方法返回删除的片段
  console.log(arr);
  // splice()方法会改变原数组
  ```

  

#### 字符串对象

#### 基本包装类型

为了方便操作基本数据类型，JS提供了三个特殊的引用类型：String，Number和Boolean

基本包装类型就是把简单的数据类型包装成复杂的数据类型，这样基本数据类型就有了属性和方法，其过程如下：

```js
// 基本包装类型
var str = '犬夜叉';
// 这条语句实际上是进行了如下包装过程
// 生成临时变量temp，将简单数据类型包装成复杂数据类型
var temp = new String('犬夜叉');
// 将临时变量赋值给声明的字符变量
var str = temp;
// 销毁临时变量
temp = null;
```

正因为如此，**在使用字符串的过程中应减少字符串变量的重复赋值操作**，因为此操作会在内存空间中生成大量的空字符串对象，占用内存

#### 查找字符串中字符位置

indexOf()和lastIndexOf()方法，返回字符在字符串中的位置，可以设置开始查找的起始索引号

```js
// 查找字符在字符串中的索引号
var str = '犬夜叉和戈薇,杀生丸和玲';
var index = str.indexOf('薇');
console.log(str[index]);
// indexOf(字符，index)第二个参数设置开始查找的起始索引号（包含）
console.log(str.indexOf('和', 4));
// 反向查找
console.log(str.lastIndexOf('薇'));
// 没有找到返回-1
console.log(str.lastIndexOf('薇', 3));
// indexOf(字符，index)第二个参数设置开始反向查找的起始索引号（包含）
console.log(str.lastIndexOf('薇', 5));
```

实际案例，统计指定字符串中指定字符的出现次数：

```js
// 统计字符在字符串中出现的次数
function countCharTimes(str, char) {
    // count用来计数
    var count = 0;
    // i作为起始索引号，找到指定字符后将索引更换为找到的位置
    for (var i = 0; ; i++) {
        i = str.indexOf(char, i);
        if (i === -1) {
            // 从起始索引处没有找到就跳出循环，返回结果
            break;
        }
        count++;
    }
    return count;
}
// 使用示例
var str = '六花喜欢勇太，勇太喜欢六花';
console.log(countCharTimes(str, '花'));

```

#### 索引确定索引处字符

```js
var str1 = '六花喜欢勇太，勇太喜欢六花';
// 根据索引输出索引处的值
console.log(str1.charAt(1));
var str2 = 'the world';
// charCodeAt()方法返回索引号的字符ASCII值，目的：判断用户按下了哪个键
console.log(str2.charCodeAt(2));
// HTML5,IE8+支持，和charAt()作用等效
console.log(str1[1]);
```



#### 统计字符串中字符出现次数

```js
// 统计字符串中字符出现次数最多的字符
var str = 'this is a test';
// 创建一个空对象
var count = {};
for (var i = 0; i < str.length; i++) {
    var chars = str.charAt(i);
    if (count[chars]) {
        // 查找到字符后将对应属性值加1
        count[chars]++;
    }
    else {
        count[chars] = 1;
    }
}
console.log(count);
var max = 0;
var char = '';
for (var k in count) {
    if (count[k] > max) {
        max = count[k];
        char = k;
    }
}
console.log(max);
console.log('出现次数最多的是：' + char)
```



#### 字符串操作方法

* concat()方法，连接字符串，可以被+连接字符串的方式代替
* substr()方法截取字符串，第一个参数是起始位置，第二个参数是截取长度
* replace()方法替换字符，第一个参数是要被替换掉的字符，第二个参数是用来替换的字符，替换的是字符串中这个字符出现的第一个位置
* split()方法参数是分隔符，根据字符串中的这个分隔符将字符串划分为数组元素，返回值是数组
* toUpperCase()方法转换大写
* toLowerCase()方法转换小写



#### 简单数据类型和复杂数据类型

* 简单数据类型-值类型 string、number、boolean、undefined、null
  * 存储时变量存储的是值本身
  * 其中简单数据类型null返回的是一个空的对象，如果有个变量以后打算存储为对象，但暂时被想好内容，就可以先给null
  * 简单数据类型存储在栈中，复杂数据类型存储在堆中

* 复杂数据类型-引用类型
  * 通过new关键字创建的对象，如Object、Array、Date等
  * 复杂数据类型指向栈中的地址，栈中的地址指向存储在堆中的实际数据



#### 堆和栈

可以看作简单数据类型存储在栈中，复杂数据类型存储在堆中，但是JS中是没有堆栈的概念的



#### Web APIs 和 JS基础关联性

JS基础学习ECMAScript基础语法，为后面做铺垫，Web APIs是JS的应用，大量使用JS基础语法做交互效果

#### API

Application Programming Interface应用程序编程接口，简称API，是一些预先定义的函数，是给程序员提供的一种工具，一遍轻松完成功能

#### Web API

Web API 是浏览器提供的一套操作浏览器功能（BOM）和页面元素的API(DOM)

Web API一般都有输入和输出（函数的传参和返回值），Web API 很多都是函数方法

[MDN详细API](https://developer.mozilla.org/zh-CN/docs/Web/API)



#### DOM

文档对象模型（Document Object Model，简称DOM），是W3C组织土建的处理HTML或XML的标准编程接口

W3C已经定义了一系列的DOM接口，通过这些DOM接口可以改变网络的内容、结构和样式

* DOM树
  * 文档：一个页面就是一个文档，DOM中使用document表示
  * 元素：页面中所有标签都是元素，DOM中使用element表示
  * 节点：网页中所有内容都是节点（标签、属性、文本、注释等），DOM中使用node表示
  * DOM把以上内容都看作对象

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

* onclick 鼠标点击左键触发
* onmouseover 鼠标经过触发
* onmouseout 鼠标离开触发
* onfocus 获得鼠标焦点触发
* onblur 失去鼠标焦点触发
* onmousemove 鼠标移动触发
* onmouseup 鼠标弹起触发
* onmousedown 鼠标按下触发


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



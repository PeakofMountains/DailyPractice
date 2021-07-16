## CSS学习

* HTML局限性：只关注内容语义,主要做结构，丑

* CSS价值：样式美化，实现结构样式相分离

* CSS使用语法:

  ```css
  <!DOCTYPE html>
  <html lang="en">
  <head>
  	<meta charset="UTF-8">
  	<meta http-equiv="X-UA-Compatible" content="IE=edge">
  	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  	<title>CSSPractice</title>
      <!-- 结构设置写在body标签中，样式设置写在head标签内的style标签中 -->
      <style>
          /* 在style标签中通过`标签名{属性：属性值}`的键值对形式进行设置 */
          /* 这里是对body标签中的标签p进行设置，p就是选择器 */
          p{
              /* 这里的color和font都是属性 */
              color: aquamarine;
              font: 100;
          }
      </style>
  </head>
  <body>
      <p> This is a CSSPractice</p>
  </body>
  </html>
  ```

* 代码风格
  * 展开风格
  * 小写字母
  * 选择器与大括号中间留一个空格，键值对的`:`后留有一个空格

* CSS选择器

  * 选择器分类：基础选择器和复合选择器

    * 基础选择器：由单个选择器组成，包括标签选择器，类选择器，id选择器，通配符选择器

      * 标签选择器：用HTML标签作为选择器，把某一类的标签全部选出来，进行统一更改设置，语法：

        ```css
        <style>
            /* 这里是对body标签中的标签p进行设置，p就是选择器 */
            p {
                /* 这里的color和font都是属性 */
                color: aquamarine;
                font: 100;
        	}
        </style>
        ```

        

      * 类选择器：单独选一个或某几个标签,语法：

        ```css
        /* 先在style标签中定义类，不能用标签作为类的名字 */
        <style>
        /* 类选择器 */
        .red {
            color: red;
        }
        </style>
        ```

        

        ```css
        /* 再在需要设置的标签中加入 class="类名" */
        <body>
            <p> This is a CSSPractice</p>
            <div class="red">选项1</div>
            <div>选项2</div>
            <div>选项3</div>
        </body>
        ```

        类选择器口诀:样式点定义，结构类(cLass)调用，一个或多个，开发最常用

        * 类选择器-多类名：给一个标签指定多个类名，从而达到更多选择的目的，这些类名都能选择出这个标签

          * 语法

            ```css
            /* 类选择器,定义了两个类 */
            <style>
                .red {
                color: red;
                }
                .font20 {
                font-size: 20px;
                }
            </style>
            
            <body>
                <!-- 在标签属性class中可以写多个类名，多个类名之间空格隔开 -->
                <div class="red font20">选项2</div>
            </body>
            ```

        * id选择器：为特定id的HTML元素指定特定样式,HTML元素以id属性来设置id选择器，经常与JavaScript搭配使用，CSS中id选择器用`#`来定义，语法：

          ```css
          /* id选择器 */
          <style>
          	#pink {
                  color: pink;
          	}
          </style>
          
          <body>
              <div id="pink">选项3</div>
          </body>
          ```

          id选择器的口诀:样式`#`定义，结构id调用，只能调用一次，别人切勿使用

        * 通配符选择器：选取页面中所有元素，语法

          ```css
          <style>
              * {
                  color: red;
              }
          <style>
          ```

          通配符选择器不需要调用，自动就给所有的元素使用样式
    
    * 复合选择器
    
      对基本选择器进行组合形成的，可以更精准搞笑选择目标元素（标签），包括后代选择器，子选择器，并集选择器，伪类选择器等
    
      * 后代选择器
    
        * 又称包含选择器，可以选择父元素里面子元素，语法：父元素写前面，子元素写后面，空格隔开，发生嵌套时内层标签就成为外层标签的后代，例：`ol li {color: red}`，这里后代指的是子孙所有
    
        * 元素1和元素2等可以是任意基础选择器
    
      * 子选择器
    
        * 只能选择作为某元素最近一级子元素，简单理解就是选亲儿子元素，语法，例：`ol>li {color: red}`
    
      * 并集选择器
    
        * 可以选择多组标签，同时为他们定义相同的样式，通常用于集体声明，语法，例：`div,p {color: red}`,任何选择器都可作为并集选择器的一部分，约定的语法规范，并集选择器喜欢竖着写，最后一个选择器不需要加`,`
    
      * 伪类选择器
    
        * 用于向某类选择器添加特殊效果，比如给连接添加特殊颜色效果
    
        * 最大特点是用`:`表示，比如`:hover`、`:first-child`
    
        * 类别很多，比如：
    
          * 结构伪类
    
          * 链接伪类
    
            * 选择未访问（点击）过的链接，例：`a:link {color: red}`
    
            * 选择访问（点击）过的链接，例：`a:visited {color: red}`
    
            * 选择鼠标经过的链接，例：`a:hover {color: red}`
    
            * 选择鼠标点击还未松开时的链接，例：`a:active {color: red}`
    
            * **为了确保生效，请按照LVHA的循顺序声明:link - :visited -:hover - :active**
    
            * **因为a链接在浏览器中具有默认样式，所以我们实际工作中都需要给链接单独指定样式**
    
            * 实际开发中一般只用以下形式（设置链接默认颜色和鼠标经过时的颜色）：
    
              ```css
              /* a是标签选择器，选择所有链接，未访问状态颜色为gray */
              a {
                  color: gray;
              }
              /*鼠标经过时变为red*/
              a:hover {
                  color: red;
              }
              ```
    
          * :focus伪类选择器
    
            用于选取获得焦点的表单元素，焦点就是光标，一般`<input>`类表单元素才能获取，因此此选择器主要针对表单元素，语法，例：`input:focus {background-color: pink}`

* CSS字体属性

  CSS Fonts(字体)属性用于定义字体系列、大小、粗细、和文字样式（如斜体）

  * 字体类型，例：`font-family: 'Microsoft YaHei';`，字体可以有多个，用`''`包含，之间用`,`隔开
  * 字体大小，例：`font-size: 16px;`,谷歌浏览器文字默认就是16像素大小，标题标签比较特殊，需要单独指定大小
  * 字体粗细，例：`font-weight: bold;`,normal正常,bold加粗，还可以是数字，700相当于bold
  * 文字样式，例：`font-style: italic;`normal正常，italic斜体
  * 字体符合属性，使用font属性时，必须按`font: font-style font-weight font-size/line-height font-family;`语法格式中的顺序书写，不能更换顺序，并且各个属性间以空格隔开,例：`font: italic 700 16px 'Microsoft yahei';`,不需要设置的属性可以省略（取默认值），但必须保留font-size和font-family属性，否则font属性将不起作用

* CSS文本属性

  定义文本的外观，比如颜色、对齐文本、装饰文本、文本缩进、行间距等

  * color，可以用英文，也可以用十六进制，或者rgb表示形式，例：

    ```css
    /* color: aquamarine; */
    /* color: #ccooff; */
    color: rgb(204,0,255);
    ```

  * 对齐文本

    text-align属性用于设置元素内文本内容的水平对齐方式，例：`text-align: center;`,属性值可为left,right,center，如果是想让图片居中对齐，则text-align属性应该写在图片的父标签中，写在图片标签中是没有用的

  * 装饰文本 

    text-decoration属性规定添加到文本的修饰，下划线，删除线，上划线等，例：`text-decoration: underline;`,属性值可以为underline,line-throught,overline,none

  * 文本缩进

    text-indent属性用来指定文本第一行的缩进，例：`text-indent: 20px`,`text-indent: 2em;`，其中px是像素单位，em是当前字体单位，1em就表示1个当前字体的大小，如果当前元素没有设置大小，就会按照父元素的字体大小

  * 行间距

    line-height行间距离，例：`line-height: 26px`

* CSS引入方式

  按照CSS样式书写位置不同分为三大类：

  * 行内样式表（CSS写在标签内部，适用于修改简单样式）
  * 内部样式表（嵌入式，CSS抽取出来放在HTML文件的style标签中，将结构和样式分离，但是没有完全分离）
  * 外部样式表（链接式，将CSS抽取出来放在css文件中，在HTML文件中用链接的方式引入css文件，实际开发中多用外部样式表），语法：
    * 创建css文件
    * 在HTML文件中用link标签引入css文件，例：创建CSSPractice.css文件，在HTML的head标签中用`<link rel="stylesheet" href="CSSPractice.css">`引入此css文件

* Chrome调试工具
  * Chrome提供了非常好用的调试工具，用于调试HTML结构和CSS样式，使用`右键检查`或者`F12`都可以打开调试页面
  * `Ctrl+滚轮`可以放大开发者工具代码大小
  * 左边是HTML元素结构，右边是CSS样式
  * 右边CSS样式可以改动数值（上下箭头或者直接输入）和查看颜色，在这里改动的数值在浏览器关闭后就会消失，不会保存在代码中，因此应该最终在代码中进行修改
  * Ctrl+0复原浏览器大小
  * 如果点击元素，发现右侧没有样式引入，极有可能是类名或者样式引入错误
  * 如果有样式，但是样式前面有黄色叹号提示，同样是样式属性书写错误，在右侧对应区域右上角会显示出错代码所在行数

Emmet语法，使用缩写，提高html/css编写速度，vscode内部已经集成该语法

* 快速生成HTML结构语法

  * 输入标签名按---`Tab`键即可补全
  * 生成多个相同标签--- 标签*数量 ，即可，例：`div*3`就能快速生成三对div标签
  * 父子级关系的标签用`>`，例：`ul>li`就可以生成`<ul> <li></li> </ul>`
  * 兄弟关系的标签用`+`连接就可以，例：`div+p`
  * 生成带有类名或者id名字，直接写`.类名`或者`#类名`加上`Tab`键就可以了
  * 如果生成的div类名是有顺序的，可以用自增符号`$`,例：`.demo$*5`
  * 在生成的标签内部写内容可以用`{}`表示，如`p{I am a demo}`,`p{demo$}*3`

* 快速生成CSS样式语法

  * 输入首字母来缩写样式代码，例：`tac`按Tab得到`text-align: center;`

  * 快速格式化代码

    在settings.json用户设置里面添加

    ```json
    "editor.formatOnType":true,
    "editor.formatOnSave":true,
    ```

    就可以在保存的时候自动格式化代码，只用设置依次即可永久生效

* CSS元素显示模式

  元素以什么方式进行显示，为了更好地布局

  HTML分类：

  * 块元素

    `<h1> <p> <div> <ul> <ol> <li>`等，特点：

    * 独占一行
    * 高度，宽度，颜色，外边距，内边距都可以设置，宽度默认是父级宽度
    * 是一个容器盒子，里面可以放行内或者块级元素

    **注意：文字类的元素标签内不能使用块级元素，如`<p> <h1>`等都是文字类块级标签**

  * 行内元素

    常见：`<a> <strong> <b> <span>`等，特点：

    * 一行可以放多个元素
    * 宽和高直接设置是无效的
    * 默认宽度就是本身内容的宽度，自动变宽或变窄调整
    * 行内元素只能容纳文本和其他行内元素

    **注意：链接里不能再放链接，特殊情况链接`<a>`里面可以放块级元素，但是给`<a>`转换一下块模式最安全

  




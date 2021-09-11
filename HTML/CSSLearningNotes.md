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

### CSS选择器

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

    **注意：链接里不能再放链接，特殊情况链接`<a>`里面可以放块级元素，但是给`<a>`转换一下块模式最安全**

  * 行内块元素

    兼具行内元素和块元素的特点，例：`<imag /> <input /> <td>`,特点：

    * 相邻行内块元素在一行，中间有空白缝隙，一行可显示多个
    * 默认高度就是本身内容的宽度
    * 宽度，行高，外边距及内边距都可以控制

  * 元素显示模式转换

    特殊情况下需要元素模式的转换，一个模式需要另一种模式的特性，语法，例：

    ```css
    a {
        /* display: block将行内元素a转换为块元素,转换后就可以设置宽高等 */
        display: block;
        width: 13em;
        height: 2em;
        background-color: black;
    }
    ```

    

    ```css
    /* 块元素div转换为行内元素 */
    div {
        display: inline;
    }
    ```

    

    ```css
    /* 行内元素转换为行内块元素 */
    span {
        display: inline-block;
    }
    ```



* **文字垂直居中**

  * CSS没有给我们提供文字垂直居中的代码.这里我们可以使用一个小技巧来实现.

  * 解决方案: 让文字的行高等于盒子的高度就可以让文字在当前盒子内垂直居中，例：

    ```css
    /* 让行高等于块的高度即可达到垂直居中的效果 */
    div {
        height: 40px
        line-height: 40px
    }
    ```

* CSS的背景

  * 背景颜色`background-color: red;`，属性值默认是transparent透明色

  * 背景图片`background-image: url()`便于控制位置（精灵图也是一种运用场景），属性值默认是none,在url()中添加图片地址

  * 背景平铺`background-repeat: repeat`,属性值可以为repeat,no-repeat,x-repeat,y-repeat,默认是repeat

    **页面元素既可以添加背景颜色也可以添加背景图片，只不过背景图片会压住背景颜色**

  * 背景图片位置`background-position: left top`

    * `background-position: left top`，参数值可以为方位词，如top，center，bottom，left，right，使用的时候如果用两个方位词，这两个方位词没有顺序都可以，搭配使用，如果只指定了一个方位名词，另一个值省略，则第二个值默认居中对齐
    * 参数值可以是坐标，分别是x和y坐标，以px为单位
    * 参数可以是混合单位，方位名词和坐标，但是注意顺序：第一个如果是像素就一定是x坐标，第二个如果是像素就一定是y坐标

  * 背景图像固定（背景附着）

    设置背景图片是否随页面其余部分滚动，后期可以制作视差滚动效果，语法：`background-attachment: fixed`，属性值可以为scroll背景图随对象滚动，或者fixed背景图固定

  * 背景复合写法
    * 为了简化背景属性的代码，我们可以将这些属性合并简写在同一个属性background中，从而节约代码量。当使用简写属性时，没有特定的书写顺序,一般习惯约定顺序为∶*background:背景颜色背景图片地址背景平铺背景图像滚动背景图片位置;*

  * 背景半透明效果
    * `background: rgba(0, 0, 0, 0.3)`,最后一个参数是透明度，范围0~1，数字越小越透明

  **shift键+alt键+鼠标左键拖动可以方块区域选取内容**

* CSS三大特性

  * 层叠性
    * 样式冲突，就近原则
    * 样式不冲突，就近原则但只覆盖重复的部分

  * 继承性

    * 子标签继承父标签的**某些样式**，如文本颜色和字号等（text-,font-,line-这些元素开头的可继承，以及color属性）

    * 行高的继承

      * 父标签行高可以跟单位也可以不跟单位，当行高不跟单位式，其行高就是 子标签文字大小*数字 的高度（**注意是子标签文字大小来乘数字，而不是子标签行高乘数字**）,例：

        ```css
        /* 这里假设body是div的父标签，则这个样式设置出的body的行高就是div的1.5倍，即30px */
        body {
            font:12px/1.5 Microsoft YaHei;
        }
        div {
            font-height: 20px
        }
        ```

  * 优先级

    当同一元素指定多个选择器时有优先级的问题存在

    * 选择器相同，则执行层叠性

    * 选择器不同，则根据选择器权重执行

      * 权重顺序：继承或者*<元素选择器<类选择器，伪类选择器<id选择器<行内样式 style=""<!important 重要的

      * **优先级权重不能继承，继承的权重是0，如果该元素没有直接选中，不管父元素权重多高，子元素得到的权重都是0**，例：

        ```css
        /* 此例中p最终颜色为pink */
        /* 在style中 */
        /* 此处父权重是最高等级的 */
        #father {
            color: red!important;
        }
        /* p从father标签继承的权重是0 */
        p {
            color: pink;
        }
        /* 在body中 */
        <div id="father">
        	<p>你还是很好看</p>
        </div>
        ```
      
      * a链接标签浏览器默认制定了一个样式：蓝色的，有下划线，如果想修改a链接标签，则必须直接选中a标签进行修改
      
      * 复合选择器的权重是各个选择器权重进行叠加，权重计算的时候，权重能叠加但是不会有进位

### 盒子模型（盛装内容的容器）

网页布局三大核心：盒子模型，浮动，定位

网页布局过程：

1. 先准备网页元素，基本都是盒子
2. 利用CSS设置好盒子样式，摆放到相应位置
3. 往盒子里装东西

* 组成部分：border边框，content内容，padding内边距，margin外边距

  * 边框border：颜色，宽度，线型，属性：
    * `border-width`，属性值为像素值
    * `border-style`,属性值为solid(实线)，dashed(虚线)，dotted(点线)等
    * `border-color`

  边框简写,例：`border: 1px solid red;`属性值没有顺序

  * 边框部分设置，例：`border-top: 1px solid red; `

  * 表格边框，例：`border-collapse: collapse;`合并单元格边框

  * 边框会增加盒子的实际大小

    因此我们有两种方案解决:

    1. 测量盒子大小的时候不量边框.
    2. 如果测量的时候包含了边框,则需要width/height减去边框宽度

* 内边距padding，边框与内容之间的距离，语法，例：`padding-left: 20px;`,简写方法：

  * `padding: 5px;`代表上下左右内边距都是5px
  * `padding: 5px 10px;`代表上下5px，左右10px
  * `padding: 5px 10px 20px;`代表上5px，左右10px，下20px
  * `padding: 5px 10px 20px 30px;`代表上5px，右10px，下20px，左30px

  给盒子设置padding值能更好地让盒子适应内容的大小，如果盒子没有设置width和height，则设置padding后不会改变盒子的大小，盒子大小跟随父盒子

* 外边距margin,盒子与盒子间距，语法，例：`margin-left: 20px;`

  * margin的简写和padding的简写格式一致

  **浏览器调试工具右边Computed菜单有元素间距表示**

  * 外边距可以让块元素水平居中，但是必须满足两个条件:
    * 盒子必须指定了宽度( width )
    * 盒子左右的外边距都设置为auto属性值 

  * 外边距设置不可以让行内元素和行内块元素对齐，因为他们不能设置宽度，行内元素或者行内块元素水平居中解决办法：
    * 给其父元素添加`text-align: center;`即可

  * **嵌套块元素垂直外边距的塌陷问题**

    子元素调整外边距时，子元素与父元素连在一起，子元素外边距不变父元素外边距变化的现象，解决方案：

    1. 可以为父元素定义上边框,`border: 1px solid transparent;`,添加一个透明的边界将父元素固定
    2. 可以为父元素定义内边距，例`padding: 1px;`，将父子元素分隔
    3. 可以为父元素添加`overflow:hiddenl`属性
    4. 还有其他方法，比如浮动、固定，绝对定位的盒子不会有塌陷问题

* 清除内外边距

  有些元素默认有内外边距，而且在不同浏览器可能不同，解决方法：

  ```css
  * {
  	/* 清除内边距 */
  	padding: 0;
  	/* 清除外边距 */
  	margin: 0;
  }
  ```

**注意∶行内元素为了照顾兼容性，尽量只设置左右内外边距，不要设置上下内外边距。如果确实需要设置上下内外边距，那就把行内元素转换为块级和行内块元素就可以设置了**

* `li`标签前面的小圆点取出方法：添加属性`list-style: none;`

这三种都是CSS3的特性

* 圆角边框

  * 设置元素外边框圆角，语法，例：`border-radius: 10px;`或`border-radius: 50%;`，后者也是利用正方形生成圆形的方法，`border-radius`后面还可以跟多个数值，表示不同的位置，还有其他表示位置的方法：
    * `border-top-left-radius`左上角
    * `border-top-right-radius`右上角
    * `border-bottom-left-radius`左下角
    * `border-bottom-right-radius`右下角

* 盒子阴影

  * `box-shadow`属性为盒子添加阴影，使用语法：`box-shadow: 10px 10px 10px 10px black;`其中参数值分别为阴影左右偏移位置，上下偏移位置，阴影虚实程度，阴影大小，阴影颜色 ，最后还可以加一个是否选择内阴影，如果是写上inset属性值，默认是外阴影

  **注意：默认的是外阴影(outset),但是不可以写这个单词，否则导致阴影无效。盒子阴影不占用空间，不会影响其他盒子排列。**

  * 前面两个属性值必须写，后面的可以省略，按默认值
  * 阴影的颜色部分可以用rgba()来设置，增加颜色的透明度更自然一点

* 文字阴影

  * `text-shadow`属性值,例：`text-shadow: 5px 5px 6px rgba(0,0,0,0.3);`

* 网页布局三种传统方式：标准流，浮动，定位

  **网页布局第一原则：多个块级元素纵向排列找标准列，多个块元素横向排列找浮动**

* 标准流：标签按照规定好的默认方式排列

### CSS浮动

可以改变元素标签默认的排列方式，语法，例：`float: left;`,属性值可以为none，left，right，float属性用于创建浮动框，将其移动到一边，直到左边缘或右边缘触及包含块或另一个浮动框的边缘。

* 浮动特性：

  * 浮动元素会脱离标准流（脱标）
    * 脱离标准流的控制移动到指定位置
    * 浮动的盒子不再保留原先的位置，如果两个盒子一个加了浮动一个没浮动，就会形成叠加（遮盖）效果，浮动的盒子会遮盖未浮动的盒子

  * 如果给多个盒子加了浮动，后一个盒子会与前一个盒子上沿对齐，并在一行，当位置不够时就浮动在第二行
  * 同一种对齐方式的浮动会使盒子边沿贴合在一起
  * 加了浮动后，不论原来时什么类型的元素都变成行内块元素，如果行内元素有了浮动，就不需要进行转换块级或行内元素的转换就能直接设置高度和宽度

  **为了约束浮动元素位置,我们网页布局一般采取的策略是:先用标准流的父元素排列上下位置,之后内部子元素采取浮动排列左右位置.符合网页布局第一准侧**
  
* 常见网络布局：

  * 垂直排列
  * 左右排列

  **不设置宽度就是默认和浏览器宽度一样**

  * 布局注意点：

    * 浮动与标准流父元素搭配使用

    * 浮动不会压住前面的标准流，浮动的盒子只能压住后面的标注流

    * 一个元素浮动了理论上其余兄弟元素也要浮动，防止引发问题

    * 有些情况下不适合给父盒子固定高度，不应该给父盒子高度，但是滋贺子浮动又不占有位置，使得父级盒子高度自动调整为0了，就会影响下面的标准流盒子，因此需要**清除浮动**：

      * 清除浮动的策略时：闭合浮动。清除浮动之后，父级就会根据浮动的子盒子自动检测高度。父级有了高度，就不会影响下面的标准流了，语法，例：`div {clear: left;}`属性值可以为：

        * left，表示不允许左侧有浮动
        * right，表示不允许右侧有浮动
        * both，同时清理左右两侧的浮动影响

        实际中基本上都用`div {clear: both}`

      清除浮动的方法：

      1. 额外标签法也称为隔墙法，是W3C推荐的做法，是指在浮动元素末尾加上一个空标签，例如`<div style=" clear:both"></div>` ，或者其他标签`<br>`等

         * 缺点∶添加许多无意义的标签，结构化较差，**注意此方法要求加入的空标签必须是块级元素，不能是行内元素**

      2. 父级添加overflow属性

         可以给父级添加overflow属性，将其属性值设置为hidden、auto或 scroll ，常用hidden属性值，例：`div { overflow: hidden;}`，

         * **注意是给父元素添加overflow属性**，缺点∶无法显示溢出的部分

      3. 父级添加`:after`伪元素（这种方法比较高级），语法，例：

         ```html
         <!DOCTYPE html>
         <html lang="en">
         
         <head>
             <meta charset="UTF-8">
             <meta http-equiv="X-UA-Compatible" content="IE=edge">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <title>伪元素浮动处理</title>
             <style>
                 /* 定义伪元素浮动处理的类，在父元素中进行调用 */
                 .clearfix:after {
                     content: "";
                     display: block;
                     height: 0;
                     clear: both;
                     visibility: hidden;
                 }
         
                 .clearfix {
                     /* IE6、7专有 */
                     *zoom: 1;
                 }
         		/* 父元素father没有设置高度，子元素的浮动会造成父元素高度自动调整为0，那么后面的anotherman元素就会挤占到本属于父元素的位置 */
                 .father {
                     width: 300px;
                     background-color: blueviolet;
                 }
         
                 .father>div {
                     float: left;
                     background-color: bisque;
                     width: 100px;
                     height: 50px;
                     margin-left: 10px;
                     margin-bottom: 10px;
                 }
         
                 .anotherman {
                     background-color: cyan;
                     height: 50px;
                 }
             </style>
         </head>
         
         <body>
             <div class="father clearfix">
                 <div class="child1">child1</div>
                 <div class="child2">child2</div>
             </div>
             <div class="anotherman"></div>
         </body>
         
         </html>
         ```

         

      4. 父级添加双伪元素

         也是给父元素添加，相当于给浮动的子元素前后都添加了空标签，语法，例：

         ```html
         <!DOCTYPE html>
         <html lang="en">
         
         <head>
             <meta charset="UTF-8">
             <meta http-equiv="X-UA-Compatible" content="IE=edge">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <title>浮动处理</title>
             <style>
                 /* 给浮动子元素前后都设置空标签，clearfix类还是用在父标签中 */
                 .clearfix:before,
                 .clearfix:after {
                     content: "";
                     display: table;
                 }
                 .clearfix:after {
                     clear: both;
                 }
                 .clearfix {
                     /* IE6、7专有 */
                     *zoom: 1;
                 }
         
                 .father {
                     width: 300px;
                     background-color: blueviolet;
                 }
         
                 .father>div {
                     float: left;
                     background-color: bisque;
                     width: 100px;
                     height: 50px;
                     margin-left: 10px;
                     margin-bottom: 10px;
                 }
         
                 .anotherman {
                     background-color: cyan;
                     height: 50px;
                 }
             </style>
         </head>
         
         <body>
             <div class="father clearfix">
                 <div class="child1">child1</div>
                 <div class="child2">child2</div>
             </div>
             <div class="anotherman"></div>
         </body>
         
         </html>
         ```

### 定位

可以让盒子自由的在某个盒子内移动位置或者固定屏幕中某个位置，并且可以压住其他盒子

* 定位=定位模式＋边偏移。定位模式用于指定一个元素在文档中的定位方式。边偏移则决定了该元素的最终位置。

  * 定位模式
    定位模式决定元素的定位方式，它通过CSS的position属性来设置，其值可以分为四个:

    * static静态定位

      是元素的默认定位方式，无定位的意思，语法，例：`div {position: static;}`

      * 静态定位按照标准流特性摆放位置，没有边偏移
      * 静态定位布局中很少用

    * relative相对定位

      是元素在移动的时候是相对于它原来的位置来说的（自恋），语法，例：`div {position: relative;}`

      * 它是相对自己原来的位置移动
      * 原来在标准流的位置继续占有，后面的盒子依然一标准流的方式对待它，不脱标，最典型的应用就是给绝对定位当爹。

    * absolute绝对定位

      元素移动位置的时候是相对它的祖先元素来说的（拼爹型），语法，例：`div {position: absolute;}`

      * 如果没有祖先元素或者祖先元素没有定位，则以浏览器为基准进行定位
      * 如果祖先元素有定位（relative，absolute，fixed）则以最近一级有定位的祖先元素为参考点移动
      * 绝对定位不再占有原先的位置（脱标）

    * fixed固定定位

      在浏览器可视窗口中定位，跟父元素无关，固定定位不占有原先位置（脱标），不随滚动条滚动更变化位置，语法，例：`div {position: fixed;}`

      

    * Sticky粘性定位

      可以被认为是相对定位和固定定位的混合。Sticky 粘性的语法，例︰`div { position: sticky; top: 10px; }`
      粘性定位的特点∶

      1. 以浏览器的可视窗口为参照点移动元素（固定定位特点)

      2. 粘性定位占有原先的位置（相对定位特点)

      3. 必须添加top . left、right、bottom其中一个才有效

      4. 跟页面滚动搭配使用。兼容性较差，IE不支持。可以用JavaScript实现

         

    **定位特殊特性**
    绝对定位和固定定位也和浮动类似，有一下特点：

    1. 行内元素添加绝对或者固定定位，可以直接设置高度和宽度。

    2. 块级元素添加绝对或者固定定位，如果不给宽度或者高度，默认大小是内容的大小。

    3. 脱标的盒子不会触发外边距塌陷，浮动元素、绝对定位(固定定位)元素的都不会触发外边距合并的问题。

    4. 绝对定位（固定定位)会完全压住盒子，而浮动元素不同，只会压住它下面标准流的盒子，但是不会压住下面标准流盒子里面的文字(图片)，但是绝对定位(固定定位）会压住下面标准流所有的内容。

       * 浮动之所以不会压住文字，因为浮动产生的目的最初是为了做文字环绕效果的。文字会围绕浮动元素，实现环绕文字的效果

       

    * 定位堆叠顺序

      z-index属性决定盒子的叠放次序，语法，例：`z-index: 1`

      * 属性值为整数（可正可负可为零）可为auto，数字越大越叠在最上面
      * 如果属性值相同，则按照书写顺序，后来居上
      * 属性值不能加单位
      * z-index属性只能用在定位的盒子上

    

    **固定定位小技巧∶固定在版心右侧位置**

    1. 让固定定位的盒子left: 50%.走到浏览器可视区（也可以看做版心）的一半位置
    2. 让固定定位的盒子margin-left:版心宽度的一半距离。多走版心宽度的一半位置就可以让固定定位的盒子贴着版心右侧对齐了。

    **固定定位小技巧：绝对定位的盒子居中**

    加了绝对定位的盒子不能通过 margin:Oauto水平居中，但是可以通过以下计算方法实现水平和垂直居中：

    * left: 50%;:让盒子的左侧移动到父级元素的水平中心位置

    * margin-left:-100px; :让盒子向左移动自身宽度的一半

      

  #### 子绝父相

  太重要了，是我们学习定位的口诀，是定位中最常用的一种方式，这句话的意思是∶子级是绝对定位的话，父级要用相对定位。

  * 子级绝对定位，不会占有位置，可以放到父盒子里面的任何一个地方，不会影响其他的兄弟盒子。
  * 父盒子需要加定位限制子盒子在父盒子内显示。
  * 父盒子布局时，需要占有位置，因此父亲只能是相对定位。

  这就是子绝父相的由来，所以相对定位经常用来作为绝对定位的父级。
  总结︰因为父级需要占有位置，因此是相对定位，子盒子不需要占有位置，则是绝对定位当然，子绝父相不是永远不变的，如果父元素不需要占有位置，子绝父绝也会遇到。

  

  * 边偏移，定位盒子移动到最终位置，有一下四个属性：

    * top顶端偏移量，定位元素相对于父元素上边线的距离，例：`top: 80px;`
    * bottom底端偏移量，定位元素相对于父元素下边线的距离，例：`bottom: 80px;`
    * left左端偏移量，定位元素相对于父元素左边线的距离，例：`left: 80px;`
    * right右端偏移量，定位元素相对于父元素右边线的距离，例：`right: 80px;`

    **如果一个盒子既有left属性也有right属性，则默认会执行left属性,同理top bottom 会执行 top属性**

### 网页布局总结

* 通过盒子模型，清楚知道大部分html标签是一个盒子
* 通过CSS浮动、定位可以让每个盒子排列成为网页
* 一个完整的网页，是标准流、浮动、定位一起完成布局的，每个都有自己的专门用法
* 标准流可以让盒子上下排列或者左右排列，垂直的块级盒子显示就用标准流布局
* 浮动可以让多个块级元素一行显示或者左右对齐盒子，多个块级盒子水平显示就用浮动布局
* 定位最大的特点是有层叠的概念，就是可以让多个盒子前后叠压来显示。如果元素自由在某个盒子内移动就用定位布局



* 元素的显示与隐藏

  * display显示隐藏，语法，例：`display: none;`隐藏对象，隐藏后不再占有位置,`display: block;`这个代码除了将元素转化成块元素外还有显示元素的功能

  * visibility显示隐藏，语法，例：`visibility: visible;`元素可见,`visibility: hidden;`元素隐藏，隐藏后继续占有原来的位置，隐藏后再刷新页面就可见了

  * overflow溢出显示隐藏，overflow属性指定了如果内容溢出一个元素的框（超过其指定高度及宽度）时，会发生什么，属性值如下：

    * visible不剪切内容也不添加滚动条

    * hidden不显示超过对象尺寸的内容，超出的部分隐藏掉

    * scroll不管超出内容否，总是显示滚动条

    * auto超出自动显示滚动条，不超出不显示滚动条
      **一般情况下，我们都不想让溢出的内容显示出来，因为溢出的部分会影响布局。**

      **但是如果有定位的盒子，请慎用overflow:hidden因为它会隐藏多余的部分**



### CSS高级技巧

#### 精灵图

一个网页中往往会应用很多小的背景图像作为修饰，当网页中的图像过多时，服务器就会频繁地接收和发送请求图片，造成服务器请求压力过大，这将大大降低页面的加载速度。
因此，为了有效地减少服务器接收和发送请求的次数，提高页面的加载速度，出现了CSS精灵技术(也称css Sprites、CSS雪碧)。
核心原理∶将网页中的一些小背景图像整合到一张大图中，这样服务器只需要一次请求就可以了。

* 精灵图( sprites )的使用
  使用精灵图核心∶
  1. 精灵技术主要针对于背景图片使用。就是把多个小背景图片整合到一张大图片中
  2. 这个大图片也称为sprites精灵图或者雪碧图
  3. 插入图片，用`background: url();`插入精灵图
  4. 移动背景图片位置，此时可以使用background-position
  5. 移动的距离就是这个目标图片的x和y坐标。注意网页中的坐标有所不同
  6. 因为一般情况下都是往上往左移动，所以数值是负值
  7. 使用精灵图的时候需要精确测量每个小背景图片的大小和位置
  8. 精灵图主要针对于小的背景图片使用。
  9. 一般情况下精灵图都是负值。(千万注意网页中的坐标∶x轴右边走是正值，左边走是负值，y轴同理。)

精灵图的处理在PS中就能进行选中要产生精灵图的原图片，将其导出为图片，然后用ps打开该图片，在想要图片所在位置用切片工具选中，右键选择切片选项，查看其中的width和height就是盒子宽高，x，y对应想要的图片在原图片中的相对位置，在代码中就给整两个值分别取相反数就是代码里的background-position的两个参数了

#### 边框图片

适用场景：盒子大小不一，边框样式相同，此时需要借助边框图片技术完成

css3中新增属性border-image属性，指定一个图片作为边框背景，并对边框图片进行一定的操作

边框图片切图操作：为了保留四个角的样式作为边框图片的共同样式，其余地方进行平铺或拉伸

方法：把四个角切出去（九宫格的由来)，中间部分可以铺排、拉伸或者环绕。按照上右下左的顺序进行切割（先得到第一刀据上边框的距离，在得到第二刀据右边框的距离，按照这样的顺序）

边框图片相关的属性：

* border-image-source

  用在边框的图片的路径（那个图片? )

* border-image-slice
  图片边框向内偏移（裁剪的尺寸，***一定不加单位***，上右下左顺序）

* border-image-width
  图片边框的宽度（**需要加单位px**)(不是边框的宽度是边框图片的宽度)

* border-image-repeat
  图像边框是否应平铺(repeat)、铺满(round)或拉伸(stretch)*默认拉伸*

#### 字体图标

字体图标iconfont，为前端工程师提供一种方便高效的图标使用方式，展示的是图标，本质属于字体。

字体图标的优点

* 轻量级︰一个图标字体要比一系列的图像要小。一旦字体加载了，图标就会马上渲染出来，减少了服务器请求
* 灵活性:本质其实是文字，可以很随意的改变颜色、产生阴影、透明效果、旋转等
* 兼容性:几乎支持所有的浏览器，请放心使用
* 注意:字体图标不能替代精灵技术，只是对工作中图标部分技术的提升和优化。

总结∶

1. 如果遇到一些结构和样式比较简单的小图标，就用字体图标
2. 如果遇到一些结构和样式复杂一点的小图片，就用精灵图

* 字体图标的下载
  推荐下载网站:

  * icomoon字库http://icomoon.io推荐指数★★★★★
    lcoMoon成立于2011年，推出了第一个自定义图标字体生成器，它允许用户选择所需要的图标，使它们成一字型。该字库内容种类繁多，非常全面，唯一的遗憾是国外服务器，打开网速较慢。
    
  * 阿里iconfont字库http://www.iconfontcn/推荐指数★★★★★
    这个是阿里妈妈M2UX的一个iconfont字体图标字库，包含了淘宝图标库和阿里妈妈图标库。可以使用AlI制作图标上传生成。重点是，免费!
  
  * 阿里iconfont字库的使用方法见此[官方教程](https://www.iconfont.cn/help/detail?spm=a313x.7781069.1998910419.13.4uXHQh&helptype=code)
  
    举例，字体Unicode使用方法：
    
    字体文件从阿里的iconfont字库中下载下来，把里面的文件拷贝到项目文件夹中，然后在代码中如下使用：
    
    ```html
    
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>字体图标的使用</title>
        <style>
            /* 这段引入必须有 */
            @font-face {
                font-family: 'iconfont';
                src: url('iconfont.woff2?t=1627226688474') format('woff2'),
                    url('iconfont.woff?t=1627226688474') format('woff'),
                    url('iconfont.ttf?t=1627226688474') format('truetype');
            }
    
            /* 这里定义了一个iconfont的类用于使用的时候进行调用 */
            /* 类的名字无所谓，但是里面内容要和此例一样（除了font-size可设置或其他字体属性如color） */
            .iconfont {
                font-family: "iconfont" !important;
                font-size: 18px;
                font-style: normal;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
    
            /* 就像这里创建了一个叫test的类，可以更改里面的font-size和color属性 */
            .test {
                font-family: "iconfont" !important;
                font-size: 16px;
                color: blueviolet;
                font-style: normal;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
        </style>
    </head>
    
    <body>
        <span class="iconfont">&#xe673;</span>
        <span class="test">&#xe673;</span>
        <span class="test">&#xe66f;</span>
    </body>
    
    </html>
    ```
    
    
    
    

#### CSS三角

网页中常见一些三角形，使用CSS直接画出来就可以，不必做成图片或者字体图标，原理：一个没有高度和宽度的盒子，其每个边就代表一个三角（三角指向内部），利用一个边设置颜色其余三边设为透明色可以达到三角的制作目的。

#### CSS用户界面样式

* 更改用户鼠标样式

  利用鼠标的cursor属性，例：

  ```html
  <ul>
      <li style="cursor: default;">我是默认的小白鼠标样式</li>
      <li style="cursor: pointer;">我是鼠标小手样式</li>
      <li style="cursor: move;">我是鼠标移动样式</li>
      <li style="cursor: text;">我是鼠标文本样式</li>
      <li style="cursor: not-allowed">我是鼠标禁止样式</li>
  </ul>
  ```

#### 表单轮廓

给表单添加`outline:0;`或者`outline: none;`样式之后，就可以去掉输入边框的默认蓝色边框。
例：`input { outline: none; }`

#### 防止表单域拖拽

例：`textarea { resize: none;}`

#### vertical-align属性应用

多用于文字和图片、表单对齐效果，vertical-align属性值：bottom，top，middle，base，默认是基线对齐。注意：用于对齐的元素必须为行内元素或行内块元素

例：`<img src="1.jpg" alt="" style="vertical-align: middle">This is a test.`

#### 解决图片底部默认空白缝隙问题
bug :图片底侧会有一个空白缝隙，原因是行内块元素会和文字的基线对齐。主要解决方法有两种:
1．给图片添加`vertical-align: middle|top|bottom;`（提倡使用的)
2．把图片转换为块级元素`display: block;`

#### 溢出的文字省略号

例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文字单行省略号显示</title>
    <style>
        .singleellipsis {
            width: 150px;
            height: 100px;
            background-color: bisque;
            /* 文字强制单行显示 */
            white-space: nowrap;
            /* 单行显示后多余文字隐藏 */
            overflow: hidden;
            /* 多余部分省略号显示 */
            text-overflow: ellipsis;
        }
    </style>
</head>

<body>
    <div class="singleellipsis">This is a test.This is a test.This is a test.</div>
</body>

</html>
```



#### 显示常见布局技巧

* margin负值的运用

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>利用margin负值合并边框</title>
      <style>
          ul li {
              float: left;
              list-style: none;
              width: 150px;
              height: 200px;
              border: 1px solid red;
              /* 利用margin属性负值将每个盒子向左移动边框宽度大小,
              盒子浮动后紧贴，之后左移就会使边框重叠 */
              margin-left: -1px;
          }
      </style>
  </head>
  <body>
      <ul>
          <li>1</li>
          <li>2</li>
          <li>3</li>
  
      </ul>
  </body>
  </html>
  ```

  这种方式能让盒子边框重叠显示，但是如果要单独对盒子进行样式设置时，这种重叠效果又会成为阻碍，这时通过提高当前盒子的层级解决此问题(如果没有有定位，则加相对定位（保留位置），如果有定位，则加z-index设置显示优先级 )

* 文字围绕浮动元素

  利用浮动时不会压住文字的特性将图片设置为浮动，则其下的文字就被挤到盒子的其他位置

* 行内块的巧妙运用

  在一行里的行内块元素会自动产生间隔，并且给父盒子加属性时会应用到全部行内块元素的特点

* css三角强化

  通过改变无宽高的盒子的边框宽度实现三角形的大小形状变化，产生不同形状的三角形，例：

  ```html
  <style>
  .zhijiao {
              width: 0px;
              height: 0px;
              margin-top: 20px;
              border-top: 40px solid transparent;
              border-bottom: 0px solid transparent;
              border-left: 20px solid transparent;
              border-right: 20px solid lawngreen;
          }
  </style>
  <body>
      <div class="zhijiao"></div>
  </body>
  ```


#### CSS初始化

不同浏览器对有些标签的默认值是不同的，为了消除不同浏览器对HTML文本呈现的差异，照顾刘览器的兼容，我们需要对CSS初始化

简单理解:CSS初始化是指重设浏览器的样式。(也称为CSS reset )每个网页都必须首先进行CSS初始化。

Unicode编码字体∶
把中文字体的名称用相应的Unicode编码来代替，这样就可以有效的避免浏览器解释CSS代码时候出现乱码的问题。
比如︰
黑体`\9ED1\4F53` 

宋体`5B8B\4F53`
微软雅黑`\5FAE\8F6F\96C5\9ED1`



### HTML5新特性

这些新特性都有兼容性问题，基本是IE9+以上版本的浏览器才支持，如果不考虑兼容性问题，可以大量使用这些新特性。

* HTML5新增的语义化标签

  <header>: 头部标签
  <nav>: 导航标签
  <article>: 内容标签
  <section>: 定义文档某个区域
  <aside>: 侧边栏标签
  <footer>: 尾部标签

  注意：

  * 这种语义化标准主要是针对搜索引擎的
  * 这些新标签页面中可以使用多次
  * 在IE9中，需要把这些元素转换为块级元素
  * 其实，我们移动端更喜欢使用这些标签
  * HTML5还增加了很多其他标签

* 新增多媒体标签

  HTMLS在不使用插件的情况下，也可以原生的支持视频格式文件的播放，当然，支持的格式是有限的。
  视频<video>标签
  当前<video>元素支持三种视频格式，尽量使用mp4格式

  video标签的属性：

  * src，属性值是视频链接

  * autoplay，属性值是autoplay时视频自动播放
  * muted，属性值是muted时静音播放
  * loop，属性值是loop时视频循环播放
  * poster，属性值是图片的地址，规定视频未加载完成时显示的图片
  * width和height属性设置播放器宽度高度
  * controls，属性值controls向用户显示播放控件

* 新增音频标签<audio>

  HTML5在不使用插件的情况下，也可以原生的支持音频格式文件的播放，当然，支持的格式是有限的，建议用mp3格式，常见属性：

  * autoplay
  * controls
  * loop
  * src

**注意：谷歌浏览器把音频和视频自动播放禁止了，可通过给视频标签添加muted属性来静音自动播放视频，但是音频不行**

更多标签属性详见菜鸟教程网站

* 新增的input特性，例：

  ```htmml
  <input type="email" />
  <input type="search" />
  <input type="number" />
  <input type="tel" />
  ```

* 新增的表单属性
  * required属性，属性值required表示输入不能为空
  * placeholder属性，值是用于提示的文本，可用`input::placeholder{color: red;}`的方式进行字体颜色的设置
  * autofocus属性，属性值为autofocus，用于设置当前位置为默认焦点位置
  * autocomplete属性值off或on，用于记住输入记录，一般用off关掉
  * multiple属性值，属性multiple设置可以多选文件提交

* CSS3新特性

  * 新增选择器

    * 属性选择器

      属性选择器可以根据元素特定属性的来选择元素。这样就可以不用借助于类或者id选择器。例：

      * E[att] 用于选择具有att属性的E元素，例：`input[type]{}`
      * E[att="val"] 选择具有att属性且属性值等于val 的E元素，例：`input[type="password"]{}`
      * E[att4="val"] 匹配具有att属性且值以val开头的E元素
      * E[att$="val"] 匹配具有att属性且值以val结尾的E元素
      * E[att*="val"] 匹配具有att属性且值中含有val 的E元素

      **注意∶类选择器、属性选择器、伪类选择器，权重为10。**

    * 结构伪类选择器

      根据文档结构来选择元素，常用于根据父级选择里面的子元素

      * att E:first-child{}匹配父元素att中第一个子元素，子元素需是E类型

      * att E:last-child{}匹配父元素att中的第一个子元素，子元素需要是E类型

      * att E:nth-child(n){}，括号中的n是指第几个孩子，从1开始计数，n可以是数字，关键字和公式，

        * 如果是关键字，则有不同选择效果，关键字如下：
          * 关键字even，选择偶数的子元素
          * 关键字odd，选择计数的子元素

        * 如果是公式，则有其他选择效果，用法如下：
          * n选择全部子元素
          * 2n选择偶数的子元素
          * 2n+1选择奇数的子元素
          * 5n选择5的正整数倍数的子元素
          * n+5选择从第5个开始（包含5）到最后的子元素
          * -n+5选择前5个（包含5）

      * att E:first-of-type(n)用法和上面基本相同
      * att E:last-of-type(n)
      * att E:nth-of-type(n)

      **区别:**

      1. E:nth-child(n)对父元素里面所有孩子排序选择(序号是固定的）先找到第n个孩子，然后看看是否和E匹配
      2. E:nth-of-type(n)对父元素里面指定子元素进行排序选择。先去匹配E，然后再根据E找第n个孩子

    * 伪元素选择器

      伪元素选择器可以帮助我们利用CSS创建新标签元素，而不需要HTML标签，从而简化HTML结构，选择符：

      * `::before`在元素内部的前部插入内容
      * `::after`在元素内部的后部插入内容

      * 语法：`element::before{}`，before和after必须有content属性

      * 伪元素选择器和标签选择器一样，权重为1

      * before和after创建一个元素，但是属于行内元素

      * 新创建的元素在文档树中是找不到的，因此称伪元素

      * 伪元素在使用的时候，例：`.test::before{content:'';}`，`.test:hover::before{}`实现鼠标经过的效果

      * 伪元素清除浮动，用双伪元素在元素前后分别插入before和after实现闭合清除浮动，也可单侧清除浮动，例：

        ```html
        .clearfix::after {
                    /* after伪类选择器必须的属性 */
                    content: "";
                    /* 插入的盒子必须是块级元素 */
                    display: block;
                    /* 让高度是0隐藏起来 */
                    height: 0;
                    /* 清除浮动的核心代码 */
                    clear: both;
                    /* 隐藏元素 */
                    visibility: hidden;
                }
        ```

  

  * CSS3 2D转换transform
  
    * 移动translate
  
      * 类似定位，可以改变元素位置，语法，例：`transform: translate(x,y);` x，y的单位是px像素

      * translate最大的优点：不会影响其他元素的位置，其中x和y也可以是百分比，是相当于自身元素大小的百分比进行移动

      * translate对于行内元素是无效的
  
    * 旋转rotate
  
      * 默认绕盒子元素中心进行旋转，语法，例：`transform: rotate(deg);` 其中deg是度数，单位是deg，要带着单位写，为正数时是顺时针，反之为逆时针，例：`tranform: rotate(45deg);`，利用rotate可以做出三角图标：盒子两个边有颜色，两个边为透明，然后对盒子进行45°旋转，形成三角图标
      * 可以对旋转参照点进行修改，利用`transform-origin`属性，语法`tranform-origin: x y;`，例：`transform-origin: left bottom;`就是绕着元素的左下角进行旋转，x和y为方位名词，当然x和y也可以为像素，要带单位，也可为百分比，默认为50%

    * 缩放scale
  
      * 缩放，可以等比例，也可以宽高不等比例缩放，语法`transform: scale(x,y);`，例：`transform: scale(2,0.5);` 就是宽变为之前的2倍，高变为之前的0.5倍，也可以进行等比例缩放的简写：`tranform: scale(2)`就是指宽和高都变为之前的2倍
      * 优势：默认相对于元素中心进行缩放，不会影响其他元素位置，也可以通过transform-origin属性设置缩放中心点

    * 这是利用旋转和缩放建立的一个例子：

      ```html
      <!DOCTYPE html>
      <html lang="en">
      
      <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>盒子旋转缩放动画</title>
          <style>
              .father {
                  width: 300px;
                  height: 300px;
                  margin: 200px auto;
                  /* 隐藏子盒子 */
                  overflow: hidden;
                  /* 父盒子进行大小scale变换 */
                  transition: all 1s;
                  background-color: gold;
              }
      
              .father::after {
                  content: "";
                  display: block;
                  width: 100%;
                  height: 100%;
                  transform-origin: left bottom;
                  transform: rotate(90deg);
                  background-color: greenyellow;
                  /* 子盒子进行旋转rotate变换 */
                  transition: all 1s;
              }
      
              .father:hover::after {
                  transform: rotate(0deg);
              }
      
              .father:hover {
                  transform: scale(2);
              }
          </style>
      </head>
      
      <body>
          <div class="father"></div>
      </body>
      
      </html>
      ```
  
      这个效果还蛮好看的
  
    * transform的属性一般搭配上transition属性进行使用能实现简单的动画效果
  
    * 同时使用多个transform转换进行搭配，其语法为：`transform: translate() rotate() scale();` 其书写顺序会影响到实现效果，先旋转会改变坐标轴方向，当有位移要求是记得将位移translate()放在最前面

* CSS动画

  动画可以通过设置多个节点来精准控制一个或一组动画，常用来实现复杂的动画效果，相比较过渡，动画能够实现连续自动播放等效果

  * 动画的使用方法：1. 定义动画 2. 使用动画

  * 例：

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>动画的使用</title>
        <style>
            /* 动画的定义,实现网站打开后盒子从左边向右平移一段距离 */
            @keyframes anim {
    
                /* 动画的初始状态 */
                0% {
                    transform: translate(0px);
                }
                50%{
                    transform: translate(500px);
                }
                /* 动画的结束状态 */
                100% {
                    transform: translate(1000px);
                }
            }
    
            div {
                width: 100px;
                height: 100px;
                background-color: gold;
                /* 调用定义好的动画 */
                animation-name: anim;
                /* 规定动画的持续时间 */
                animation-duration: 2s;
            }
        </style>
    </head>
    
    <body>
        <div></div>
    </body>
    
    </html>
    ```

    其中from关键字可以替代0%，to关键字可以替代100%，利用百分比可以设置动画的时间进程上的不同动作

  * 动画常用属性：

    * @keyframes 规定动画。
    
    * animation
      所有动画属性的简写属性，除了animation-play-state属性。
      
    * animation-name
      规定@keyframes动画的名称。(必须的)
      
    * animation-duration
      规定动画完成一个周期所花费的秒或毫秒，默认是0。(必须的)
      
    * animation-timing-function
      规定动画的速度曲线，默认是"ease"，还可以是步数"step"等。
      
      * 利用这个属性可以做出打字机的效果：
      
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>利用动画animation-timing-function属性值step实现打字机效果</title>
            <style>
                .typewriter {
                    font-size: 16px;
                    height: 20px;
                    line-height: 20px;
                    color: black;
                    animation: boxwidth 4s steps(20) forwards;
                    white-space: nowrap;
                    overflow: hidden;
                }
                @keyframes boxwidth {
                    0% {
                        width: 0px;
                    }
                    100% {
                        width: 400px;
                    }
                }
            </style>
        </head>
        <body>
            <div class="typewriter">
                这是一个打字机这是一个打字机这是一个打字机
            </div>
        </body>
        </html>
        ```
      
        
      
    * animation-delay
      规定动画何时开始，默认是0。
      
    * animation-iteration-count
      规定动画被播放的次数，默认是1，还有infinite是无限循环播放
      
    * animation-direction
      规定动画是否在下一周期逆向播放，默认是“normal ",alternate逆方向播放
      
    * animation-play-state
      规定动画是否正在运行或暂停。默认是"running",还有"paused"。
      
    * animation-fill-mode
      规定动画结束后状态，保持forwards回到起始backwards

* 动画简写，遵循下面格式： `animation: name duration timing-function delay iteration-count direction fill-mode;` 
  * 简写属性里面不包含animation-play-state
  * 暂停动画: `animation-play-state: puased;`
  * 经常和鼠标经过等其他配合使用想要动画走回来，而不是直接跳回来:`animation-direction : alternate`
  * 盒子动画结束后，停在结束位置: `animation-fill-mode : forwards`

  

### CSS3D转换

利用perspective透视实现，理解成安排一个光源在电脑屏幕外，之间是被观测物体，光源发出的光在物体上的投影投到电脑屏幕上，实现近大远小的效果，透视的单位是像素px

* 透视perspective写在想要实现3D效果元素的父元素上，大小代表光源距离屏幕的距离
* 当perspective固定下来之后，通过改变translateZ(物体距离屏幕的距离)同样能实现3D效果，值越大物体越大
* 3D旋转rotate3d
  * 默认3D坐标轴的轴心在盒子的中心
  * 旋转正方向由左手定则判断，拇指指向轴的正方向，四指弯曲方向就是旋转正方向
  * `transform: rotateX(deg);`沿着x轴旋转
  * `transform: rotateY(deg);`沿y轴
  * `transform: rotateZ(deg);`沿z轴
  * `transform: rotate3d(x,y,z,deg);`x，y，z表示旋转轴的矢量，最终的旋转轴由这三个矢量合成来计算，最后一个表示旋转的角度
* transform-style属性，控制子元素是否开启三维立体环境
  * 属性值默认为flat子元素不开启三位立体环境，属性值还可以为preserve-3d子元素开启三维空间环境
  * 这个属性代码写给父元素，但是执行的效果在子元素
* 同时具有移动和旋转属性时要把移动属性放在前面

* 通过3D变换制作木马旋转图的效果：

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>3D旋转实现旋转木马效果</title>
      <style>
          body {
              perspective: 1000px;
          }
  
          section {
              position: relative;
              width: 300px;
              height: 200px;
              margin: 300px auto;
              /* 子元素开启3D立体环境 */
              transform-style: preserve-3d;
              /* 动画调用，让大盒子旋转起来 */
              animation: rotate 5s linear infinite;
          }
  
          /* 当鼠标经过的时候停止旋转 */
          section:hover {
              animation-play-state: paused;
          }
  
          /* 设定图片的大小 */
          section div img {
              width: 100%;
              height: 100%;
          }
  
          section div {
              position: absolute;
              left: 0px;
              top: 0px;
              width: 100%;
              height: 100%;
          }
  
          section div:nth-of-type(1) {
              transform: translateZ(300px);
          }
  
          section div:nth-of-type(2) {
              transform: rotateY(60deg) translateZ(300px);
          }
  
          section div:nth-of-type(3) {
              transform: rotateY(120deg) translateZ(300px);
          }
  
          section div:nth-of-type(4) {
              transform: rotateY(180deg) translateZ(300px);
          }
  
          section div:nth-of-type(5) {
              transform: rotateY(240deg) translateZ(300px);
          }
  
          section div:nth-of-type(6) {
              transform: rotateY(300deg) translateZ(300px);
          }
  
          /* 动画样式的定义 */
          @keyframes rotate {
              0% {
                  transform: rotateY(0deg);
              }
  
              100% {
                  transform: rotateY(360deg);
              }
          }
      </style>
  </head>
  
  <body>
      <!-- section作为大盒子装六张图片盒子 -->
      <section>
          <!-- 每个小盒子中分别装一张图片 -->
  <!-- 这里为了方便都装的是一张图片，可根据自己的文件目录选择背景图片 -->
          <div><img src="./images/1.jpg" alt=""></div>
          <div><img src="./images/1.jpg" alt=""></div>
          <div><img src="./images/1.jpg" alt=""></div>
          <div><img src="./images/1.jpg" alt=""></div>
          <div><img src="./images/1.jpg" alt=""></div>
          <div><img src="./images/1.jpg" alt=""></div>
      </section>
  </body>
  
  </html>
  ```

  



* CSS3盒子模型

  CSS3中可以通过 box-sizing来指定盒模型，属性值可指定为content-box或border-box，这样我们计算盒子大小的方式就发生了改变。
  可以分成两种情况：

  1. `box-sizing: content-box`盒子大小为width + padding + border (默认)
  2. `box-sizing: border-box`盒子大小为width，如果盒子模型改为了`box-sizing: border-box`，那padding和border就不会撑大盒子（前提padding和border不会超过width宽度)

* CSS3滤镜filter属性，用于将模糊或者颜色偏移等图形效果应用于元素，语法，例：`filter: blur(1px);`此语句中blur函数是添加模糊效果，数值越大越模糊，数值要加单位

* CSS3 计算calc函数，此CSS函数让你在声明CSS属性值时执行一些计算。如：`width: calc(100% - 80px);`放在子元素中能实现此子元素永远比父元素宽度小80px
  括号里面可以使用`+`,`-`,`*`,`/`来进行计算。

* 过渡(transition)

  是CSS3中具有颠覆性的特征之一，我们可以在不使用Flash 动画或JavaScript 的情况下，当元素从一种样式变换为另一种样式时为元素添加效果。

  * 过渡动画:是从一个状态渐渐的过渡到另外一个状态
    可以让我们页面更好看，更动感十足，虽然低版本浏览器不支持 ( ie9以下版本）但是不会影响页面布局。

  * 我们现在经常和:hover一起搭配使用。

  * 语法：transition:要过渡的属性 花费时间 运动曲线 何时开始;  ,谁做过渡给谁加。

    1. 属性：想要变化的css属性，宽度高度背景颜色内外边距都可以。如果想要所有的属性都变化过渡，写一个all就可以。
    2. 花费时间:单位是秒(必须写单位）比如0.5s
    3. 运动曲线:默认是ease (可以省略)
    4. 何时开始︰单位是秒(必须写单位)可以设置延迟触发时间默认是0s(可以省略)

    例：

    ```css
    div {
        width: 200px;
        height: 100px;
        background-color: pink;
        /* transition:变化的属性 花费时间 运动曲线 何时开始; */
        transition: width .5s ease 1s;
            }
    div:hover {
        width: 400px;
    }
    ```

    

    


### 浏览器私有前缀

* -moz-：代表firefox浏览器私有属性
* -ms-：代表IE浏览器私有属性
* -webkit-：代表safari、chrome私有属性
* -o-：代表Opera私有属性
* 例：`-moz-border-radius: 10px;`


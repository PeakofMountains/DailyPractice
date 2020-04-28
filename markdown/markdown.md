### Markdown的学习使用
![image](https://w.wallhaven.cc/full/13/wallhaven-13mk9v.jpg)

今天学习了怎么用Markdown来编辑一个文本通过[菜鸟教程](https://www.runoob.com/markdown/md-tutorial.html)

Markdown是一个功能强大的文字格式编辑器，能让文档好看起来，还能实现链接，图片等功能，学起来很简单，用的时候也不麻烦。

下面是我在学习和使用Markdown过程中的一些错误启示：
* 经过我的多次尝试，好像在GitHub上用markdown插入的图片只有`jpg`格式的能直接显示出来
* 在标题的使用时，符号'#'和要输入的文字之间要有一个空格才能识别为一个一级标题，其余的项目符号也一样
* 在段落的使用时，敲一个回车之后并没有默认换行，要手都敲两次回车，或者在上一行的末尾先敲两个空格再敲一下回车才能形成分行的效果(文字之前有项目符号的除外)
* 图片的插入使用时，如果后面有标记内容，括号里的图片地址和标记内容中间要有空格隔开
* ` ``` `来包裹一段代码，并指定代码的语言(也可以不指定)，实现代码段的效果，但是要注意一对` ``` `符号要上下对齐，同时要求代码必须严格对齐，注意大括号是否对齐，所有的大括号都不能超过类的修饰限定符之前
* 用单个的 ` 符号可以引用单行代码片段或者一个函数
* 分割线的使用要保证当前行没有其他符号、文字
* 用左右各一个`*`表示中间的字符是斜体格式，左右各两个`*`表示中间的字符加粗，左右各三个`*`表示中间的字符加粗倾斜，要注意左右的`*`与紧挨着的字符之间不能有空格，否则格式失效。
* 也可以用`<`和`>`来将链接括起来，直接表示一个链接
* 可以用文字后面加`[comment]`表示中括号里的`comment`是前面的文字的注释，可以在文末用`[comment]:comments`输入注释的内容，同一个文件中`[comment]`这个括号内的名字是唯一的
* 关于表格的制作：第一行为标题栏，第二行为分割栏，下面的其余行是表格的内容，不同的板块之间都用`|`进行分割，通过修改第二行可以改变表格的排版样式如`|---------|---------|`这样子，像这样`|:----------|-----------:|`把`:`加在左边就是左对齐，加在右边就是右对齐，左右都加上就是中间对齐，最两边的`|`可以不打，默认是有的
* 缩进的处理：用`&emsp`表示缩进一个中文字符，用`&ensp`缩进半个中文字符，用`&nbsp`缩进四分之一的中文字符，后面再编辑内容就行了
* 可以用html的标签格式实现居中处理：```<div align=center>  内容  </div>  ```实现的效果就是将内容居中显示，可以是文字也可以是图片


下面几条参考了[这位博主的文章](https://www.jianshu.com/p/3344f61b053c)方法介绍


* 如果要修改图片大小，可以使用HTML的处理方式来插入图片，并设置固定大小,例如这种格式：`<img src="https://raw.githubusercontent.com/linux-downey/bloc_test/master/picture/Makedown/Makedown.png" width=100 height=60 />`
* 同时，也可以按照比例来设置图片大小，例如这种格式：`<img src="https://raw.githubusercontent.com/linux-downey/bloc_test/master/picture/Makedown/Makedown.png" width="%50" height="%50" />`
* 用markdown插入视频的方法：`<video src="http://qiniu.swarma.org/newUser.mp4" controls="controls" width="100%" height="auto"/>`  `src`：视频地址  `controls`：显示或隐藏播放器 `true/false` , `width` ：播放器宽度 , `height`：播放器的高度  **现在的GitHub并不支持插入视频，可以通过放置链接实现**
* 设置字体颜色和大小：
  > 设置字体颜色：`<font color="#FF4500">我要变成这个颜色#FF4500</font>`
  
    > [十六进制颜色对照表](https://www.w3school.com.cn/cssref/css_colornames.asp)
    
  > 设置字体大小：`<font size="1">我要变成1号字</font>`
  
  > 设置文字背景颜色：`<table><tr><td bgcolor="#7FFF00">我要变成#7FFF00背景色</td></tr></table>`
  
  
* ***GitHub并不支持所有的markdown格式***  

* * * * * *

# JAVA Learning

![image](https://w.wallhaven.cc/full/5d/wallhaven-5dlky9.jpg)

## 本次实验中解决的问题和要注意的知识
* 实验楼的平台不同于eclipse，他只是Java编辑器，不用新建project和package
* char 类型不同于C 语言的char，java的char占用的是两个字节
* 使用 long 修饰的变量需要在数值后面加上 L 或者 l，比如 long num = 1L;，一般使用大写 L，为了避免小写 l 与数值 1 混淆。
* float 类型的数值后面需要加上 F 或者 f，否则会被当成 double 类型处理。
* double 类型的数值可以加上 D 或 d，也可以不加。
* 字符 a 也可以写成char a = 97(十进制)，也可以用十六进制表示char a = '\u0061'。
* Java 中布尔值不能和整数类型或者其它类型互相转换。
* 中文字符也是一个字符
* **字符串内容比较用equals()方法，而使用 "==" 比较的是两个对象在内存中存储的地址是否一样**
* 字符串忽略掉大小写关系的比较 equalsIgnoreCase() 方法
* 字符串连接有两种方法：
    1. 使用 +，比如 String s = "Hello " + "World!"。
    2. 使用 String 类的 concat() 方法。
* 使用 + 进行连接，不仅可以连接字符串，也可以连接其他类型。但是要求进行连接时至少有一个参与连接的内容是字符串类型。
    ![image.png](https://dn-simplecloud.shiyanlou.com/courses/uid1365409-20200425-1587776776362)

* ****

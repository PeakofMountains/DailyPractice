# JAVA Learning

![image](https://w.wallhaven.cc/full/5d/wallhaven-5dlky9.jpg)

----------------------------------
### 基本语法
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
     ```java
    public class Test {
    public static void main(String[] args){
        String s0 = new String("Hello ");
        String s1 = "World" + "!";  //+号连接字符串
        //s1 = 1;     //错误: 不兼容的类型: int无法转换为String
        String s2 = "World" + "!"+1;//但是连接部分中如果有字符串，
                    //就可以将int类型的自动转换成String并进行连接
        String s3 = s0.concat(s1);  //concat()方法连接
        //s2.concat(1);    //.concat()方法中的参数只能String类型
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
        }
    }
        /*执行结果：
        World!
        World!1
        Hello World!
        */  
    
     ```  
 * charAt() 方法的作用是按照索引值（规定字符串中第一个字符的索引值是 0，第二个字符的索引值是 1，依次类推），获得字符串中的指定字符。
 * 有关String常用提取方法：
     ```java
     
    public class StringTest {
    public static void main(String[] args) {
         String s = "abcdefabc";
         System.out.println("字符a第一次出现的位置为"+s.indexOf('a'));     //搜索字符 ch 第一次出现的索引
         System.out.println("字符a最后一次出现的位置为"+s.lastIndexOf('a'));//搜索字符 a 最后一次出现的索引
         System.out.println("字符串bc第一次出现的位置为"+s.indexOf("bc"));  //搜索字符串 bc 第一次出现的索引
         System.out.println("字符串bc最后一次出现的位置为"+s.lastindexOf("bc"));  //搜索字符串 bc 最后一次出现的索引
         System.out.println("从位置3开始到结束的字符串"+s.substring(3));    //提取从位置索引开始到结束的字符串
         System.out.println("从位置3开始到6之间的字符串"+s.substring(3,6)); //提取 beginindex 和 endindex 之间的字符串部分
         //在字符串中，第一个字符的索引为 0，子字符串包含 beginindex 的字符，但不包含 endindex 的字符。
            }
        }  
    
    ```
     
* 两种自增自减运算：
    1. 前缀自增自减法 (++i,--i): 先进行自增或者自减运算，再进行表达式运算。
    2. 后缀自增自减法 (i++,i--): 先进行表达式运算，再进行自增或者自减运算
* 位运算符：
    ```java
    
        public static void main(String args[]) {
        int a = 60;
        int b = 13;
        System.out.println("a & b = " + (a & b));
        System.out.println("a | b = " + (a | b));
        System.out.println("a ^ b = " + (a ^ b));
        //^按位异或,如果相对应位值相同，则结果为 0，否则为 1
        System.out.println("~a = " + (~a));
        //~按位补，翻转操作数的每一位，即 0 变成 1，1 变成 0
        System.out.println("a << 2 = " + (a << 2));
        //按位左移，左操作数按位左移右操作数指定的位数
        System.out.println("a >> 2 = " + (a >> 2));
        //按位右移，左操作数按位右移右操作数指定的位数
        System.out.println("a >>> 2 = " + (a >>> 2));
        //按位右移补零，左操作数的值按右操作数指定的位数右移，移动得到的空位以零填充
            }
        }
        /*结果：
        a & b = 12
        a | b = 61
        a ^ b = 49
        ~a = -61
        a << 2 = 240
        a >> 2 = 15
        a >>> 2 = 15
        */  
    
    ```
* ^	异或操作符,如果两个操作数逻辑相同，则结果为假，否则为真
* java中`return;`还可以用做在循环中跳出程序
* 掌握`.charAt()`方法//访问索引值处的char
* 掌握`.length()`方法//得到字符串的长度
* 掌握`.toString()`方法//能把其他类型转换成字符串形式
    //StringBuild和StringBuffer类的与String不一样，要输出也得用toString()方法来转换
* `switch-case`语句使用的时候`case`语句要注意记得每个case后面要考虑是否需要`break;`
* 数组的使用:
    ```java
    int ages[];      //数组使用之前先声明  
    //声明数组后，需要为数组分配空间，也就是定义多大的数组
    //分配方法：数组名 = new  数据类型 [ 数组长度 ];
     
    ```  
* 上面的这个分配空间大小的有特例:对于`Integer`类型的分配空间时不是这种形式，出现The constructor Integer(int) is deprecated since version 9提示，建议采用`arrayname = Integer.valueOf(int i);`、`name = Integer.valueOf(int i);`这种方式来实例化
* 可以在数组声明的时候初始化数组，或者在声明时就为它分配好空间，这样就不用再为数组分配空间
------------------
### 异常处理

* 鲁棒是Robust的音译，也就是健壮和强壮的意思。它也是在异常和危险情况下系统生存的能力。比如说，计算机软件在输入错误、磁盘故障、网络过载或有意攻击情况下，能否不死机、不崩溃，就是该软件的鲁棒性。所谓“鲁棒性”，也是指控制系统在一定（结构，大小）的参数摄动下，维持其它某些性能的特性。
* 异常通常有四类：
    1. Error：系统内部错误，这类错误由系统进行处理，程序本身无需捕获处理。
    2. Exception：可以处理的异常。
    3. RuntimeException：可以捕获，也可以不捕获的异常。
    4. 继承 Exception 的其他类：必须捕获，通常在 API 文档中会说明这些方法抛出哪些异常。
    
* 平时主要关注的异常是 Exception 下的异常，而 Exception 异常下又主要分为两大类异常，一个是派生于 RuntimeExcption 的异常，一个是除了 RuntimeExcption 体系之外的其他异常。

* RuntimeExcption 异常（运行时异常）通常有以下几种：
    1. 错误的类型转换
    2. 数组访问越界
    3. 访问 null 指针
    4. 算术异常

* 一般来说，RuntimeException 都是代码逻辑出现问题。

* 非 RuntimeException（受检异常，Checked Exception）一般有：
    1. 打开一个不存在的文件
    2. 没有找到具有指定名称的类
    3. 操作文件异常
* 受检异常是编译器要求必须处理的异常，必须使用 try catch 处理，或者使用 throw 抛出，交给上层调用者处理。
* throws 用于声明异常，表示该方法可能会抛出的异常。如果声明的异常中包括 checked 异常（受检异常），那么调用者必须捕获处理该异常或者使用 throws 继续向上抛出。throws 位于方法体前，多个异常之间使用 , 分割。    
* 通常抛出异常后，还需要将异常捕获。使用 try 和 catch 语句块来捕获异常，有时候还会用到 finally。
对于上述三个关键词所构成的语句块，try 语句块是必不可少的，catch 和 finally 语句块可以根据情况选择其一或者全选。你可以把可能发生错误或出现问题的语句放到 try 语句块中，将异常发生后要执行的语句放到 catch 语句块中，而 finally 语句块里面放置的语句，不管异常是否发生，它们都会被执行。
你可能想说，那我把所有有关的代码都放到 try 语句块中不就妥当了吗？可是你需要知道，捕获异常对于系统而言，其开销非常大，所以应尽量减少该语句块中放置的语句。
    ```java
    public class CatchException {
    public static void main(String[] args) {
        try {
            // 下面定义了一个try语句块

            System.out.println("I am try block.");

            Class<?> tempClass = Class.forName("");
            // 声明一个空的Class对象用于引发“类未发现异常”
            System.out.println("Bye! Try block.");
            //语句异常后不向下执行，跳出try语句块，进入 catch语句块

        } catch (ClassNotFoundException a) {
            // 下面定义了一个catch语句块
            System.out.println("I am catch block.");

            a.printStackTrace();
            //printStackTrace()的意义在于在命令行打印异常信息在程序中出错的位置及原因

            System.out.println("Goodbye! Catch block.");

        } finally {
            // 下面定义了一个finally语句块
            System.out.println("I am finally block.");
            }
        }
    }
    /*执行结果：
    I am try block.
    I am catch block.
    java.lang.ClassNotFoundException:
            at java.lang.Class.forName0(Native Method)
            at java.lang.Class.forName(Class.java:264)
            at CatchException.main(CatchException.java:8)
    Goodbye! Catch block.
    I am finally block.
    */  

    ```
* 在输出时有`.hasNext("exit")`可以用作输入的判断是否为括号内的内容，返回值是`Boolean`型的
* 对于用户不断的输入，如果用字符串数组储存的话，应该用`ArrayList`容器，它是可变大小的，创建动态字符串数组的格式如下`ArrayList<String> str = new ArrayList<String>();`，这里的`<String>`指的是限定输入是字符串类型，这个部分不能少
* 
*************** 

## Unity3D学习笔记
兴趣使然，很久以前就想做一款自己的游戏，一方面由于时间不允许，而是惧怕学习的难度，但是最近经常玩游戏，耽误了很多时间，在卸载游戏后突然有种看穿游戏的感觉，加之之前与同学一起用java做过一款大富翁游戏，想着自己其实可以用这些游戏时间来自己做些有价值的事——例如开发一款游戏。
目前开发游戏最流行的就是Unity引擎，一方面可以做游戏，另一方面也可以做动画学渲染等技能。我找到很多资源，最终决定在B站上跟着视频来学习更好些，[感谢Up主的分享，也感谢授课老师幽默的讲解](https://www.bilibili.com/video/BV12s411g7gU)，希望我能一直坚持下来，利用疫情暑假的时间掌握这项技能，做出自己的一款游戏！

### Day 1

#### Unity软件基本使用，基本概念，理解Unity开发架构

* 在新建项目时项目名和项目位置最好时全英文，不要出现汉字，否则可能会出现意想不到的错误意外。
* 在edit菜单里preference菜单里language里可以修改菜单栏显示语言。
* 进入项目后可以通过右上角的Layout菜单改为不同的布局界面，在Project上右键也可以更改project显示的布局。
* Project里放游戏的素材，包括音频，模型什么的。
* Assets里放的（资产），包括项目的model什么的。
* model等资源都可以通过将文件拖到到Unity面板里达到添加的作用。
* Hierarchy面板里放游戏对象，在游戏运行的时候能看见的。
* Scene面板能对游戏对象进行设计操作。
* Game面板能看见游戏真实运行起来用户看起来的效果。
* 鼠标右键移动视野旋转，滚轮滚动视野变近或远(缩放场景)，按下鼠标滚轮拖动场景。
* 选中对象后按`F`键可以让选中对象居中。
* 点击右键同时按下W/S/A/D/Q/E键实现场景漫游
* 按住Alt键同时通过鼠标左键围绕物体旋转场景，鼠标右键缩放场景。
* Inspector检视面板，可以查看修改选中对象的组件(功能)信息。Position参数是选中对象相对世界原点的坐标。鼠标移到X.Y,Z上往左拽或者往右拽也可以进行数值微调，输入的数值可以为简单的四则运算式子。Rotation是对象沿轴旋转的角度，注意XYZ轴的方向。Scale为模型显示比例，一般都为1，1，1
* 点击对象中间的白块可以进行等比例的缩放。
* 按住对象然后Ctrl+D可以进行对象的复制。
* 顶点吸附：选中一个对象，按住V不放，选中其中一个顶点，拖拽移动后松开V键，再松开左键。
* 变换切换：Center，Pivot改变对象的中心点位置，Pivot是美工做的时候确定的中心
* 坐标：Globol全局局视角，Local自身视角
* 中间上部三个图标从左到右为连续播放，暂停和逐帧播放
* 视图的两种模式：ISO——正交视角(平面感觉)，Persp——透视观察模式——3D视角(近大远小)
* 场景Scene(游戏对象的集合)，作为文件储存的时候后缀为.unity,为Unity的图标。Ctrl+S保存的就是场景。Ctrl+N就是新创建一个场景。
* 组件：Transform变换组件决定物体的位置角度比例，Mesh Filter网格过滤器，获取网格信息，Mesh Renderer网格渲染，才能看见。
* 对象在创建的时候默认是在世界坐标的原点创建
* 若要将两个或多个对象捆绑在一起作为一个整体，可以让其中一个作为父对象，其他作为子对象，当移动父对象的时候子对象也跟着一起移动，当然也可以创建一个空的对象让其他所有的对象作为此对象的子对象，这样当父对象移动的时候，同样其余也跟着一起移动，父子对象关系的创建可以直接在Hierarchy窗口通过拖动对象A到对象B实现B作为A的父对象。
* 当建立父子对象关系之后，子对象的position就是相对于父对象的position，而父对象的position仍然是相对世界坐标而言的。当使用空对象作为其余的父对象的时候要确定这个空对象的位置在哪里，因为他是看不见的，在作为判定标准的时候要格外小心。
* 在父子对象捆绑完毕之后给所以子对象全选中，点击右边transform的设置图标，执行reset。让对象transform更新一下，让其都变成与父对象的相对位置。
* 一般让对象都成为空对象的子对象，把对象的行为都绑在父物体上，这样当子对象要更换模型的时候这些行为就不用再更改了。
* material其实本质上是shader的实例，在Project面板右键然后create选项选中material可以创建自己的material，在创建material之后点击自己创建的material，在右边Inspector处有Albedo选项，左面的框就是贴图的地方，右面的框是取色的地方，要进行设置，在设置完毕之后可以将自己的material拖动到想要着色的对象名上，也可以点击想要着色的对象，将material拖动到对象的Mech Renderer组件下的Materials地方。不能将material用于给空的对象着色，因为它没有Mech Renderer组件，不具有materials属性。给对象改颜色其实也可以直接点击对象名，在右边的Albedo直接修改。
* 右边material下有个Rendering Mode渲染模式，一般直接创建的立体是默认的Default Material不允许修改Rendering Mode等，此时就可以用自己创建的Material，这样这些对方就可以选择更改了。右边material下有个Rendering Mode渲染模式，其中cut out选项就指不显示透明通道的渲染，其中Transparent选项就是透明渲染，当然光设置为透明渲染还不行，如果要达到自己需要的透明目标还需要在Albedo处设置A的数值(即透明度)，其中Fade选项就是淡入淡出效果，最后也得在Albedo处设置A的数值(即透明度)。
* Camera组件，作为光锥捕获画面给玩家，Audio Listener组件捕获声音给玩家。
* Camera组件里的Clear Flag就是处理场景的空白部分，其中选项SkyBox天空盒用于包装模拟天空材质，使用天空盒，方式一：Camera中添加组件Skybox，方法二：光照窗口Window-Lighting-Environment Lighting-Skybox，方法二可将天空盒作为反射源将天空颜色反射到物体身上看起来更逼真。
* Camera组件里的Culling Mask里面就是想让摄像机能看见的东西。
* Camera组件里的Projection就是显示的模式，Perspective就是显示有近大远小的3D效果，Orthographic是2D效果。
* 在用Unity的时候突然发现太阳和camera不见了，但是光照和设想画面还在，解决办法：点击Scene面板上的Gizmos，就会显示了
* Camera组件里的Clipping Planes就是视野的调整，Viewport Rect就是摄像画面的显示位置，X,Y是目前的画面坐标，W,H为画面的宽和高，这四个的取值范围都是0~1。
* Camera组件里的Depth数值设置的是渲染的次序，后渲染的会覆盖先渲染的，因此要看见先渲染的Depth值应该比后渲染的Camera组件的Depth值大。因此游戏的小地图Camera应该比Main Camera大，因为小地图Camera应该先渲染。
* 选中物体后Ctrl+Shift+F指定移动后的位置可以迅速移动物体到指定位置。可用于摄像机等的快捷移动。
* 对象的Layer部分可以Add Layer，添加自己设计的层(起个名字就行)，然后选择自己设计的Layer，选择Culling Mask，把自己的层前的勾去掉就可以达到在当前camera不显示这个物体的效果。
* 渲染管线：图形数据在GPU上经过运算处理，最后输出到屏幕上的过程。游戏->图形API->|(CPU与GPU分界线)->顶点处理->图元装配->光栅化->像素处理->缓存，绘制调用Draw Call每次引擎准备数据并通知
GPU的过程，通俗讲，每帧调用显卡渲染物体的次数，要尽量减少Draw Call。
* CPU的顶点处理：接收模型顶点数据，坐标系转换。CPU的图元装配：组装面，连接相邻的顶点,绘制为三角面。CPU光栅化：计算三角面上的像素,并为后面着色阶段提供合理的插值参数。CPU像素处理对每个像素区域进行着色。写入到缓存中。CPU缓存：一个存储像素数据的内存块，最重要的缓存是帧缓存与深度缓存。帧缓存:存储每个像素的色彩,即渲染后的图像。帧缓存常常在显存中, 显卡不断读取并输出到屏幕中。深度缓存z-buffer :存储像素的深度信息,即物体到摄像机的距离。光栅化时便计算各像素的深度值,如果新的深度值比现有值更近，则像素颜色被写到帧缓存,并替换深度缓存。
---------------------------------------------------------
### Day 2

* 即时遮挡剔除Instant Occlusion Culling，遮挡剔除:当物体被送进渲染流水线之前，将摄像机视角内看不到的物体进行剔除,从而减少了每帧渲染数据量, 提高渲染性能。
* 多细节层次Levels of DetailLOD技术指根据物体模型的节点在显示环境中所处的位置和重要度，决定物体渲染的资源分配,降低非重要物体的面数和细节度,从而获得高效率的渲染运算。
* Lighting Setting是在Window-Rendering-Lighting Settings打开。
* 光照系统：  
Global Illumination简称GI ,即全局光照。能够计算直接光、间接光、环境光以及反射光的光照系统。通过GI算法可以使渲染出来的光照效果更为真实丰富。  
Shadow Type阴影类型: Hard 硬阴影、Soft 软阴影、Strength硬度:阴影的黑暗程度。Resolution分辨率:设置阴影的细节程度。Bias偏移: 物体与阴影的偏移。通过Mesh Renderer组件启用禁用阴影 ，Cast /Receive Shadows当前物体是否投射/接收阴影，Off不投射阴影, On投射阴影, Two Sided双面阴影，Shadows Only隐藏物体只投射阴影，阴影剔除:设置显示阴影的距离Edit- > Project Settings- >Quality-> Shadows Disdance
* 环境光照：  
作用于场景内所有物体的光照,通过Environment Lighting中Ambient控制。Ambient Source环境光源，Skybox通过天空盒颜色设置环境光照，Gradient梯度颜色，Sky天空颜色、Equator 地平线颜色、Ground 地面颜色Ambient Color纯色Ambient Intensity环境光强度Ambient GI环境光GI模式Realtime实时更新，环境光源会改变选择此项。Backed烘焙，环境光源不会改变选择此项。
* 反射光照：  
根据天空盒或立方体贴图计算的作用于所有物体的反射效果，通过Environment Lighting中Reflection控制。Reflection Source反射源Skybox天空盒Resolution分辨率Compression 是否压缩Custom自定义
Cubemap立方体贴图Reflection Intensity反射强度Reflection Bounces使用Reflection Probe后允许不同游戏对象间来回反弹的次数。  
* 间接光照：物体表面在接受光照后反射出来的光。通过Light组件中Bounce Intensity反弹强度控制。可以通过Scene面板Irradiance模式查看间接光照。
  注意:
  > 1. 只有标记`Lightmaping Static`的物体才能产生间接反弹光照。
  > 2. 设置间接光照的之前需要将不移动的物体在右面的`Inspector`面板里`static`打上勾作为静态物体。Unity的间接光计算很复杂。
* 实时GI：  
Realtime GI 所谓"实时"是指在运行期间任意修改光源,而所有的变化可以立即更新。正是由于Unity 5引入了行业领先的实时全局光照技术Enlighten系统,才可以在运行时产生间接光照,使场景更为真实丰富。
  操作步骤:
> 1.游戏对象设置为`Lightmaping Static`
> 2.启用`Lighting`面板的`Precomputed Realtime GI`
> 3.点击`Build`按钮(如果勾选Auto编辑器会自动检测场景的改动修复光照效果)
* 在`Edit-preference-GI Cache`可*查看缓存和更改缓存的位置*。
* 烘焙`Lightmap`：
  当场景包含大量物体时,实时光照和阴影对游戏性能有很大影响。使用烘焙技术,可以将光线效果预渲染成贴图再作用到物体上模拟光影,从而提高性能。适用于在性能较低的设备上运行的程序。*设置之前也需要将静止物体设为*`static`，**烘焙只能针对静态的物体**。
* 光源侦测`Light Probes`  
由于`LightMapping`只能作用于`static`物体，所以导致运动的物体与场景中的光线无法融合在一起,显得非常不真实。而`Light Probes`组件可以通过`Probe`收集光影信息,然后对运动物体邻近的几个`Probe`进行插值运算,最后将光照作用到物体上。
* 步骤
> 1.创建游戏对象`Light Probe Group`。
> 2.添加侦测小球`Add Probe`。
> 3.点击`Build`按钮。( 如果勾选`Auto`,编辑器会自动检测
场景的改动修复光照效果)
> 4.勾选需要侦测物体的`MeshRenderer`组件的`Use Light
Probes`属性。  
* 声音：  
  Unity支持的音频文件格式:mp3，ogg，wav,aif,mod,it,s3m,xm。
  声音分为2D、3D两类:
  > 3D声音: 有空间感,近大远小。
  > 2D声音:适合背景音乐。
  在场景中产生声音,主要依靠两个重要组件:
   > `Audio Listener`音频监听器:接收场景中  
   > 音频源`Audio Source`发出的声音，通过计算机的扬声器播放声音。
* Audio Source**音频源**:
> `Audio Clip`音频剪辑:需要播放的音频资源。
> `Mute`静音:如果启用,播放音频没有声音。
> `Play On Awake`唤醒播放:勾选后场景启动时自动播放。
> `Loop`循环:循环播放音频。
> `Volume`音量:音量大小
> `Pitch`音调: 通过改变音调值调节音频播放速度。1是正常播放。
> `Stereo Pan` : 2D声音设置左右声道。
> `Spatial Blend` : 2D与3D声音切换。

---------------------------------------------------------
### C#语言基础

* .NET dotnet
  Microsoft新代多语言的开发平台,用于构建和运行应用程序。
* Mono
  Novell公司支持在其他操作系统下开发.NET程序的框架。
  `Unity`借助`Mono`实现跨平台，核心是`NET Framework`框架
* `namespace`——定义命名空间，类的地址
* `using + 类的命名空间` 相当于其他语言中的`import`库操作
* `Ctrl+A`全选后用`Ctrl+K+F`可以**自动处理缩进**
* 网速10M指的是`Mbps` (兆位/秒)是速率单位,换算成字节应该是`10/8=1.25兆字节/秒`
* C#**数据类型**：
  **整数**：  
  1字节：有符号`sbyte` 无符号`byte`  
  2字节：有符号`short`，无符号`ushort`  
  4字节：有符号`int`，无符号`uint`  
  8字节：有符号`long`，无符号`ulong` 
  浮点数：  
  4字节：`float`  
  8字节：`double`  
  16字节：`decimal`  
  注意事项:  
> 1. 非整形变量赋值*要加上后缀*,如果不加默认为`double`.  
> 2. 浮点型运算会出现*舍入误差*.    
`bool number= 1.0f- 0.9f == 0.1f; ` 
二进制无法精确表示`1/10` ,就像十进制无法精确表示`1/3`,所以二进制表示十进制会有一些*舍入误差*，对于精度要求较高的场合会导致代码的缺陷,可以使用`decimal`代替。  
`decimal`浮点数的后缀是`m` 
非数值类型：  
`char`, `bool`, `string`  
* 建议命名规则:  
以*小写字母*开头,如果包含多个单词,*除第一个单词外其他单词首字母大写*  
* 调试：  
  > 1. 在可能出错的行加断点  
  > 2. 按`F5`**启动**调试  
  > 3. 按`F11`**逐语句**执行
  > 4. 按`Shift+F5`**停止**调试
* 在项目上*右键设为启动项目再进行编辑*
* `Console.WriteLine("金额: {0:c}", 10);`输出: 金额`￥10.00`
* `Console.WriteLine("{0:d2}",5)`输出:` 05`,作用：填充为两位
* `Console.WriteLine("{0:f1}",1.26);`输出:` 1.3`, 保留一位小数  
* `Console.WriteLinet("{0:p0}",0.1);`输出:` 10%`,以百分数显示
* **转义符**也是`\`
* 源代码(`.cs`的文本文件) `CLS`编译- 通用中间语言(`exe dII`)--`CLR`编译---机器码  
* **公共语言运行库**`Common Language Runtime`程序的运行环境,负责内存分配、垃圾收集、安全检查等工作。
* **字符串连接**：字符串可以用`+`连接
* **字符串比较**：可以直接用`==`比较是否相同
* **逻辑运算符** `&&`  `||`  `!`  
* 运算符大部分都和C的语法相同
* **数据类型转换**：  
  `数据类型.Parse(string)`将字符串`string`转换成此数据类型  
  `数据类型.ToString()`将任意类型转换为`string`类型   
* **隐式类型转换(自动转换)**,只能从低字节到高字节类型，**显示类型转换(强制类型转换)**
* `C#`里的`for`循环里可以用`for(int i=0;i<3;i++){}`的形式，支持在`for`循环中用`int i`的形式
* `Random`关键字创建一个随机数，创建格式为`Random random = new Random();int number = random.Next(1,101);`来生成一个`1`到`101`的随机数，**前闭后开**。
* 定义方法:  
 > 访问修饰符+可选修饰符+返回类型+方法名称(参数列表)  
 > {  
 >   //方法体  
 >   //return结果;  
 > }
* 出现报错："*并非所有的代码路径都有返回值*"的原因是方法体中缺少return关键字  
* 强大的**注释方法**：在自己编写的函数之前敲`///`会自动生成注释格式，可以在标签之间书写文字，将来文字会以*提示形式显示在调用方法处
* 在方法名上按`F12`就会*跳到相应方法定义的位置*
* 解决不同参数类型的同一类问题，可以让方法名相同，参数不同，程序会根据方法的参数列表判断是用的哪个方法，让调用者仅仅记忆1个方法，这个就是**方法重载**，同时在调用方法打出括号的时候就会显示有多少个重载的方法，*按上下箭头*可以查看使用各个重载方法
* **递归**，方法调用方法自身来解决问
* 当代码中的一个变量名更改的时候，在这个变量名更改后，按` Ctrl+. `，就可以让*所有原来的这个名字都变成新的名字*，也可以点击左边的提示灯泡，选择重命名**变量的选项**

-------------------------------------------------------------

### Day 3
* **创建数组**的其他方法：
> 1. 初始化+赋值  
> `string[] array01;  
> array01 = new string[2] {"a" ,"b"};`
> 2. 声明+初始化+赋值  
> `bool[]array02 ={true,false,false};`  
* 在数组作为参数传给函数时**创建数组**的快捷方法，例：`float max = GetMax(new float[3]{ 1,3, 7 });`
* C#支持**foreach循环遍历数组**，格式：  
  `foreach(元素类型 变量名 in 数组名称)
   {
      //变量名 即 数组每个元素
   }`  
  局限性:  
  1. 只能读取全部元素(语句本身)  
  2. 不能修改元素  
  3. 只能遍历实现lenumerable接口的集合对象  
  创建foreach循环的快捷方式：  
  `foreach+Tab+Tab`，然后光改变量名  
  生成的模板中var是推断类型(根据所赋数据推断出类型，适用性：数据类型名称较长)
* 用父类可以创建子类数组，声明父类类型赋值子类对象,例：  
  `Array arr01 = new int[2];`  
  当方法的参数是父类时，调用的时候可以将其子类作为参数来调用  
 * object类是万类之祖，所有类型的父类
 * **数组的常用方法及属性**：  
> 数组长度:数组名.Length  
> 清除元素值: Array.Clear  
> 复制元素: Array.Copy  
> 数组名.CopyTo  
> 克隆:数组名.Clone  
> 查找元素: Array.IndexOf Array.LastIndexOf   
> 排序: Array.Sort  
> 反转: Array.Reverse  
* C#**创建二维数组**例：
  创建5行3列的二维数组:`int[,] array = new int[5, 3];`
  访问二维数组的元素时也时这种形式，例：第一行第二列元素就是`array[0,1]`
* 在本行用Ctrl+K+Ctrl+C快捷注释掉这一行

----------------------------------------
### Day 4
* 二维数组array，用array.GetLength(0)获得第一维的长度(行数)array.GetLength(1)获得第二维的长度（列数）  
* 交错数组：每个元素都相当于一个一维数组，每个元素的大小可以不同  
交错数组初始化：   
`int[][] array02 = new int[4];//创建具有4个元素的交错数组`  
创建一维数组赋值给交错数组的每个元素个元素，一维数组的大小可以不一致  
`array02[0] = new int[3];  
 array02[1] = new int[5];  
 array02[2] = new int[4];  
 array02[3] = new int[1];`   
 将数据1赋值给交错数组的第一个元素的第一个元素  
`array02[0][0] = 1;`  
* 交错数组显示所有元素得用两个foreach套用或者两个for循环套用
* 参数数组：  
  格式：`params int[] array`//array为数组名，int为数据类型)：  
  对于方法内部而言:就是个普通数组，对于方法外部而言，参数数组是可以传递数组，也可以传递一组数据类型相同的变量，也可以不传递参数。
* 由于数据结构的东西比较多，图片比较重要就没做这里的笔记，放个[视频地址1](https://www.bilibili.com/video/BV12s411g7gU?p=79)和[视频地址2](https://www.bilibili.com/video/BV12s411g7gU?p=80)
* 值参数:按值传递-传递实参变量存储的内容(可能是地址也可能是值，看实参存储的是什么)
例：`private static void Fun1 (int a,int []arr){}`  
  引用参数:按引用传递-传递实参变量自身的内存地址  
例：`private static void Fun2(ref int a){}`，这里的ref是引用参数的标志，在调用方法的时候也要加，例:`int a1 = 1；Fun2(ref a1);`
引用参数传递进的方法内部修改引用参数实质上就是在修改实参变量，就像上面的`Fun2(ref a1);`传入的是a1的引用(地址)，在Fun2()中如果修改a1的值(例`a = 2;`)，那么就相当于把a1变成了2  
输出参数:按引用传递-传递实参变量自身的内存地址
例：`private static void Fun3(out int a){}`这里的out是输出参数的标志，在调用方法的时候也要加，例:`int a1；Fun3(out a1);`  
输出参数与引用参数的区别：
> 1. 输出参数 传递 之前 不赋值，引用参数和值参数 传递 之前 必须赋值
> 2. 输出参数传入的方法内部必须为输出参数赋值  
输出参数的作用是接受方法内部的结果，用于处理方法中多个返回结果的情况，可以定义多个输出参数，给输出参数在方法内赋值，外面的就能直接接收上变化。  
引用参数的作用就是可以修改传入的实参的值，不论实参存储的是值还是内存地址，这就解决了方法内部不能修改存储值的实参的缺陷。  
* C#也有垃圾回收器，当栈中的方法执行完毕以后，栈清空，栈里所存参数指向的堆中的数据没办法访问到了，就成了内存中的垃圾
* 装箱 box：值类型隐式转换为object类型或由此值类型实现的任何接口类型的过程。
内部机制:  
> 1. 在堆中开辟内存空间,多开两块
> 2. 将值类型的数据复制到堆中
> 3. 返回堆中新分配对象的地址
* 拆箱 unbox：从object类型到值类型或从接类型到实现该接的值类型的显式转换。
内部机制： 
> 1. 判断给定类型是否是装箱时的类型
> 2. 返回已装箱实例中属于原值类型字段的地址
* 形参object类型,实参传递值类型,则装箱，可以通过重载。泛型避免。
* 字符串常量放在字符串池中，提高字符串利用率，字符串常量具备字符串池特性，字符串常量在创建前，首先在字符串池中查找是否存在相同文本。如果存在，则直接返回该对象引用;如果不存在，则开辟空间存储。  
目的:提高内存利用率。  
字符串具有不可变性字符串常量一旦进入内存，就不得再次改变。因为如果在原位置改变会使其他对象内存被破坏，导致内存泄漏(修改的值的大小可能超过原值的空间大小，导致内存泄漏)。当遇到字符串变量引用新值时,会在内存中新建一个字符串 ,将该字符串地址交由该变量引用。
* C#里也有StringBuilder，可理解为变长度的字符串，用Append()方法进行字符串连接，但是StringBuilder不是真正的String类型，因此要获得最终的String还要用ToString()方法，通过StringBuilder来实现字符串的拼接减少了直接用String导致的内存大量消耗和产生大量垃圾的问题。同时StringBuilder来提供了Insert(),Replace(),Remove()等方法。
* 数据类型中需要特别注意的点：  
> 1. 值类型:直接存储数据
> 2. 引用类型:存储数据的**引用**(内存地址)
> 3. 方法执行在**栈中**,*执行完毕清除栈帧*。
> 4. 局部变量的值类型:*声明在栈中,数据在栈中*。
> 5. 局部变量的引用类型:*声明在栈中,数据在堆中*,栈中存储数据的引用。
> 6. 区分修改的是栈中存储的引用,还是堆中数据
* 枚举：自定义的数据类型，相当于给对象加标签
### Day 5
* 定义枚举类型，例：  
```C#
namespace Day05
{
/// <summary>
///定义枚举类型:移动方向
///</summary>
[Flags]
enum PersonStyle
{
 tall = 1,     //00000001
 rich = 2,     //00000010
 handsome = 4, //00000100
 white = 8,    //00001000
 beauty = 16   //00010000
}
private static void PrintPersonStyle(PersonStyle style )
{ //判断
if ((style & PersonStyle.tall) == PersonStyle.tall)
Console.WriteLine("大个子");
if((style & PersonStyle.rich) == PersonStyle.rich)
Console.WriteLine("土豪");
if((style & PersonStyle.handsome) == PersonStyle.handsome)
Console.WriteLine("英俊");
if((style & PersonStyle.white) == PersonStyle.white)
Console.WriteLine("洁白");
//或者用这种方法,判断与运算的结果是否不为0
if ((style & PersonStyle.beauty) != 0)
Console.WriteLine("漂亮");
}
static void Main()
{
  PrintPersonStyle(PersonStyle.tall | PersonStyle.handsome);
  //如果要用数据类型转换就要进行强制类型转换
  //字符串转枚举要用`PersonStyle style = (PersonStyle)Enum.Parse(typeof(PersonStyle),String str);//PersonStyle 是枚举类`
}
}
/*
*选择多个枚举值
*使用按位或运算符`|`
* 条件:  
* 1. 定义枚举时，使用[Flags]标记此枚举类型可以多选
* 2. 任意多个枚举值做|运算的结果不能与其他枚举值相同，设置值的时候设为2的n次方，例子在上面：
*判断标志枚举是否包含指定枚举值
*运算符& (按位与) : 两个对应的二进制位中都为1 , 结果位为1
//这样设置下来进行或运算就不会与其他枚举重复
*/
```
* C#里也有类和对象的概念
* 成员变量具有初始值，可以与局部变量重名
* 在C#类中类方法默认为private访问类型，只能在类内访问，应该让成员变量私有化，对外提供的方法公开化
* 可以用
```C#
//属性:保护字段 本质就是2个方法
//设置年龄属性
public string Name
{
//读取时保护，去掉后就达到不可读取的效果
  get
  { return name; }
 //写入时保护 value--要设置的数据，去掉set方法就达到不可修改的效果
  set
  { this.name = value; }
}
```
来代替下面代码，这是C#的一种简化的操作特性
```C#
public void SetName(string name)
{
//this这个对象(引用)
this.name = name;
}
public string GetName()
{
return name;
}
```
* C#字段首字母应小写，属性名应大写
* 构造函数如果为字段赋值,属性中的代码块不会执行
* 一个类若没有构造函数,那么编译器会自动提供一个无参数构造函数
* 一个类若具有构造函数,那么编译器不会提供无参数构造函数
* 如果不希望在类的外部被创建对象,就将构造函数私有化
* visul studio中的x个引用是说此方法被调用的次数，点击可以查看调用位置
* 构造函数不能作为一个方法直接被调用，但是可以通过下面的格式来调用
```C#
public Wife()
{
  Console.WriteLine("创建对象就执行");
}
//例：调用无参数构造函数的格式
public Wife(string name):this()
{
  this.name = name;
}
//例：调用带参的构造函数的格式
public Wife(string name, int age):this(name)
{
  this.Age = age;
}
```
* 构造函数特点：
> 1. 与类同名。
> 2. 没有返回值,也不能写void.
> 3. 不能被直接调用，必须通过new运算符在创建对象时才会自动调用,有特例，在上面。
> 4. 每个类都必须至少有一个构造函数,若不提供,编译器自动生成一个无参构造函数。
> 5. 如果程序员定义了构造函数，则编译器不会再提供。
* 在C#里写类的时候，里面那个属性可以有更方便的方式创建：  
`//自动属性包含1个字段2个方法
public string Password{ get; set; }`  
就相当于写了：
```C#
private string password;
public string Password
{
  get
  {
    return this.password;
  }
  set
  {
    this.password = value;
  }
}
```
* 一个类中一般有以下部分：成员变量(字段)，属性，构造函数，对外方法
* 一般字段名首字母小写，属性名首字母大写
* 方法调用的时候，打半个括号就能看见方法的使用规则
* 提取方法  
作用：将一段代码从当前位置提取出来，重新做个方法  
使用方法：将目标代码选中，右键选择快速操作和重构，选择提取方法，修改方法名即可
* c#泛型集合 List<数据类型>，可以理解为变长数组，可以自动进行扩容
用法： List<User> listname = new List<User>();//这里的User是自己创建的类，也是数据类型
* 字典集合 根据key 查找value
 用法： 
 ```C#
  Dictionary<string, User> dic = new Dictionary<string, User>;//创建字典  
  dic.Add("Ih", new User("Ih", "123"));//向字典中添加键值对
  User lhUser = dic["Ih"];//通过键查找到对应的值
 ```
* 创建属性的快捷键：prop+Tab+Tab，自动生成一个属性结构
* 两个类概念上讲从属于同一个类，内容上有很多代码重复或相似，那么可以让这两个或多个类继承同一个父类，继承关系用`:`描述，用法：`class SonClass:FatherClass{}`,父类只能使用父类成员，不可使用子类成员，子类可以使用自己的成员，也可以使用父类的成员。父类的私有(private)成员子类不能直接使用，父类成员protected类型，则子类可以使用，但是外面的类不能使用此成员
* 如果父类的引用指向了子类对象(`FatherClass father = new SonClass();`)，只能使用父类成员，如果需要访问该子类成员，要使用强制类型转换(`SonClass son = (SonClass)father;`)
* 静态成员变量通过类名调用
* 静态成员变量可在不同实例中共同修改
* 实例成员从属于对象，静态成员从属于类
* 静态构造函数不能有访问级别的限制
* 实例构造函数作用:提供创建对象的方式,初始化类的实例数据成员
* 实例化成员变量的初始化应该在实例构造函数中进行
* "非静态字段要求对象引用"的错误出现的原因：静态代码块,只能访问静态成员，不能访问实例成员。
* 实例代码块可以访问实例成员，也可以访问静态成员
* 静态 static 适用性：
  利:单独空间存储,所有对象共享,可直接被类名调用。  
  弊:静态方法中只能访问静态成员,共享数据被多个对象访问会出现并发。
  适用场合:
> 1. 所有对象需要共享的数据。
> 2. 在没有对象前就要访问成员。
> 3. 工具类适合做静态类(常用,不需要过多数据，例如Math类)。
* 二维数组的元素查找调用的常用类(助手类)，得自己写，创建方法：[视频地址](https://www.bilibili.com/video/BV12s411g7gU?p=106)和[视频地址](https://www.bilibili.com/video/BV12s411g7gU?p=107)
* 结构 struct  
定义:用于封装小型相关变量的值类型。与类语法相似,都可以包含数据成员和方法成员。但结构属于值类型，类
属于引用类型。  
适用性:  
表示点、颜色等轻量级对象。如创建存储1000个点的数组，如果使用类，将为每个对象分配更多内存，使用结构可以节约资源。
* 因为结构体自带无参数构造函数,所以结构体不能包含无参数构造函数
* 结构体与类的最大区别是，结构体是值类型，类是引用类型
* 声明常量const关键字
* Alt+左键 能按矩形选择区域
* 选中变量后Ctrl+R+Ctrl+F选择替换所有此变量 
C#基础部分完结  
  
#### 面向对象思想: 分而治之， 高内聚， 低耦合
-----------------------------------------------

### Unity脚本

* 脚本是附加在游戏物上用于定义游戏对象行为的指令代码。  
  Unity支持三种高级编程语言:  
  C#、javascript和Bo0o Script(已废弃)
* 脚本语法结构：
```C#
using namespace;//加命名空间是为了防止类的重名
public class ClassName: MonoBehaviour//附加到游戏物体的脚本类必须继承MonoBehaviour类
{
  void方法名()
  {
    Debug.Log("调试显示信息");
    print("本质就是Debug.Log方法");
  }
}
```
* 文件名与类名必须一致
* 写好的脚本必须附加到物体上才执行
* 附加到游戏物体的脚本类必须从MonoBehaviour类继承
* 在Unity中可以通过菜单设置修改默认的脚本编辑器: Edit- Preferences- External Tools- ExternalScript-Editor
* Unity生命周期： Unity脚本从唤醒到销毁的过程。  
消息(必然事件):当满足某种条件Unity引擎自动调用的函数。  
* Unity中出现"以下文件中的行尾不一致,是否将行尾标准化?"提示是由于编码格式导致的，直接点是就行了
* 脚本中设置为public变量，则此变量会显示在Unity的面板上(需要将脚本挂到对象上)
* 序列化字段`[SerializeField]` 作用:在编辑器中显示私有变量
```C#
[SerializeField]
private int a = 100;//让a不能被其他类访问但是能显示在Unity的编辑器界面上
```
* 序列化字段`[HidelnInspector]`作用:在编译器中隐藏字段
```C#
[HidelnInspector]
public int b;//让b能被其他类访问但是不会显示在Unity的编辑器界面上
```
* 写脚本的时候一般不写属性部分，因为即使写了它也不能显示到Unity编辑器里
* 不要在脚本中写构造函数
* 同一组件的Awake的执行在Start之前，执行的时候所有物体的Awake先执行后才Start
* 初始化操作放在Awake或者Start中
* 游戏物体创建Awake立即执行1次，物体创建并且脚本启用Start才执行1次
* OnEnable:每当脚本对象启用时调用。
* FixedUpdate 固定时间执行(默认0.02s):脚本启用后,固定时间被调用，适用于对游戏对象做物理操作，例如移动等,不会受到渲染的影响。
* Update 执行时机：渲染桢执行，执行间隔不固定，适用性：
* LateUpdate 延迟更新 执行时机：在Update函数被调用后执行,适用于跟随逻辑
*  鼠标相关的执行：  
> OnMouseEnter鼠标移入:鼠标移入到当前Collider时调用。
> OnMouseOver鼠标经过:鼠标经过当前Collider时调用。
> OnMouseExit鼠标离开:鼠标离开当前Collider时调用。
> OnMouseDown鼠标按下:鼠标按下当前Collider时调用。
> OnMouseUp鼠标抬起:鼠标在当前Collider上抬起时调用。
* > OnBecameVisible 当可见:当Mesh Renderer在任何相机上可见时调用。
  > OnBecameInvisible当不可见:当Mesh Renderer在任何相机上都不可见时调用。
* OnDisable当不可用时执行:对象变为不可用或附属游戏对象非激活状态时此函数被调用。
OnDestroy当销毁时执行:当脚本销毁或附属的游戏对象被销毁时被调用。
OnApplicationQuit当程序结束时结束:应用程序退出时被调用。
* 
### Day 6

* Unity调试方法： 1. Windows-Console显示控制台，程序的执行信息会显示到这里(适合简单逻辑)。 2. 定义共有变量,程序运行后在检测面板查看数据
* Console的选项功能：clear：清除功能；Collapse：折叠相同项；Clear on Play：执行前清空(建议选上)；error pause：出异常程序就暂停
* Console窗口的右上角三个都选上
* Unity中的Print()方法只能在脚本中用
* 调试过程中,输入代码方法:右键--快速监视或查看“即时窗口”
* 单帧调试:启动调试-运行场景-暂停游戏-加断点-按住单帧执行按钮不放进行单帧执行-结束调试
* 设置物体颜色的方法：例（设为红色）：`this.GetComponent<MeshRenderer>().material.color = Color.red;`
* 程序里颜色的RGB设置范围是0~1，所以程序里写的应该是标准RGB除以255的值
* 获取当前物体所有组件:
```C#
  var allComponent = this.GetComponents<Component>();
  foreach (var item in allComponent)
  {
    Debug.Log(item.GetType());
  }
```
* 获取后代物体的指定类型组件(从自身开始)
```C#
var allComponent = this.GetComponentsInChildren<MeshRenderer>();
foreach (var item in allComponent)
{}
```
* 获取前代物体的指定类型组件(从自身开始)
```C#
var allComponent = this.GetComponentsInParent<MeshRenderer>();
foreach (var item in allComponent)
{}
```
* Component类提供了查找(在当前物体、后代、先辈)组件的方法
* this.transform.position找到的是世界坐标，this.transform.localPosition找到的是与父类的相对坐标
* this.transform.localScale是相对于父类的倍数，this.transform.lossyScale是相对于最原始模型的比例
* 向自身坐标系z轴移动1米：`this.transform.Translate(O, 0, 1);`  
  向世界坐标系z轴移动1米：`this.transform.Translate(0, 0, 1,Space.World);`
* 沿自身坐标系y轴旋转10度：`this.transform.Rotate(O, 0, 1);` 
  沿世界坐标系y轴旋转10度：`this.transform.Rotate(0, 10, 0, Space.World);`
* 围绕旋转的方法：例，绕世界的z轴旋转1度：`this.transform.RotateAround(Vector3.zero, Vector3.forward,1);`(Vector3.zero是世界原点，Vector3.forward是绕世界z轴，Vector3.up是绕世界y轴旋转)
* Unity中快速创建一个Button用来测试的方法：
```C#
private void OnGUI()
{
  if (GUILayout.Button("ButtonName"))
  {
    //按下按钮发生的事件
  }
}
```
* Unity中快速创建一个Button用来测试的方法,与上面的区别在于这个Button一直按着事件就能重复执行：
```C#
private void OnGUI()
{
  if (GUILayout.RepeatButton("ButtonName"))
  {
    //按下按钮发生的事件
  }
}
```
* 获取根物体变换组件 `Transform rootTF = this.transform.root;`
* 获取父物体变换组件 `Transform parentTF = this.transform.parent;`
* 设置父物体： 
当第二个参数设为false时，当前物体的位置视为localPosition，不加第二个参数默认为true，也就是世界坐标
`this.transform.SetParent(tf,false);`
* 根据名称找子物体组件：`Transform childTF = this.transform.Find("子物体名称");`
* Transform类提供了查找(父、根、子)变换组件、改变位置、角度、大小功能
* 在场景中物体激活状态(物体实际激活状态)`this.gameObject.activelnHierarchy`
  物体自身激活状态(物体实际激活状态,也就是物体在Inspect面板的激活状态)`this.gameObject.activeSelf`
* 设置物体启用或禁用`this.gameObject.SetActive()`
* 在场景中根据名称查找物体(慎用):`GameObject.Find("游戏对象名称")`
* 获取所有使用该标签的物体  
`GameObjectO allEnemy = GameObject.FindGameObjectsWithTag("Enemy");`
获取使用该标签的物体(单个)  
`GameObject playerGO = GameObject.FindWithTag("Player");`   
* GameObject的AddComponent()方法添加组件
* 出现"The referenced script on this Behaviour is missing"错误是由于有的预制件的组件中包含了脚本，但是这个脚本已经删除了，那么在脚本组件的位置将显示一个丢失的信息。你需要移除这个组件，或者替换上更新后的脚本。其它的情况大体如此。细心检查，将丢失的资源补上或者移除即可。
* 在写TransformHelper类(用于查找未知位置的组件)的时候，程序编写正确，但是在找指定的组件的时候发生了"NullReferenceException: Object reference not set to an instance of an object" 的错误，经过自己排查，发现原因是由于使用的多个例子组件直接没有构成层级关系，因此在方法中调用GetChild(0)的时候必然返回null值，那么调用的地方就会因为这个原因，导致发生上面的错误。
* Time类，Time.time记录的是从游戏开始执行到现在的时间
* 用这种方式保证旋转速度不受机器性能以及渲染影响`this.transform.Rotate(0, 100 * Time.deltaTime, 0);`，渲染快那么Time.deltaTime就会小了，能实现渲染出来的旋转速率统一
* Time.deltaTime是渲染两帧之间的时间间隔
* 

------------------------------------------------------------

### Day 7

* Time.timeScale能控制游戏的快慢与暂停，`Time.timeScale = 0;`实现游戏的暂停
* Time.timeScale不影响渲染的频率
* Time.unscaledDeltaTime不受缩放(游戏快慢)影响的时间，暂停以后其值仍然变化
* 重复调用的InvokeRepeating方法，3个参数(被执行的方法名称,第一次执行时间,每次执行间隔)
例：`InvokeRepeating("Timer", 1, 1);`
* 取消调用：参数为方法名，例：`Cancellnvoke("Timer");`
* 立即调用方法Invoke，2个参数(被执行的方法，开始调用时间)
* 做倒计时的三种方法：1.通过Time.time，方法放在Update中 2.通过Time.deltaTime方法放在Update中 3.通过InvokeRepeating()方法放在Start中
* 预制件：把场景里要多次使用的组件从Hierarchy面板拽到Project面板，当要使用的时候将其拽到需要附加的物体上即可，而且这样做在以后要对这个组件统一进行修改的时候也非常的方便
* 当单独修改个体此组件之后，预制件就不再控制此个体的这个组件了。
* 预制件Prefab：一种资源类型，可以多次在场景进行实例。  
  优点:对预制件的修改,可以同步到所有实例,从而提高开发效率。  
  注意：如果单独修改实例的属性值，则该值不再随预制件变化。  
  Select键:通过预制件实例选择对应预制件  
  Revert键:放弃实例属性值,还原预制件属性值  
  Apply键:将某一实例的修改应用到所有实例  
* 录制动画：
1. Window-Animation开启录制窗口  
2. 给所选物体在右边Inspector面板添加Animation组件,会创建一个本地文件，选择名字和存储的位置
3. 在Animation面板选Add Property添加属性
4. 选中相应的组件点击右侧加号添加进来
5. 点击红点开始录制，在面板的右面是时间轴，滑动滚轮改变时间的跨度，数字的显示意义，例1：60就是动画开始过了1秒过了60帧，在对应的地方双击创建控制点，在控制点设置动画结束和动画开始的属性，他会自动帮你完成中间的过渡。
6. 录制可以点击三角号进行预览
7. 再次点击结束录制
8. 在使用的时候要将录制的文件拖动到Inspector面板的Animation部分的第一个Animation处，然后就可以在运行的时候播放动画了  
注意事项：  
1. 第一次做的时候遇到了"xx AnimationEvent has no function name specified!"问题，解决方案：由于在录制动画的时候设置了几个时间点但是未修改其值(动画编辑器中我们添加了动画事件（Animation Event）但是并没有进行后续处理)，因此解决办法删去多余的未修改的时间点。
2. 在设置的Event上右键选择Delete key可以删除这个时间点
3. Animation面板最上面的数字是定位到播放的帧数
* 直接播放动画animation.Play("动画名"):
按照队列一个播完了播下一个动画animation.PlayQueued("动画名");
播放有淡入淡出效果animation.CrossFade ("动画名");

-------------------------------------------------------------

### Day 8

* 两个物体三维空间距离的计算方法：Vector3.Distance(),其中的两个参数为两个物体transform组件上的position
* 找此物体的tranform组件可以直接用this访问到，但是其他组件必须要靠GetCompunent<组件>()方法才能找到
* 判断是否当前位置到达指定点应该判断两点之间的距离是否小于指定的误差范围，如果直接判断两个位置是否完全相等可能达不到目的，因为位置使用float类型表示的，因此浮点数的表示会存在误差，因此及时到达同一个点，有可能他的位置坐标还不相同

-------------------------------------------------------

### Day 9

* 今天在人物动画的播放操作上困扰了很久，最初人物不按照指定的路线进行移动，最终发现原因是我将创建的人物作为了空物体的子对象，而将脚本挂在了空物体上，运行的时候应该有移动，但是因为是空物体所以看不见移动。这个问题解决了之后又发现人物只有移动没有移动时奔跑的动画和停止时射击的动画，这个问题更是耗费了很长时间才解决：要保证脚本挂在此物体上，同时控制动画播放的脚本要开启(组件前的框要打上对勾)，同时还要保证人物Model里的Animation前的方框也要勾选，还要设置指定时机的播放的动画名称。
* 在脚本的类之前加上这样的语句能一起引入组件，例(这里引入的是EnemyAnimation组件)：`[RequireComponent(typeof(EnemyAnimation))];`
-----------------------------------------
### Day 10

* 预制件创建的物体最终如果想将结果也保存到预制件上，就在Inspect窗口找到override面板里边有Apply all选项
* Input类，获取鼠标输入：  
当指定的鼠标按钮被按下时返回true：`bool result= Input.GetMouseButton(0);`  
在用户按下指定鼠标按键的第一帧返回true：`bool result= Input. GetMouseButtonDown(0);`  
在用户释放指定鼠标按键的第一帧返回true: `bool result= Input. GetMouseButtonUp(0);`  
按钮值设定: 0对应左键, 1对应右键，2对应中键。  
* 对鼠标的检测应该放在Update中持续进行检测
* Input类：获取键盘输入(参数为按键的枚举)  
当通过名称指定的按键被用户按住时返回true：`bool result=Input.GetKey(KeyCode.A);`
当用户按下指定名称按键时的那一帧返回true: `bool result=Input. GetKeyDown(KeyCode.A);`
在用户释放给定名称按键的那帧返回true: `bool result =Input. GetKeyUp(KeyCode.A);`
* 如何判断两个按键是否同时按下, : `if(Input.GetKey(KeyCode.C) && Input.GetKeyDown(KeyCode.D);`
* 利用Mathf.Lerp()方法实现线性效果（镜头从远到近由快变慢，镜头由近到远由慢变快）Lerp(起点，终点，比例)，返回起点到终点比例处的值
* Mathf.Abs()绝对值函数
* 
### Day 11
* 在场景中点击右键不放松，然后用键盘的wsad可以控制视角的移动，更好用
* InputManage：即输入管理器
在Unity的Edit- -Project Settings- -Input进行设置，使用脚本通过虚拟轴名称获取自定义键的输入。让玩家可以在游戏启动时根据个人喜好对虚拟轴进行修改。
* 一个虚拟按钮可以绑定4个真实按键
* 虚拟按钮可以重名
* Mouse X默认向右返回值为正，向左返回值为负，Mouse Y默认向上返回值为正，向下返回值为负
* 虚拟按钮的个数可以修改
* 获取虚拟轴：
```C#
bool result=Input. GetButton(”虚拟轴名");
bool result=Input. GetButtonDown(虚拟轴名");
bool result=Input. GetButtonUp("虚拟轴名”);
float value=Input.GetAxis (" 虚拟轴名”);
float value= Input.GetAxisRaw (" 虚拟轴名”);
```
* 实现摄像机视角跟随玩家鼠标移动：
```C#
    public float rotateSpeed = 10;
    public void FixedUpdate()
    {
        float x = Input.GetAxis("Mouse X");
        float y = Input.GetAxis("Mouse Y");
        x *=  rotateSpeed;
        y *=  rotateSpeed;
        //竖直旋转采用自身坐标
        this.transform.Rotate(-y , 0,0);
        //水平旋转采用世界坐标
        this.transform.Rotate(0, x, 0, Space.World);
    }
```
* pos为一个三维向量，此方法能拿到他的模长：`pos.magnitude;`
* 获取向量方向也称"标准化向量”，或"归一化向量",即获取该向量的单位向量，几何意义：将向量的模长变为1
* 获取向量的方向向量（归一化标准化）：`Vector3 n01 = pos/pos.magnitude;`
或`Vector3 n02 = pos.normalized;`
* 用Translate实现移动时给的应该是归一化操作之后的方向向量而不是直接差值得到的向量
* 三角函数API（要求radian为弧度）：
Mathf.sin(float radian)
Mathf.cos(float radian)
Mathf.tan(float radian)
反三角函数API（要求radian为弧度）：
Mathf.Asin(float radian)
Mathf.Acos(float radian)
Mathf.Atan(float radian)
* 角度与弧度的转换：  
角度变弧度：`y = x * Mathf.Deg2Rad;`其中y为弧度，x为角度
弧度变角度：`y = x * Mathf.Rad2Deg;`其中y为角度，x为弧度
* 将自身坐标系下的坐标转换为世界坐标系的坐标，`Vector3 worldPoint = transform.TransformPoint(O, 0, 10);`
* 
### Day 12

* 点乘的API：`float dot=Vector3.Dot(va, vb);`,其中的向量va，vb应该是方向向量（单位向量）（用.normalized）
* 叉乘的API：`Vector vector= Vector3. Cross (a, b);`
* 得到自身正前方世界坐标系下的方向向量`this.transform.forward`，得到自身正右方的世界坐标系下的方向向量`this.transform.right`，得到自身正上方的世界坐标系下的方向向量`this.transform.up`
* 欧拉角：使用三个角度来保存方位。
特点：X与Z沿自身坐标系旋转, Y沿世界坐标系旋转。
API : `Vector3 eulerAngle = this.transform.eulerAngles;`
优点：  
> 1. 仅使用三个数字表达方位,占用空间小。
> 2. 沿坐标轴旋转的单位为角度,符合人的思考方式。
> 3. 任意三个数字都是合法的,不存在不合法的欧拉角。
缺点：  
> 1. 表达方式不唯一：对于一个方位,存在多个欧拉角描述,因此无法判断多个欧拉角代表的角位移是否相同。  
为了保证任意方位都只有独一无二的表示, Unity引擎限制了角度范围,即沿X轴旋转限制在90到90之间,沿Y与Z轴旋转限制在0到360之间。  
> 2. 万向节死锁：
物体沿X轴旋转+90度,自身坐标系Z轴与世界坐标系Y轴将
重合，此时再沿Y或Z轴旋转时，将失去一个自由度。 
在万向节死锁情况下,规定沿Y轴完成绕竖直轴的全部旋转
即此时Z轴旋转为0。
> Unity用三维向量来表示欧拉角。但是他没有方向,大小的概念,欧拉角的x.y.z ,表示各个轴向，上的旋转角度。
> 四元数Quaternion在3D图形学中代表旋转,由一个三维向量(X/Y/Z)和一个标量(W)组成。
旋转轴为V ,旋转弧度为 θ ,如果使用四元数表示,则四个
分量为:
x=sin(θ /2)*V.x
y=sin(θ /2)*V.y
z=sin(θ /2)*V.z
w=cos(θ /2)
X、Y、Z、W的取值范围是-1到1。
API : `Quaternion qt = this.transform.rotation;`
> 创建和使用四元数的代码：
```C#
//旋转轴
Vector3 axis = Vector3.up;
//旋转弧度
float rad = 50 * Mathf.Deg2Rad;
Quaternion qt = new Quaternion();
qt.x = Mathf.Sin(rad 12) * axis.x;
qt.y = Mathf.Sin(rad/2) * axis.y;
qt.z = Mathf.Sin(rad 12) * axis.z;
qt.w = Mathf.Cos(rad/ 2);
this.transf form.rotation = qt;
```

同时Unity也提供了一种更简单的方式：
```C#
//欧拉角->四元数
this.transform.rotation = Quaternion.Euler(0, 50, 0);
```

* 四元数表示能避免万向节死锁的出现
* 四元数可以与向量相乘(顺序必须是四元数在前)达到旋转向量的目的。两个四元数相乘可以组合旋转效果。例如:
```C#
Quaternion rotation01 = Quaternion.Euler(O, 30, 0) * Quaternion.Euler(O, 20, 0);
Quaternion rotation02 = Quaternion.Euler(O, 50, 0);
//rotation01与rotation02相同
```

* 四元数的旋转是按照自身的x、y、z轴转的
* 四元数的缺点：  
难于使用,不建议单独修改某个数值。  
存在不合法的四元数。  
* 对向量的控制：
```C#
// vect向量根据当前物体的旋转而旋转
vect = this.transform.rotation * new Vector3(0, 0, 10);
// vect向量沿y轴旋转30度
vect = Quaternion.Euler(O, 30, 0) * vect;
// vect向量移动到当前物体位置
vect = this.transform.position + vect;
```  
* normalized与normalize()方法的区别：  
```C#
Vector3 vect = new Vector3(O, 0, 10); 
Vector3 norm = vect.normalized;//返回一个单位向量0 0 1
vect.Normalize();/将vect设置为0 0 1
```  
* 
### Day 13

* 注视旋转不改变物体的位置（position），只改变他的朝向`this.transform.rotation = Quaternion. LookRotation(dir);`
* 
1. 欧拉角->四元数  
`Quaternion.Euler(欧拉角);`
2. 四元数-->欧拉角  
`Quaternion qt = this.transform.rotation;  
Vector3 euler = qt.eulerAngles;`
3. 轴/角的旋转
`this.transform.rotation = Quaternion.AngleAxis(50, Vector3.up);`,这里第二个参数为轴的向量表示，可以是不言坐标轴的其他轴
4. 注视旋转  
`this.transform.rotation = Quaternion.LookRotation(dir);
//this.transform.LookAt(tf);通过LookAt实现的旋转是在一瞬间完成的`
5. 差值旋转Lerp
`this.transform.rotation = Quaternion.Lerp(this.transform,rotation,dir,0.1f);`
6. 匀速旋转RotateTowards
`this.transform.rotation = Quaternion.RotateTowards(this.transform,rotation,dir,0.1f);`
* 通过两个四元数判断角度是否接近的方法：
`if(Quaternion.Angle(this.transform.rotation, dir) < 1){}`其中1为判断允许的误差度数
*  Screen Space屏幕坐标系：
屏幕坐标系:以像素为单位，屏幕左下角为原(0,0)点，右上角为屏幕宽、高度(Screen.width ，Screen.height) , Z为到相机的距离。X向右，Y向上  
作用:表示物体在屏幕中的位置。
* Viewport Space视口(摄像机)坐标系:屏幕左下角为原(0,0)点，右上角为(1,1) , Z为到相机的距离。  
作用:表示物体在摄像机中的位置。
* Local Space -> World Space
transform.forward在世界坐标系中表示物体正前方。
transform.right在世界坐标系中表示物体正右方。
transform.up在世界坐标系中表示物体正上方。
transform.TransformPoint
转换点,受变换组件位置、旋转和缩放影响。
transform.TransformDirection
转换方向,受变换组件旋转影响。
transform.TransformVector
转换向量,受变换组件旋转和缩放影响。
* World Space -> Local Space 
transform. InverseTransformPoint
转换点,受变换组件位置、旋转和缩放影响。
transform.InverseTransformDirection
转换方向,受变换组件旋转影响。
transform.InverseTransformVector
转换向量,受变换组件旋转和缩放影响。
* World Space <--> Screen Space
Camera.main.WorldToScreenPoint
将点从世界坐标系转换到屏幕坐标系中
Camera.rain.Screen ToWorldPoint
将点从屏幕坐标系转换到世界坐标系中
* World Space <--> Viewport Space
Camera.main.WorldToViewportPoint
将点从世界坐标系转换到视口]坐标系中
Camera.rain.Viewport ToWorldPoint
将点从屏幕坐标系转换到世界坐标系中
* Screen.width得到的屏幕宽度其实是camera的视锥宽度大小，摄像机的视锥大小决定了显示屏幕的宽度
* 实现移动的限制：如果超过屏幕,停止运动，如果到了最左边并且还想向左移动或者到了最右边并且还想向右移动
```C#
Vector3 screenPoint = Camera.main.WorldToScreenPoint(this.transform.position);
if((screenPoint.x <= 0 && hor <0) || (screenPoint.x >= Screen.width && hor>0))
{hor= 0;}
```
* 物理引擎
给物体加Rigidbody组件变成具有物理特性的刚体，给物体加collider碰撞器组件产生碰撞效果，根据不同的需求选择不同的形状碰撞器(能满足需求的情况下尽量选择面少的)
* Rigidbody属性  
质量Mass : 物体的质量。  
阻力Drag : 当受力移动时物体受到的空气阻力。0表示没有空气阻力,极大时可使物体停止运动，通常砖头0.001 ,羽毛设置为10。  
角阻力Angular Drag : 当受扭力旋转时物体受到的空气阻力。0表示没有空气阻力,极大时使物体停止旋转。  
使用重力Use Gravity :若激活,则物体受重力影响。  
是否是运动学Is Kinematic : 若激活,该物体不再受物理引擎控制,而只能通过变换组件来操作。  
插值Interpolate :用于缓解刚体运动时的抖动。  
无None --不应用插值。  
内插值Interpolate -基于上一帧的变换来平滑本帧变换。  
外插值Extrapolate --基于下一-帧的预估变换来平滑本帧变换。    
碰撞检测Collision Detection : 碰撞检测模式。快速移动的刚体在碰撞时有可能互相穿透,可以设置碰撞检测频率，但频率越高对物理引|擎性能影响越大。  
不连续Discrete : 不连续碰撞检测。适用于普通碰撞(默认模式)。  
连续Continuous :连续碰撞检测。  
动态连续Continuous Dynamic :连续动态碰撞检测,适用于高速物体。  
约束Constraints :对刚体运动的约束。  
冻结位置Freeze Position :刚体在世界中沿所选X , Y , Z轴的移动，将无效。  
冻结旋转Freeze Rotation :刚体在世界中沿所选的X,Y,Z轴的旋转,将无效。  
* 让自身能作为刚体但是发生碰撞的时候自己不受到力的作用，而另一个物体受到力的作用就给这个Rigidbody里的Is Kinematic勾选上
* 碰撞条件：1. 两者具有碰撞组件 2. 运动的物体具有刚体组件
当进入碰撞时执行  `void OnCollisionEnter(Collision collOther)`
当碰撞体与刚体接触时每帧执行 `void OnCollisionStay(Collision collOther)`
当停止碰撞时执行 `void OnCollisionExit(Collision collOther)`
* 触发条件：  
1. 两者具有碰撞组件
2. 其中之一带有刚体组件
3. 其中之一勾选isTrigger
触发三阶段
当Collider(碰撞体)进入触发器时执行
void OnTriggerEnter( ollider cldOther)
当碰撞体与触发器接触时每帧执行
void OnTriggerStay(Collider cldOther)
当停止触发时执行
void OnTriggerExit (Collider cldOther)
* 如果物体移动速度过快,碰撞检测将失效
解决方案:开始时,使用射线检测
* 让子类方法不覆盖父类方法的办法：  
在不想被子类同名方法覆盖的方法前用protected修饰，同时在权限修饰符后加override，然后在子类中敲override+空格之接就会出现要求重写的方法，自动生成格式，在方法中写重写的内容，此方法中的base.方法名其实就是父类的方法，将来就是父类的这个方法和子类的方法都执行
* 通过代码读取资源：  
资源必须放到Resources目录下
```C#
GameObject prefabGO = Resources.Load<GameObject>("目录/资源名称");
  // 创建资源
 Instantiate(prefabGO);
```
* 如果确实是自己项目中的代码文件但是vs总是认为他是杂项文件的话就在vs的资源管理器中找所有文件选项显示出当前的所有文件，找到出现问题的文件，右键包含在项目中就可以了
* 
--------------------------------------------

### Day 14

* 可以在project面板creat一个physical material，设置改变这个材料的物理属性，例如摩擦力，弹力(数值设置0~1)
* Trail Renderer组件能实现拖尾效果，可以用于子弹
* 在网上找到了一种在Unity中查找指定物体下是否有指定脚本的方法：[解决办法：在Unity的面板中能生成一个查找的面板](https://blog.csdn.net/alayeshi/article/details/52039314)
* 使用此方法能将变量设置为public的同时，在编译器中隐藏达到在编译器中不可修改而其他方法中可以对这个参数进行修改的目的，例：  
```C#
[HideInInspector]//在编译器中隐藏
public float atk;
```
* 经实践发现用面或者立方体绘制出的图形不能当作准星，因为这样绘制出来的图形会随着光线的变化颜色也发生改变，甚至在黑暗中准星就变成黑色的了，这显然和真实的效果不一致
* 

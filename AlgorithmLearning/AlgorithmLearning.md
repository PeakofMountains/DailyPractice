### 在数学建模大赛前进行的相关算法学习

感谢[B站这位up主的教程](https://www.bilibili.com/video/BV1Kb41167QZ?p=1)

由于时间匆忙，在这里我只列举出算法的基本使用方法、适用场景和注意问题，具体的解决方法和代码实现链接的视频中有介绍或者通过网络查找获得

![image](https://pic1.zhimg.com/80/v2-fb8863b0b3699f22684ede39c5dec684_1440w.jpg)

### 1.层次分析法  

* 适用场景：多个因素影响下做决策。如在考虑经济，路线，景色等因素的情况下在三个景点选择最佳目的地
* 构建模型：最高层：目标层  最底层：决策层  中间层：因素层
* 思路：构建计算决策目标的权重，构造成对比较矩阵，通过决策目标的权重进行选择
* 需要确定的问题：各个因素之间的权重，决策目标的权重，分别构造成对比较矩阵(用到matlab)
* 解决方案：通过构建两两因素之间的成对比较矩阵和每个决策目标在两个因素间的成对比较矩阵，进而计算出每个决策目标的权重

### 2.多属性决策模型  

介绍加权算术平均算子  
* 适用场景：多个量纲不统一的属性下进行决策
* 构建模型：构建各个属性的决策矩阵(题目中可能会给出资料)
* 思路：对决策矩阵进行归一化(量纲统一)处理，转化为层次分析法的问题
* 需要确定的问题：量纲不统一的问题，转化为层次分析法进行求解
* 解决方案：对属性进行分类，属性值的归一化处理，层次分析法的使用

### 3.灰色预测  

* 适用场景：已知信息不全，进行预测
* 构建模型：灰色系统生成，运用GM(1,1)模型
* 思路：通过累加生成等生成方法构建灰色系统，通过GM(1,1)模型的预测公式进行预测
* 需要确定的问题：灰色系统建立，GM(1,1)模型的运用，预测精度检验
* 解决方案：GM(1,1)模型的预测公式，预测值的求解和精度检验(代码)


### 4.图论模型-Dijstra算法  

* 适用场景：图论，计算两个点直间的最短路径(权值)
* 构建模型：构建所有有关点的图(无向图和有向图都可以)，构建带权邻接矩阵
* 思路：通过构建带权邻接矩阵通过程序得到结果
* 需要确定的问题：带权邻接矩阵的构建，程序相关内容的改造
* 解决方案：手工完成带权邻接矩阵的构建和程序内容的修改

### 5.图论模型-Floyd算法  

* 适用场景：图论，计算两个点之间的最短路径(权值)
* 构建模型：构建所有有关点的图(无向图和有向图都可以)，构建带权邻接矩阵
* 思路：通过构建带权邻接矩阵通过程序得到结果,对结果进一步理解得到最终的结果
* 需要确定的问题：带权邻接矩阵的构建，程序相关内容的改造，程序结果的解读
* 解决方案：手工完成带权邻接矩阵的构建和程序内容的修改，对程序的结果进行解读(详情见视频)

### 6.模拟退火模型  

TSP问题目前没有找到有效的精确算法，倾向于认为其为NP完全问题和NP难题，不存在有效的算法实现  
因此TSP问题用的模拟退火模型其实是有效的近似算法
* 适用场景：解决TSP“旅行商问题(遍历每个点的最短路径)”包括:如何规划最合理高效的道路交通，以减少拥堵;如何更好地规划物流，以减少运营成本;在互联网环境中如何更好地设置节点，以更好地让信息流动等。
* 构建模型：主要是理解算法的适用问题
* 思路：多个点的坐标通过程序找到最短路径
* 需要确定的问题：点的坐标的确定，相关程序内容的修改
* 解决方案：点的坐标查资料或者题目中给出，程序的修改方法视频中有介绍

### 7.种群竞争模型  

* 适用场景：种群生存竞争，不同企业推出的类似产品的销售情况
* 构建模型：竞争模型的构建
* 思路：竞争模型构建后直接通过程序得到结果图形
* 需要确定的问题：竞争模型的建立，程序的修改
* 解决方案：视频中有详细介绍


### 8.排队论  

* 适用场景：涉及排队类问题，先后次序服务
* 构建模型：视频中只介绍了M/M/1单队单服务和M/M/S单队多服务两种排队模型，多队多服务可以拆分成多个单队单服务模型
  根据各元素类型选择对应的排队模型
   排队系统的要素
  * 顾客输入过程;
  * 排队结构与排队规则;
  * 服务机构与服务规则;
* 思路：做好适用的排队模型的分类，通过程序输出结果和图像
* 需要确定的问题：对问题场景的分类
* 解决方案：根据问题所属进行分类，并代入相关模型求解

### 9.线性规划模型  

* 适用场景：多元素相互影响，能得到线性规划的问题,一般会和其他模型一起运用
* 思路：写出目标函数和约束条件用lingo求解
* 需要确定的问题：目标函数和约束条件

### 10.非线性规划和01规划模型  

* 适用场景：非线性问题的最优解和01规划问题的最优解(一个工作只能有一个人完成，一个人只能完成一个工作)
* 思路：数据确定后通过lingo程序求解
* 需要确定的问题：相关变量值的修改和程序的修改

### 11.  

* 适用场景：
* 构建模型：
* 思路：
* 需要确定的问题：
* 解决方案：


### 12.  

* 适用场景：
* 构建模型：
* 思路：
* 需要确定的问题：
* 解决方案：


### 13.  

* 适用场景：
* 构建模型：
* 思路：
* 需要确定的问题：
* 解决方案：

--------------------
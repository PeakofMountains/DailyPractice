# ECharts数据可视化

## 简介

ECharts是一个使用JavaScript实现的开源可视化库，可以流畅的运行在PC和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖矢量图形库ZRender，提供直观，交互丰富，可高度个性化定制的数据可视化图表。

## 官方网址

[**ECharts官网**](https://echarts.apache.org/examples/zh/index.html)

## ECharts使用五部曲

1. 下载并引入echarts.js文件
   * 从官网选下载，点击自定下载，选择自己需要的模块进行打包下载
   * 将下载好的文件放在项目的js文件夹下
   * 从GitHub下载的那个方法目前（2021-9-11）有bug，不知道什么原因
2. 准备一个具备大小的DOM容器
3. 初始化echarts实例对象
4. 指定配置项和数据(option)
5. 将配置项设置给echarts实例对象

## 数据配置项

[配置项官方文档](https://echarts.apache.org/v4/zh/option.html#title)

### 基本配置

* title:标题组件
* tooltip:提示框组件
* legend :图例组件
* toolbox:工具栏
* grid:直角坐标系内绘图网格
* xAxis:直角坐标系grid中的×轴
* yAxis:直角坐标系grid 中的y轴
* series:系列列表。每个系列通过 type决定自己的图表类型(什么类型的图标)
* color:调色盘颜色列表
* series:系列列表
  * type:类型(什么类型的图表)比如line是折线bar 柱形等
  * name:系列名称，用于tooltip的显示，legend的图例筛选变化
  * stack:数据堆叠。如果设置相同值，则会数据堆叠。
    * 数据堆叠:第二个数据值=第一个数据值＋第二个数据值，第三个数据值=第二个数据值＋第三个数据值...依次叠加
    * 如果给stack指定不同值或者去掉这个属性则不会发生数据堆叠


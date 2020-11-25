# DeepFake 一阶运动模型，让万物皆可动起来  
### [参考文章](https://mp.weixin.qq.com/s/CyWyrVvWs3-iFKOUdDg0pQ)  [参考项目](https://github.com/anandpawara/Real_Time_Image_Animation/blob/master/README.md)  

## 概述

目的：利用DeepFake一阶运动模型进行图片的视频化  
重点、难点：运行环境的搭建  

介绍：First Order Motion，也就是一阶运动模型，来自 NeurIPS 2019 论文，实现静态图片运动。首先进行关键点检测，然后根据关键点，进行运动估计，最后使用图像生成模块，生成最终效果。
在运动估计模块中，该模型通过自监督学习将目标物体的外观和运动信息进行分离，并进行特征表示。而在图像生成模块中，模型会对目标运动期间出现的遮挡进行建模，然后从给定的图片中提取外观
信息，结合先前获得的特征表示，生成图片。除了需要用到这个一阶运动模型，还需要使用 OpenCV 和 ffmpeg 做视频、音频和图像的处理。  


## 详细操作

### 环境搭建
[Real_Time_Image_Animation项目中已经有很完整的教程](https://github.com/anandpawara/Real_Time_Image_Animation/blob/master/README.md)  
此处只说明搭建过程中我遇到的问题和解决办法：  
1. python的版本应保持在3.7.3版本以上，并且确定好自己的python版本（可以在cmd中用`python`命令查看自己的python版本），也要特别注意python的版本是32位还是64位，事关后续其他文件的
对应版本下载安装。
2. 教程中Activate virtual environment部分，是指通过cmd进入指定的对应activate文件目录中，然后再运行后续命令  
3. 在使用pip命令之前先通过`pip install update`命令确保自己的pip升到最新版本。  
4. `pip install -r requirements.txt`命令在activate文件夹下安装文件夹内的requirements.txt中指定的文件  
如果出现`No such file or directory: 'requirements.txt\\requirements.txt`错误提示，是因为当前文件夹下并没有这个requirements.txt文件。  
解决办法：  
用`pip freeze > requirements.txt`命令生成这个文件，然后用之前的`pip install -r requirements.txt`命令进行安装
5. requirements.txt中是列出了很多要求的配置库和相应的版本，用pip进行安装requirements.txt中指定的很多配置库的时候
对网络要求很高，否则就会因为网络问题导致`Read time out`问题，导致安装程序退出。  
* 确保自己在一个网络较好的网络环境下(不容易出现因为网络原因安装中断)。  
* 用pip进行安装之前用`pip install update`命令先将pip升级到最新版本。  
* 默认用国外源进行安装，可以将pip的安装源切换为国内的镜像，速度会快上很多（强烈推荐，否则很容易导致Read time out的错误），详细的[使用方法](https://blog.csdn.net/sinat_21591675/article/details/82770360)在此片
博客中有详细介绍。
* 安装过程中如果出现因为"Read time out"的错误中断就将安装程序的命令重新运行一遍(之前已经安装好的库默认不用进行重新安装，接着上次没安装完的继续安装)
* 如果出现某一个库安装一直失败(前提是确保不是因为网络问题)，就单独对这个库进行安装，用`pip install 库名 `的命令进行安装,按照上面的链接中的切换国内镜像源的方法能快上很多。  
* 通过单独安装的库一般是最新版的，就和requirements.txt中的版本不一样了，要通过requirements.txt继续安装剩余的库，就需要对requirements.txt中的内容进行修改，将对应库的版本号改成自己目前
安装成功的版本的版本好，或者删除这个文件中的这个库，这样接下来的安装就不会再对这个库进行安装。
6. 安装torch和torchvision时我出现了错误，通过控制台的canda的pip的安装方法都安装不上。  
尝试过conda进行安装，但是用conda进行安装的时候出现“Solving environment: failed with 
initial frozen solve. Retrying with flexibl”的错误提示，根据网上的解决方法也不能解决这个问题。  
尝试pip进行安装，但是通过官网给的pip命令进行安装出现“could not find a version that satisfies the requirement torch”类似问题，不能得到很好的解决。  
解决办法：
采用手动下载对应的wheel文件手动进行安装  
* 进入清华源（下载速度高很多，成功率更大）或者就在官网提供的源里找自己对应torch版本（各个参数都要对应，可以参考官网给出的版本指导）的wheel用pip进行安装  
  详细方法：
* wheel下载完成后用cmd进入到下载文件所在的目录，用`pip install **********`的命令进行安装  
* 如果出现错误提示“*** is not a supported wheel on this platform”，是因为你下载torch的版本和电脑上的python版本不一致，尝试更换python版本或者重新下载torch的wheel，再进行安装  
* 安装完毕之后通过`python`命令进入python环境，用`import torch`语句看有没有错误提示，如果没有就说明安装成功（或者直接通过`pip list`列出目前电脑上安装的所有包，查看有没有torch）  
* 在python环境中用`exit()`语句退出python环境，重新进入命令行模式。

7. [ffmpeg下载安装](https://ffmpeg.zeranoe.com/builds/)，安装的时候注意配置环境变量，这样才能在命令行启动。  

至此环境配置完毕(其实是否完毕还要看之后的运行时会不会出现)

相关模型等文件下载：[参考这篇文章作者给出的链接](https://mp.weixin.qq.com/s/CyWyrVvWs3-iFKOUdDg0pQ)  

项目的执行方法在原项目中有详细介绍


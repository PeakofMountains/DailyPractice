### 在GitHub上搭建简单的个人博客方法

今天在[B站](https://www.bilibili.com/video/BV1st411r7Sj?from=search&seid=2714152515882042670)上学习了git和GitHub的基本使用方法，学会了从git向GitHub提交文件，修改文件的基本步骤，以及基于GitHub搭建简单的个人博客方法

下面时学习和使用时的一些错误和心得：


* 先要明确从git向GitHub提交文件的流程，是从工作区先用'git add 文件名'的方式把文件提交到缓存区，再用git commit -m ''将缓存区的文件提交到本机仓库中去
，最后通过git push将本机仓库同步到GitHub仓库。
* 使用git commit -m ''命令的时候一定记着commit 后面的参数以及引号中的内容
* 使用git push 之前要先保证修改之前本地仓库与GitHub端仓库文件是一致的，否则会报错
* 在搭建个人网页的时候，在 [Peakofmountains.github.io](https://peakofmountains.github.io/)这个网页要访问到我的个人网页时，这个仓库里只能有一个html文件，不能有其他的文件，访问的显示也是html文件的内容
* 如果不想自己写html文件的话，也可以采用选择主题(默认建立READEME.md文件)，同样这时候也就要求仓库里只能由这一个文件
* 在GitHub上进行了相应的修改操作后如果访问的仍是原先的内容，是缓存没有清理的缘故，用快捷键'CTRL+shift+delete'启动清空缓存，在访问就可以看见修改后的效果了
* 也可以在其他仓库中建立网页，访问的方法就是***用户名.github.io/仓库名***
* GitHub上建立的网页只是静态网页
![image](https://w.wallhaven.cc/full/nr/wallhaven-nr2okq.jpg)

* * * * * * * *

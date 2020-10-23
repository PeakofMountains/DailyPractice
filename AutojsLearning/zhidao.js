/*
 * Name: zhidao.js
 * Author: PeakofMountains
 * Date: 2020-10-22
 * Version: 1.0
 * Describe: auto look through videos in the zhidao app
 * 后续需要改进地方：
 * 1. 将脚本打包成apk
 * 2. 对编程过程中的问题加以解决
 * 3. 用电脑进行脚本的调试
 * 3. 拓展更多方面的应用 
*/


auto();     // 要求进行无障碍服务是否开启的检测
var name = "知到";  
app.launchApp(name);    // 通过软件名启动软件
sleep(17000);       // 等待启动界面
// 点击学习板块
click(354,2119,455,2220);
sleep(5000);
// 点击课程名字
click(102,1872,318,1945);
sleep(2000);
// 点击学习资源
click(26,552,190,743);
//初始化检测控件是否存在
var sign = text("重播").findOnce();
//进入永久循环检测
while(1)
{
    if(sign)
    {
        var next = text("下一篇").findOnce();
        if(next)
        {// 点击“下一篇”控件
            next.click();
        }
    }
    //此处是检测时间间隔，这里设置的是270s检测一次
    for(i=0;i<30;i++)
    {
        sleep(9000);
    }
    sign = text("重播").findOnce();
}

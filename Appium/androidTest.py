'''
# @Filename：androidTest.py
# @Author： PeakOfMountains
# @Version : 1.0
# @Date: 2020-8-26
# @Description:本程序实现电脑有线连接手机，在电脑上运行此代码，
    通过电脑的Appium server服务器驱动手机打开手机上的bilibili
    应用并搜索内容，将搜索到的第一页视频标题在电脑端打印在控制台。
'''


from appium import webdriver    # 从appium库中调用webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
# 创建Appium Server的初始化条件字典
desired_caps = {
'platformName' : 'Android',     # 被测手机是安卓
'platformVersion':'10',     # 手机安卓版本，在手机上的android版本
'deviceName' :'xxx',    # 设备名，安卓手机可以随意填写,方便自己区别就行
'appPackage': 'tv.danmaku.bili',    # 启动APP的Package名称
'appActivity': '.ui.splash.SplashActivity',     # 启动Activity名称
'unicodeKeyboard' :True,    # 使用自带输入法，如果过程中需要输入中文时，填True
'resetKeyboard' : True,     # 执行完程序恢复原来输入法(实际上没有起作用，需要自己在程序执行完后在手机上自行切换回原来的输入法)
'noReset': True,    # 设置为True是不要重置App，否则会清理此应用的使用数据，进入应用的时候变成刚安装的状态
'newCommandTimeout': 6000,      # 允许的等待时间
'automationName': 'UiAutomator2'
}
# 启动Appium,连接Appium Server，初始化白动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 没置缺省等待时间
driver.implicitly_wait(20)
# 根据id定位瘦索位置框，点击操作
driver.find_element_by_id("expand_search").click()
# 根据id定位搜索输入框，点击
sbox = driver.find_element_by_id('search_src_text')
sbox.send_keys('指定的搜索内容')
# 输入回车键操作，确定搜索
driver.press_keycode(AndroidKey.ENTER)
# 选择(定位)所有视频标题
eles = driver.find_elements_by_id("title")
for ele in eles:
    # 打印标题在控制台
    print(ele.text)

input('***press to quit***')
driver.quit()


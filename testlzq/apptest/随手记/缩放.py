from time import sleep

from  appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['platforVersion']='7.1.2'
desired_caps['automationName']='uiautomator2'
desired_caps['app']=r'C:\Users\lzq\Documents\Tencent Files\1468186089\FileRecv\com.baidu.BaiduMap.apk'
desired_caps['appPackage']='com.baidu.BaiduMap'
desired_caps['appActivity']='com.baidu.baidumaps.WelcomeScreen'
desired_caps['noReset']="True"#启动app时不清除app里的原有的数据true 清楚 false
desired_caps['unicodeKeyboard']="True"#使用unicode输入法
desired_caps['resetKeyboard']="True"#重置输入法到初始状态
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# return driver
def suofang():
    a=TouchAction(driver)
    a.press(x=546,y=446).move_to(x=666,y=288).release()
    b=TouchAction(driver)
    b.press(x=575,y=1156).move_to(x=398,y=1455).release()
    c=MultiAction(driver)
    c.add(a,b)
    sleep(3)
    c.perform()
for i in range(5):
    suofang()


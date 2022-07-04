from  appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['platforVersion']='7.1.2'
desired_caps['automationName']='uiautomator2'
desired_caps['app']=r'C:\Users\lzq\Documents\Tencent Files\1468186089\FileRecv\mymoney.apk'
desired_caps['appPackage']='com.mymoney'
desired_caps['appActivity']='com.mymoney.biz.splash.SplashScreenActivity'
desired_caps['noReset']="True"#启动app时不清除app里的原有的数据true 清楚 false
desired_caps['unicodeKeyboard']="True"#使用unicode输入法
desired_caps['resetKeyboard']="True"#重置输入法到初始状态
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
# return driver
driver.find_element_by_id('com.mymoney:id/splash_skip_tv').click()
TouchAction(driver).press(x=540,y=693).wait(2000)\
        .move_to(x=717,y=691).wait(1000)\
        .move_to(x=369,y=520).wait(1000)\
        .move_to(x=534,y=861).wait(1000)\
        .move_to(x=709,y=499).wait(1000)\
        .move_to(x=387,y=693).wait(1000)\
        .move_to(x=727,y=867).wait(1000)\
        .move_to(x=544,y=521).wait(1000)\
        .move_to(x=357,y=870).wait(1000).release().perform()
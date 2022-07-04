from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
def driver():
    desired_caps={}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'wszxmruoby89mz5d'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['app'] = r'C:\dingding.apk'
    desired_caps['appPackage'] = 'com.alibaba.android.rimet'
    desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.LaunchHomeActivity'
    desired_caps['noReset'] = "False"   #启动app时不清除app里的原有的数据true 清楚 false
    desired_caps['unicodeKeyboard'] = "True"   #使用unicode输入法
    desired_caps['resetKeyboard'] = "True"   #重置输入法到初始状态
    driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver






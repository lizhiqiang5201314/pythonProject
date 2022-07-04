from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()    #初始化chrome浏览器
driver.maximize_window()
driver.get("https://dev.ejiayou.com/activity/admin/login")  #浏览器打开页面

def gettoken(b):  #登录万有引力系统
    driver.find_element_by_id('usernameInput').send_keys('admin')
    driver.find_element_by_id('passwordInput').send_keys('123456')
    driver.find_element_by_id('loginBtn').click()
    sleep(3)  # 休眠3s
    a = driver.current_url  # 获取当前url
    b= a.split('=')[-2].split('&')[0]  # 截取token
    driver.quit()  # 关闭浏览器
    print(b)
    return b

gettoken()





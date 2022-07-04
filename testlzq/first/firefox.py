from selenium import webdriver  #导入驱动
from time import sleep  #导入等待时间
#driver = webdriver.Chrome()   #打开火狐浏览器
driver=webdriver.Firefox()
driver.maximize_window() #将打开的浏览器最大化
#driver.set_window_size(400,800)#控制浏览器打开大小
driver.get("http://www.baidu.com")#打开对应的网址
# driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_name("wd").send_keys("python")
# driver.find_element_by_id("su").click()
driver.find_element_by_id("su").click()

driver.refresh()#刷新
sleep(2)  #暂停时间
driver.back()#后退
sleep(3)
driver.forward()#前进
sleep(2)
driver.quit()#关闭浏览器

from selenium import  webdriver #导入驱动
from time import  sleep         #导入等待时间
driver = webdriver.Chrome()     #打开火狐浏览器
driver.maximize_window()        #将打开的浏览器最大化
#driver.set_window_size(400,800)    #控制浏览器打开大小
driver.get("http://www.baidu.com/") #打开对应网址
# driver.find_element_by_name("wd").send_keys("奥运会")
# sleep(5)
# driver.find_element_by_partial_link_text("新").click()
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input").send_keys("奥运会")
# driver.find_element_by_xpath('//*[@id="kw" and @name="wd"]').send_keys("奥运会")
# driver.find_element_by_css_selector('[name="wd"]').send_keys("1")
driver.find_element_by_css_selector('form#from/span/input').send_keys("奥运会")
driver.find_element_by_id("su").click()
# driver.refresh()
sleep(5)
driver.quit()#关闭浏览器


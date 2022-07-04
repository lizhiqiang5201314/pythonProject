# #双击操作
# ActionChains(driver).double_click(element).perform()
#
# sleep(2)
#
# #右击操作
# ActionChains(driver).context_click(element).perform()
#
# sleep(3)
#
# #鼠标悬停
# above=driver.find_element_by_css_selector(".pf")
# ActionChains(driver).move_to_element(above).perform()

from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.runoob.com/")
driver.maximize_window()
driver.implicitly_wait(5)
# driver.find_element_by_css_selector('#kw').send_keys("奥运会")
# double=driver.find_element_by_css_selector('#su')
# ActionChains(driver).double_click(double).perform()
# sleep(2)
# right=driver.find_element_by_css_selector('#su')
# ActionChains(driver).context_click(right).perform()
# xf=driver.find_element_by_css_selector('#s-usersetting-top')
# ActionChains(driver).move_to_element(xf).perform()
# driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
# driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
# driver.get("https://www.sogou.com/")
# driver.find_element_by_css_selector('#query').send_keys(Keys.CONTROL,'v')
# driver.find_element_by_css_selector('#stb').click()
# select=Select(driver.find_element_by_css_selector('#province'))
# select.select_by_value("bj")
# element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
# element.send_keys("Selenium")
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("奥运会")
# driver.find_element(By.CSS_SELECTOR,'#su').click()



driver.find_element(By.LINK_TEXT,'用户笔记').click() #4

driver.find_element(By.LINK_TEXT,'本地书签').click() #3

driver.find_element(By.LINK_TEXT,'菜鸟笔记').click() #2

driver.find_element(By.LINK_TEXT,'菜鸟工具').click() #1
aa=driver.window_handles
print(aa)
driver.switch_to.window(aa[1])
driver.find_element(By.LINK_TEXT,'Python 在线工具').click()





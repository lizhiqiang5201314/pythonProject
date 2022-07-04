from selenium import  webdriver
from time import  sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"C:\Users\lzq\Documents\Tencent Files\1468186089\FileRecv\jgtc.html")
driver.find_element_by_css_selector('#prompt').click()
alert=driver.switch_to_alert()
alert.send_keys("嗯") #输入
sleep(2)
alert.accept()#确认
sleep(2)
# alert.dismiss() #取消
sleep(5)
driver.quit()
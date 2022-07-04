import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.quge6.com/140_140838/7838899.html')
dd = True
while(dd):
    for i in range(1,9):
        num = i*1000
        js = 'window.scrollTo(0,{})'.format(num)
        driver.execute_script(js)
        time.sleep(1)
        print(num)
        if num == 8000:
            driver.find_element_by_link_text('下一章').click()
            time.sleep(1)
from selenium import  webdriver
from time import  sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wjx.cn/vm/Q0p20Fp.aspx")
# driver.switch_to_frame('search')
# driver.find_element_by_css_selector('#query').send_keys("奥运会")
# driver.find_element_by_css_selector('#stb').click()
# js= "window.scrollTo(500,1000);"
# driver.execute_script(js)

driver.find_element_by_xpath('//*[@id="div1"]/div[2]/div[1]/span/a').click()
driver.find_element_by_id('//*[@id="div2"]/div[2]/div[2]/span/a').click()
driver.find_element_by_id('//*[@id="div3"]/div[2]/div[2]/span/a').c
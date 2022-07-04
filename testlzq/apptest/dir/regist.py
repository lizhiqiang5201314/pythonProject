from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from testlzq.apptest.dir.driver import driver

WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id("elementID")) #app显示等待
driver = driver()
def regist():
    driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView').click()
    driver.find_element_by_id('com.tal.kaoyan:id/save').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys("lzqlzq123")
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys("li112233")
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys("1557489263@qq.com")
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

try:
    driver.find_element_by_id("android:id/button2")
except NoSuchElementException :
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
    regist()
else:
    driver.find_element_by_id("android:id/button2").click()
    driver.find_element_by_class_name("android.widget.TextView").click()
    regist()





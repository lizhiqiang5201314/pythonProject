import unittest

# from ddt import data,ddt,unpack
from selenium import  webdriver
from time import  sleep

from unittestreport import list_data, ddt,json_data,rerun

# cases = [{'title': '正确的用户和密码', 'data': ["1468186089@qq.com",123456], 'expected': '1468186089@qq.com'},
#          {'title': '错误的密码', 'data': ["1468186089@qq.com",666666], 'expected': '密码错误！'},
#          {'title': '用户不正确', 'data': ["57343255@qq.com",123456], 'expected': '用户不存在'}]



@ddt
class TestShopping(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://101.34.91.232/TinyShop/index.php?con=simple&act=login")
    # @data(*test1)
    # @unpack
    # @list_data(cases)
    @json_data(r"C:\Users\lzq\PycharmProjects\pythonProject1\test\cc.json")

    def testlogin(self,case):
        name=case["data"][0]
        pwd=case["data"][1]
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="account"]').send_keys(name)
        driver.find_element_by_css_selector('[name="password"]').send_keys(pwd)
        driver.find_element_by_css_selector('[class="btn btn-main "]').click()
        try:
            aa = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[2]/dl/dd/table/tbody/tr[1]/td/b').text
            self.assertEqual(aa, case["expected"], msg="登陆成功")
        except:
            bb =driver.find_element_by_xpath('//*[@id="field-info"]').text
            self.assertIn(bb,case["expected"],msg="登陆失败")

    def testlogin1(self,name,pwd):
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="account"]').send_keys(name)
        driver.find_element_by_css_selector('[name="password"]').send_keys(pwd)
        driver.find_element_by_css_selector('[class="btn btn-main "]').click()
        try:
            bb=driver.find_element_by_xpath('//*[@id="field-info"]').text
            self.assertEqual(bb,"密码错误！",msg="登陆错误")
        except:
            self.assertEqual(11,22,msg="傻逼")




    def tearDown(self) -> None:
        self.driver.quit()


# driver.find_element_by_link_text("服装").click()
# driver.find_element_by_partial_link_text("BRIOSO格子衬衫 女 长袖201").click()
# driver.find_element_by_css_selector('[class="spec-values "]').click()
# driver.find_element_by_partial_link_text("XL").click()
# driver.find_element_by_partial_link_text("立即购买").click()
# driver.quit()






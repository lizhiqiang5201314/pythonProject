import unittest

from selenium import  webdriver
from time import  sleep
from unittestreport import list_data, ddt,json_data,rerun


@ddt
class Testuser(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://101.34.251.228/shopxo/")

    @json_data(r"C:\Users\lzq\PycharmProjects\pythonProject1\first\shoping\aa.json")
    def testzhuce1(self,case):
        name=case["data"][0]
        pwd=case["data"][1]
        driver=self.driver
        driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/a[2]').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[1]/input').send_keys(name)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[2]/div/input').send_keys(pwd)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[3]/label').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[4]/button').click()
        try:
            aa = driver.find_element_by_xpath('//*[@class="top-nav-left"]/div/div/em[2]').text
            self.assertEqual(aa, case["expected"], msg="注册成功")
        except:
            bb =driver.find_element_by_xpath('//*[@id="common-prompt"]/div/p').text
            self.assertIn(bb,case["expected"],msg="注册失败")

    # @json_data(r"C:\Users\lzq\PycharmProjects\pythonProject1\first\shoping\bb.json")
    # @ddt
    # def Testzhuce2(self,case):
    #     name = case["data"][0]
    #     pwd = case["data"][1]
    #     driver = self.driver
    #     driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/a[2]').click()
    #     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[1]/input').send_keys(name)
    #     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[2]/div/input').send_keys(pwd)
    #     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[3]/label').click()
    #     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[4]/button').click()
    #     try:
    #         aa = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/em/span/em[2]').text
    #         self.assertEqual(aa, case["expected"], msg="注册成功")
    #     except:
    #         bb = driver.find_element_by_xpath('//*[@id="common-prompt"]/div/p').text
    #         self.assertIn(bb, case["expected"], msg="注册失败")
    def tearDown(self) -> None:
        self.driver.quit()


class Test_login(unittest.TestCase):
    @json_data(r'D:\idea\Pycharm\pythonProject1\com\cs\login.json')
    def test_login(self, case):
        title = case['title']
        """{}""".format(title)
        data = case['data']
        expected = case['expected']
        name, password = data
        driver = self.driver
        # 点击登录
        driver.find_element(By.LINK_TEXT, '登录').click()
        # 输入账号
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@name="accounts"]').send_keys(name)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@name="pwd"]').send_keys(password)  # 输入密码
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@class="am-btn am-btn-primary am-btn-block am-radius am-btn-sm btn-loading-example"]').click()  # 点击登录
        time.sleep(2)
        try:
            em = driver.find_element(By.XPATH, '//*[@class="top-nav-left"]/div/div/em[2]').text
            self.assertEqual(em, expected, title)
        except:
            p = driver.find_element(By.XPATH, '//*[@class="prompt-msg"]').text
            self.assertEqual(p, expected, title)

        def tearDown(self) -> None:
            self.driver.quit()

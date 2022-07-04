import unittest

from selenium import  webdriver
from time import  sleep
from unittestreport import list_data, ddt,json_data,rerun
class Test_a(unittest.TestCase) :
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://101.34.251.228/shopxo/")
    def setUp(self):
        print("************每条用例执行之前都会执行这个方法********")
    def test_001(self):
        print("测试用例001")
    def test_002(self):
        print("执行用例002")
    def tearDown(self):
        print("************每条用例执行之后都会执行这个方法********")
    @classmethod
    def tearDownClass(cls):
        print("************测试类执行之后会执行这个动作aa**********")

class Test_b(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("************测试类执行之前都会执行的动作bb**********")
    def setUp(self):
        print("************每条用例执行之前都会执行这个方法********")
    def test_001(self):
        print("测试用例003")
    def test_002(self):
        print("执行用例004")
    def tearDown(self):
        print("************每条用例执行之后都会执行这个方法********")
    @classmethod
    def tearDownClass(cls):
        print("************测试类执行之后会执行这个动作bb**********")



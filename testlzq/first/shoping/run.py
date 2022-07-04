import unittest
import time
import unittestreport
from unittestreport import TestRunner
suite=unittest.defaultTestLoader.discover(r"C:\Users\lzq\PycharmProjects\pythonProject1")
import unittestreport
now=time.strftime("%Y-%M-%d %H-%M-%S")
suite = unittest.defaultTestLoader.discover(r'C:\Users\lzq\PycharmProjects\pythonProject1\first\shoping')
runner = unittestreport.TestRunner(suite,
                                   tester='测试人员—李志强',
                                   filename="商城用户注册{}".format(now),
                                   report_dir=r"C:\Users\lzq\PycharmProjects\pythonProject1\first",
                                   title='测试报告',
                                   desc='小钉钉项目测试生成的报告描述',
                                   templates=1
                                   )

runner.run()

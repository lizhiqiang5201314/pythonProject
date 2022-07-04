import time
import unittest
import time

import unittestreport
from unittestreport import TestRunner

# from test_001 import *
# from test import test_001
#创建一个测试套件
# suite=unittest.TestSuite()
# #创建一个用例加载器
# loader=unittest.TestLoader()
#将用例加载到套件中
# suite.addTest(loader.loadTestsFromTestCase(Test_a))#通过类名加载
# suite.addTest(loader.loadTestsFromModule(test_001)) #通过模块加载
# suite.addTest(loader.discover(r"C:\Users\lzq\PycharmProjects\pythonProject1")) #通过路径加载
suite=unittest.defaultTestLoader.discover(r"C:\Users\lzq\PycharmProjects\pythonProject1") #通过路径加载
# report_dir=r'C:\Users\lzq\PycharmProjects\pythonProject1\teset_report\1.html'
# now=time.strftime()
# runner = unittestreport.TestRunner(suite,
#                                    tester='测试人员—小柠檬',
#                                    filename="jj.html",
#                                    report_dir=r"C:\Users\lzq\PycharmProjects\pythonProject1\test",
#                                    title='芙蓉区院士',
#                                    desc='小JJ项目测试生成的报告描述',
#                                    templates=2
#                                    )
# runner = TestRunner(suite)
# runner.run()
#
# print(suite.countTestCases()) #检查套件中用例总数
import unittestreport
# 1、加载测试用例到套件中
now=time.strftime("%Y-%M-%d %H-%M-%S")
suite = unittest.defaultTestLoader.discover(r'C:\Users\lzq\PycharmProjects\pythonProject1\test')

# 2、创建一个用例运行程序
runner = unittestreport.TestRunner(suite,
                                   tester='测试人员—小钉钉',
                                   filename="钉钉报告{}".format(now),
                                   report_dir=r"C:\Users\lzq\PycharmProjects\pythonProject1\first",
                                   title='钉钉报告',
                                   desc='小钉钉项目测试生成的报告描述',
                                   templates=2
                                   )

# 3、运行测试用例
runner.run()

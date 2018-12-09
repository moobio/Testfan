import HTMLTestRunner
import unittest

class MyUnit(unittest.TestCase):
    mylst=[]

    def setUp(self):
        self.mylst = [1, 2, 3]
        print("333333333")
    def test_case_num(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("1111111")
    def test_case_list(self):
        self.assertEqual([1,2,3],self.mylst,"they are not equal")   # assert 断言
        print("2222222")

    def tearDown(self):
        self.mylst = None
        print("44444444")



def mysuite():
    suite=unittest.TestSuite()
    suite.addTest(MyUnit("test_case_num"))
    suite.addTest(MyUnit("test_case_list"))
    return suite

if __name__ == "__main__":
    filename = 'E:\\Testfun\\20181202\\tryunitest\\TestfanResult.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title="报告结果",
    description="用例执行情况：")

    runner=unittest.TextTestRunner()
    runner.run(mysuite())
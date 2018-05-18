import unittest
# import AboutName不可行
from aclazz.help import AboutName

class A_test(unittest.TestCase):
    '''测试get_format_name函数'''
    def test_get_format_name(self):
        format_name = AboutName.get_format_name("liang",'ben')
        self.assertEqual(format_name , "liang ben")

    def test_get_format_midd_name(self):
        format_name2 = AboutName.get_format_name("liang", 'ben', "xia")
        self.assertEqual(format_name2, "liang xia ben")

unittest.main
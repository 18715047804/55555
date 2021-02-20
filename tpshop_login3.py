# 导包
import unittest
from selenium import webdriver
import time


# 自定义测试类
# class TestTPShopLogin(unittest.TestCase):
#     """测试是十四"""
#     driver = None
#
#     # 使用类级别的 steUp()方法做测试准备工作
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#         # 设置全屏显示
#         cls.driver.maximize_window()
#         # 设置隐式等待
#         cls.driver.implicitly_wait(30)
#         cls.driver.get("https://qh.sxxml8.cn/k0wkc5ckk0/auth/login")
#
#     # 使用类级别的 tearDown()方法做测试收尾工作
#     @classmethod
#     def tearDownClass(cls):
#         time.sleep(3)
#         cls.driver.quit()
#
#         time.sleep(2)
#
# #___________________________________________________________________
#
#     # 使用方法级别的 steUp() 方法给下一条用例的执行做准备
#     def setUp(self) -> None:
#         self.driver.get("https://t01.titi168.cn/k0wkc5ckk0/auth/login")
#
#         # 点击首页的‘登录’链接，进入登录页面
#
#
#     def tearDown(self) -> None:
#         time.sleep(3)
# #___________________________________________________________________
#     # 自定义测试方法
#     def test_account_does_not_exist(self):
#
#
#         self.driver.find_element_by_id("username1").send_keys("admin")
#         time.sleep(3)
#         self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("1234567")
#         time.sleep(3)
#         self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[6]/div/button").click()
#         print("先走1")
#         a=self.driver.page_source
#
#         if "用户名和密码不符" in a:
#             print("用户名和密码不符第一个用列")
#         else:
#             print("判断错误")
#
#
#     def test_account_does_noty_extst(self):
#
#         self.driver.find_element_by_id("username1").send_keys("admin")
#         time.sleep(3)
#         self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("1234567")
#         time.sleep(3)
#         self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[6]/div/button").click()
#         print("再走2")
#
#         n= self.driver.page_source
#
#         if "用户名和密码不符" in n:
#             print("用户名和密码不符")
#         else:
#             print("判断错误")
#
#     def test_account_does_noot_exst(self):
#
#         self.driver.find_element_by_id("username1").send_keys("admin")
#         time.sleep(3)
#         self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("")
#         time.sleep(3)
#         self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[6]/div/button").click()
#         print("再走3")
#
#         n = self.driver.page_source
#
#         if "用户名和密码不符" in n:
#             print("用户名和密码不符")
#         else:
#             print("判断错误")










def add(a,b):
    return a+b

#第一步 导包
import  unittest
#___________________________________________________________________________________________
#第二不 自定义测试类并且要继承框架类unittest.TestCase 不继承就是一个普通的类
class TestAdd2(unittest.TestCase):
     """测试"""
# ___________________________________________________________________________________________

    # 第三步 自定义测试方法 (必须test开头)
     def test_add_011(self):
        result = add(1,1,)
        print(result)

     def test_add_022(self):
         result = add(1, 0 )
         print(result)

     def test_add_033(self):
         result = add(0, 0, )
         print(result)

#___________________________________________________________________________________________

# 打开运行方式
if __name__ == '__main__':
    unittest.main()


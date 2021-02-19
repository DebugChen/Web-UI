from selenium import webdriver
import time
import unittest


class MyTestCase_XBDY_Login_GG(unittest.TestCase):
    '''新北斗云平台-登录公共方法'''

    @classmethod
    def setUpClass(cls):
        # # 启动Chrome浏览器
        # cls.dr = webdriver.Chrome()

        chromedriver = "D:\chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "E:\自动化下载文件存放"}
        chromeOptions.add_experimental_option("prefs", prefs)
        cls.dr = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("http://172.30.1.200:8080/#/")
        # 输入用户名
        cls.dr.find_element_by_xpath('//input[@placeholder="请输入账号"]').send_keys("XD0020")
        time.sleep(1)
        # 输入密码
        cls.dr.find_element_by_xpath(
            '//input[@placeholder="请输入密码"]').send_keys("Douniu2918")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//*[@id="app"]/div/div/div/button').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

if __name__=='__main__':
    unittest.main()
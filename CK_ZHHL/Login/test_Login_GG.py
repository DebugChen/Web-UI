from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase_ZHHL_Login_GG(unittest.TestCase):
    '''城市基础设施监测平台-登录公共模块-测试集'''

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
        cls.dr.get("http://172.30.1.200:7070/")
        wait = WebDriverWait(cls.dr, 10, 0.2)
        # 输入用户名
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入账号"]'))).send_keys("chenkai")
        # 输入密码
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入密码"]'))).send_keys("Xd0020110")
        # 输入验证码
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入验证码"]'))).send_keys("1111")
        # 点击登录按钮
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'loginEvent'))).click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

if __name__ == '__main__':
    unittest.main()
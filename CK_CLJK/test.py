import time
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase_CLJK_Login(unittest.TestCase):

    def test_46js4a(self):
        """控制滚动条-整个浏览器-scrollTo()"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

        wait = WebDriverWait(self.driver, 10, 0.2)
        wait.until(EC.visibility_of_element_located((By.ID, "kw"))).send_keys('Python')
        wait.until(EC.visibility_of_element_located((By.ID, "su"))).click()

        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "su"))).click()
        # self.driver.find_element_by_id('kw').send_keys('Python')
        # self.driver.find_element_by_id('su').click()
        time.sleep(2)

        js1 = 'window.scrollTo(0,10000)'
        self.driver.execute_script(js1)
        time.sleep(2)
        js2 = 'window.scrollTo(0,0)'
        self.driver.execute_script(js2)
        time.sleep(1)
        self.driver.quit()

if __name__=='__main__':
     unittest.main()

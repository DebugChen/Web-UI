import os
from BeautifulReport import BeautifulReport
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZHHL_ZHGL_Cx(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-账户管理模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\ZHGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\ZHGL\img"), img_name))

    # 关闭测试用例方法
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_ZHGL_Cx')
    def test_ZHHL_ZHGL_Cx(self):
        '''账户管理模块-查询测试用例'''
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 鼠标悬停在“系统管理”链接上
        link = wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')))
        ActionChains(self.dr).move_to_element(link).perform()
        # 点击账号管理菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//p[.="账号管理"]'))).click()
        time.sleep(2)
        # #按登录账号精确查询
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[1]/div/input')\
            .send_keys('chenkai')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, 'chenkai', '按登录账号精确查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

        # #按登录账号模糊查询
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[1]/div/input') \
            .send_keys('chen')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span2, 'chenkai', '按登录账号模糊查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

        # #按手机号精确查询
        # 输入手机号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[2]/div/input')\
            .send_keys('13636056931')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span3 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]/'
            'div[2]/table/tbody/tr/td[3]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span3, '13636056931', '按手机号精确查询失败')
        time.sleep(2)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

        # #按手机号模糊查询
        # 输入手机号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[2]/div/input') \
            .send_keys('6931')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span3 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]/'
            'div[2]/table/tbody/tr/td[3]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span3, '13636056931', '按手机号模糊查询失败')
        time.sleep(2)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

        # #按账号类型查询：星豆
        # 选择账号类型
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[3]/div/div[1]/div/span').click()
        time.sleep(0.5)
        # 选中：星豆
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[3]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr[1]/td[5]/div/div/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '星豆', '按账号类型查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

        # #按账号类型查询：组织
        # 选择账号类型
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[3]/div/div[1]/div/span').click()
        time.sleep(0.5)
        # 选中：组织
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[3]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr[1]/td[5]/div/div/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '组织', '按账号类型查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

        # #按账号状态查询：启用中
        # 选择账号状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[4]/div/div[1]/div/span').click()
        time.sleep(0.5)
        # 选中：启用中
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[4]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div3 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]/'
            'div[2]/table/tbody/tr[1]/td[4]/div/div/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div3, '启用中', '按账号状态查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

        # #按账号状态查询：已禁用
        # 选择账号状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[4]/div/div[1]/div/span').click()
        time.sleep(0.5)
        # 选中：已禁用
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[4]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div3 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]/'
            'div[2]/table/tbody/tr[1]/td[4]/div/div/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div3, '已禁用', '按账号状态查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

    @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_ZHGL_Fy')
    def test_ZHHL_ZHGL_Fy(self):
        '''账户管理模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(0.5)
        # 选中：50条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[1]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(1)

        # #按100条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(0.5)
        # 选中：100条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[1]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(1)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(0.5)
        # 选中：20条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[1]/div/div[2]/ul[2]/li[1]').click()
        time.sleep(1)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath('//li[@title="下一页"]').click()
        time.sleep(2)
        # 点击上一页
        self.dr.find_element_by_xpath('//li[@title="上一页"]').click()
        time.sleep(2)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath('//li[@title="3"]').click()
        time.sleep(2)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[2]/input').send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]'
            '/ul/div/div[2]/input').send_keys('4')
        time.sleep(1)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath(
            '//div[@class="page-box pagingChild"]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_ZHGL_Cx('test_ZHHL_ZHGL_Cx'))
    testunit.addTest(MyTestCase_ZHHL_ZHGL_Cx('test_ZHHL_ZHGL_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-账户管理模块-查询测试报告',
                  description='城市基础设施监测平台-账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)
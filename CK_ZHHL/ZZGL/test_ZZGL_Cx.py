from BeautifulReport import BeautifulReport
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZHHL_ZZGL_Cx(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-组织管理模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\ZZGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\ZZGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_ZZGL_Cx')
    def test_ZHHL_ZZGL_Cx(self):
        '''组织管理模块-查询测试用例'''
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 鼠标悬停在“系统管理”链接上
        link = wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')))
        ActionChains(self.dr).move_to_element(link).perform()
        # 点击组织管理菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//p[.="组织管理"]'))).click()
        time.sleep(3)
        # #按组织名称精确查询
        # 输入组织名称
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[1]/div/input').send_keys('软件部')
        time.sleep(0.5)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '软件部', '按组织名称查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(3)

        # #按组织名称模糊查询
        # 输入组织名称
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[1]/div/input').send_keys('软件')
        time.sleep(0.5)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span2, '软件部', '按组织名称查询失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(3)

        # #按组织状态查询（启用中）
        # 选择组织状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[2]/div/div[1]').click()
        time.sleep(1)
        # 选中组织状态：启用中
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[2]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/div/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '启用中', '按组织状态查询失败')
        time.sleep(2)

        # #按组织状态查询（已禁用）
        # 选择组织状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[2]/div/div[1]').click()
        time.sleep(1)
        # 选中组织状态：已禁用
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[2]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/div/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '已禁用', '按组织状态查询失败')
        time.sleep(2)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)

    @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    # @BeautifulReport.add_test_img('test_ZHHL_ZZGL_Fy')
    def test_ZHHL_ZZGL_Fy(self):
        '''组织管理模块-分页测试用例'''
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
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_ZZGL_Zzscx')
    def test_ZHHL_ZZGL_Zzscx(self):
        '''组织管理模块-组织树测试用例'''
        # 输入组织树客户
        self.dr.find_element_by_xpath('//input[@placeholder="请选择组织"]').send_keys('软件部')
        time.sleep(0.5)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/span/img').click()
        time.sleep(2)
        # 选中组织树：软件部
        self.dr.find_element_by_xpath('//*[@id="ztree_20_span"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span3 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span3, '软件部', '按组织名称查询失败')
        time.sleep(1)
        # 点击刷新界面
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div[2]/img').click()
        time.sleep(3)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_ZZGL_Cx('test_ZHHL_ZZGL_Cx'))
    testunit.addTest(MyTestCase_ZHHL_ZZGL_Cx('test_ZHHL_ZZGL_Fy'))
    testunit.addTest(MyTestCase_ZHHL_ZZGL_Cx('test_ZHHL_ZZGL_Zzscx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-组织管理模块-查询测试报告',
                  description='城市基础设施监测平台-组织管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # fp = open('../ZZGL/report/result1.html', 'wb')
    # # 定义测试报告
    # runner = HTMLTestRunner(stream=fp,
    #                         title='智慧护栏平台-UI自动化测试报告',
    #                         description='客户信息管理模块-测试用例执行情况')
    # # 执行测试用例
    # runner.run(testunit)
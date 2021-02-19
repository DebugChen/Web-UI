import os
from BeautifulReport import BeautifulReport
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZZHL_WHRYGL_Edit(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-成员管理模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\CYGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\WHRYGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZZHL_WHRYGL_Edit1')
    def test_ZZHL_WHRYGL_Edit1(self):
        '''维护人员管理模块-成员管理模块-状态：锁定'''
        # 鼠标悬停在“工单管理”链接上
        link = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/div/div[1]/li')
        ActionChains(self.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击维护单位菜单
        self.dr.find_element_by_xpath("//p[.='成员管理']").click()
        time.sleep(2)
        # 输入维护人员
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的维护人员名称"]').send_keys('测试维护人员A')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑按钮
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[7]/div/button[2]').click()
        time.sleep(2)
        # 修改维护人员
        self.dr.find_element_by_xpath('//input[@placeholder="请输入维护人员名称"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入维护人员名称"]').send_keys('测试维护人员A')
        time.sleep(1)
        # 修改维护人员账户
        self.dr.find_element_by_xpath('//input[@placeholder="请输入维护人员账号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入维护人员账号"]').send_keys('测试维护人员A')
        time.sleep(1)
        # 修改联系电话
        self.dr.find_element_by_xpath('//input[@placeholder="请输入维护人员联系电话"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入维护人员联系电话"]').send_keys('13366666666')
        time.sleep(1)
        # 选择证件类型
        self.dr.find_element_by_xpath('//input[@placeholder="请选择维护人员证件类型"]').click()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护人员证件类型"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护人员证件类型"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 修改证件号码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入证件号码"]').send_keys('420902199902011222')
        time.sleep(1)
        # 选择维护单位
        self.dr.find_element_by_xpath('//input[@placeholder="请选择维护单位"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护单位"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护单位"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 选择状态：锁定
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[7]/div/label[2]/span[1]/span').click()
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[2]/div/div[3]/div/button[1]').click()
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(1)
        # 输入维护人员
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的维护人员名称"]').send_keys('测试维护人员A')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '测试维护人员A', '编辑维护人员失败')
        time.sleep(1)
        # 获取查询结果，保存在变量里
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '锁定', '编辑维护人员失败')
        time.sleep(1)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZZHL_WHRYGL_Edit2')
    def test_ZZHL_WHRYGL_Edit2(self):
        '''维护人员管理模块-成员管理模块-状态：正常'''
        # 输入维护人员
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的维护人员名称"]').send_keys('测试维护人员A')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[7]/div/button[2]').click()
        time.sleep(2)
        # 修改维护人员
        self.dr.find_element_by_xpath('//input[@placeholder="请输入维护人员名称"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入维护人员名称"]').send_keys('测试维护人员A')
        time.sleep(1)
        # 修改维护人员账户
        self.dr.find_element_by_xpath('//input[@placeholder="请输入维护人员账号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入维护人员账号"]').send_keys('测试维护人员A')
        time.sleep(1)
        # 修改联系电话
        self.dr.find_element_by_xpath('//input[@placeholder="请输入维护人员联系电话"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入维护人员联系电话"]').send_keys('13366666666')
        time.sleep(1)
        # 选择证件类型
        self.dr.find_element_by_xpath('//input[@placeholder="请选择维护人员证件类型"]').click()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护人员证件类型"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护人员证件类型"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 修改证件号码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入证件号码"]').send_keys('420902199902011111')
        time.sleep(1)
        # 选择维护单位
        self.dr.find_element_by_xpath('//input[@placeholder="请选择维护单位"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护单位"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择维护单位"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 选择状态：正常
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[7]/div/label[1]/span[1]/span').click()
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[2]/div/div[3]/div/button[1]').click()
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(1)
        # 输入维护人员
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的维护人员名称"]').send_keys('测试维护人员A')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '测试维护人员A', '编辑维护人员失败')
        time.sleep(1)
        # 获取查询结果，保存在变量里
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '正常', '编辑维护人员失败')
        time.sleep(1)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZZHL_WHRYGL_Edit('test_ZZHL_WHRYGL_Edit1'))
    testunit.addTest(MyTestCase_ZZHL_WHRYGL_Edit('test_ZZHL_WHRYGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-成员管理模块-编辑测试报告',
                  description='城市基础设施监测平台-成员管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)
import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sblb_Plgx(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-设备列表模块-批量更新测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\SBLB\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\SBLB\img"), img_name))

    # 执行文件上传方法
    @staticmethod
    def upload_file(exe, browser, filename):
        """
        使用autoIt上传文件
        :param exe: 上传文件的exe程序所在目录
        :param browser: 浏览器类型： firefox chrome ie
        :param filename: 待上传文件路径
        :return: none
        """
        cmd = exe + ' ' + browser + ' ' + filename
        os.system(cmd)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sblb_Plgx')
    def test_XBDY_Sblb_Plgx(self):
        '''设备列表模块-批量更新测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换设备列表菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[2]').click()
        time.sleep(2)

        # 点击批量更新
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[3]/div[1]/div/div[1]/button[4]').click()
        time.sleep(1)
        # 点击选取文件弹出上传文件窗口
        upload_element = self.dr.find_element_by_xpath(
            '//div[@class="ivu-upload ivu-upload-select"]/button[2]')
        action = ActionChains(self.dr)
        action.move_to_element(upload_element).click().perform()
        action.release()
        time.sleep(3)
        # 选取要上传的文件
        MyTestCase_XBDY_Sblb_Plgx.upload_file(
            r'E:\123.exe ', 'chrome', r'E:\自动化下载文件存放\新北斗云-设备列表模板.xlsx')
        time.sleep(2)
        # 点击上传
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div/div[2]/button').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-custom-content ivu-message-success"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '数据导入成功！', '批量更新失败')
        time.sleep(1)
        # 点击关闭
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[3]/div/div/button').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sblb_Plgx('test_XBDY_Sblb_Plgx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-设备列表模块-批量更新测试报告',
                  description='新北斗云平台-设备列表模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)
import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sblb_Edit(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-设备列表模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\SBLB\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'  .format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\SBLB\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sblb_Edit')
    def test_XBDY_Sblb_Edit(self):
        '''设备列表模块-编辑测试用例'''
        self.dr = webdriver.Chrome()

        # 切换设备列表菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[2]').click()
        time.sleep(2)

        # #按IMEI精确查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI号"]').send_keys('352736081541925')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[2]'
            '/div[1]/div[1]/div[2]/table/tbody/tr/td[10]/div/div/button[1]').click()
        time.sleep(1)

        # 修改设备信息
        # 修改服务到期时间
        self.dr.find_element_by_xpath('//input[@placeholder="输入服务到期时间"]').click()
        time.sleep(1)
        # 选中2020-11-24
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-select-dropdown ivu-date-picker-transfer"]'
            '/div/div/div/div[2]/div/span[24]').click()
        time.sleep(1)

        # 修改用户信息
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]').click()
        time.sleep(1)
        # 修改绑定用户姓名
        self.dr.find_element_by_xpath('//input[@placeholder="请输入姓名"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入姓名"]').send_keys('张三')
        time.sleep(1)
        # 修改性别
        self.dr.find_element_by_xpath('//div[@splaceholder="请选择性别"]').click()
        time.sleep(1)
        # 选中男
        self.dr.find_element_by_xpath('//div[@splaceholder="请选择性别"]/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 修改年龄
        self.dr.find_element_by_xpath('//input[@placeholder="请输入年龄"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入年龄"]').send_keys('18')
        time.sleep(1)
        # 修改手机号码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys('13654254525')
        time.sleep(1)
        # 修改证件类型
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[2]'
            '/div/div/div[2]/div[2]/form/div[3]/div[3]/div/div/div').click()
        time.sleep(1)
        # 选中护照
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[2]'
            '/div/div/div[2]/div[2]/form/div[3]/div[3]/div/div/div/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        # 修改证件号码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').send_keys('420902199803051254')
        time.sleep(1)

        # 修改其他绑定信息
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div/div/div[1]/div/div/div/div/div[4]').click()
        time.sleep(1)
        # 修改车牌号
        self.dr.find_element_by_xpath('//input[@placeholder="请输入车牌号"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入车牌号"]').send_keys('鄂A11111')
        time.sleep(1)
        # 修改车辆颜色
        self.dr.find_element_by_xpath('//input[@placeholder="请输入车辆颜色"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入车辆颜色"]').send_keys('黑色')
        time.sleep(1)

        # 修改物联网卡信息
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div/div/div[1]/div/div/div/div/div[5]').click()
        time.sleep(1)

        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[3]/div/div/button[1]').click()
        time.sleep(1)

        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[3]/div/div/button/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '关闭', '查看详情失败')
        time.sleep(1)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sblb_Edit('test_XBDY_Sblb_Edit'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-设备列表模块-编辑测试报告',
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
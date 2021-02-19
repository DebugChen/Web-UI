import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Rzcx_Cx(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-日志查询模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\RZCX\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'  .format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\RZCX\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Rzcx_Cx')
    def test_XBDY_Rzcx_Cx(self):
        '''日志查询模块-查询测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换日志查询菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[5]').click()
        time.sleep(2)

        # #按IMEI精确查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI号"]').send_keys('861097040963096')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '861097040963096', '按IMEI精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按IMEI模糊查询
        # 输入IMEi
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI号"]').send_keys('3096')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '808029800123096', '按IMEI模糊查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按ICCID精确查询
        # 输入ICCID
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入ICCID"]').send_keys('89860416141871873632')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '89860416141871873632', '按ICCID精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按ICCID模糊查询
        # 输入ICCID
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入ICCID"]').send_keys('3632')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '89860410171980036329', '按ICCID模糊查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按激活时间查询
        # 选择激活时间
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div/div[1]/button').click()
        time.sleep(1)
        # 选择开始时间
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选择月份
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/span[3]/span[2]').click()
        time.sleep(1)
        # 选中11月
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/span[11]/em').click()
        time.sleep(1)
        # 选中日期
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选中5日
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/span[5]/em').click()
        time.sleep(1)

        # 选择结束时间
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[3]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选择月份
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/span[3]/span[2]').click()
        time.sleep(1)
        # 选中11月
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/'
            'div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/'
            'div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/span[11]/em').click()
        time.sleep(1)
        # 选中日期
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[3]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选中8日
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/span[8]/em').click()
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]/div/span').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '2020-09-01 00:00:00', '按接入时间精确查询失败')
        # time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)
        #
        # #按服务到期时间查询
        # 点击更多
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[4]/div[1]').click()
        time.sleep(1)
        # 选中服务到期时间项
        self.dr.find_element_by_xpath('//input[@value="服务到期时间"]').click()
        time.sleep(1)
        # 选择服务到期时间
        self.dr.find_element_by_xpath(
            '//div[@class="search-wrapper"]/div[2]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        # 选择开始时间
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选择月份
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/span[3]/span[2]').click()
        time.sleep(1)
        # 选中11月
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/span[11]/em').click()
        time.sleep(1)
        # 选中日期
        self.dr.find_element_by_xpath(
            '//div[@class="search-wrapper"]/div[2]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="search-wrapper"]/div[2]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选中28日
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/span[28]/em').click()
        time.sleep(1)

        # 选择结束时间
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[3]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选择月份
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/span[3]/span[2]').click()
        time.sleep(1)
        # 选中11月
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/span[11]/em').click()
        time.sleep(1)
        # 选中日期
        self.dr.find_element_by_xpath(
            '//div[@class="search-wrapper"]/div[2]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="search-wrapper"]/div[2]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]'
            '/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div'
            '/div[3]/div/div[1]/div/input').click()
        time.sleep(1)
        # 选中30日
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]'
            '/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div'
            '/div[3]/div/div[2]/div/div/div/div[2]/div/span[30]/em').click()
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]'
            '/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[5]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '2020-11-30 00:00:00', '按服务到期时间查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按IMEIS查询
        # 点击更多
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[4]/div[1]').click()
        time.sleep(1)
        # 选中IMEIS项
        self.dr.find_element_by_xpath('//input[@value="IMEIS"]').click()
        time.sleep(1)
        # 选择IMEIS
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]'
            '/div/div[2]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="imei imei"]').send_keys('352736081541925 352736082365209')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]'
            '/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span1 = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '352736081541925', '按IMEIS查询失败')
        # 获取页面元素，保存到变量
        span2 = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[2]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span2, '352736082365209', '按IMEIS查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # 按车牌号查询
        # 点击更多
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[4]/div[1]').click()
        time.sleep(1)
        # 选中车牌号项
        self.dr.find_element_by_xpath('//input[@value="车牌号"]').click()
        time.sleep(1)
        # 选择车牌号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]'
            '/div/div[2]/div[3]/div/div[1]/button').click()
        time.sleep(1)
        # 输入车牌号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入车牌号"]').send_keys('WJZ62010')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]'
            '/div/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 点击查看详情
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[2]'
            '/div[1]/div[1]/div[2]/table/tbody/tr/td[10]/div/div/button[2]').click()
        time.sleep(1)
        # 切换到其他绑定信息界面
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[2]'
            '/div/div/div[1]/div/div/div/div/div[4]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[2]'
            '/div/div/div[2]/div[3]/form/div[1]/div[1]/div/div/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, 'WJZ62010', '按车牌号查询失败')
        time.sleep(1)
        # 点击关闭
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[3]/div/div/button').click()
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Rzcx_Fy')
    def test_XBDY_Rzcx_Fy(self):
        '''日志查询模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中50条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(3)

        # #按100条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中100条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(3)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中20条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[2]/ul[2]/li[1]').click()
        time.sleep(3)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath('//li[@title="下一页"]').click()
        time.sleep(3)
        # 点击上一页
        self.dr.find_element_by_xpath('//li[@title="上一页"]').click()
        time.sleep(3)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath('//li[@title="3"]').click()
        time.sleep(3)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[3]/div[2]/div[2]/div/ul/div/div[2]/input').send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[3]/div[2]/div[2]/div/ul/div/div[2]/input').send_keys('4')
        time.sleep(1)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//ul[@class="ivu-page"]').click()
        time.sleep(2)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Rzcx_Cx('test_XBDY_Rzcx_Cx'))
    testunit.addTest(MyTestCase_XBDY_Rzcx_Cx('test_XBDY_Rzcx_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-日志查询模块-查询测试报告',
                  description='新北斗云平台-日志查询模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)
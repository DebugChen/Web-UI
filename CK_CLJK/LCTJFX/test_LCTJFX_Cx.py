import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_LCTJFX_Cx(unittest.TestCase):
    '''车辆监控平台-里程统计分析模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\LCTJFX\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://ebeta.starlinkware.com/")
        # 输入用户名
        cls.dr.find_element_by_id("username").send_keys("chenkai")
        time.sleep(1)
        # 输入密码
        cls.dr.find_element_by_id("password").send_keys("Xd0020110")
        time.sleep(1)
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(3)
        # 鼠标悬停在“数据统计分析”链接上
        link = cls.dr.find_element_by_xpath(
            '//div[@class="happy-scroll-content"]/div/ul/li[4]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击里程统计分析菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[3]/ul').click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\LCTJFX\image\LCTJFX_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_LCTJFX_Cx')
    def test_CLJK_LCTJFX_Cx(self):
        '''里程统计分析模块-查询测试用例'''
        # 选择时间
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的月份"]').click()
        time.sleep(2)
        # 选中十月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[3]/td[2]/div').click()
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(15)

        # #按客户名称精确查询
        # 输入客户名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的客户名称"]').send_keys('长城安防公司')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '长城安防公司', '按客户名称精确查询里程信息失败')
        time.sleep(2)

        # #按客户名称模糊查询
        # 输入客户名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的客户名称"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的客户名称"]').send_keys('玉桥')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '三大队-玉桥', '按客户名称模糊查询里程信息失败')
        time.sleep(2)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除搜索条件"]').click()
        time.sleep(5)

        # #按IMEI精确查询
        # 选择时间
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的月份"]').click()
        time.sleep(2)
        # 选中十月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[3]/td[2]/div').click()
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(15)
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的IMEI号"]').send_keys('097040762134')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '097040762134', '按IMEI精确查询里程信息失败')
        time.sleep(2)

        # #按IMEI模糊查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的IMEI号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的IMEI号"]').send_keys('6166')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '097040526166', '按IMEI模糊查询里程信息失败')
        time.sleep(2)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除搜索条件"]').click()
        time.sleep(5)

        # #按车牌号精确查询
        # 点击更多
        self.dr.find_element_by_xpath('//button[@title="更多搜索条件"]').click()
        # 选择时间
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的月份"]').click()
        time.sleep(2)
        # 选中十月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[3]/td[2]/div').click()
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(15)
        # 输入车牌号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号"]').send_keys('随X01807安防')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '随X01807安防', '按车牌号精确查询里程信息失败')
        time.sleep(2)

        # #按车牌号模糊查询
        # 输入车牌号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号"]').send_keys('355')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '随J03355', '按车牌号模糊查询里程信息失败')
        time.sleep(2)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除搜索条件"]').click()
        time.sleep(5)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_LCTJFX_Fy')
    def test_CLJK_LCTJFX_Fy(self):
        '''里程统计分析模块-分页测试用例'''
        # 选择时间
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的月份"]').click()
        time.sleep(1)
        # 选中十月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[3]/td[2]/div').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(15)

        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按50条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(15)

        # #按200条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(15)

        # #按500条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按500条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(15)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(15)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath('//button[@class="btn-next"]').click()
        time.sleep(15)
        # 点击上一页
        self.dr.find_element_by_xpath('//button[@class="btn-prev"]').click()
        time.sleep(15)
        # 点击任意一页（5页）
        self.dr.find_element_by_xpath('//ul[@class="el-pager"]/li[5]').click()
        time.sleep(15)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//input[@class="el-input__inner"][@min="1"]').send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        # 获取到输入页码框，并输入页码号“8”
        self.dr.find_element_by_xpath(
            '//input[@class="el-input__inner"][@min="1"]').send_keys('8')
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//div[@class="dataList"]/div/div[3]').click()
        time.sleep(10)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_LCTJFX_Cx('test_CLJK_LCTJFX_Cx'))
    testunit.addTest(MyTestCase_CLJK_LCTJFX_Cx('test_CLJK_LCTJFX_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-里程统计分析模块-查询测试报告',
                  description='车辆监控平台-里程统计分析模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)
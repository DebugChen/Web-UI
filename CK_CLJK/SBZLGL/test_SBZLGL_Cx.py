import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_SBZLGL_Cx(unittest.TestCase):
    '''车辆监控平台-设备资料管理模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_CLJK\SBZLGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\SBZLGL\img"), img_name))

    @classmethod
    # 启动测试用例方法
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr=webdriver.Chrome()
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
        time.sleep(2)
        # 鼠标悬停在“客户资料管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//div[@class="happy-scroll-content"]/div/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“设备资料管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul/li')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击设备资料管理
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul/li').click()
        time.sleep(6)

    @classmethod
    # 关闭测试用例方法
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBZLGL_CX')
    def test_CLJK_SBZLGL_Cx(self):
        '''设备资料管理模块-查询测试用例'''
        # #按IMEI精确查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索IMEI号"]').send_keys('861097040303442')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '861097040303442', '按IMEI查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按IMEI模糊查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索IMEI号"]').send_keys('3442')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '861097040303442', '按IMEI查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按车主姓名精确查询
        # 输入车主姓名
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车主姓名"]').send_keys('张主任')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '张主任', '按车主姓名查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按车主姓名模糊查询
        # 输入车主姓名
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车主姓名"]').send_keys('寒妮')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '张寒妮', '按车主姓名查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按状态查询（正常）
        # 点击状态
        self.dr.find_element_by_xpath('//input[@placeholder="请选择设备状态"]').click()
        time.sleep(2)
        # 鼠标下键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择设备状态"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 鼠标回撤键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择设备状态"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '正常', '按正常状态查询设备失败')
        time.sleep(2)

        # #按状态查询（锁定）
        # 点击状态
        self.dr.find_element_by_xpath('//input[@placeholder="请选择设备状态"]').click()
        time.sleep(2)
        # 鼠标下键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择设备状态"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 鼠标回撤键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择设备状态"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '锁定', '按锁定状态查询设备失败')
        time.sleep(2)

        # #按状态查询（拆除）
        # 点击状态
        self.dr.find_element_by_xpath('//input[@placeholder="请选择设备状态"]').click()
        time.sleep(2)
        # 鼠标下键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择设备状态"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 鼠标回撤键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择设备状态"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '拆除', '按拆除状态查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按所属客户精确查询
        # 点击更多按钮
        self.dr.find_element_by_xpath('//button[@title="更多搜索条件"]').click()
        time.sleep(2)
        # 定位所属客户框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的所属客户"]').send_keys('二大队')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '二大队', '按所属客户查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按所属客户模糊查询
        # 定位所属客户框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的所属客户"]').send_keys('二')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '二大队', '按所属客户查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按车牌号精确查询
        # 定位车牌号框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索设备的车牌号"]').send_keys('荆州Z06537')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[4]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '荆州Z06537', '按车牌号查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按车牌号模糊查询
        # 定位车牌号框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索设备的车牌号"]').send_keys('荆州')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[4]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '荆州Z03732', '按车牌号查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按电话号码精确查询
        # 定位电话号码框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入电话号码"]').send_keys('13697061760')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '13697061760', '按电话号码查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按电话号码模糊查询
        # 定位电话号码框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入电话号码"]').send_keys('1760')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertIn(div, '13697061760', '按电话号码查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按IMEI批量查询
        # 定位IMEI批量搜索框，输入信息
        self.dr.find_element_by_xpath('//input[@placeholder="请输入IMEI IMEI"]')\
            .send_keys('861097040300398 861097040300018')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 获取页面标签，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '861097040300018', '按IMEI批量查询设备失败')
        time.sleep(2)
        # 获取页面标签，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[2]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '861097040300398', '按IMEI批量查询设备失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

        # #按安装时间查询
        # 点击安装时间
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备的安装时间"]').click()
        time.sleep(2)
        # 点击上一年
        self.dr.find_element_by_xpath('//button[@aria-label="前一年"]').click()
        time.sleep(2)
        # 点击月份
        self.dr.find_element_by_xpath(
            '//div[@class="el-picker-panel__body"]/div[1]/span[2]').click()
        time.sleep(1)
        # 选中十一月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[3]/td[3]/div/a').click()
        time.sleep(1)
        # 选中2019-11-27
        self.dr.find_element_by_xpath(
            '//table[@class="el-date-table"]/tbody/tr[6]/td[4]/div/span').click()
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(5)
        # 点击查看
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[7]/div/button[1]').click()
        time.sleep(2)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[4]/div/div[2]/div[1]/div[4]/div[4]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '2019-11-27 20:34:56', '按安装时间查询失败')
        time.sleep(2)
        # 点击关闭按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[4]/div/div[2]/div[2]/div/div/button').click()
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBZLGL_Fyxs')
    def test_CLJK_SBZLGL_Fyxs(self):
        '''设备资料管理模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按50条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(6)

        # #按200条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(7)

        # #按500条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按500条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(8)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(6)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath('//div[@class="pagingChild"]/div/div/button[2]').click()
        time.sleep(6)
        # 点击上一页
        self.dr.find_element_by_xpath('//div[@class="pagingChild"]/div/div/button[1]').click()
        time.sleep(6)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath('//div[@class="pagingChild"]/div/div/ul/li[3]').click()
        time.sleep(6)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/span[3]/div/input')\
            .send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/span[3]/div/input').send_keys('4')
        time.sleep(1)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath(
            '//div[@class="el-pagination is-background"]').click()
        time.sleep(6)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(6)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBZLGL_Khscx')
    def test_CLJK_SBZLGL_Khscx(self):
        '''设备资料管理模块-客户树查询测试用例'''
        # 获取右侧客户树，输入查询信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择客户"]').send_keys('陈凯测试')
        # 点击查询
        time.sleep(2)
        self.dr.find_element_by_xpath('//div[@class="ztreeSearch"]/i').click()
        # 点击陈凯测试客户
        time.sleep(2)
        self.dr.find_element_by_xpath(
            '//div[@class="ztree"]/div/div/div/div/li/a/span[2]').click()
        time.sleep(3)
        # 获取页面标签，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '861097041076716', '客户树查询设备失败')
        time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_SBZLGL_Cx('test_CLJK_SBZLGL_Cx'))
    testunit.addTest(MyTestCase_CLJK_SBZLGL_Cx('test_CLJK_SBZLGL_Fyxs'))
    testunit.addTest(MyTestCase_CLJK_SBZLGL_Cx('test_CLJK_SBZLGL_Khscx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-设备资料管理模块-查询测试报告',
                  description='车辆监控平台-设备资料管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)
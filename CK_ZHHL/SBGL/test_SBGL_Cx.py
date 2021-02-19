import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_ZHHL_SBZLGL_Cx(unittest.TestCase):
    '''智慧护栏平台-设备资料管理模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\SBGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\SBZLGL\img"), img_name))

    @classmethod
    # 启动测试用例方法
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr=webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://railbeta.starlinkware.com/")
        time.sleep(2)
        # 输入用户名
        cls.dr.find_element_by_id("username").send_keys("adminCK")
        time.sleep(1)
        # 输入密码
        cls.dr.find_element_by_id("password").send_keys("Douniu2918")
        time.sleep(1)
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(3)
        # 鼠标悬停在“客户资料管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击设备资料管理菜单
        cls.dr.find_element_by_xpath("/html/body/div[2]/ul/li[2]/ul/li").click()
        time.sleep(2)

    @classmethod
    # 关闭测试用例方法
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\untitled_CLJK\SBGL\image\SBZLGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_SBZLGL_Cx')
    def test_ZHHL_SBZLGL_Cx(self):
        '''设备资料管理模块-查询测试用例'''
        # #按IMEI精确查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的IMEI号"]').send_keys('861097040343935')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '861097040343935', '按IMEI查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # # #按IMEI模糊查询
        # # 定位IMEI框，输入信息
        # self.dr.find_element_by_xpath(
        # '//input[@placeholder="请输入需要搜索的IMEI号"]').send_keys('3935')
        # time.sleep(2)
        # # 点击查询按钮
        # self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        # time.sleep(2)
        # # 获取页面元素，保存到变量
        # div = self.dr.find_element_by_xpath(
        # '//table[@class="el-table__body"]/tbody/tr/td[1]/div').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(div, '861097040343935', '按IMEI查询失败')
        # time.sleep(2)
        # # 点击清除按钮
        # self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        # time.sleep(2)

        # #按护栏线名称精确查询
        # 定位护栏线名称框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的护栏线名称"]')\
            .send_keys('四川成都高升桥兴蓉西巷(a-b)')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '四川成都高升桥兴蓉西巷(a-b)', '按护栏线名称查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # # #按护栏线名称模糊查询
        # # 定位护栏线名称框，输入信息
        # self.dr.find_element_by_xpath(
        # '//input[@placeholder="请输入需要搜索的护栏线名称"]').send_keys('(a-b)')
        # time.sleep(2)
        # # 点击查询按钮
        # self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        # time.sleep(2)
        # # 获取页面元素，保存到变量
        # div = self.dr.find_element_by_xpath(
        # '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(div, '四川成都高升桥兴蓉西巷(a-b)', '按护栏线名称查询失败')
        # time.sleep(2)
        # # 点击清除按钮
        # self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        # time.sleep(2)

        # #按状态查询（安装）
        # 点击状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').click()
        time.sleep(1)
        # 键盘下键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 键盘回撤键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '安装', '按安装状态查询失败')
        time.sleep(2)

        # #按状态查询（未安装）
        # 点击状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').click()
        time.sleep(1)
        # 鼠标下键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 鼠标回撤键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '未安装', '按未安装状态查询失败')
        time.sleep(2)

        # #按状态查询（拆除）
        # 点击状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').click()
        time.sleep(2)
        # 鼠标下键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 鼠标回撤键
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的设备状态"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '拆除', '按拆除状态查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按路口名称查询
        # 点击更多按钮
        self.dr.find_element_by_xpath('//button[@title="更多搜索条件"]').click()
        time.sleep(2)
        # 输入路口名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的路口名称"]').send_keys('a')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '四川成都高升桥兴蓉西巷(a-b)', '按路口名称查询失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按路口名称查询
        # 定位所属客户框，输入信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的路口名称"]').send_keys('b')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '四川成都高升桥兴蓉西巷(a-b)', '按路口名称查询失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按安装时间查询
        # 选择安装时间
        self.dr.find_element_by_xpath('//input[@placeholder="请选择安装日期"]').click()
        time.sleep(2)
        # 点击年份
        self.dr.find_element_by_xpath(
            '//div[@class="el-picker-panel__body"]/div[1]/span[1]').click()
        time.sleep(1)
        # 点击上一年
        self.dr.find_element_by_xpath(
            '//div[@class="el-picker-panel__body"]/div[1]/button[1]').click()
        time.sleep(1)
        # 选中2019年
        self.dr.find_element_by_xpath(
            '//table[@class="el-year-table"]/tbody/tr[3]/td[2]/a').click()
        time.sleep(1)
        # # 点击月份
        # self.dr.find_element_by_xpath(
        #     '//div[@class="el-picker-panel__body"]/div[1]/span[2]').click()
        # time.sleep(1)
        # 选中十月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[3]/td[2]/div/a').click()
        time.sleep(2)
        # 选中十六日
        self.dr.find_element_by_xpath(
            '//table[@class="el-date-table"]/tbody/tr[4]/td[4]/div/span').click()
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '861097040343935', '按安装时间查询失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按是否停用报警查询（开启）
        # 点击是否停用报警
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[1]/div[2]/div/div/div[6]/div/div/div/input').click()
        time.sleep(2)
        # 鼠标下键
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[1]/div[2]/div/div/div[6]/div/div/div/input')\
            .send_keys(Keys.DOWN)
        time.sleep(2)
        # 鼠标回撤键
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[1]/div[2]/div/div/div[6]/div/div/div/input')\
            .send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[1]/div[3]/'
            'table/tbody/tr[1]/td[7]/div/button[4]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '停用报警', '按是否停用报警查询失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按是否停用报警查询（停用）
        # 点击是否停用报警
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[1]/div[2]/div/div/div[6]/div/div/div/input').click()
        time.sleep(2)
        # 鼠标下键
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[1]/div[2]/div/div/div[6]/div/div/div/input')\
            .send_keys(Keys.DOWN)
        time.sleep(2)
        # 鼠标回撤键
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[1]/div[2]/div/div/div[6]/div/div/div/input')\
            .send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[1]/div[3]/'
            'table/tbody/tr[1]/td[7]/div/button[4]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '恢复报警', '按是否停用报警查询失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按批量搜索IMEI查询
        # 输入批量搜索IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI IMEI"]').send_keys('861097040343935 861097040713780')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[2]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '861097040343935', '按IMEI批量查询失败')
        # 获取页面元素，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '861097040713780', '按IMEI批量查询失败')
        time.sleep(1)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_SBZLGL_Fy')
    def test_ZHHL_SBZLGL_Fy(self):
        '''设备资料管理模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div/div/span[2]/div/div[1]/input').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div/div/span[2]/div/div[1]/input')\
            .send_keys(Keys.DOWN)
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div/div/span[2]/div/div[1]/input')\
            .send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按50条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div/div/span[2]/div/div[1]/input')\
            .send_keys(Keys.ENTER)
        time.sleep(2)

        # #按200条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[7]/div[1]/div[3]'
                                      '/div[2]/div/div/span[2]/div/div[1]/input').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]'
            '/div/div/span[2]/div/div[1]/input').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div'
            '/div/span[2]/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)

        # #按500条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]'
                                      '/div/div/span[2]/div/div[1]/input').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div/'
            'div/span[2]/div/div[1]/input').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按500条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div'
            '/div/span[2]/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]'
                                      '/div/div/span[2]/div/div[1]/input').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div/'
            'div/span[2]/div/div[1]/input').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[2]/div/'
            'div/span[2]/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/button[2]').click()
        time.sleep(2)
        # 点击上一页
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/button[1]').click()
        time.sleep(2)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/ul/li[3]').click()
        time.sleep(3)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/span[3]/div/input')\
            .send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/span[3]/div/input').send_keys('4')
        time.sleep(2)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath(
            '//div[@class="el-pagination is-background"]').click()
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_SBZLGL_Khscx')
    def test_ZHHL_SBZLGL_Khscx(self):
        '''设备资料管理模块-客户树查询测试用例'''
        # 获取右侧客户树，输入查询信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择客户"]').send_keys('星豆慧联')
        # 点击查询
        time.sleep(2)
        self.dr.find_element_by_xpath('//div[@class="ztreeSearch"]/i').click()
        # 点击星豆慧联
        time.sleep(2)
        self.dr.find_element_by_xpath('//a[@title="星豆慧联"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '861097040969622', '按客户树查询查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_SBZLGL_Cx('test_ZHHL_SBZLGL_Cx'))
    testunit.addTest(MyTestCase_ZHHL_SBZLGL_Cx('test_ZHHL_SBZLGL_Fy'))
    testunit.addTest(MyTestCase_ZHHL_SBZLGL_Cx('test_ZHHL_SBZLGL_Khscx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-设备资料管理模块-查询测试报告',
                  description='智慧护栏平台-设备资料管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)
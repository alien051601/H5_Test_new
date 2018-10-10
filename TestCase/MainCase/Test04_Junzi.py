from time import sleep
from Test02_Login import Login
import unittest
from read_excel import *

class Junzi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化Login(),打开浏览器以及网页
        cls.l = Login()
        cls.l.test_1_inter_borrow_detail()
        cls.driver = cls.l.driver
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # 开户流程---从产品页面进入开户页面
    def test_1_open_auto_bid(self):
        junzi_page_title_css = read_css_path(124)
        # print(junzi_page_title_css)
        junzi_page_title = self.l.wait_element_get_text_by_css(junzi_page_title_css)
        print('进入页面：', junzi_page_title)

        # 点击《自动投标授权委托书》
        auto_bid_book_css = read_css_path(125)
        self.l.click_element_by_css(auto_bid_book_css)
        sleep(2)

        # 获取当前页面的url属性，current_ulr
        url_current = self.driver.current_url

        aim_url = 'Agreement/tBcontent.html'
        self.assertIn(aim_url, url_current,'没有进入到自动投标授权委托书详情页面')
        sleep(1)
        self.driver.back()
        sleep(1)

        # 点击【开启】自动投标授权
        open_auto_bid_css = read_css_path(126)
        self.l.click_element_by_css(open_auto_bid_css)
        sleep(1)

        # 捕获到汇付页面--点击【确认】开启自动投标
        auto_bid_confirm_huifu_title_css = read_css_path(128)
        auto_bid_confirm_huifu_title = self.l.wait_element_get_text_by_css(auto_bid_confirm_huifu_title_css)
        auto_bid_confirm_huifu_title_1 = '开启自动投标及自动承接债权转让'
        self.assertEqual(auto_bid_confirm_huifu_title, auto_bid_confirm_huifu_title_1)
        sleep(1)
        auto_bid_confirm_huifu_css = read_css_path(129)
        self.l.click_element_by_css(auto_bid_confirm_huifu_css)
        sleep(1)

        # 输入交易密码并确定
        auto_bid_input_pw_title_css = read_css_path(130)
        auto_bid_input_pw_title_1 = '请输入交易密码，完成本次自动投标计划开启'
        auto_bid_input_pw_title = self.l.wait_element_get_text_by_css(auto_bid_input_pw_title_css)
        self.assertEqual(auto_bid_input_pw_title_1, auto_bid_input_pw_title)
        sleep(1)

        auto_bid_input_pw_css = read_css_path(131)
        auto_bid_input_pw_confirm_css = read_css_path(132)
        self.l.input_element_by_css(auto_bid_input_pw_css, 'abc123456')
        sleep(1)
        self.l.click_element_by_css(auto_bid_input_pw_confirm_css)
        sleep(5)


if __name__ == '__main__':
    unittest.main()



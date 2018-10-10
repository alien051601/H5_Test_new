from read_excel import *
from utilities.settings import *
from utilities.common_method import *
import unittest
from Test02_Login import Login


class OpenAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.l = Login()
        cls.l.test_1_inter_borrow_detail()

    def test_1_openAccount(self):
        page_title_openAccount_css = read_css_path(92)
        page_title_openAccount = self.l.driver.find_element_by_css_selector(page_title_openAccount_css).text
        print('进入到：',page_title_openAccount, '页面')

        # 获取开户需要的数据，以及各个数据对应的css元素
        real_name_openAccount,bank_mobile_openAccount,idno_openAccount,bank_card_no_openAccount = read_open_account_data(row_num_real)

        real_name_openAccount_css = read_css_path(93)
        bank_mobile_openAccount_css = read_css_path(98)
        idno_openAccount_css = read_css_path(94)
        bank_card_no_openAccount_css = read_css_path(97)

        # 输入姓名
        self.l.c.wait_element_input_by_css(real_name_openAccount_css, real_name_openAccount)
        sleep(1)
        # 输入身份证号
        self.l.c.input_element_by_css(idno_openAccount_css, idno_openAccount)
        sleep(1)

        # 点击选择银行卡，并选择建设银行
        bank_choose_openAccount_css = read_css_path(95)
        self.l.c.click_element_by_css(bank_choose_openAccount_css)
        sleep(1)
        jianshe_bank_openAccount_css = read_css_path(96)
        self.l.c.click_element_by_css(jianshe_bank_openAccount_css)
        sleep(1)

        # 银行卡号
        self.l.c.wait_element_input_by_css(bank_card_no_openAccount_css, bank_card_no_openAccount)
        sleep(1)

        # 银行预留手机号
        self.l.c.input_element_by_css(bank_mobile_openAccount_css, bank_mobile_openAccount )
        sleep(1)

        # 短信验证码
        sms_button_openAccount_css = read_css_path(99)
        sms_input_openAccount_css = read_css_path(100)
        self.l.c.click_element_by_css(sms_button_openAccount_css)
        sleep(1)
        self.l.c.input_element_by_css(sms_input_openAccount_css, '666666')
        sleep(1)

        # 点击---【确认】
        submit_openAccount_css = read_css_path(101)
        self.l.c.click_element_by_css(submit_openAccount_css)
        sleep(10)

    def test_2_huifu(self):
        set_buy_pw_title_css = read_css_path(102)
        set_buy_pw_title = self.l.driver.find_element_by_css_selector(set_buy_pw_title_css).text
        print('进入如下页面：',set_buy_pw_title)

        # 输入交易密码
        buy_pw_openAccount_css = read_css_path(103)
        self.l.c.input_element_by_css(buy_pw_openAccount_css, 'abc123456')
        sleep(1)

        # 点击---【下一步】
        next_step_set_buy_pw_css = read_css_path(104)
        self.l.c.click_element_by_css(next_step_set_buy_pw_css)
        sleep(1)

        # 进入到开户结果页
        success_info_openAccount_result_css = read_css_path(105)
        success_info_openAccount_result = self.l.driver.find_element_by_css_selector(success_info_openAccount_result_css).text
        print('开户结果为：',success_info_openAccount_result)

        # 点击风险评测
        risk_test_openAccount_result_css = read_css_path(107)
        self.l.c.click_element_by_css(risk_test_openAccount_result_css)
        sleep(1)

        # 全部答案都选择第二个
        i = 1
        answer_second_css = read_css_path(110)
        for i in range(10):
            if i<10:
                self.l.c.wait_element_click_by_css(answer_second_css)
                i +=1

        submit_risk_test_css = read_css_path(120)
        # 点击---【提交】风险评测
        self.l.c.click_element_by_css(submit_risk_test_css)
        sleep(1)

        # 点击--【确定】
        result_ok_risk_test_css = read_css_path(122)
        self.l.c.wait_element_click_by_css(result_ok_risk_test_css)
        sleep(2)


if __name__=='__main__':
    o = OpenAccount()
    o.test_1_openAccount()
    o.test_2_huifu()


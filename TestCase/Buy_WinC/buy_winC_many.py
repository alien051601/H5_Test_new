from read_excel import *
from utilities.settings import *
from utilities.common_method import *
from write_excel import *

class Login(CommonMethod):

    def __init__(self):
        super(Login).__init__()
        self.c = CommonMethod()

        # 点击首页的---【我的】----【注册/登录】
        my_account_css = read_css_path(63)
        print(my_account_css)
        self.c.click_element_by_css(my_account_css)
        sleep(1)
        register_login_css = read_css_path(64)
        self.c.click_element_by_css(register_login_css)
        sleep(1)

        # 获取登录信息的css元素以及登录账号信息
        mobile_login_css = read_css_path(76)
        pw_login_css = read_css_path(77)
        pw_visible_login_css = read_css_path(78)
        submit_login_css = read_css_path(79)
        print(pw_visible_login_css)
        print(submit_login_css)
        self.login_mobile, self.login_pw = read_login_data(row_num_real)

        # 输入登录信息并提交
        self.c.input_element_by_css(mobile_login_css,self.login_mobile)
        sleep(1)
        self.c.input_element_by_css(pw_login_css, self.login_pw)
        sleep(1)
        # self.c.driver.find_element_by_css_selector(pw_visible_login_css).click()
        self.c.click_element_by_css(pw_visible_login_css)
        sleep(1)
        self.c.click_element_by_css(submit_login_css)
        sleep(3)

        # 点击---【出借】
        buy_css = read_css_path(62)
        self.c.wait_element_click_by_css(buy_css)
        sleep(1)

    def test_1_buy(self):
        win_c_type_css = read_css_path(66)
        self.c.click_element_by_css(win_c_type_css)
        sleep(1)

        # win_c_borrow_name_css = read_css_path(67)
        # print(win_c_borrow_name_css)
        # self.c.click_element_by_css(win_c_borrow_name_css)
        # sleep(1)

        css = "p.planBidTitle>span.planBidTitleTips1>img"
        xpath = '//*[@id="section-3"]/div[1]/p/span[1]'
        self.c.driver.find_element_by_xpath(xpath).click()
        sleep(1)

        # 点击---【立即加入】
        buy_right_now_css = read_css_path(68)
        self.c.click_element_by_css(buy_right_now_css)
        sleep(2)

        # 购买过程
        buy_amount_buy_css = read_css_path(69)
        self.c.input_element_by_css(buy_amount_buy_css, '500')
        sleep(2)

        agree_on_buy_css = read_css_path(70)
        self.c.click_element_by_css(agree_on_buy_css)
        sleep(1)

        buy_assure_buy=read_css_path(71)
        self.c.click_element_by_css(buy_assure_buy)
        sleep(2)

        # 捕获结果页面
        result_buy_buy_css = read_css_path(72)
        result = self.c.driver.find_element_by_css_selector(result_buy_buy_css).text
        print('购买结果为：', result)
        return result

    def test_2_buy(self):
        # 点击继续出借
        buy_continue_buy_css = read_css_path(73)
        self.c.click_element_by_css(buy_continue_buy_css)
        sleep(2)


if __name__ == "__main__":
    l = Login()
    i = 1
    for i in range(50):
        if i<50:
            result = l.test_1_buy()
            write_excel_common(i, result)
            sleep(1)
            l.test_2_buy()
            sleep(1)
            i+=1






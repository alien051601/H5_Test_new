from read_excel import *
from utilities.settings import *
from utilities.common_method import *


class Register(CommonMethod):

    def __init__(self):
        super(Register).__init__()
        self.c = CommonMethod()

        # 如下的属性，方便其他类调用的时候使用
        self.driver = self.c.driver

        # 点击首页的---【我的】----【注册/登录】--【注册领818红包】
        my_account_css = read_css_path(63)
        print(my_account_css)
        self.c.click_element_by_css(my_account_css)
        sleep(1)
        register_login_css = read_css_path(64)
        self.c.click_element_by_css(register_login_css)
        sleep(1)
        register_login_css = read_css_path(133)
        self.c.click_element_by_css(register_login_css)
        sleep(1)

    def test_1_registr(self):
        # 进入到注册页面
        page_title_register_css = read_css_path(136)
        page_title_register = self.c.wait_element_get_text_by_css(page_title_register_css)
        print('进入到页面：', page_title_register)
        sleep(1)

        # 获取注册需要的数据
        mobile,password,invitcode = read_register_data(row_num_real)

        # 输入手机号，点击下一步
        input_mobile_register_css = read_css_path(134)
        self.c.wait_element_input_by_css(input_mobile_register_css,mobile)
        sleep(1)
        next_step_register_css = read_css_path(135)
        self.c.click_element_by_css(next_step_register_css)
        sleep(1)

        # 输入注册的信息
        input_img_code_register_css = read_css_path(137)
        self.c.wait_element_input_by_css(input_img_code_register_css, 'abcd')
        sleep(1)
        get_sms_code_register_css = read_css_path(140)
        self.c.click_element_by_css(get_sms_code_register_css)
        sleep(1)
        input_sms_code_register_css = read_css_path(139)
        self.c.input_element_by_css(input_sms_code_register_css, '123456')
        sleep(1)
        input_login_pw_register_css = read_css_path(141)
        self.c.input_element_by_css(input_login_pw_register_css, password)
        sleep(1)
        pw_visible_register_css = read_css_path(142)
        self.c.click_element_by_css(pw_visible_register_css)
        sleep(1)
        submit_register_css = read_css_path(143)
        self.c.click_element_by_css(submit_register_css)
        sleep(1)

        # 进入到注册结果页
        title_register_result_css = read_css_path(144)
        title_register_result = self.c.wait_element_get_text_by_css(title_register_result_css)
        print('注册结果为：', title_register_result)
        sleep(1)

        # 进入到开户页面再返回
        open_account_register_result_css = read_css_path(145)
        self.c.click_element_by_css(open_account_register_result_css)
        sleep(2)
        self.c.driver.back()
        sleep(1)

        # 点击【跳过，下次再说】
        skip_register_result_css = read_css_path(146)
        self.c.click_element_by_css(skip_register_result_css)
        sleep(2)

if __name__ =="__main__":
    r = Register()
    r.test_1_registr()

# env config
from selenium import webdriver
ENV = 'test'

APP_VERSION = 'V1.0'

HEADERS = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}


# PC端 ======================================================
# UAT环境
API_TEST_BASE_URL = "https://hlwm-test.chinazyjr.net/"

# SIT环境
# API_TEST_BASE_URL = "http://hlwm-sit.chinazyjr.net/"

# Testgl环境
# API_TEST_BASE_URL = "http://api-testgl.chinazyjr.com/"

# Online环境
# API_TEST_BASE_URL = "https://hlwm.chinazyjr.com/"


# H5 ======================================================
# UAT环境
# API_TEST_BASE_URL = "https://hlwm-uat.chinazyjr.net/"

# Dev环境
# API_TEST_BASE_URL = "https://hlwm-dev.chinazyjr.net/"


# mysql--test config
DB_HOST = '192.168.xxx.xxx'
DB_PORT = '60220'
DB_USER = 'test'
DB_PASSWORD = 'password'

# driver = webdriver.Firefox(executable_path='D:\Program Files\Mozilla Firefox\geckodriver.exe')
# driver.get("http://hlw-test.chinazyjr.net/")
row_num_real = int(212)

# 代表【出借】页面的第几个标的，从上到下第几个标的（包含新手标）
num_borrow_serial = str(1)


new_mobile = '16812340018'

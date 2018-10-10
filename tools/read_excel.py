# -*- coding: utf-8 -*-
import xlrd
from settings import *

file_path = "D:\Mywork\合规工作流程20180614.xls"

# 定义row_num & col_num,这2个值是excel里面的实际行号以及列号
def read_excel(row_num, col_num):

    # 打开文件
    workbook = xlrd.open_workbook(file_path)
    # 打开“元素”sheet表格
    sheet1 = workbook.sheet_by_name('元素')
    api_url = sheet1.cell_value(row_num - 1, col_num - 1)
    return api_url

def read_css_path(row_num):
    # 打开文件
    workbook = xlrd.open_workbook(file_path)
    # 打开“元素”sheet表格
    sheet1 = workbook.sheet_by_name('元素')
    api_url = sheet1.cell_value(row_num - 1, 5)
    return api_url


def read_login_data(row_num):
    # 打开文件
    workbook = xlrd.open_workbook(file_path)

    sheet1 = workbook.sheet_by_name('登录账号')

    username = int(sheet1.cell_value(row_num - 1, 1))
    password = sheet1.cell_value(row_num - 1, 2)
    return username, password


def read_register_data(row_num):
    workbook = xlrd.open_workbook(file_path)
    sheet1 = workbook.sheet_by_name('登录账号')
    mobile = int(sheet1.cell_value(row_num - 1, 1))
    password = sheet1.cell_value(row_num - 1, 2)
    try:
        invitcode = int(sheet1.cell_value(row_num - 1, 12))
    except:
        invitcode = '17521523665'

    return mobile, password, invitcode


def read_open_account_data(row_num):
    workbook = xlrd.open_workbook(file_path)
    sheet1 = workbook.sheet_by_name('登录账号')

    real_name = sheet1.cell_value(row_num - 1, 8)
    bank_mobile = int(sheet1.cell_value(row_num - 1, 9))
    pc_id = str(sheet1.cell_value(row_num - 1, 10))
    bank_code = int(sheet1.cell_value(row_num - 1, 11))
    return real_name, bank_mobile, pc_id, bank_code


sms_button_css = read_css_path(19)
print(sms_button_css)

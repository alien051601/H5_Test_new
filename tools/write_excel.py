from xlrd import open_workbook
from xlutils.copy import copy
import xlwt

file_path = r"C:\Users\huqinlong\Desktop\buy_result.xls"

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 定义具体的字体

    font.bold = bold  # 定义是否加粗
    font.color_index = 4  # 定义字体颜色
    font.height = height  # 定义字体高度

    style.font = font  # 最终把自定义的字体，定义到风格里面
    return style

# 写excel
def write_excel():
    # 读取一个excel文件
    rd_excel = open_workbook(file_path)
    # 将xlrd的对象转化为xlwt的对象
    new_excel = copy(rd_excel)
    # 获得要操作的sheet
    table = new_excel.get_sheet(0)
    # 准备要输入的内容
    values = ['小明', '小李', 'Lily', 'Toms', '小王']

    # xlwt对象的写方法，参数分别是行、列、值
    table.write(1, 0, values[0], set_style('微软雅黑', 300, True))
    table.write(2, 0, values[1], set_style('Arial', 100, True))
    table.write(3, 0, values[2], set_style('微软雅黑', 400, False))
    table.write(4, 0, values[3], set_style('宋体', 200, True))
    table.write(5, 0, values[4], set_style('Arial', 300, False))

    # xlwt对象的保存方法，这时便覆盖掉了原来的excel
    new_excel.save(file_path)

def write_excel_common(raw, info):
    # 读取一个excel文件
    rd_excel = open_workbook(file_path)
    # 将xlrd的对象转化为xlwt的对象
    new_excel = copy(rd_excel)
    # 获得要操作的sheet
    table = new_excel.get_sheet(0)
    # 准备要输入的内容

    # xlwt对象的写方法，参数分别是行、列、值
    table.write(raw, 0, info)

    # xlwt对象的保存方法，这时便覆盖掉了原来的excel
    new_excel.save(file_path)

# if __name__ == '__main__':
#     write_excel_common(1,'你好')
#     write_excel_common(2,'wohao')

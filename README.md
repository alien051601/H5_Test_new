## （1）项目介绍：
HLY——上海银行存管平台H5_UI自动化测试代码(haoliwang)

里面部分代码没来得及修改，仅供参考学习使用


## （2）结构介绍：
- MainCase文件夹下面是测试用例，根据功能划分的每个模块
- tools文件夹下面，是一些常用的基础类，例如base.py 负责浏览器的打开、设置等操作，common_method.py文件，这个是常用的一些点击、等待之后点击、捕获按钮等操作的基础方法，所有页面元素的具体执行方法均来源这些方法。settings.py文件是基础类参数，read_excel.py & write_excel.py 2个是有关excel的读取和写入的
- 所有的元素的均采用css方法捕获，read_excel 里面的read_css_path（）方法，此方法输入的参数是excel行号，excel里面存放每个元素CSS的信息。


## （3）个人博客
https://blog.csdn.net/chenmozhe22

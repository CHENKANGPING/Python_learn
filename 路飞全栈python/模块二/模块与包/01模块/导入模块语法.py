"""
模块与包的命名遵循小写加下划线
导入的模块名和函数一样是一等公民
使用 ”import module" 导入模块的本质就是将module.py中
全部代码加载到内存并执行，然后将整个模块内容的值给与模块同名的变量
导入同一个模块多次，python只执行一次

导入语法
import module as 别名
from module import 变量
from module import *
"""
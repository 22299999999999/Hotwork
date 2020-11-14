import sys

# import time

print(sys.path)

print("hello python")

# def sum(a,b)
#     return sum=a+b
#     print("a+b="sum)
#
#     c=sum(2，3)
# import yaml
# import requests

""""
hahah 
"""

for i in range(101):
    print(i)


# 函数的定义
def func1(a):
    """
    在函数名字和函数体中间，输入3个双引号后回车，会自动生成函数说明
    :param a:
    :return:
    """
    print("a=", a)


# 函数的调用
# ctrl+d复制一行代码
func1(3)

# 位置参数(a,b,c)
# 默认参数  定义函数时的 k=v的形式的参数
# 关键字参数， 调用函数时 k=v的形式的参数
# 函数的定义和调用时，关键字参数必需在位置参数的后面
# dir() 展示当前模块可被调用的对象  包括：变量、方法和类

print("dir()")
print(dir())

print("dir(sys)")
print(dir(sys))

func3 = lambda x: x * 2
print(func3(2))

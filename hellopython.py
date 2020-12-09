import sys

# import time
import random

print(sys.path)

print("hello python")

# 字符串切片
str_a = "2345678"
# 从第2位取到第三位
print(str_a[1:3])

# 分支语句、多重分支、分支嵌套
a = 3
if a == 0:
    print("a=0")
elif a == 1:
    print("a=1")
else:
    print("a!0 1")

# 嵌套分支
x = 0
if x >= -1:
    if x <= 1:
        y = x + 2
    else:
        y = 3 * x - 5
else:
    y = 5 * x + 3
print(y)

# 多重分支,建议选择多重分支，嵌套分支影响代码的可读性
x = 0
if x > 1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
else:
    y = 5 * x + 3
print(y)

# 循环结构
# for-in循环
# eg；1-100的求和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 分支结构实现1-100的偶数求和
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)
for i in range(2, 10, 2):
    print(i)

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

for i in range(3):
    print(i)
a = 0
while a < 3:
    print("a=", a)
    a = a + 1


# # 猜数游戏
# suiji=random.randint(1,100)
# print(suiji)
# while True:
#     people = int(input("请输入一个数字："))
#     if people>suiji:
#         print("太大了")
#     elif people<suiji:
#         print("太小了")
#
#     else:
#         print("猜对啦")
#         break
#

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


# 定义函数是，k=v的方式， 此处a是默认参数。在调用函数时，若a没有传参就会使用默认值
def abc(b, c, a=0):
    """
    输入3个双引号点回车，
    :param a:
    :param b:
    :param c:
    :return:
    ctrl+d 快捷键，可复制一行
    """

    print("函数说明文档", a)
    print("函数说明文档", b)
    print("函数说明文档", c)


abc(1, 2, 3)
# 位置参数、默认参数、关键字参数

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

list_hog = [1, 2, 3, 4]
list_hog.append(0)
print(list_hog)

# 逻辑错误
num = 1
if num >= 1:
    print("num<1")


# 除数为0
def div(a, b):
    return a / b


print(div(1, 0))

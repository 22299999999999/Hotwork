import math
import os
import time
import urllib.request
from urllib import response

import allure
import requests


class Person:
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    def __init__(self, name, age, gender, weight):
        print("这是一个构造方法")
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # 添加装饰器，使类方法也可被调用
    @classmethod
    def eat(self):
        print("eating")

    def jump(self):
        print("jumpping")


# 实例化类
zs = Person("zhangsan", "30", "female", "150")

# 类变量、实例变量
print(Person.name)
print(zs.name)
print(f"zs的名字为：", {zs.name})
print("zs的名字为：", zs.name)

# 类方法和实例方法
Person.eat()
zs.eat()

# 创建一个目录
# os.mkdir("testdir")
# 列出当前目录下的文件和文件夹
print(os.listdir("./"))
# 删除文件夹
# os.remove("testdir")
# 获取当前路径的地址
print(os.getcwd())
# 验证当前文件夹是否存在 testdir文件夹   true是存在，false是不存在
print(os.path.exists("testdir"))

print(time.time())
print(time.localtime())
print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))

response: object = urllib.request.urlopen("https://www.baidu.com")
print(response.status)
print(response.read())
print(response.headers)

print(math.ceil(5.5))
print(math.floor(5.6))
print(math.sqrt(81))

r = requests.get("https://www.baidu.com")
print(r.text)
print(r.status_code)

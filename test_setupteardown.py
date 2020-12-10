import pytest


def setup_module():
    print("模块执行前调用")


def teardown_module():
    print("模块执行后调用")


# 类外的方法用 setup/teardown  或setup_function/teardown_function
# def setup():
#     print("类外的方法执行前调用")
# def teardown():
#     print("类外的方法执行后调用")
def setup_function():
    print("类外的方法执行前调用")


def teardown_function():
    print("类外的方法执行后调用")


def test_1():
    print("hahahha")


class TestClass:
    def setup_class(self):
        print("每个类执行前调用")

    def teardown_class(self):
        print("每个类执行后调用")

    def setup_method(self):
        print("每个类方法执行前调用")

    def teardown_method(self):
        print("每个类方法执行后调用")

    # 类内的方法用 setup_method/teardown_method
    def test_one(self):
        print("test_one")

    def test_two(self):
        print("test_two")

    def test_three(self):
        print("test_three")

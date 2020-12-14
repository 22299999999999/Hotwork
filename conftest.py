import pytest
from pythoncode.calculator import Calculator


# @pytest.fixture()
# def login():
# 	print("登录")

# @pytest.fixture(params=["233","556"])
# def login(request):
#     # print("执行testPytest里的前置函数，%s" % request.param)
# 	print("登录:,%s" % request.param)


@pytest.fixture()
def shilihua():
    cal = Calculator()
    return cal
    print("实例化类")

import pytest
from pythoncode.calculator import Calculator
from selenium import webdriver


# @pytest.fixture()
# def login():
# 	print("登录")

# @pytest.fixture(params=["233","556"])
# def login(request):
#     # print("执行testPytest里的前置函数，%s" % request.param)
# 	print("登录:,%s" % request.param)


@pytest.fixture(scope="function", autouse="true")
def shilihua():
    cal = Calculator()
    return cal
    print("实例化类")


@pytest.fixture(autouse="false", scope="module")
def myfixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

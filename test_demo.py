import pytest


# 被测方法
def add(a, b):
    return a + b


# 参数化   ids是别名
# @pytest.mark.parametrize("a,b,expect",[(1,2,3),(2,3,5)],ids=["test1","test2"])
# def test_add(a,b,expect):
#     assert add(a,b) == expect

# 参数组合，  22得4，可得到4个测试用例
@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [1, 2])
def test_add(a, b):
    assert add(a, b) == a + b

# class Test_demo:
#
#     def test_one(self):
#         a = 5
#         b = 1
#         assert a != b
#         print("diyigeyongli")
#

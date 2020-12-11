import pytest


@pytest.fixture()
def login():
    print("登录")


class TestDemo:
    def test_a(self, login):
        print("a方法需要登录")

    def test_b(self):
        print("b方法不需要登录")

    def test_c(self, login):
        print("c方法需要登录")

import allure
import pytest

from pythoncode.calculator import Calculator


@allure.feature("测试类")
class TestCalc:
    def setup_method(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @allure.story("子功能")
    @pytest.mark.parametrize("a,b,expe", [(1, 2, 3), (3, 4, 5)], ids=["sum1", "sum2"])
    def test_add(self, a, b, expe):
        with allure.step("步骤"):
            print("执行加法的函数")
        assert expe == self.cal.sum(a, b)

    @pytest.mark.parametrize("a,b,expe", [(1, 2, -1), (6, 4, 2)], ids=["sum1", "sum2"])
    def test_jian(self, a, b, expe):
        assert expe == self.cal.jian(a, b)

    @pytest.mark.parametrize("a,b,expe", [(1, 2, 2), (3, 4, 5)], ids=["sum1", "sum2"])
    def test_cheng(self, a, b, expe):
        assert expe == self.cal.cheng(a, b)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("a,b,expe", [(4, 2, 2), (3, 4, 5)], ids=["sum1", "sum2"])
    def test_div(self, a, b, expe):
        assert expe == self.cal.div(a, b)

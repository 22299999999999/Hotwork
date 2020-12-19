import allure
import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("../data.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas

@allure.feature("测试类")
class TestCalc:
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expe", get_datas()["datas_add"], ids=get_datas()["ids_add"])
    def test_add(self, a, b, expe, shilihua):
        assert expe == shilihua.sum(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expe", get_datas()["datas_jian"], ids=get_datas()["ids_jian"])
    def test_jian(self, a, b, expe, shilihua):
        assert expe == shilihua.jian(a, b)

    @pytest.mark.parametrize("a,b,expe", get_datas()["datas_cheng"], ids=get_datas()["ids_cheng"])
    def test_cheng(self, a, b, expe, shilihua):
        assert expe == shilihua.cheng(a, b)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("a,b,expe", get_datas()["datas_div"], ids=get_datas()["ids_div"])
    def test_div(self, a, b, expe, shilihua):
        assert expe == shilihua.div(a, b)

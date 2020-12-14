import allure
import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("./data.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas_add"]
        add_ids = datas["ids_add"]
        jian_datas = datas["datas_jian"]
        jian_ids = datas["ids_jian"]
        cheng_datas = datas["datas_cheng"]
        cheng_ids = datas["ids_cheng"]
        div_datas = datas["datas_div"]
        div_ids = datas["ids_div"]
        return [add_datas, add_ids, jian_datas, jian_ids, cheng_datas, cheng_ids, div_datas, div_ids]


@allure.feature("测试类")
class TestCalc:
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expe", get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expe, shilihua):
        assert expe == shilihua.sum(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expe", get_datas()[2], ids=get_datas()[3])
    def test_jian(self, a, b, expe, shilihua):
        assert expe == shilihua.jian(a, b)

    @pytest.mark.parametrize("a,b,expe", get_datas()[4], ids=get_datas()[5])
    def test_cheng(self, a, b, expe, shilihua):
        assert expe == shilihua.cheng(a, b)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("a,b,expe", get_datas()[6], ids=get_datas()[7])
    def test_div(self, a, b, expe, shilihua):
        assert expe == shilihua.div(a, b)

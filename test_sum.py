import pytest
import yaml

from pythoncode.calculator import Calculator


class TestSum:
    # @pytest.fixture()
    # def shilihua(self):
    #     self.cal = Calculator()

    # def test_sum(self,a,b,expe):
    #     assert expe == self.cal.sum(a, b)
    @pytest.mark.parametrize("a,b,expe", yaml.safe_load(open("./data.yaml"))["datas_add"],
                             ids=yaml.safe_load(open("./data.yaml"))["ids_add"])
    def test_add(self, a, b, expe, shilihua):
        ele = shilihua
        assert expe == ele.sum(a, b)

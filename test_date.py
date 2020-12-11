import pytest
import yaml


# 参数化
# @pytest.mark.parametrize("a,b",[(2,3),(4,5),(4,6)])
# def test_a(a,b):
#     print(a+b)

# yaml
@pytest.mark.parametrize("a,b", yaml.safe_load(open("./data.yaml")))
def test_b(a, b):
    print(a + b)


def test_c():
    a = 5
    print("a的值是：", a)
    print(f"a的值是：", {a})

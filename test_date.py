import pytest
import yaml


# 参数化
# @pytest.mark.parametrize("a,b",[(2,3),(4,5),(4,6)])
# def test_a(a,b):
#     print(a+b)

# yaml
@pytest.mark.parametrize("a,b", yaml.safe_load(open("./data1.yaml"))["datas"],
                         ids=yaml.safe_load(open("./data1.yaml"))["myid"])
def test_b(a, b):
    print(a + b)


def test_c():
    a = 5
    print("a的值是：", a)
    print(f"a的值是：", {a})


def test_get_datas():
    with open("./data1.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas, add_ids]

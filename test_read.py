import pytest
import yaml


def test_read():
    with (open("./data.yaml"))as f:
        datas = yaml.load(f)
        print(datas["datas_add"])
        print(datas["datas_add"])
        print(type(datas))
        return datas


def test_a():
    print(test_read()["datas_add"])


@pytest.mark.parametrize("a,b,expe", test_read()["datas_add"], ids=test_read()["ids_add"])
def test_add(a, b, expe, shilihua):
    assert expe == shilihua.sum(a, b)
    # add_datas = datas["datas"]
    # add_ids = datas["myid"]
    # return [add_datas, add_ids]

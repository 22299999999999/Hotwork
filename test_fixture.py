import pytest
import pythoncode.calculator


@pytest.mark.flaky(reruns=6, reruns_delay=1)
def test_a():
    print("需要登录")
    assert 2 == 2


@pytest.mark.run(order=1)
def test_b():
    print("不需要登录")
    pytest.assume(2 == 2)
    pytest.assume(2 == 2)

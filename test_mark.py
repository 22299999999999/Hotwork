import pytest


@pytest.mark.demo
def test_one():
    print("第一个用例")


@pytest.mark.smoke
@pytest.mark.demo
def test_two():
    print("第二个用例")


# 执行 pytest -vs -m "smoke and demo" test_mark.py  ,test_two()被执行
# 执行 pytest -vs -m "smoke or demo" test_mark.py  ,test_one test_two()都会被执行
'''
消除warning的方法： 项目下创建1个pytest_ini 文件 ，内容如下
[pytest]
markers = demo
          smoke
          
          
再次运行，即可没有warning
'''

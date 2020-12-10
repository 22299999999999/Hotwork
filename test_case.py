import allure

TEST_CASE_LINK = 'http://10.172.190.157/testlink/index.php?caller=login'


@allure.testcase(TEST_CASE_LINK, '测试标题')
def test_with_testcase_link():
    pass

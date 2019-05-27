import allure, pytest

class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤01")
    def test_001_1(self):
        print("--->test_001_1")
        allure.attach("标题", "具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试步骤02")
    def test_001_2(self):
        allure.attach("用户名", "张三")
        allure.attach("密码", "123456")
        print("--->test_001_2")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是一个测试步骤03")
    def test_001_3(self):
        print("--->test_001_3")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是一个测试步骤04")
    def test_001_4(self):
        print("--->test_001_4")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是一个测试步骤05")
    def test_001_5(self):
        print("--->test_001_5")
        assert True


class Test_002:

    def test_add_png(self):
        """添加一张abc.png截图到测试报告"""

        with open("/Users/mac/Documents/Worker/sh-app8-day08/scripts/abc.png", "rb") as f:
            # 添加图片内容到测试报告，以附件的方式
            allure.attach("截图", f.read(), allure.attach_type.PNG)

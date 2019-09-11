import

from v4.page.page_login import PageLogin


class TestLogin:
    # 初始化
    def setup_class(self):
        self.login =PageLogin()

    # 结束
    def teardown_class(self):
        self.login


    # 登录测试方法
    def test_login(self):
        pass

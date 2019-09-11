from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化启动
    def __init__(self):
        # 准备启动参数
        caps = {}
        # 必填-且正确
        caps['platformName'] = 'Android'
        # 必填-且正确
        caps['platformVersion'] = '5.1'
        # 必填
        caps['deviceName'] = '192.168.56.101:5555'
        # APP包名 /
        caps['appPackage'] = 'com.vcooline.aike'
        # 启动名
        caps['appActivity'] = '.umanager.LoginActivity'
        # 获取driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # 查找元素->输入点击
    def base_find(self,loc,timeout=30,poll_frequency=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency)\
            .until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_input(self):
        el = self.base_find
        el.clear()
        el.send_keys()
    # 点击方法
    def base_click(self):
        self.base_find().click()

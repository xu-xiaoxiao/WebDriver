import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.network_page import NetWorkPage
from base.base_action import BaseAction


class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.networkPage = NetWorkPage(self.driver)
        self.baseAction = BaseAction(self.driver)

    def test_network_2G(self):
        # 点击更多
        self.networkPage.click_more()
        # 点击移动网络
        self.networkPage.click_network()
        # 点击首选网络类型
        self.networkPage.click_first_type()
        # 点击2G
        self.networkPage.click_2G()

    def test_network_3G(self):
        self.networkPage.click_more()
        self.networkPage.click_network()
        self.networkPage.click_first_type()
        self.networkPage.click_3G()

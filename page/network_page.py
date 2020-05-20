from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NetWorkPage(BaseAction):
    more_button = By.XPATH, "//*[contains(@text, '更多')]"

    network_button = By.XPATH, "//*[contains(@text, '移动网络')]"

    first_type_button = By.XPATH, "//*[contains(@text, '首选网络类型')]"

    G2_button = By.XPATH, "//*[contains(@text, '2G')]"

    G3_button = By.XPATH, "//*[contains(@text, '3G')]"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # self.driver = driver
        # 点击显示（init里面可以去写已经确定的这个模块所有的前置功能）

    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '更多')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text, '更多')]").click()
        # self.find_element(self.more_button).click()
        self.click(self.more_button)

    def click_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '移动网络')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text, '移动网络')]").click()
        # self.find_element(self.network_button).click()
        self.click(self.network_button)

    def click_first_type(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '首选网络类型')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text, '首选网络类型')]").click()
        # self.find_element(self.first_type_button).click()
        self.click(self.first_type_button)

    def click_2G(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '2G')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text, '2G')]").click()
        # self.find_element(self.G2_button).click()
        self.click(self.G2_button)

    def click_3G(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '3G')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text, '3G')]")
        # self.find_element(self.G3_button).click()
        self.click(self.G3_button)

    def find_element(self, loc):
        return self.find_element(loc[0], loc[1])

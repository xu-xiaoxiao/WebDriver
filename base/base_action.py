from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))

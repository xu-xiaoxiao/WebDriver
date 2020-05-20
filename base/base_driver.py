from appium.webdriver import webdriver


def init_driver():
    # server启动参数
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app参数信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.settings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明driver对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# Android environment
from appium import webdriver


class IosDriver:
    def __init__(self):
        appium_url = 'http://localhost:4723/wd/hub'

        desired_caps = dict(
            platformName='iOS',
            deviceName='iPhone SE (1st generation)',
            platformVersion='12.4',
            app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/app/<APP-FULL-NAME>'
        )

        self.instance = webdriver.Remote(appium_url, desired_caps)

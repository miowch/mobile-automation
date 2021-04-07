# Android environment
from appium import webdriver


class AndroidDriver:
    def __init__(self):
        appium_url = 'http://localhost:4723/wd/hub'

        desired_caps = dict(
            platformName='Android',
            deviceName='AndroidTestDevice',
            platformVersion='10',
            appPackage='org.wikipedia',
            appActivity='.main.MainActivity',
            # app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/apks/org.wikipedia.apk'
        )

        self.instance = webdriver.Remote(appium_url, desired_caps)

import os
from typing import Final
from appium import webdriver


class Driver:
    platform_android: Final = "android"
    platform_ios: Final = "ios"

    def __init__(self):
        appium_url = 'http://localhost:4723/wd/hub'
        desired_caps = self.get_capabilities_by_platform_env()
        self.instance = webdriver.Remote(appium_url, desired_caps)

    def get_capabilities_by_platform_env(self):
        platform = os.environ['PLATFORM']

        if platform == self.platform_android:
            desired_caps = dict(
                platformName='Android',
                deviceName='AndroidTestDevice',
                platformVersion='10',
                appPackage='org.wikipedia',
                appActivity='.main.MainActivity',
                # app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/apks/org.wikipedia.apk'
            )
        elif platform == self.platform_ios:
            desired_caps = dict(
                platformName='iOS',
                deviceName='iPhone SE (1st generation)',
                platformVersion='12.4',
                # app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/app/<APP-FULL-NAME>'
            )
        else:
            raise OSError('Cannot get run platform from env variable. Platform value ' + platform)

        return desired_caps

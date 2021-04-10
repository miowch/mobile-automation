import os
from typing import Final
from appium import webdriver


class Platform:
    platform_android: Final = "android"
    platform_ios: Final = "ios"
    appium_url: Final = 'http://localhost:4723/wd/hub'

    def get_driver(self):
        if self.is_android():
            return webdriver.Remote(self.appium_url, self.__get_android_desired_capabilities())
        elif self.is_ios():
            return webdriver.Remote(self.appium_url, self.__get_ios_desired_capabilities())
        else:
            raise OSError("Cannot detect Driver type. Platform value: " + self.__get_platform_var())

    def is_android(self):
        return self.__is_platform(self.platform_android)

    def is_ios(self):
        return self.__is_platform(self.platform_ios)

    def __get_platform_var(self):
        return os.environ['PLATFORM']

    def __is_platform(self, my_platform):
        platform = self.__get_platform_var()
        return my_platform == platform

    def __get_android_desired_capabilities(self):
        desired_caps = dict(
                        platformName='Android',
                        deviceName='AndroidTestDevice',
                        platformVersion='10',
                        appPackage='org.wikipedia',
                        appActivity='.main.MainActivity',
                        # app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/apks/org.wikipedia.apk'
        )

        return desired_caps

    def __get_ios_desired_capabilities(self):
        desired_caps = dict(
            platformName='iOS',
            deviceName='iPhone SE (1st generation)',
            platformVersion='12.4',
            # app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/app/<APP-FULL-NAME>'
        )

        return desired_caps

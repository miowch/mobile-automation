import os
from typing import Final

from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver


class Platform:
    __instance = None

    platform_android: Final = "android"
    platform_ios: Final = "ios"
    platform_mobile_web: Final = "mobile_web"
    appium_url: Final = 'http://localhost:4723/wd/hub'
    wikipedia_url = 'https://en.m.wikipedia.org'

    def __init__(self):
        if Platform.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Platform.__instance = self

    def get_driver(self):
        if self.is_android():
            return appium_webdriver.Remote(self.appium_url, self.__get_android_desired_capabilities())
        elif self.is_ios():
            return appium_webdriver.Remote(self.appium_url, self.__get_ios_desired_capabilities())
        elif self.is_mw():
            return selenium_webdriver.Chrome(
                executable_path="../chromedriver",
                options=self.__get_mw_chrome_options())
        else:
            raise OSError("Cannot detect Driver type. Platform value: " + self.get_platform_var())

    def is_android(self):
        return self.__is_platform(self.platform_android)

    def is_ios(self):
        return self.__is_platform(self.platform_ios)

    def is_mw(self):
        return self.__is_platform(self.platform_mobile_web)

    def __is_platform(self, my_platform):
        platform = self.get_platform_var()
        return my_platform == platform

    @staticmethod
    def get_instance():
        if Platform.__instance is None:
            Platform()
        return Platform.__instance

    @staticmethod
    def get_platform_var():
        return os.environ['PLATFORM']

    @staticmethod
    def __get_android_desired_capabilities():
        desired_caps = dict(
            platformName='Android',
            deviceName='AndroidTestDevice',
            platformVersion='10',
            appPackage='org.wikipedia',
            appActivity='.main.MainActivity',
            app='/Users/miowch/Documents/Private/GitHub/mobile-automation/PythonAppiumAutomation/apks/org.wikipedia.apk'
        )

        return desired_caps

    @staticmethod
    def __get_ios_desired_capabilities():
        desired_caps = dict(
            platformName='iOS',
            deviceName='iPhone SE (1st generation)',
            platformVersion='12.4',
            # app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/app/<APP-FULL-NAME>'
        )

        return desired_caps

    @staticmethod
    def __get_mw_chrome_options():
        mobile_emulation = {
            "deviceMetrics": {
                "width": 360,
                "height": 640,
                "pixelRatio": 3.0
            },
            "userAgent": 'Mozilla/5.0 (Linux; Android 10; SM-G970F) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3396.81 Mobile Safari/537.36',
        }

        chrome_options = selenium_webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # chrome_options.add_argument('headless')
        # chrome_options.add_argument("disable_gpu")

        return chrome_options

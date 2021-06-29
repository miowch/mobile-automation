import os
import traceback
import unittest

import allure
from jproperties import Properties

from utils.platform import Platform
from utils.ui.welcome_page_object import WelcomePageObject


class CoreTestCase(unittest.TestCase):
    @allure.step("Run driver and session")
    def setUp(self):
        self.driver = Platform.get_instance().get_driver()
        self.create_allure_property_file()
        self.rotate_screen_portrait()
        self.skip_welcome_screen_for_ios_app()
        self.open_wiki_web_page_for_mobile_web()

    @allure.step("Remove driver and session")
    def tearDown(self):
        self.driver.quit()

    @allure.step("Rotate screen to portrait mode")
    def rotate_screen_portrait(self):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.driver.orientation = "PORTRAIT"
        else:
            print("Method rotate_scree_portrait does nothing for platform " + Platform.get_instance().__str__())

    @allure.step("Rotate screen to landscape mode")
    def rotate_screen_landscape(self):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.driver.orientation = "LANDSCAPE"
        else:
            print("Method rotate_scree_landscape does nothing for platform " + Platform.get_platform_var())

    @allure.step("Put the app to the background")
    def background_app(self, seconds):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.driver.background_app(seconds)
        else:
            print("Method background_app does nothing for platform " + Platform.get_platform_var())

    @allure.step("Skip the Welcome screen")
    def skip_welcome_screen_for_ios_app(self):
        if Platform.get_instance().is_ios():
            welcome_page = WelcomePageObject(self.driver)
            welcome_page.click_skip()

    @allure.step("Open Wiki web page")
    def open_wiki_web_page_for_mobile_web(self):
        if Platform.get_instance().is_mw():
            self.driver.get('https://en.m.wikipedia.org/')
        else:
            print("Method open_wiki_web_page_for_mobile_web does nothing for platform " + Platform.get_platform_var())

    @staticmethod
    def create_allure_property_file():
        path = os.environ['allureRD']
        try:
            props = Properties()
            props["Environment"] = Platform.get_instance().get_platform_var()
            with open(path + "/environment.properties", "wb") as property_file:
                props.store(property_file, encoding="utf-8")
                property_file.close()
        except IOError:
            print("IO problem when writing Allure properties file")
            traceback.print_exc()

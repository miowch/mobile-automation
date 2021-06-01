import unittest

from utils.platform import Platform
from utils.ui.welcome_page_object import WelcomePageObject


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Platform.get_instance().get_driver()
        self.rotate_screen_portrait()
        self.skip_welcome_screen_for_ios_app()
        self.open_wiki_web_page_for_mobile_web()

    def tearDown(self):
        self.driver.quit()

    def rotate_screen_portrait(self):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.driver.orientation = "PORTRAIT"
        else:
            print("Method rotate_scree_portrait does nothing for platform " + Platform.get_instance().__str__())

    def rotate_screen_landscape(self):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.driver.orientation = "LANDSCAPE"
        else:
            print("Method rotate_scree_landscape does nothing for platform " + Platform.get_platform_var())

    def background_app(self, seconds):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.driver.background_app(seconds)
        else:
            print("Method background_app does nothing for platform " + Platform.get_platform_var())

    def skip_welcome_screen_for_ios_app(self):
        if Platform.get_instance().is_ios():
            welcome_page = WelcomePageObject(self.driver)
            welcome_page.click_skip()

    def open_wiki_web_page_for_mobile_web(self):
        if Platform.get_instance().is_mw():
            self.driver.get('https://en.m.wikipedia.org/')
        else:
            print("Method open_wiki_web_page_for_mobile_web does nothing for platform " + Platform.get_platform_var())

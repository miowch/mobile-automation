import unittest
from utils.platform import Platform
from utils.ui.welcome_page_object import WelcomePageObject


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Platform.get_instance().get_driver()
        self.rotate_screen_portrait()
        self.skip_welcome_screen_for_ios_app()

    def tearDown(self):
        self.driver.quit()

    def rotate_screen_portrait(self):
        self.driver.orientation = "PORTRAIT"

    def rotate_screen_landscape(self):
        self.driver.orientation = "LANDSCAPE"

    def background_app(self, seconds):
        self.driver.background_app(seconds)

    def skip_welcome_screen_for_ios_app(self):
        if Platform.get_instance().is_ios():
            welcome_page = WelcomePageObject(self.driver)
            welcome_page.click_skip()

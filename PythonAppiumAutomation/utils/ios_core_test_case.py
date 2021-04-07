import unittest
from utils.ios_webdriver import IosDriver


class IosCoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = IosDriver().instance
        self.rotate_screen_portrait()  # Ex7*

    def tearDown(self):
        self.driver.quit()

    def rotate_screen_portrait(self):
        self.driver.orientation = "PORTRAIT"

    def rotate_screen_landscape(self):
        self.driver.orientation = "LANDSCAPE"

    def background_app(self, seconds):
        self.driver.background_app(seconds)

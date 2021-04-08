import unittest
from utils.webdriver import Driver


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().instance
        self.rotate_screen_portrait()

    def tearDown(self):
        self.driver.quit()

    def rotate_screen_portrait(self):
        self.driver.orientation = "PORTRAIT"

    def rotate_screen_landscape(self):
        self.driver.orientation = "LANDSCAPE"

    def background_app(self, seconds):
        self.driver.background_app(seconds)

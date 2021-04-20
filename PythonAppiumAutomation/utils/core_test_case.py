import unittest
from utils.platform import Platform


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Platform.get_instance().get_driver()
        self.rotate_screen_portrait()

    def tearDown(self):
        self.driver.quit()

    def rotate_screen_portrait(self):
        self.driver.orientation = "PORTRAIT"

    def rotate_screen_landscape(self):
        self.driver.orientation = "LANDSCAPE"

    def background_app(self, seconds):
        self.driver.background_app(seconds)

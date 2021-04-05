import unittest
from utils.webdriver import Driver


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().instance

    def tearDown(self):
        self.driver.orientation = "PORTRAIT"
        self.driver.quit()

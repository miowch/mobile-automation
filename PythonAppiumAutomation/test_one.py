import unittest
from webdriver import Driver


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().instance

    def test_one(self):
        print("First test run")

    def tearDown(self):
        self.driver.quit()

import unittest

import pytest

from utils.platform import Platform
from utils.ui.welcome_page_object import WelcomePageObject


@pytest.mark.testsuite
class TestGetStarted(unittest.TestCase):
    def setUp(self):
        self.driver = Platform.get_instance().get_driver()
        self.rotate_screen_portrait()

    def rotate_screen_portrait(self):
        self.driver.orientation = "PORTRAIT"

    def tearDown(self):
        self.driver.quit()

    def test_pass_through_welcome(self):
        if Platform.get_instance().is_android():
            return

        welcome_page = WelcomePageObject(self.driver)
        welcome_page.wait_for_learn_more_link()

        welcome_page.wait_for_learn_more_link()

        welcome_page.click_next_button()

        welcome_page.wait_for_new_way_to_explore_text()
        welcome_page.click_next_button()

        welcome_page.wait_for_add_or_edit_preferred_lang_link()
        welcome_page.click_next_button()

        welcome_page.wait_for_learn_more_about_data_collected_link()
        welcome_page.click_get_started_button()

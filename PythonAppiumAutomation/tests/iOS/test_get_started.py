from utils.core_test_case import CoreTestCase
from utils.ui.welcome_page_object import WelcomePageObject


class TestGetStarted(CoreTestCase):
    def test_pass_through_welcome(self):
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

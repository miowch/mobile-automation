from typing import Final

from appium.webdriver.common.mobileby import MobileBy
from utils.ui.main_page_object import MainPageObject


class WelcomePageObject(MainPageObject):
    step_learn_more_link: Final = "Learn more about Wikipedia"
    step_new_ways_to_explore_text: Final = "New ways to explore"
    step_add_or_edit_preferred_languages: Final = "Add or edit preferred languages"
    step_learn_more_about_data_collected_link: Final = "Learn more about data collected"

    next_button: Final = "Next"
    get_started_button: Final = "Get started"

    def wait_for_learn_more_link(self):
        self.wait_for_element_present(
            by=(MobileBy.ID, self.step_learn_more_link),
            error_message="Cannot find 'Learn more about Wikipedia' link",
            timeout_in_sec=10
        )

    def wait_for_new_way_to_explore_text(self):
        self.wait_for_element_present(
            by=(MobileBy.ID, self.step_new_ways_to_explore_text),
            error_message="Cannot find 'New ways to explore' text",
            timeout_in_sec=10
        )

    def wait_for_add_or_edit_preferred_lang_link(self):
        self.wait_for_element_present(
            by=(MobileBy.ID, self.step_add_or_edit_preferred_languages),
            error_message="Cannot find 'Add or edit preferred languages' link",
            timeout_in_sec=10
        )

    def wait_for_learn_more_about_data_collected_link(self):
        self.wait_for_element_present(
            by=(MobileBy.ID, self.step_learn_more_about_data_collected_link),
            error_message="Cannot find 'Learn more about data collected' link",
            timeout_in_sec=10
        )

    def click_next_button(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, self.next_button),
            error_message="Cannot find and click 'Next' button",
            timeout_in_sec=10
        )

    def click_get_started_button(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, self.get_started_button),
            error_message="Cannot find and click 'Get started' button",
            timeout_in_sec=10
        )

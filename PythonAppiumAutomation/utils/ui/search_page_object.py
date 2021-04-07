from typing import Final
from appium.webdriver.common.mobileby import MobileBy
from utils.ui.main_page_object import MainPageObject


class SearchPageObject(MainPageObject):
    search_init_field: Final = "//*[@resource-id='org.wikipedia:id/search_container']" + \
                               "//*[contains(@class, 'android.widget.TextView')]"
    search_init_element: Final = "//*[contains(@text, 'Search Wikipedia')]"
    search_input: Final = "//*[contains(@text, 'Search…')]"
    search_result_element: Final = "//*[@resource-id='org.wikipedia:id/search_results_list']" + \
                                   "/*[@resource-id='org.wikipedia:id/page_list_item_container']"
    search_result_title: Final = "//*[@resource-id='org.wikipedia:id/page_list_item_title']"
    empty_result_label: Final = "//*[@text='No results found']"
    search_cancel_button: Final = "org.wikipedia:id/search_close_btn"
    search_empty_message_element: Final = "org.wikipedia:id/search_empty_message"

    search_result_by_substring_tpl: Final = "//*[@resource-id='org.wikipedia:id/page_list_item_container']" + \
                                            "//*[@text='SUBSTRING']"

    def assert_search_input_has_placeholder(self, placeholder):
        self.assert_element_has_text(
            by=(MobileBy.XPATH, self.search_init_field),
            expected_text=placeholder,
            error_message="Search field has another placeholder")

    def init_search_input(self):
        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, self.search_init_element),
            error_message="Cannot find and click search init element"
        )

        self.wait_for_element_present(
            by=(MobileBy.XPATH, self.search_init_element),
            error_message="Cannot find search input after clicking search init element"
        )

    def type_search_line(self, search_line):
        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, self.search_input),
            value=search_line,
            error_message="Cannot find and type into search input"
        )

    def wait_for_search_result(self, substring):
        search_result_xpath = self.get_result_search_element(substring)

        self.wait_for_element_present(
            by=(MobileBy.XPATH, search_result_xpath),
            error_message="Cannot find search result with substring " + substring,
            timeout_in_sec=15
        )

    def wait_for_search_results(self):
        return self.wait_for_elements_present(
            by=(MobileBy.XPATH, self.search_result_element),
            error_message="No search results")

    def wait_for_empty_result_label(self):
        self.wait_for_element_present(
            by=(MobileBy.XPATH, self.empty_result_label),
            error_message="Cannot find empty result label by the request",
            timeout_in_sec=15
        )

    def assert_no_search_results(self):
        self.assert_element_not_present(
            locator_strategy=MobileBy.XPATH,
            locator=self.search_result_element,
            error_message="We supposed not to find any results"
        )

    def click_by_article_with_substring(self, substring):
        search_result_xpath = self.get_result_search_element(substring)

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, search_result_xpath),
            error_message="Cannot find and click search result with substring " + substring,
            timeout_in_sec=10
        )

    def wait_for_cancel_button_to_appear(self):
        self.wait_for_element_present(
            by=(MobileBy.ID, self.search_cancel_button),
            error_message="Cannot find search cancel button"
        )

    def wait_for_cancel_button_to_disappear(self):
        self.wait_for_element_not_present(
            by=(MobileBy.ID, self.search_cancel_button),
            error_message="'Close' button is still present on the page"
        )

    def click_cancel_search(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, self.search_cancel_button),
            error_message="Cannot find 'close' button to cancel search"
        )

    def get_amount_of_found_articles(self):
        self.wait_for_element_present(
            by=(MobileBy.XPATH, self.search_result_element),
            error_message="Cannot find anything by the request ",
            timeout_in_sec=15
        )

        return self.get_amount_of_elements(
            locator_strategy=MobileBy.XPATH,
            locator=self.search_result_element)

    def assert_search_empty_message(self, message):
        self.assert_element_has_text(
            by=(MobileBy.ID, self.search_empty_message_element),
            expected_text=message,
            error_message="Search empty message differs from expected one")

    def assert_search_results_contain_required_word(self, word):
        self.assert_elements_contain_required_word(
            elements_xpath=self.search_result_element,
            element_xpath=self.search_result_title,
            word=word,
            error_message="Search result does not contain required word"
        )

    # TEMPLATES METHODS
    def get_result_search_element(self, substring):
        return self.search_result_by_substring_tpl.replace('SUBSTRING', substring)

    # TEMPLATES METHODS

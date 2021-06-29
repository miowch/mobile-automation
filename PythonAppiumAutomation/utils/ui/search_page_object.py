import allure

from utils.ui.main_page_object import MainPageObject


class SearchPageObject(MainPageObject):
    search_init_field: str
    search_init_element: str
    search_input: str
    search_result_element: str
    search_result_title: str
    empty_result_label: str
    search_cancel_button: str
    search_empty_message_element: str
    search_result_by_substring_tpl: str

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Assert the main page is open")
    def assert_main_page_is_open(self):
        self.assert_element_present(
            self.search_init_element,
            error_message="Cannot find search init element on the main page"
        )

    @allure.step("Assert search field has placeholder '{placeholder}'")
    def assert_search_input_has_placeholder(self, placeholder):
        self.assert_element_has_text(
            self.search_init_field,
            expected_text=placeholder,
            error_message="Search field has another placeholder")

    @allure.step("Init searching")
    def init_search_input(self):
        self.wait_for_element_and_click(
            self.search_init_element,
            error_message="Cannot find and click search init element"
        )

        self.wait_for_element_present(
            self.search_input,
            error_message="Cannot find search input after clicking search init element"
        )

    @allure.step("Type '{search_line}' to the search field")
    def type_search_line(self, search_line):
        self.wait_for_element_and_send_keys(
            self.search_input,
            value=search_line,
            error_message="Cannot find and type into search input"
        )

    @allure.step("Wait for search result with substring '{substring}'")
    def wait_for_search_result(self, substring):
        search_result_xpath = self.get_result_search_element(substring)

        self.wait_for_element_present(
            search_result_xpath,
            error_message="Cannot find search result with substring " + substring,
            timeout_in_sec=15
        )

    @allure.step("Wait for search results")
    def wait_for_search_results(self):
        return self.wait_for_elements_present(
            self.search_result_element,
            error_message="No search results",
            timeout_in_sec=15
        )

    @allure.step("Wait for empty result label")
    def wait_for_empty_result_label(self):
        self.wait_for_element_present(
            self.empty_result_label,
            error_message="Cannot find empty result label by the request",
            timeout_in_sec=15
        )

    @allure.step("Assert there is no search results")
    def assert_no_search_results(self):
        self.assert_element_not_present(
            self.search_result_element,
            error_message="We supposed not to find any results"
        )

    @allure.step("Click on Article with the following substring: '{substring}'")
    def click_by_article_with_substring(self, substring):
        search_result_xpath = self.get_result_search_element(substring)

        self.wait_for_element_and_click(
            search_result_xpath,
            error_message="Cannot find and click search result with substring " + substring,
            timeout_in_sec=10
        )

    @allure.step("Wait for 'Cancel' button to appear")
    def wait_for_cancel_button_to_appear(self):
        self.wait_for_element_present(
            self.search_cancel_button,
            error_message="Cannot find search cancel button"
        )

    @allure.step("Wait for 'Cancel' button to disappear")
    def wait_for_cancel_button_to_disappear(self):
        self.wait_for_element_not_present(
            self.search_cancel_button,
            error_message="'Close' button is still present on the page"
        )

    @allure.step("Click 'Cancel' button to cancel the search")
    def click_cancel_search(self):
        self.wait_for_element_and_click(
            self.search_cancel_button,
            error_message="Cannot find 'close' button to cancel search",
            timeout_in_sec=15
        )

    @allure.step("Get amount of found articles")
    def get_amount_of_found_articles(self):
        self.wait_for_element_present(
            self.search_result_element,
            error_message="Cannot find anything by the request ",
            timeout_in_sec=15
        )

        return self.get_amount_of_elements(self.search_result_element)

    @allure.step("Assert there is the following message for no results: '{message}'")
    def assert_search_empty_message(self, message):
        self.assert_element_has_text(
            self.search_empty_message_element,
            expected_text=message,
            error_message="Search empty message differs from expected one")

    @allure.step("Assert search results contain the word '{word}'")
    def assert_search_results_contain_required_word(self, word):
        self.assert_elements_contain_required_word(
            elements_xpath=self.search_result_element,
            element_xpath=self.search_result_title,
            word=word,
            error_message="Search result does not contain required word"
        )

    # TEMPLATES METHODS
    def get_result_search_element(self, substring):
        return self.search_result_by_substring_tpl.replace('{SUBSTRING}', substring)

    # TEMPLATES METHODS

from utils.core_test_case import CoreTestCase
from utils.ui.search_page_object import SearchPageObject


class TestSearch(CoreTestCase):
    def test_search_input_box_has_placeholder(self):
        search_page_object = SearchPageObject(self.driver)
        search_page_object.assert_search_input_has_placeholder("Search Wikipedia")

    def test_search(self):
        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.wait_for_search_result("General-purpose programming language")

    def test_cancel_search(self):
        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
        search_page_object.wait_for_cancel_button_to_appear()
        search_page_object.click_cancel_search()
        search_page_object.wait_for_cancel_button_to_disappear()

    def test_perform_and_cancel_search(self):
        search_page_object = SearchPageObject(self.driver)

        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.wait_for_search_results()
        search_page_object.click_cancel_search()
        search_page_object.assert_search_empty_message("Search and read the free encyclopedia in your language")

    def test_search_results_contain_required_word(self):
        word = "Python"

        search_page_object = SearchPageObject(self.driver)

        search_page_object.init_search_input()
        search_page_object.type_search_line(word)
        search_page_object.assert_search_results_contain_required_word(word)

    def test_amount_of_not_empty_search(self):
        search_line = "Linkin Park Discography"

        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(search_line)
        amount_of_search_results = search_page_object.get_amount_of_found_articles()

        self.assertTrue(
            amount_of_search_results,
            "We found too few results"
        )

    def test_amount_of_empty_search(self):
        search_line = "ghgkg"

        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(search_line)
        search_page_object.wait_for_empty_result_label()
        search_page_object.assert_no_search_results()

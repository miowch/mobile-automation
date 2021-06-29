import allure
import pytest

from utils.core_test_case import CoreTestCase
from utils.platform import Platform
from utils.ui.factories.search_page_object_factory import SearchPageObjectFactory


@pytest.mark.testsuite
class TestSearch(CoreTestCase):
    @allure.title("Search input has placeholder")
    def test_search_input_box_has_placeholder(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)

        if Platform.get_instance().is_mw():
            search_page_object.init_search_input()

        search_page_object.assert_search_input_has_placeholder("Search Wikipedia")

    @allure.title("Search for an article and check the results are valid")
    def test_search(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")

        if Platform.get_instance().is_mw():
            search_page_object.wait_for_search_result("eneral-purpose, high-level programming language")
        else:
            search_page_object.wait_for_search_result("eneral-purpose programming language")

    @allure.title("Cancel button appears in search field when it is selected")
    def test_cancel_search(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.wait_for_cancel_button_to_appear()
        search_page_object.click_cancel_search()
        search_page_object.wait_for_cancel_button_to_disappear()

    @allure.title("Cancel search when there are some results already")
    def test_perform_and_cancel_search(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)

        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.wait_for_search_results()
        search_page_object.click_cancel_search()

        if Platform.get_instance().is_mw():
            search_page_object.assert_main_page_is_open()
        else:
            search_page_object.assert_search_empty_message("Search and read the free encyclopedia in your language")

    @allure.title("Search results contains required word")
    def test_search_results_contain_required_word(self):
        word = "Python"

        search_page_object = SearchPageObjectFactory.get(self.driver)

        search_page_object.init_search_input()
        search_page_object.type_search_line(word)
        search_page_object.assert_search_results_contain_required_word(word)

    @allure.title("Start searching and get some results")
    def test_amount_of_not_empty_search(self):
        search_line = "Linkin Park Discography"

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(search_line)
        amount_of_search_results = search_page_object.get_amount_of_found_articles()

        self.assertTrue(
            amount_of_search_results,
            "We found too few results"
        )

    @allure.title("Start searching with no result")
    def test_amount_of_empty_search(self):
        search_line = "Qhgkg"

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(search_line)
        search_page_object.wait_for_empty_result_label()
        search_page_object.assert_no_search_results()

import allure
import pytest

from utils.core_test_case import CoreTestCase
from utils.platform import Platform
from utils.ui.factories.article_page_object_factory import ArticlePageObjectFactory
from utils.ui.factories.search_page_object_factory import SearchPageObjectFactory


@pytest.mark.testsuite
class TestArticle(CoreTestCase):
    @allure.title("Compare article title with expected one")
    @allure.description("Check opened article has expected title. ")
    @allure.step("Starting test_compare_article_title")
    def test_compare_article_title(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")

        if Platform.get_instance().is_mw():
            search_page_object.click_by_article_with_substring("eneral-purpose, high-level programming language")
        else:
            search_page_object.click_by_article_with_substring("eneral-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_title = article_page_object.get_article_title()

        self.assertEqual(
            first=article_title,
            second="Python (programming language)",
            msg="We see unexpected title")

    @allure.title("Swipe article to the footer")
    @allure.description("Check article can be swiped to the footer. ")
    @allure.step("Starting test_swipe_article")
    def test_swipe_article(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")

        if Platform.get_instance().is_mw():
            search_page_object.click_by_article_with_substring("eneral-purpose, high-level programming language")
        else:
            search_page_object.click_by_article_with_substring("eneral-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.wait_for_title_element()
        article_page_object.swipe_to_footer()

    @pytest.mark.skip("The test was created just for learning purposes to distinguish assert from wait")
    def test_article_has_title(self):
        word = "Python"

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(word)

        if Platform.get_instance().is_mw():
            search_page_object.click_by_article_with_substring("eneral-purpose, high-level programming language")
        else:
            search_page_object.click_by_article_with_substring("eneral-purpose programming language")

        # time.sleep(5)
        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.assert_article_has_title()

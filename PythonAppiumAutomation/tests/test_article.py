import time
from utils.core_test_case import CoreTestCase
from utils.ui.factories.article_page_object_factory import ArticlePageObjectFactory
from utils.ui.factories.search_page_object_factory import SearchPageObjectFactory


class TestArticle(CoreTestCase):
    def test_compare_article_title(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_title = article_page_object.get_article_title()

        self.assertEqual(
            first=article_title,
            second="Python (programming language)",
            msg="We see unexpected title")

    def test_swipe_article(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.wait_for_title_element()
        article_page_object.swipe_to_footer()

    def test_article_has_title(self):  # the test was created just for learning purposes to distinguish assert from wait
        word = "Python"

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(word)
        search_page_object.click_by_article_with_substring("General-purpose programming language")
        # time.sleep(5)
        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.assert_article_has_title()

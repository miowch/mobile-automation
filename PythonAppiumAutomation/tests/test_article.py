from utils.core_test_case import CoreTestCase
from utils.ui.article_page_object import ArticlePageObject
from utils.ui.search_page_object import SearchPageObject


class TestArticle(CoreTestCase):
    def test_compare_article_title(self):
        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObject(self.driver)
        article_title = article_page_object.get_article_title()

        self.assertEqual(
            first=article_title,
            second="Python (programming language)",
            msg="We see unexpected title")

    def test_swipe_article(self):
        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Appium")
        search_page_object.click_by_article_with_substring("Appium")

        article_page_object = ArticlePageObject(self.driver)
        article_page_object.wait_for_title_element()
        article_page_object.swipe_to_footer()

    def test_article_has_title(self):
        word = "Python"

        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(word)
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObject(self.driver)
        article_page_object.assert_article_has_title()

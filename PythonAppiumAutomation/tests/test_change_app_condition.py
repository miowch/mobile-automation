import pytest

from utils.core_test_case import CoreTestCase
from utils.platform import Platform
from utils.ui.factories.article_page_object_factory import ArticlePageObjectFactory
from utils.ui.factories.search_page_object_factory import SearchPageObjectFactory


@pytest.mark.testsuite
class TestChangeAppCondition(CoreTestCase):
    def test_change_screen_orientation_on_search_result(self):
        if Platform.get_instance().is_mw():
            return

        search_line = "Python"

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(search_line)
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        title_before_rotation = article_page_object.get_article_title()

        self.rotate_screen_landscape()
        title_after_rotation = article_page_object.get_article_title()

        self.assertEqual(
            title_before_rotation,
            title_after_rotation,
            "Article title have been changed after rotation")

        self.rotate_screen_portrait()
        title_after_second_rotation = article_page_object.get_article_title()

        self.assertEqual(
            title_before_rotation,
            title_after_second_rotation,
            "Article title have been changed after second rotation")

    def test_check_search_article_in_background(self):
        if Platform.get_instance().is_mw():
            return

        search_line = "Python"

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line(search_line)
        search_page_object.wait_for_search_result("General-purpose programming language")
        self.background_app(2)
        search_page_object.wait_for_search_result("General-purpose programming language")

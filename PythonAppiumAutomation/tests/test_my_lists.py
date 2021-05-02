from utils.core_test_case import CoreTestCase
from utils.platform import Platform
from utils.ui.factories.article_page_object_factory import ArticlePageObjectFactory
from utils.ui.factories.my_lists_page_object_factory import MyListsPageObjectFactory
from utils.ui.factories.navigation_ui_factory import NavigationUIFactory
from utils.ui.factories.search_page_object_factory import SearchPageObjectFactory


class TestMyLists(CoreTestCase):
    name_of_folder = "Learning programming"

    def test_save_first_article_to_my_list(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.wait_for_title_element()
        article_title = article_page_object.get_article_title()

        if Platform.get_instance().is_android():
            article_page_object.add_article_to_my_list(self.name_of_folder)
            article_page_object.wait_for_title_element()
        else:
            article_page_object.add_article_to_my_saved()

        article_page_object.close_article()

        navigation_ui = NavigationUIFactory.get(self.driver)
        navigation_ui.open_my_lists()

        my_lists_page_object = MyListsPageObjectFactory.get(self.driver)

        if Platform.get_instance().is_android():
            my_lists_page_object.open_folder_by_name(self.name_of_folder)

        my_lists_page_object.swipe_by_article_to_delete(article_title)

    def test_save_two_articles_in_one_folder(self):
        # Save the first article

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.wait_for_title_element()
        first_article_title = article_page_object.get_article_title()
        article_page_object.add_article_to_my_list(self.name_of_folder)
        article_page_object.wait_for_title_element()
        article_page_object.close_article()

        # Save the second article

        search_page_object.init_search_input()
        search_page_object.type_search_line("Java")
        search_page_object.click_by_article_with_substring("Object-oriented programming language")

        article_page_object.wait_for_title_element()
        second_article_title = article_page_object.get_article_title()
        article_page_object.add_article_to_my_list(self.name_of_folder)
        article_page_object.wait_for_title_element()
        article_page_object.close_article()

        # Remove first article from savings

        navigation_ui = NavigationUIFactory.get(self.driver)
        navigation_ui.open_my_lists()

        my_lists_page_object = MyListsPageObjectFactory.get(self.driver)
        my_lists_page_object.open_folder_by_name(self.name_of_folder)
        my_lists_page_object.swipe_by_article_to_delete(first_article_title)

        # Check that second article remains

        my_lists_page_object.open_article_by_title(second_article_title)
        title_of_opened_article = article_page_object.get_article_title()

        self.assertEqual(
            first=second_article_title,
            second=title_of_opened_article,
            msg="Title of remaining article differs from expected one")

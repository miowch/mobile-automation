from utils.core_test_case import CoreTestCase
from utils.ui.article_page_object import ArticlePageObject
from utils.ui.factories.search_page_object_factory import SearchPageObjectFactory
from utils.ui.my_lists_page_object import MyListsPageObject
from utils.ui.navigaion_ui import NavigationUI


class TestMyLists(CoreTestCase):
    def test_save_first_article_to_my_list(self):
        name_of_folder = "Learning programming"

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObject(self.driver)
        article_page_object.wait_for_title_element()
        article_title = article_page_object.get_article_title()
        article_page_object.add_article_to_my_list(name_of_folder)
        article_page_object.wait_for_title_element()
        article_page_object.close_article()

        navigation_ui = NavigationUI(self.driver)
        navigation_ui.open_my_lists()

        my_lists_page_object = MyListsPageObject(self.driver)
        my_lists_page_object.open_folder_by_name(name_of_folder)
        my_lists_page_object.swipe_by_article_to_delete(article_title)

    def test_save_two_articles_in_one_folder(self):
        name_of_folder = "Learning programming"

        # Save the first article

        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")
        search_page_object.click_by_article_with_substring("General-purpose programming language")

        article_page_object = ArticlePageObject(self.driver)
        article_page_object.wait_for_title_element()
        first_article_title = article_page_object.get_article_title()
        article_page_object.add_article_to_my_list(name_of_folder)
        article_page_object.wait_for_title_element()
        article_page_object.close_article()

        # Save the second article

        search_page_object.init_search_input()
        search_page_object.type_search_line("Java")
        search_page_object.click_by_article_with_substring("Object-oriented programming language")

        article_page_object.wait_for_title_element()
        second_article_title = article_page_object.get_article_title()
        article_page_object.add_article_to_my_list(name_of_folder)
        article_page_object.wait_for_title_element()
        article_page_object.close_article()

        # Remove first article from savings

        navigation_ui = NavigationUI(self.driver)
        navigation_ui.open_my_lists()

        my_lists_page_object = MyListsPageObject(self.driver)
        my_lists_page_object.open_folder_by_name(name_of_folder)
        my_lists_page_object.swipe_by_article_to_delete(first_article_title)

        # Check that second article remains

        my_lists_page_object.open_article_by_title(second_article_title)
        title_of_opened_article = article_page_object.get_article_title()

        self.assertEqual(
            first=second_article_title,
            second=title_of_opened_article,
            msg="Title of remaining article differs from expected one")

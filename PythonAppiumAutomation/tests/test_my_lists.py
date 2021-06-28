import time
from typing import Final

import pytest

from utils.core_test_case import CoreTestCase
from utils.platform import Platform
from utils.ui.authorization_page_object import AuthorizationPageObject
from utils.ui.factories.article_page_object_factory import ArticlePageObjectFactory
from utils.ui.factories.my_lists_page_object_factory import MyListsPageObjectFactory
from utils.ui.factories.navigation_ui_factory import NavigationUIFactory
from utils.ui.factories.search_page_object_factory import SearchPageObjectFactory


@pytest.mark.testsuite
class TestMyLists(CoreTestCase):
    name_of_folder = "Learning programming"
    login: Final = "PAA test account"
    password: Final = "29yFqiKk2XLS*6y"

    def test_save_first_article_to_my_list(self):
        search_page_object = SearchPageObjectFactory.get(self.driver)
        search_page_object.init_search_input()
        search_page_object.type_search_line("Python")

        if Platform.get_instance().is_mw():
            search_page_object.click_by_article_with_substring("eneral-purpose, high-level programming language")
        else:
            search_page_object.click_by_article_with_substring("eneral-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.wait_for_title_element()
        article_title = article_page_object.get_article_title()

        if Platform.get_instance().is_android():
            article_page_object.add_article_to_my_list(self.name_of_folder)
            article_page_object.wait_for_title_element()
        else:
            article_page_object.add_article_to_my_saved()

        if Platform.get_instance().is_mw():
            auth = AuthorizationPageObject(self.driver)
            auth.click_auth_button()
            auth.enter_login_data(self.login, self.password)
            auth.submit_form()

            article_page_object.wait_for_title_element()

            assert article_title == article_page_object.get_article_title(), "We aren't on the same page after login"

        article_page_object.close_article()

        navigation_ui = NavigationUIFactory.get(self.driver)
        navigation_ui.click_hamburger_button()
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

        if Platform.get_instance().is_mw():
            search_page_object.click_by_article_with_substring("eneral-purpose, high-level programming language")
        else:
            search_page_object.click_by_article_with_substring("eneral-purpose programming language")

        article_page_object = ArticlePageObjectFactory.get(self.driver)
        article_page_object.wait_for_title_element()
        first_article_title = article_page_object.get_article_title()

        if Platform.get_instance().is_android():
            article_page_object.add_article_to_my_list(self.name_of_folder)
            article_page_object.wait_for_title_element()
        else:
            article_page_object.add_article_to_my_saved()

        if Platform.get_instance().is_mw():
            auth = AuthorizationPageObject(self.driver)
            auth.click_auth_button()
            auth.enter_login_data(self.login, self.password)
            auth.submit_form()

            article_page_object.wait_for_title_element()

            assert first_article_title == article_page_object.get_article_title(), "We aren't on the same page after login"

        article_page_object.close_article()

        # Save the second article

        search_page_object.init_search_input()
        search_page_object.type_search_line("Java")
        search_page_object.click_by_article_with_substring("Object-oriented programming language")

        if Platform.get_instance().is_android():
            article_page_object.wait_for_title_element()
            article_page_object.add_article_to_my_list(self.name_of_folder)
            article_page_object.wait_for_title_element()
        else:
            article_page_object.add_article_to_my_saved()

        article_page_object.close_article()

        # Remove first article from savings

        navigation_ui = NavigationUIFactory.get(self.driver)
        navigation_ui.click_hamburger_button()
        navigation_ui.open_my_lists()

        my_lists_page_object = MyListsPageObjectFactory.get(self.driver)

        if Platform.get_instance().is_android():
            my_lists_page_object.open_folder_by_name(self.name_of_folder)

        my_lists_page_object.swipe_by_article_to_delete(first_article_title)

        # Check that second article remains

        if Platform.get_instance().is_android():
            my_lists_page_object.return_to_my_lists_overview()

        navigation_ui.open_explore()

        search_page_object.init_search_input()
        search_page_object.type_search_line("Java")
        search_page_object.click_by_article_with_substring("Object-oriented programming language")

        if Platform.get_instance().is_android():
            article_page_object.click_save_button()
            article_page_object.assert_article_is_saved_in_list(self.name_of_folder)
        else:
            article_page_object.assert_article_is_saved_in_list()

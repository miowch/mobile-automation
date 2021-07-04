import time

import allure

from utils.platform import Platform
from utils.ui.main_page_object import MainPageObject


class ArticlePageObject(MainPageObject):
    title: str
    footer_element: str
    options_button: str
    options_add_to_my_list_button: str
    options_font_and_theme_button: str
    options_remove_from_my_list_button: str
    add_to_my_list_overlay: str
    my_list_name_input: str
    submit_my_list_creation_button: str
    offer_to_sync_saved_article: str
    close_offer_to_sync_my_saved: str
    close_article_button: str
    save_button: str
    activate_to_unsave_button: str

    my_list_by_name_tpl: str
    button_to_remove_from_list_by_name_tpl: str

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Wait for the title on the article page")
    def wait_for_title_element(self):
        return self.wait_for_element_present(
            self.title,
            error_message="Cannot find article title on page",
            timeout_in_sec=15
        )

    @allure.step("Get the title on the article page")
    def get_article_title(self):
        title_element = self.wait_for_title_element()
        self.screenshot(self.take_screenshot("article_title"))
        return title_element.text

    @allure.step("Assert the article has the title")
    def assert_article_has_title(self):
        self.assert_element_present(
            self.title,
            error_message="The article has no title"
        )

    def assert_article_is_saved_in_list(self, name_of_folder=None):
        raise NotImplementedError("Subclass must implement this abstract method")

    def swipe_to_footer(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    @allure.step("Add article to the list")
    def add_article_to_my_list(self, name_of_folder):
        self.wait_for_element_and_click(
            self.options_button,
            error_message="Cannot find button to open article options"
        )

        self.wait_for_element_present(
            self.options_font_and_theme_button,
            error_message="Cannot find the last setting in More Options list"
        )

        self.wait_for_element_and_click(
            self.options_add_to_my_list_button,
            error_message="Cannot find option to add article to reading list"
        )

        is_first_time_of_adding_article = self.get_amount_of_elements(self.add_to_my_list_overlay)

        if is_first_time_of_adding_article:
            self.wait_for_element_and_click(
                self.add_to_my_list_overlay,
                error_message="Cannot find 'GOT IT' tip overlay"
            )

            self.wait_for_element_and_clear(
                self.my_list_name_input,
                error_message="Cannot find input to set name of article folder"
            )

            self.wait_for_element_and_send_keys(
                self.my_list_name_input,
                value=name_of_folder,
                error_message="Cannot put text into article folder input"
            )

            self.wait_for_element_and_click(
                self.submit_my_list_creation_button,
                error_message="Cannot press OK button"
            )
        else:
            my_list_xpath = self.get_my_list_element(name_of_folder)

            self.wait_for_element_and_click(
                my_list_xpath,
                error_message="Cannot find created folder to add the second article"
            )

    @allure.step("Confirm adding the article to the list by clicking the Save button")
    def click_save_button(self):
        self.wait_for_element_and_click(
            self.save_button,
            error_message="Cannot find save button to add article to reading list"
        )

    @allure.step("Add article to My Saved")
    def add_article_to_my_saved(self):
        if Platform.get_instance().is_mw():
            self.remove_article_from_my_saved_if_it_is_added()

        self.click_save_button()

        if Platform.get_instance().is_ios():
            is_offer_to_sync_saved_articles = self.get_amount_of_elements(self.offer_to_sync_saved_article)

            if is_offer_to_sync_saved_articles:
                self.wait_for_element_and_click(
                    self.close_offer_to_sync_my_saved,
                    error_message="Cannot find close button to close the offer to sync saved articles"
                )

    @allure.step("Remove article from My Saved if it was added")
    def remove_article_from_my_saved_if_it_is_added(self):
        if self.is_element_present(self.options_remove_from_my_list_button):
            self.wait_for_element_and_click(
                locator=self.options_remove_from_my_list_button,
                error_message="Cannot click button to remove article from my saved"
            )
            self.wait_for_element_present(
                locator=self.save_button,
                error_message="Cannot find button to add article to saved list after removing it from this list"
            )
            time.sleep(1)

    @allure.step("Close the article")
    def close_article(self):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.wait_for_element_and_click(
                self.close_article_button,
                error_message="Cannot close article, cannot find X button"
            )
        else:
            print("Method closeArticle() does nothing for platform " + Platform.get_instance().get_platform_var())

    # TEMPLATES METHODS
    def get_my_list_element(self, name_of_list):
        return self.my_list_by_name_tpl.replace('NAME_OF_LIST', name_of_list)

    def get_remove_from_list_element(self, name_of_list):
        return self.button_to_remove_from_list_by_name_tpl.replace('NAME_OF_LIST', name_of_list)

    # TEMPLATES METHODS

from typing import Final
from appium.webdriver.common.mobileby import MobileBy
from utils.ui.main_page_object import MainPageObject


class MyListsPageObject(MainPageObject):
    folder_by_name_tpl: Final = "//*[@text='FOLDER_NAME']"
    article_by_title_tpl: Final = "//*[@text='ARTICLE_TITLE']"

    def __init__(self, driver):
        super().__init__(driver)

    def open_folder_by_name(self, name_of_folder):
        folder_name_xpath = self.get_folder_xpath_by_name(name_of_folder)

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, folder_name_xpath),
            error_message="Cannot find folder by name " + name_of_folder
        )

    def wait_for_article_to_appear_by_title(self, article_title):
        saved_article_xpath = self.get_saved_article_xpath_by_title(article_title)

        self.wait_for_element_present(
            by=(MobileBy.XPATH, saved_article_xpath),
            error_message="Cannot find saved article by title " + article_title,
            timeout_in_sec=15
        )

    def wait_for_article_to_disappear_by_title(self, article_title):
        saved_article_xpath = self.get_saved_article_xpath_by_title(article_title)

        self.wait_for_element_not_present(
            by=(MobileBy.XPATH, saved_article_xpath),
            error_message="Saved article still present with title " + article_title,
            timeout_in_sec=15
        )

    def swipe_by_article_to_delete(self, article_title):
        self.wait_for_article_to_appear_by_title(article_title)
        saved_article_xpath = self.get_saved_article_xpath_by_title(article_title)

        self.swipe_element_to_left(
            by=(MobileBy.XPATH, saved_article_xpath),
            error_message="Cannot find saved article"
        )

        self.wait_for_article_to_disappear_by_title(article_title)

    # TEMPLATES METHODS
    def get_folder_xpath_by_name(self, name_of_folder):
        return self.folder_by_name_tpl.replace("FOLDER_NAME", name_of_folder)

    def get_saved_article_xpath_by_title(self, article_title):
        return self.article_by_title_tpl.replace("ARTICLE_TITLE", article_title)

    # TEMPLATES METHODS

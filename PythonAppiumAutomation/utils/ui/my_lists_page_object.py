from utils.platform import Platform
from utils.ui.main_page_object import MainPageObject


class MyListsPageObject(MainPageObject):
    navigate_up: str
    folder_by_name_tpl: str
    article_by_title_tpl: str
    remove_from_my_saved_button_tpl: str

    def __init__(self, driver):
        super().__init__(driver)

    def open_folder_by_name(self, name_of_folder):
        folder_name_xpath = self.get_folder_xpath_by_name(name_of_folder)

        self.wait_for_element_and_click(
            folder_name_xpath,
            error_message="Cannot find folder by name " + name_of_folder
        )

    def wait_for_article_to_appear_by_title(self, article_title):
        saved_article_xpath = self.get_saved_article_xpath_by_title(article_title)

        self.wait_for_element_present(
            saved_article_xpath,
            error_message="Cannot find saved article by title " + article_title,
            timeout_in_sec=15
        )

    def wait_for_article_to_disappear_by_title(self, article_title):
        saved_article_xpath = self.get_saved_article_xpath_by_title(article_title)

        self.wait_for_element_not_present(
            saved_article_xpath,
            error_message="Saved article still present with title " + article_title,
            timeout_in_sec=15
        )

    def open_article_by_title(self, article_title):
        saved_article_xpath = self.get_saved_article_xpath_by_title(article_title)

        self.wait_for_element_and_click(
            saved_article_xpath,
            error_message="Cannot open saved article by title " + article_title,
            timeout_in_sec=15
        )

    def return_to_my_lists_overview(self):
        self.wait_for_element_and_click(
            self.navigate_up,
            error_message="Cannot return to My Lists overview",
            timeout_in_sec=15
        )

    def swipe_by_article_to_delete(self, article_title):
        self.wait_for_article_to_appear_by_title(article_title)
        saved_article_xpath = self.get_saved_article_xpath_by_title(article_title)

        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.swipe_element_to_left(
                saved_article_xpath,
                error_message="Cannot find saved article"
            )
        else:
            remove_locator = self.get_remove_button_by_title(article_title)
            self.wait_for_element_and_click(
                locator=remove_locator,
                error_message="Cannot click button to remove article from my saved",
                timeout_in_sec=10
            )

        if Platform.get_instance().is_ios():
            self.click_element_to_the_right_upper_corner(
                saved_article_xpath,
                error_message="Cannot find saved article"
            )
        if Platform.get_instance().is_mw():
            self.driver.refresh()

        self.wait_for_article_to_disappear_by_title(article_title)

    # TEMPLATES METHODS
    def get_folder_xpath_by_name(self, name_of_folder):
        return self.folder_by_name_tpl.replace("{FOLDER_NAME}", name_of_folder)

    def get_saved_article_xpath_by_title(self, article_title):
        return self.article_by_title_tpl.replace("{ARTICLE_TITLE}", article_title)

    def get_remove_button_by_title(self, article_title):
        return self.remove_from_my_saved_button_tpl.replace("{ARTICLE_TITLE}", article_title)

    # TEMPLATES METHODS

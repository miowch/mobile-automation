from typing import Final
from appium.webdriver.common.mobileby import MobileBy
from utils.ui.main_page_object import MainPageObject


class ArticlePageObject(MainPageObject):
    title: Final = "org.wikipedia:id/view_page_title_text"
    footer_element: Final = "//*[@text='View page in browser']"
    options_button: Final = "//android.widget.ImageView[@content-desc='More options']"
    options_add_to_my_list_button: Final = "//*[@text='Add to reading list']"
    options_font_and_theme_button: Final = "//*[@text='Font and theme']"
    add_to_my_list_overlay: Final = "org.wikipedia:id/onboarding_button"
    my_list_name_input = "org.wikipedia:id/text_input"
    submit_my_list_creation_button = "//*[@text='OK']"
    close_article_button: Final = "//android.widget.ImageButton[@content-desc='Navigate up']"

    my_list_by_name_tpl: Final = "//*[@resource-id='org.wikipedia:id/item_title']" + \
                                 "[@text='NAME_OF_LIST']"

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_title_element(self):
        return self.wait_for_element_present(
            by=(MobileBy.ID, self.title),
            error_message="Cannot find article title on page",
            timeout_in_sec=15
        )

    def get_article_title(self):
        title_element = self.wait_for_title_element()
        return title_element.text

    def assert_article_has_title(self):
        self.assert_element_present(
            locator_strategy=MobileBy.ID,
            locator=self.title,
            error_message="The article has no title"
        )

    def swipe_to_footer(self):
        self.swipe_up_to_find_element(
            by_xpath=self.footer_element,
            error_message="Cannot find the end of the article",
            max_swipes=20
        )

    def add_article_to_my_list(self, name_of_folder):
        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, self.options_button),
            error_message="Cannot find button to open article options"
        )

        self.wait_for_element_present(
            by=(MobileBy.XPATH, self.options_font_and_theme_button),
            error_message="Cannot find the last setting in More Options list"
        )

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, self.options_add_to_my_list_button),
            error_message="Cannot find option to add article to reading list"
        )

        is_first_time_of_adding_article = self.get_amount_of_elements(
            locator_strategy=MobileBy.ID,
            locator=self.add_to_my_list_overlay
        )

        if is_first_time_of_adding_article:
            self.wait_for_element_and_click(
                by=(MobileBy.ID, self.add_to_my_list_overlay),
                error_message="Cannot find 'GOT IT' tip overlay"
            )

            self.wait_for_element_and_clear(
                by=(MobileBy.ID, self.my_list_name_input),
                error_message="Cannot find input to set name of article folder"
            )

            self.wait_for_element_and_send_keys(
                by=(MobileBy.ID, self.my_list_name_input),
                value=name_of_folder,
                error_message="Cannot put text into article folder input"
            )

            self.wait_for_element_and_click(
                by=(MobileBy.XPATH, self.submit_my_list_creation_button),
                error_message="Cannot press OK button"
            )
        else:
            my_list_xpath = self.get_my_list_element(name_of_folder)

            self.wait_for_element_and_click(
                by=(MobileBy.XPATH, my_list_xpath),
                error_message="Cannot find created folder to add the second article"
            )

    def close_article(self):
        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, self.close_article_button),
            error_message="Cannot close article, cannot find X button"
        )

    # TEMPLATES METHODS
    def get_my_list_element(self, name_of_list):
        return self.my_list_by_name_tpl.replace('NAME_OF_LIST', name_of_list)

    # TEMPLATES METHODS

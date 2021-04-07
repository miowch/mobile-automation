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

    def swipe_to_footer(self):
        self.swipe_up_to_find_element(
            by_xpath=self.footer_element,
            error_message="Cannot find the end of the article",
            max_swipes=20
        )

    def close_article(self):
        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, self.close_article_button),
            error_message="Cannot close article, cannot find X button"
        )


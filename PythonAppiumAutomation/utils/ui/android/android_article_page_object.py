from typing import Final
from utils.ui.article_page_object import ArticlePageObject


class AndroidArticlePageObject(ArticlePageObject):
    title: Final = "id:org.wikipedia:id/view_page_title_text"
    footer_element: Final = "xpath://*[@text='View page in browser']"
    options_button: Final = "xpath://android.widget.ImageView[@content-desc='More options']"
    options_add_to_my_list_button: Final = "xpath://*[@text='Add to reading list']"
    options_font_and_theme_button: Final = "xpath://*[@text='Font and theme']"
    add_to_my_list_overlay: Final = "id:org.wikipedia:id/onboarding_button"
    my_list_name_input = "id:org.wikipedia:id/text_input"
    submit_my_list_creation_button = "xpath://*[@text='OK']"
    close_article_button: Final = "xpath://android.widget.ImageButton[@content-desc='Navigate up']"
    save_button: Final = "xpath://android.widget.ImageView[@content-desc='Add this article to a reading list']"

    my_list_by_name_tpl: Final = "xpath://*[@resource-id='org.wikipedia:id/item_title']" + \
                                 "[@text='NAME_OF_LIST']"
    button_to_remove_from_list_by_name_tpl: Final = "xpath://*[@text='Remove from NAME_OF_LIST']"

    def __init__(self, driver):
        super().__init__(driver)

    def assert_article_is_saved_in_list(self, name_of_folder=None):
        remove_from_the_list_element_xpath = self.get_remove_from_list_element(name_of_folder)

        self.wait_for_element_present(
            remove_from_the_list_element_xpath,
            error_message="The article is not saved in list " + name_of_folder
        )

    def swipe_to_footer(self):
        self.swipe_up_to_find_element(
            self.footer_element,
            error_message="Cannot find the end of the article",
            max_swipes=50
        )

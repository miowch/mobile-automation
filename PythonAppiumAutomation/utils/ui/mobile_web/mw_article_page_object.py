from typing import Final

from utils.ui.article_page_object import ArticlePageObject


class MWArticlePageObject(ArticlePageObject):
    title: Final = "css:#content h1"
    footer_element: Final = "css: footer"
    save_button: Final = "css:#page-actions a#ca-watch.menu__item--page-actions-watch"
    options_remove_from_my_list_button: Final = "css:#page-actions li#ca-watch.menu__item--page-actions-watch watched button"

    def __init__(self, driver):
        super().__init__(driver)

    def assert_article_is_saved_in_list(self, name_of_folder=None):
        pass

    def swipe_to_footer(self):
        self.scroll_web_page_till_element_not_visible(
            locator=self.footer_element,
            error_message="Cannot find the end of article",
            max_swipes=40
        )

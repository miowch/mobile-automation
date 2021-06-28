from typing import Final

from utils.ui.my_lists_page_object import MyListsPageObject


class MWMyListsPageObject(MyListsPageObject):
    article_by_title_tpl: Final = "xpath://ul[contains(@class, 'watchlist')]//h3[contains(text(), '{ARTICLE_TITLE}')]"
    remove_from_my_saved_button_tpl: Final = "xpath://ul[contains(@class, 'watchlist')]//" \
                                             "h3[contains(text(), '{ARTICLE_TITLE}')]/../../" \
                                             "a[contains(@class, 'watched')]"

    def __init__(self, driver):
        super().__init__(driver)
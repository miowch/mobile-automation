from typing import Final
from utils.ui.my_lists_page_object import MyListsPageObject


class IosMyListsPageObject(MyListsPageObject):
    article_by_title_tpl: Final = "xpath://XCUIElementTypeLink[contains(@name,'ARTICLE_TITLE')]"

    def __init__(self, driver):
        super().__init__(driver)

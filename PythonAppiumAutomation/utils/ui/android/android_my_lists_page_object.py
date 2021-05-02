from typing import Final
from utils.ui.my_lists_page_object import MyListsPageObject


class AndroidMyListsPageObject(MyListsPageObject):
    folder_by_name_tpl: Final = "xpath://*[@text='FOLDER_NAME']"
    article_by_title_tpl: Final = "xpath://*[@text='ARTICLE_TITLE']"

    def __init__(self, driver):
        super().__init__(driver)
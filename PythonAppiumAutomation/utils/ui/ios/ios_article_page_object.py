from typing import Final
from utils.ui.article_page_object import ArticlePageObject


class IosArticlePageObject(ArticlePageObject):
    title: Final = "id:Python (programming language)"
    footer_element: Final = "id:View article in browser"
    options_add_to_my_list_button: Final = "id:Save for later"
    offer_to_sync_saved_article: Final = "id:Sync your saved articles?"
    close_offer_to_sync_my_saved: Final = "id:places auth close"
    close_article_button: Final = "id:Back"

    def __init__(self, driver):
        super().__init__(driver)

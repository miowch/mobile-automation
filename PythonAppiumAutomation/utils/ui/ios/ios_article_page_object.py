from typing import Final
from utils.ui.article_page_object import ArticlePageObject


class IosArticlePageObject(ArticlePageObject):
    title: Final = "id:Python (programming language)"
    footer_element: Final = "id:View article in browser"
    options_add_to_my_list_button: Final = "id:Save for later"
    close_article_button: Final = "id:Back"

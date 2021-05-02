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

    my_list_by_name_tpl: Final = "xpath://*[@resource-id='org.wikipedia:id/item_title']" + \
                                 "[@text='NAME_OF_LIST']"

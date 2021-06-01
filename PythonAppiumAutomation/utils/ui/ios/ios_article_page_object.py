from typing import Final

from utils.ui.article_page_object import ArticlePageObject


class IosArticlePageObject(ArticlePageObject):
    title: Final = "id:Python (programming language)"
    footer_element: Final = "id:View article in browser"
    save_button: Final = "id:Save for later"
    offer_to_sync_saved_article: Final = "id:Sync your saved articles?"
    close_offer_to_sync_my_saved: Final = "id:places auth close"
    close_article_button: Final = "id:Back"
    activate_to_unsave_button: Final = "id:Saved. Activate to unsave."

    def __init__(self, driver):
        super().__init__(driver)

    def assert_article_is_saved_in_list(self, name_of_folder=None):
        self.wait_for_element_present(
            self.activate_to_unsave_button,
            error_message="There is not Saved status on the button. The article is not saved in list."
        )

    def swipe_to_footer(self):
        self.swipe_up_till_element_appears(
            self.footer_element,
            error_message="Cannot find the end of the article",
            max_swipes=50
        )

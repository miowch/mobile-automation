from utils.platform import Platform
from utils.ui.main_page_object import MainPageObject


class ArticlePageObject(MainPageObject):
    title: str
    footer_element: str
    options_button: str
    options_add_to_my_list_button: str
    options_font_and_theme_button: str
    add_to_my_list_overlay: str
    my_list_name_input: str
    submit_my_list_creation_button: str
    close_article_button: str

    my_list_by_name_tpl: str

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_title_element(self):
        return self.wait_for_element_present(
            self.title,
            error_message="Cannot find article title on page",
            timeout_in_sec=15
        )

    def get_article_title(self):
        title_element = self.wait_for_title_element()
        return title_element.text

    def assert_article_has_title(self):
        self.assert_element_present(
            self.title,
            error_message="The article has no title"
        )

    def swipe_to_footer(self):
        if Platform.get_instance().is_android():
            self.swipe_up_to_find_element(
                self.footer_element,
                error_message="Cannot find the end of the article",
                max_swipes=50
            )
        else:
            self.swipe_up_till_element_appears(
                self.footer_element,
                error_message="Cannot find the end of the article",
                max_swipes=50
            )

    def add_article_to_my_list(self, name_of_folder):
        self.wait_for_element_and_click(
            self.options_button,
            error_message="Cannot find button to open article options"
        )

        self.wait_for_element_present(
            self.options_font_and_theme_button,
            error_message="Cannot find the last setting in More Options list"
        )

        self.wait_for_element_and_click(
            self.options_add_to_my_list_button,
            error_message="Cannot find option to add article to reading list"
        )

        is_first_time_of_adding_article = self.get_amount_of_elements(self.add_to_my_list_overlay)

        if is_first_time_of_adding_article:
            self.wait_for_element_and_click(
                self.add_to_my_list_overlay,
                error_message="Cannot find 'GOT IT' tip overlay"
            )

            self.wait_for_element_and_clear(
                self.my_list_name_input,
                error_message="Cannot find input to set name of article folder"
            )

            self.wait_for_element_and_send_keys(
                self.my_list_name_input,
                value=name_of_folder,
                error_message="Cannot put text into article folder input"
            )

            self.wait_for_element_and_click(
                self.submit_my_list_creation_button,
                error_message="Cannot press OK button"
            )
        else:
            my_list_xpath = self.get_my_list_element(name_of_folder)

            self.wait_for_element_and_click(
                my_list_xpath,
                error_message="Cannot find created folder to add the second article"
            )

    def close_article(self):
        self.wait_for_element_and_click(
            self.close_article_button,
            error_message="Cannot close article, cannot find X button"
        )

    # TEMPLATES METHODS
    def get_my_list_element(self, name_of_list):
        return self.my_list_by_name_tpl.replace('NAME_OF_LIST', name_of_list)

    # TEMPLATES METHODS

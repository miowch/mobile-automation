from typing import Final
from utils.ui.search_page_object import SearchPageObject


class AndroidSearchPageObject(SearchPageObject):
    search_init_field: Final = "xpath://*[@resource-id='org.wikipedia:id/search_container']" + \
                               "//*[contains(@class, 'android.widget.TextView')]"
    search_init_element: Final = "xpath://*[contains(@text, 'Search Wikipedia')]"
    search_input: Final = "xpath://*[contains(@text, 'Search…')]"
    search_result_element: Final = "xpath://*[@resource-id='org.wikipedia:id/search_results_list']" + \
                                   "/*[@resource-id='org.wikipedia:id/page_list_item_container']"
    search_result_title: Final = "xpath://*[@resource-id='org.wikipedia:id/page_list_item_title']"
    empty_result_label: Final = "xpath://*[@text='No results found']"
    search_cancel_button: Final = "id:org.wikipedia:id/search_close_btn"
    search_empty_message_element: Final = "id:org.wikipedia:id/search_empty_message"

    search_result_by_substring_tpl: Final = "xpath://*[@resource-id='org.wikipedia:id/page_list_item_container']" + \
                                            "//*[@text='SUBSTRING']"

    def __init__(self, driver):
        super().__init__(driver)

from typing import Final

from utils.ui.search_page_object import SearchPageObject


class IosSearchPageObject(SearchPageObject):
    search_init_field: Final = "xpath://XCUIElementTypeSearchField"
    search_init_element: Final = "xpath://XCUIElementTypeSearchField[@name='Search Wikipedia']"
    search_input: Final = "xpath://XCUIElementTypeSearchField[@label='Search Wikipedia']"
    search_result_element: Final = "xpath://XCUIElementTypeLink"
    empty_result_label: Final = "xpath://XCUIElementTypeStaticText[@value='No results found']"
    search_cancel_button: Final = "id:Close"
    search_empty_message_element: Final = "xpath://XCUIElementTypeStaticText[@name='No results found']"

    search_result_by_substring_tpl: Final = "xpath://XCUIElementTypeLink[contains(@name,'SUBSTRING')]"

    def __init__(self, driver):
        super().__init__(driver)

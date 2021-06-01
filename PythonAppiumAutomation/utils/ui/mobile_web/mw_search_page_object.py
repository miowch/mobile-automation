from typing import Final

from utils.ui.search_page_object import SearchPageObject


class MWSearchPageObject(SearchPageObject):
    search_init_field: Final = "css:form.search-box"
    search_init_element: Final = "css:button#searchIcon"
    search_input: Final = "css:form>input[type='search']"
    search_result_element: Final = "css:ul.page-list>li.page-summary"
    search_result_title: Final = "xpath://li[contains(@class, 'page-summary')]/a[contains(@class, 'title')]/h3"
    empty_result_label: Final = "xpath://p[contains(@class,'without-results')][contains(text(),'No page with this title.')]"
    search_cancel_button: Final = "css:div.header-action>button.cancel"
    search_empty_message_element: Final = "css:p.without-results"

    search_result_by_substring_tpl: Final = "xpath://div[contains(@class,'wikidata-description')][contains(text(),'{SUBSTRING}')]"

    def __init__(self, driver):
        super().__init__(driver)

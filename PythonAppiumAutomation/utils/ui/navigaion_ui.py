from utils.ui.main_page_object import MainPageObject


class NavigationUI(MainPageObject):
    my_lists_button: str
    explore_button: str

    def __init__(self, driver):
        super().__init__(driver)

    def open_my_lists(self):
        self.wait_for_element_and_click(
            self.my_lists_button,
            error_message="Cannot find navigation button to my lists"
        )

    def open_explore(self):
        self.wait_for_element_and_click(
            self.explore_button,
            error_message="Cannot find navigation button to explore page"
        )

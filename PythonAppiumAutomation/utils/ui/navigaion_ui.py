from utils.platform import Platform
from utils.ui.main_page_object import MainPageObject


class NavigationUI(MainPageObject):
    my_lists_button: str
    explore_button: str
    open_navigation: str

    def __init__(self, driver):
        super().__init__(driver)

    def open_my_lists(self):
        if Platform.get_instance().is_mw():
            self.try_click_element_with_few_attempts(
                locator=self.my_lists_button,
                error_message="Cannot find navigation button to my lists",
                amount_of_attempts=5
            )
        else:
            self.wait_for_element_and_click(
                self.my_lists_button,
                error_message="Cannot find navigation button to my lists"
            )

    def open_explore(self):
        if Platform.get_instance().is_android() or Platform.get_instance().is_ios():
            self.wait_for_element_and_click(
                self.explore_button,
                error_message="Cannot find navigation button to explore page"
            )

    def click_hamburger_button(self):
        if Platform.get_instance().is_mw():
            self.wait_for_element_and_click(
                locator=self.open_navigation,
                error_message="Cannot find and click open navigation button"
            )
        else:
            print("Method open_navigation does nothing for platform " + Platform.get_instance().get_platform_var())

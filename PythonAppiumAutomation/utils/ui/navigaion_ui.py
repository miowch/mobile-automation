from typing import Final
from appium.webdriver.common.mobileby import MobileBy
from utils.ui.main_page_object import MainPageObject


class NavigationUI(MainPageObject):
    my_lists_button: Final = "xpath://android.widget.FrameLayout[@content-desc='My lists']"

    def __init__(self, driver):
        super().__init__(driver)

    def open_my_lists(self):
        self.wait_for_element_and_click(
            self.my_lists_button,
            error_message="Cannot find navigation button to my lists"
        )

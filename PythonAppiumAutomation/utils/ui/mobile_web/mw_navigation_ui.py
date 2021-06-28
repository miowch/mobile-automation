from typing import Final

from utils.ui.navigaion_ui import NavigationUI


class MWNavigationUI(NavigationUI):
    my_lists_button: Final = "css:a[data-event-name='menu.unStar']"
    open_navigation: Final = "css:#mw-mf-main-menu-button"

    def __init__(self, driver):
        super().__init__(driver)

from typing import Final

from utils.ui.navigaion_ui import NavigationUI


class IosNavigationUI(NavigationUI):
    my_lists_button: Final = "id:Saved"
    explore_button: Final = "id:Explore"

    def __init__(self, driver):
        super().__init__(driver)

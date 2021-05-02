from utils.platform import Platform
from utils.ui.android.android_navigation_ui import AndroidNavigationUI
from utils.ui.ios.ios_navigation_ui import IosNavigationUI


class NavigationUIFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidNavigationUI(driver)
        else:
            return IosNavigationUI(driver)

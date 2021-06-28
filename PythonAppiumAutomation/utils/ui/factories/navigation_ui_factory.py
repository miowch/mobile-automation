from utils.platform import Platform
from utils.ui.android.android_navigation_ui import AndroidNavigationUI
from utils.ui.ios.ios_navigation_ui import IosNavigationUI
from utils.ui.mobile_web.mw_navigation_ui import MWNavigationUI


class NavigationUIFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidNavigationUI(driver)
        elif Platform.get_instance().is_ios():
            return IosNavigationUI(driver)
        else:
            return MWNavigationUI(driver)

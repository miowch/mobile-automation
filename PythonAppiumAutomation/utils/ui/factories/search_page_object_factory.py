from utils.platform import Platform
from utils.ui.android.android_search_page_object import AndroidSearchPageObject
from utils.ui.ios.ios_search_page_object import IosSearchPageObject
from utils.ui.mobile_web.mw_search_page_object import MWSearchPageObject


class SearchPageObjectFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidSearchPageObject(driver)
        elif Platform.get_instance().is_ios():
            return IosSearchPageObject(driver)
        else:
            return MWSearchPageObject(driver)

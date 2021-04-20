from utils.platform import Platform
from utils.ui.android.android_search_page_object import AndroidSearchPageObject
from utils.ui.ios.ios_search_page_object import IosSearchPageObject


class SearchPageObjectFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidSearchPageObject(driver)
        else:
            return IosSearchPageObject(driver)

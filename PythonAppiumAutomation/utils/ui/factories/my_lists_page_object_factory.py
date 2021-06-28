from utils.platform import Platform
from utils.ui.android.android_my_lists_page_object import AndroidMyListsPageObject
from utils.ui.ios.ios_my_lists_page_object import IosMyListsPageObject
from utils.ui.mobile_web.mw_my_lists_page_object import MWMyListsPageObject


class MyListsPageObjectFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidMyListsPageObject(driver)
        elif Platform.get_instance().is_ios():
            return IosMyListsPageObject(driver)
        else:
            return MWMyListsPageObject(driver)

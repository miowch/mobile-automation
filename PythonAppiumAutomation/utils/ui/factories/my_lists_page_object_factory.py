from utils.platform import Platform
from utils.ui.android.android_my_lists_page_object import AndroidMyListsPageObject
from utils.ui.ios.ios_my_lists_page_object import IosMyListsPageObject


class MyListsPageObjectFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidMyListsPageObject(driver)
        else:
            return IosMyListsPageObject(driver)

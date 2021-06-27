from utils.platform import Platform
from utils.ui.android.android_article_page_object import AndroidArticlePageObject
from utils.ui.ios.ios_article_page_object import IosArticlePageObject
from utils.ui.mobile_web.mw_article_page_object import MWArticlePageObject


class ArticlePageObjectFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidArticlePageObject(driver)
        elif Platform.get_instance().is_ios():
            return IosArticlePageObject(driver)
        else:
            return MWArticlePageObject(driver)

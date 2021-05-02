from utils.platform import Platform
from utils.ui.android.android_article_page_object import AndroidArticlePageObject
from utils.ui.ios.ios_article_page_object import IosArticlePageObject


class ArticlePageObjectFactory:
    @staticmethod
    def get(driver):
        if Platform.get_instance().is_android():
            return AndroidArticlePageObject(driver)
        else:
            return IosArticlePageObject(driver)

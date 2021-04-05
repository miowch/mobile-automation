from appium.webdriver.common.mobileby import MobileBy
from utils.core_test_case import CoreTestCase
from utils.ui.main_page_object import MainPageObject


class TestClass(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.main_page_object = MainPageObject(self.driver)

    def test_search_input_box_has_placeholder(self):
        self.main_page_object.assert_element_has_text(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/search_container']" +
                "//*[contains(@class, 'android.widget.TextView')]"),
            expected_text="Search Wikipedia",
            error_message="Search field has another placeholder")

    def test_search(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search Wikipedia')]"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'General-purpose programming language' topic searching by Python",
            timeout_in_sec=15)

    def test_clear_and_cancel_search(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_clear(
            by=(MobileBy.ID, "org.wikipedia:id/search_src_text"),
            error_message="Cannot find search field")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_close_btn"),
            error_message="Cannot find 'close' button to cancel search")

        self.main_page_object.wait_for_element_not_present(
            by=(MobileBy.ID, "org.wikipedia:id/search_close_btn"),
            error_message="'Close' button is still present on the page"
        )

    def test_perform_and_cancel_search(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_elements_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/search_results_list']" +
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']"),
            error_message="No search results")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_close_btn"),
            error_message="Cannot find 'close' button to cancel search")

        self.main_page_object.assert_element_has_text(
            by=(MobileBy.ID, "org.wikipedia:id/search_empty_message"),
            expected_text="Search and read the free encyclopedia in your language",
            error_message="Search empty message differs from expected one")

    def test_search_results_contain_required_word(self):
        word = "Python"

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=word,
            error_message="Cannot find search input")

        search_results = self.main_page_object.wait_for_elements_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/search_results_list']" +
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']"),
            error_message="No search results")

        for i in search_results:
            title_element = i.find_element_by_xpath("//*[@resource-id='org.wikipedia:id/page_list_item_title']")

            self.assertTrue(
                word.lower() in title_element.text.lower(),
                "Search result does not contain required word")

    def test_compare_article_title(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        title_element = self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        article_title = title_element.text

        self.assertEqual(
            first=article_title,
            second="Python (programming language)",
            msg="We see unexpected title")

    def test_swipe_article(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Appium",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_title']" +
                "[@text='Appium']"),
            error_message="Cannot find 'Appium' article in search",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.main_page_object.swipe_up_to_find_element(
            by_xpath="//*[@text='View page in browser']",
            error_message="Cannot find the end of the article",
            max_swipes=20
        )

    def test_save_first_article_to_my_list(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageView[@content-desc='More options']"),
            error_message="Cannot find button to open article options"
        )

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@text='Font and theme']"),
            error_message="Cannot find the last setting in More Options list"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@text='Add to reading list']"),
            error_message="Cannot find option to add article to reading list"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/onboarding_button"),
            error_message="Cannot find 'GOT IT' tip overlay"
        )

        self.main_page_object.wait_for_element_and_clear(
            by=(MobileBy.ID, "org.wikipedia:id/text_input"),
            error_message="Cannot find input to set name of article folder"
        )

        name_of_folder = "Learning programming"

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.ID, "org.wikipedia:id/text_input"),
            value=name_of_folder,
            error_message="Cannot put text into article folder input"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@text='OK']"),
            error_message="Cannot press OK button"
        )

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageButton[@content-desc='Navigate up']"),
            error_message="Cannot close article, cannot find X button"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.FrameLayout[@content-desc='My lists']"),
            error_message="Cannot find navigation button to my lists"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                f"//*[@text='{name_of_folder}']"),
            error_message="Cannot find created folder"
        )

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@text='Python (programming language)']"),
            error_message="Cannot find the article in the list"
        )

        self.main_page_object.swipe_element_to_left(
            by=(MobileBy.XPATH,
                "//*[@text='Python (programming language)']"),
            error_message="Cannot find saved article"
        )

        self.main_page_object.wait_for_element_not_present(
            by=(MobileBy.XPATH,
                "//*[@text='Python (programming language)']"),
            error_message="Cannot delete saved article"
        )

    def test_amount_of_not_empty_search(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        search_line = "Linkin Park Discography"
        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=search_line,
            error_message="Cannot find search input")

        search_result_locator = "//*[@resource-id='org.wikipedia:id/search_results_list']" + \
                                "/*[@resource-id='org.wikipedia:id/page_list_item_container']"

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH, search_result_locator),
            error_message="Cannot find anything by the request " + search_line,
            timeout_in_sec=15
        )

        amount_of_search_results = self.main_page_object.get_amount_of_elements(
            locator_strategy=MobileBy.XPATH,
            locator=search_result_locator)

        self.assertTrue(
            amount_of_search_results,
            "We found too few results"
        )

    def test_amount_of_empty_search(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        search_line = "ghgkg"
        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=search_line,
            error_message="Cannot find search input")

        search_result_locator = "//*[@resource-id='org.wikipedia:id/search_results_list']" + \
                                "/*[@resource-id='org.wikipedia:id/page_list_item_container']"

        empty_result_label = "//*[@text='No results found']"

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH, empty_result_label),
            error_message="Cannot find empty result label by the request " + search_line,
            timeout_in_sec=15
        )

        self.main_page_object.assert_element_not_present(
            locator_strategy=MobileBy.XPATH,
            locator=search_result_locator,
            error_message="We've found some results by request " + search_line
        )

    def test_change_screen_orientation_on_search_result(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        search_line = "Python"
        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=search_line,
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'General-purpose programming language' topic searching by " + search_line,
            timeout_in_sec=15)

        title_before_rotation = self.main_page_object.wait_for_element_and_get_attribute(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            attribute="text",
            error_message="Cannot find title of article",
            timeout_in_sec=15
        )

        self.driver.orientation = "LANDSCAPE"

        title_after_rotation = self.main_page_object.wait_for_element_and_get_attribute(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            attribute="text",
            error_message="Cannot find title of article",
            timeout_in_sec=15
        )

        self.assertEqual(
            title_before_rotation,
            title_after_rotation,
            "Article title have been changed after rotation")

        self.driver.orientation = "PORTRAIT"

        title_after_second_rotation = self.main_page_object.wait_for_element_and_get_attribute(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            attribute="text",
            error_message="Cannot find title of article",
            timeout_in_sec=15
        )

        self.assertEqual(
            title_before_rotation,
            title_after_second_rotation,
            "Article title have been changed after second rotation")

    def test_check_search_article_in_background(self):
        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        self.driver.background_app(10)

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find article after returning from background",
            timeout_in_sec=15)

    def test_save_two_articles_in_one_folder(self):
        # Save the first article

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageView[@content-desc='More options']"),
            error_message="Cannot find button to open article options"
        )

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@text='Font and theme']"),
            error_message="Cannot find the last setting in More Options list"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@text='Add to reading list']"),
            error_message="Cannot find option to add article to reading list"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/onboarding_button"),
            error_message="Cannot find 'GOT IT' tip overlay"
        )

        self.main_page_object.wait_for_element_and_clear(
            by=(MobileBy.ID, "org.wikipedia:id/text_input"),
            error_message="Cannot find input to set name of article folder"
        )

        name_of_folder = "Learning programming"

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.ID, "org.wikipedia:id/text_input"),
            value=name_of_folder,
            error_message="Cannot put text into article folder input"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@text='OK']"),
            error_message="Cannot press OK button"
        )

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageButton[@content-desc='Navigate up']"),
            error_message="Cannot close article, cannot find X button"
        )

        # Save the second article

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Java",
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='Object-oriented programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageView[@content-desc='More options']"),
            error_message="Cannot find button to open article options"
        )

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@text='Font and theme']"),
            error_message="Cannot find the last setting in More Options list"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@text='Add to reading list']"),
            error_message="Cannot find option to add article to reading list"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/item_title']" +
                f"[@text='{name_of_folder}']"),
            error_message="Cannot find created folder to add the second article"
        )

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageButton[@content-desc='Navigate up']"),
            error_message="Cannot close article, cannot find X button"
        )

        # Remove one article from savings

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.FrameLayout[@content-desc='My lists']"),
            error_message="Cannot find navigation button to my lists"
        )

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                f"//*[@text='{name_of_folder}']"),
            error_message="Cannot find created folder"
        )

        article_to_remove = "Python (programming language)"

        self.main_page_object.wait_for_element_present(
            by=(MobileBy.XPATH,
                f"//*[@text='{article_to_remove}']"),
            error_message="Cannot find the article in the list"
        )

        self.main_page_object.swipe_element_to_left(
            by=(MobileBy.XPATH,
                f"//*[@text='{article_to_remove}']"),
            error_message="Cannot find saved article"
        )

        self.main_page_object.wait_for_element_not_present(
            by=(MobileBy.XPATH,
                f"//*[@text='{article_to_remove}']"),
            error_message="Cannot delete saved article"
        )

        # Check that another article remains

        remaining_article = "Java (programming language)"

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                f"//*[@text='{remaining_article}']"),
            error_message="Cannot find remaining article"
        )

        self.main_page_object.assert_element_has_text(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            expected_text=remaining_article,
            error_message="Title of remaining article differs from expected one"
        )

    def test_article_has_title(self):
        word = "Python"

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.main_page_object.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=word,
            error_message="Cannot find search input")

        self.main_page_object.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        self.main_page_object.assert_element_present(
            locator_strategy=MobileBy.ID,
            locator="org.wikipedia:id/view_page_title_text",
            error_message="The article has no title"
        )

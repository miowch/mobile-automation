import unittest

from appium.webdriver.common.touch_action import TouchAction

from webdriver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().instance

    def test_search_input_box_has_placeholder(self):
        self.assert_element_has_text(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/search_container']" +
                "//*[contains(@class, 'android.widget.TextView')]"),
            expected_text="Search Wikipedia",
            error_message="Search field has another placeholder")

    def test_search(self):
        self.wait_for_element_and_click(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search Wikipedia')]"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'General-purpose programming language' topic searching by Python",
            timeout_in_sec=15)

    def test_clear_and_cancel_search(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.wait_for_element_and_clear(
            by=(MobileBy.ID, "org.wikipedia:id/search_src_text"),
            error_message="Cannot find search field")

        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_close_btn"),
            error_message="Cannot find 'close' button to cancel search")

        self.wait_for_element_not_present(
            by=(MobileBy.ID, "org.wikipedia:id/search_close_btn"),
            error_message="'Close' button is still present on the page"
        )

    def test_perform_and_cancel_search(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.wait_for_elements_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/search_results_list']" +
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']"),
            error_message="No search results")

        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_close_btn"),
            error_message="Cannot find 'close' button to cancel search")

        self.assert_element_has_text(
            by=(MobileBy.ID, "org.wikipedia:id/search_empty_message"),
            expected_text="Search and read the free encyclopedia in your language",
            error_message="Search empty message differs from expected one")

    def test_search_results_contain_required_word(self):
        word = "Python"

        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=word,
            error_message="Cannot find search input")

        search_results = self.wait_for_elements_present(
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
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        title_element = self.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        article_title = title_element.text

        self.assertEqual(
            first=article_title,
            second="Python (programming language)",
            msg="We see unexpected title")

    def test_swipe_article(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Appium",
            error_message="Cannot find search input")

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_title']" +
                "[@text='Appium']"),
            error_message="Cannot find 'Appium' article in search",
            timeout_in_sec=15)

        self.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.swipe_up_to_find_element(
            by_xpath="//*[@text='View page in browser']",
            error_message="Cannot find the end of the article",
            max_swipes=20
        )

    def test_save_first_article_to_my_list(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        self.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageView[@content-desc='More options']"),
            error_message="Cannot find button to open article options"
        )

        self.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@text='Font and theme']"),
            error_message="Cannot find the last setting in More Options list"
        )

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@text='Add to reading list']"),
            error_message="Cannot find option to add article to reading list"
        )

        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/onboarding_button"),
            error_message="Cannot find 'GOT IT' tip overlay"
        )

        self.wait_for_element_and_clear(
            by=(MobileBy.ID, "org.wikipedia:id/text_input"),
            error_message="Cannot find input to set name of article folder"
        )

        name_of_folder = "Learning programming"

        self.wait_for_element_and_send_keys(
            by=(MobileBy.ID, "org.wikipedia:id/text_input"),
            value=name_of_folder,
            error_message="Cannot put text into article folder input"
        )

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@text='OK']"),
            error_message="Cannot press OK button"
        )

        self.wait_for_element_present(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            error_message="Cannot find article title",
            timeout_in_sec=15)

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.ImageButton[@content-desc='Navigate up']"),
            error_message="Cannot close article, cannot find X button"
        )

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//android.widget.FrameLayout[@content-desc='My lists']"),
            error_message="Cannot find navigation button to my lists"
        )

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                f"//*[@text='{name_of_folder}']"),
            error_message="Cannot find created folder"
        )

        self.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@text='Python (programming language)']"),
            error_message="Cannot find the article in the list"
        )

        self.swipe_element_to_left(
            by=(MobileBy.XPATH,
                "//*[@text='Python (programming language)']"),
            error_message="Cannot find saved article"
        )

        self.wait_for_element_not_present(
            by=(MobileBy.XPATH,
                "//*[@text='Python (programming language)']"),
            error_message="Cannot delete saved article"
        )

    def test_amount_of_not_empty_search(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        search_line = "Linkin Park Discography"
        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=search_line,
            error_message="Cannot find search input")

        search_result_locator = "//*[@resource-id='org.wikipedia:id/search_results_list']" + \
                                "/*[@resource-id='org.wikipedia:id/page_list_item_container']"

        self.wait_for_element_present(
            by=(MobileBy.XPATH, search_result_locator),
            error_message="Cannot find anything by the request " + search_line,
            timeout_in_sec=15
        )

        amount_of_search_results = self.get_amount_of_elements(
            locator_strategy=MobileBy.XPATH,
            locator=search_result_locator)

        self.assertTrue(
            amount_of_search_results,
            "We found too few results"
        )

    def test_amount_of_empty_search(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        search_line = "ghgkg"
        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=search_line,
            error_message="Cannot find search input")

        search_result_locator = "//*[@resource-id='org.wikipedia:id/search_results_list']" + \
                                "/*[@resource-id='org.wikipedia:id/page_list_item_container']"

        empty_result_label = "//*[@text='No results found']"

        self.wait_for_element_present(
            by=(MobileBy.XPATH, empty_result_label),
            error_message="Cannot find empty result label by the request " + search_line,
            timeout_in_sec=15
        )

        self.assert_element_not_present(
            locator_strategy=MobileBy.XPATH,
            locator=search_result_locator,
            error_message="We've found some results by request " + search_line
        )

    def test_change_screen_orientation_on_search_result(self):
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        search_line = "Python"
        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value=search_line,
            error_message="Cannot find search input")

        self.wait_for_element_and_click(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'General-purpose programming language' topic searching by " + search_line,
            timeout_in_sec=15)

        title_before_rotation = self.wait_for_element_and_get_attribute(
            by=(MobileBy.ID, "org.wikipedia:id/view_page_title_text"),
            attribute="text",
            error_message="Cannot find title of article",
            timeout_in_sec=15
        )

        self.driver.orientation = "LANDSCAPE"

        title_after_rotation = self.wait_for_element_and_get_attribute(
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

        title_after_second_rotation = self.wait_for_element_and_get_attribute(
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
        self.wait_for_element_and_click(
            by=(MobileBy.ID, "org.wikipedia:id/search_container"),
            error_message="Cannot find 'Search Wikipedia' input")

        self.wait_for_element_and_send_keys(
            by=(MobileBy.XPATH, "//*[contains(@text, 'Search…')]"),
            value="Python",
            error_message="Cannot find search input")

        self.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find 'Search Wikipedia' input",
            timeout_in_sec=15)

        self.driver.background_app(10)

        self.wait_for_element_present(
            by=(MobileBy.XPATH,
                "//*[@resource-id='org.wikipedia:id/page_list_item_container']" +
                "//*[@text='General-purpose programming language']"),
            error_message="Cannot find article after returning from background",
            timeout_in_sec=15)

    def tearDown(self):
        self.driver.quit()

    def wait_for_element_present(self, by, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)

        return wait.until(
            EC.presence_of_element_located(by),
            message=error_message + '\n')

    def wait_for_elements_present(self, by, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)

        return wait.until(
            EC.presence_of_all_elements_located(by),
            message=error_message + '\n')

    def assert_element_has_text(self, by, expected_text, error_message):
        element = self.wait_for_element_present(by, error_message)
        return self.assertEqual(element.text, expected_text, error_message)

    def wait_for_element_and_click(self, by, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(by, error_message, timeout_in_sec)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, by, value, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(by, error_message, timeout_in_sec)
        element.send_keys(value)
        return element

    def wait_for_element_not_present(self, by, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)

        return wait.until(
            EC.invisibility_of_element_located(by),
            message=error_message + '\n')

    def wait_for_element_and_clear(self, by, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(by, error_message, timeout_in_sec)
        element.clear()
        return element

    def swipe_up(self, time_of_swipe=200):
        action = TouchAction(self.driver)
        size = self.driver.get_window_size()

        x = int(size['width'] / 2)
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)

        action \
            .press(x=x, y=start_y) \
            .wait(time_of_swipe) \
            .move_to(x=x, y=end_y) \
            .release() \
            .perform()

    def swipe_up_to_find_element(self, by_xpath, error_message, max_swipes):
        already_swiped = 0

        while not self.driver.find_elements_by_xpath(by_xpath):

            if already_swiped > max_swipes:
                self.wait_for_element_present(
                    by=(MobileBy.XPATH, by_xpath),
                    error_message="Cannot find element by swiping up. \n" + error_message,
                    timeout_in_sec=0)
                return

            self.swipe_up()
            already_swiped += 1

    def swipe_element_to_left(self, by, error_message):
        element = self.wait_for_element_present(
            by,
            error_message,
            timeout_in_sec=10)

        left_x = int(element.location['x'])
        right_x = int(left_x + element.size['width'])

        upper_y = int(element.location['y'])
        lower_y = int(upper_y + element.size['height'])

        middle_y = int((upper_y + lower_y) / 2)

        action = TouchAction(self.driver)
        action \
            .press(x=right_x, y=middle_y) \
            .wait(300) \
            .move_to(x=left_x, y=middle_y) \
            .release() \
            .perform()

    def get_amount_of_elements(self, locator_strategy, locator):
        return len(self.driver.find_elements(locator_strategy, locator))

    def assert_element_not_present(self, locator_strategy, locator, error_message):
        amount_of_elements = self.get_amount_of_elements(locator_strategy, locator)
        if amount_of_elements:
            default_message = "An element '" + str(locator) + "' supposed to be not present"
            raise AssertionError(default_message + " " + error_message)

    def wait_for_element_and_get_attribute(self, by, attribute, error_message, timeout_in_sec):
        element = self.wait_for_element_present(by, error_message, timeout_in_sec)

        return element.get_attribute(attribute)

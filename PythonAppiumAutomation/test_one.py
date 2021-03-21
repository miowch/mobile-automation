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

        action.press(x=x, y=start_y).wait(time_of_swipe).move_to(x=x, y=end_y).release().perform()

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

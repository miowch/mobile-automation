import unittest
from webdriver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().instance

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

    def test_cancel_search(self):
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

    def tearDown(self):
        self.driver.quit()

    def wait_for_element_present(self, by, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)

        return wait.until(
            EC.presence_of_element_located(by),
            message=error_message + '\n')

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

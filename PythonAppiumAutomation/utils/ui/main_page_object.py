from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPageObject:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_locator_by_string(locator_with_type):
        exploded_locator = locator_with_type.split(":", 1)
        locator_strategy = exploded_locator[0]
        locator = exploded_locator[1]

        if locator_strategy == "xpath":
            return MobileBy.XPATH, locator
        elif locator_strategy == "id":
            return MobileBy.ID, locator
        else:
            raise ValueError("Cannot get type of locator. Locator: " + locator_strategy)

    def wait_for_element_present(self, locator, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)
        by = self.get_locator_by_string(locator)

        return wait.until(
            EC.presence_of_element_located(by),
            message=error_message + '\n')

    def wait_for_elements_present(self, locator, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)
        by = self.get_locator_by_string(locator)

        return wait.until(
            EC.presence_of_all_elements_located(by),
            message=error_message + '\n')

    def get_amount_of_elements(self, locator_string):  # string from PO with strategy and locator
        locator_strategy, locator = self.get_locator_by_string(locator_string)
        return len(self.driver.find_elements(locator_strategy, locator))

    def wait_for_element_not_present(self, locator, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)
        by = self.get_locator_by_string(locator)

        return wait.until(
            EC.invisibility_of_element_located(by),
            message=error_message + '\n')

    def wait_for_element_and_get_attribute(self, locator, attribute, error_message, timeout_in_sec):
        element = self.wait_for_element_present(locator, error_message, timeout_in_sec)
        return element.get_attribute(attribute)

    def wait_for_element_and_click(self, locator, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(locator, error_message, timeout_in_sec)
        element.click()
        return element

    def wait_for_element_and_clear(self, locator, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(locator, error_message, timeout_in_sec)
        element.clear()
        return element

    def wait_for_element_and_send_keys(self, locator, value, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(locator, error_message, timeout_in_sec)
        element.click()
        element.send_keys(value)
        return element

    def assert_element_has_text(self, locator, expected_text, error_message):
        element = self.wait_for_element_present(locator, error_message)
        return element.text == expected_text

    def assert_element_present(self, locator, error_message):
        amount_of_elements = self.get_amount_of_elements(locator)
        if not amount_of_elements:
            default_message = "An element '" + str(locator) + "' supposed to be present. "
            raise AssertionError(default_message + " " + error_message)

    def assert_element_not_present(self, locator, error_message):
        amount_of_elements = self.get_amount_of_elements(locator)
        if amount_of_elements:
            default_message = "An element '" + locator + "' supposed to be not present. "
            raise AssertionError(default_message + " " + error_message)

    def assert_elements_contain_required_word(self, elements_xpath, element_xpath, word, error_message):
        element_xpath = self.get_locator_by_string(element_xpath)[1]

        elements = self.wait_for_elements_present(
            locator=elements_xpath,
            error_message="No elements found",
            timeout_in_sec=15
        )

        for i in elements:
            element = i.find_element_by_xpath(element_xpath)

            if word.lower() not in element.text.lower():
                default_message = "Element '" + str(element_xpath) + "' supposed to contain the word " + word
                raise AssertionError(default_message + " " + error_message)

    def is_element_located_on_the_screen(self, locator):
        element_location_by_y = self.wait_for_element_present(
            locator,
            error_message="Cannot find element by locator" + locator,
            timeout_in_sec=10
        ).location['y']

        screen_size_by_y = self.driver.get_window_size()['height']
        return element_location_by_y < screen_size_by_y

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

    def swipe_up_to_find_element(self, locator_with_type, error_message, max_swipes):
        locator_strategy, locator = self.get_locator_by_string(locator_with_type)
        already_swiped = 0

        while not self.driver.find_elements(locator_strategy, locator):
            if already_swiped > max_swipes:
                self.wait_for_element_present(
                    locator=locator_with_type,
                    error_message="Cannot find element by swiping up. \n" + error_message,
                    timeout_in_sec=0)
                return

            self.swipe_up()
            already_swiped += 1

    def swipe_up_till_element_appears(self, locator, error_message, max_swipes):
        already_swiped = 0

        while not self.is_element_located_on_the_screen(locator):
            if already_swiped > max_swipes:
                assert self.is_element_located_on_the_screen(locator), error_message

            self.swipe_up()
            already_swiped += 1

    def swipe_element_to_left(self, locator, error_message):
        element = self.wait_for_element_present(
            locator,
            error_message,
            timeout_in_sec=15)

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

    def click_element_to_the_right_upper_corner(self, locator, error_message):
        element = self.wait_for_element_present(
            locator + "/..",
            error_message,
            timeout_in_sec=15)

        right_x = int(element.location['x'])
        upper_y = int(element.location['y'])
        lower_y = int(upper_y + element.size['height'])
        middle_y = int((upper_y + lower_y) / 2)
        width = int(element.size['width'])

        point_to_click_x = (right_x + width) - 3
        point_to_click_y = middle_y

        action = TouchAction(self.driver)
        action\
            .tap(x=point_to_click_x, y=point_to_click_y)\
            .perform()



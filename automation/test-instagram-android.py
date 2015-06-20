import os
import unittest
from appium import webdriver
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class InstagramTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Nexus 5'
        desired_caps['appPackage'] = 'com.instagram.android'
        desired_caps['appActivity'] = '.activity.MainTabActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_like_photo(self):
        like_button = self.driver.find_element_by_id("row_feed_button_like")
        like_button.click()
        assert like_button.is_enabled() == True

    def test_comment_on_photo(self):
        self.driver.find_element_by_id("row_feed_button_comment").click()
        comment_field = self.driver.find_element_by_class_name("android.widget.EditText")
        comment = "love!"
        comment_field.send_keys(comment)
        self.driver.find_element_by_id("layout_comment_thread_button_send").click()
        comments = self.driver.find_elements_by_id("row_comment_textview_comment")
        assert comment in comments[-1].text


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstagramTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

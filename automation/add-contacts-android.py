import os
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '079ca4dd00f33313'
        desired_caps['app'] = PATH(
            '../../../sample-code/apps/ContactManager/ContactManager.apk'
        )
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = '.ContactManager'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        add = self.driver.find_element_by_accessibility_id("Add Contact")
        add.click()

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Jackie Luo")
        textfields[1].send_keys("0000000000")
        self.driver.find_element_by_id("contactPhoneTypeSpinner").click()
        self.driver.find_element_by_name("Mobile").click()
        textfields[2].send_keys("jacqueline.luo@percolate.com")
        self.driver.find_element_by_id("contactEmailTypeSpinner").click()
        self.driver.find_element_by_name("Work").click()

        self.assertEqual('Jackie Luo', textfields[0].text)
        self.assertEqual('0000000000', textfields[1].text)
        self.assertEqual('jacqueline.luo@percolate.com', textfields[2].text)

        self.driver.find_element_by_accessibility_id("Save").click()
        alert = self.driver.switch_to_alert()
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
        self.driver.press_keycode(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

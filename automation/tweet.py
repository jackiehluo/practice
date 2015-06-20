from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://twitter.com")
assert "Twitter" in driver.title
driver.find_element_by_id("signin-email").send_keys("jackiehluo")
driver.find_element_by_id("signin-password").send_keys("REDACTED")
driver.find_element_by_name("remember_me").click()
driver.find_element_by_xpath("//input[@value='Log in']").click()
driver.find_element_by_id("tweet-box-home-timeline").send_keys("I'm a robot! Jackie's testing some code.")
driver.find_element_by_class_name("tweet-action").click()

driver.close()
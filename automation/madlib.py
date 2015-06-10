from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.glowwordbooks.com/blog/category/kids-online-mad-libs/")
assert "Mad Libs" in driver.title
driver.find_element_by_id("ml-2015-06-01-4-box").send_keys("cats")
driver.find_element_by_id("ml-2015-06-01-6-box").send_keys("funny")
driver.find_element_by_id("ml-2015-06-01-8-box").send_keys("Flawless")
driver.find_element_by_id("ml-2015-06-01-7-box").send_keys("Beyonce")
driver.find_element_by_id("ml-2015-06-01-5-box").send_keys("sad")
driver.find_element_by_id("ml-2015-06-01-9-box").send_keys("sleeping")
driver.find_element_by_id("ml-2015-06-01-2-box").send_keys("New York")
driver.find_element_by_id("ml-2015-06-01-3-box").send_keys("mangoes")
driver.find_element_by_id("ml-2015-06-01-10-box").send_keys("bikes")
driver.find_element_by_id("ml-2015-06-01-1-box").send_keys("Jackie")
driver.find_element_by_id("ml-2015-06-01-button").click()

print driver.find_element_by_id("ml-2015-06-01-result").text

driver.close()
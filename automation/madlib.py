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

correct_result = "Say 'Jackie,' the photographer said as the camera flashed! New York and I had gone to sushi to get our photos taken today. The first photo we really wanted was a picture of us dressed as cats pretending to be a sad. When we saw the proofs of it, I was a bit funny because it looked different than in my head. (I hadn't imagined so many Beyonce behind us.) However, the second photo was exactly what I wanted. We both looked like Flawless wearing sleeping and bikes--exactly what I had in mind!"
result = driver.find_element_by_id("ml-2015-06-01-result").text

try:
	assert correct_result in result
except AssertionError:
	print ":("
finally:
	driver.close()
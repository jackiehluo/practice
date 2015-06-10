from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("http://marcojakob.github.io/dart-dnd/basic/web/")
assert "Drag and Drop" in driver.title
source = driver.find_element_by_class_name("document")
target = driver.find_element_by_class_name("trash")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(source, target).perform()

driver.close()
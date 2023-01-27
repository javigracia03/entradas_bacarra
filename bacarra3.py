from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.support.select import Select

# create Safari driver instance
driver = WebDriver()
driver.get("http://www.example.com")

# locate the drop-down menu element
dropdown = driver.find_element_by_id("dropdown_id")

# create a Select object
select = Select(dropdown)

# select an option by its visible text
select.select_by_visible_text("Option 1")

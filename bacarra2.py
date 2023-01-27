from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create an instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open a new tab by simulating key press event of 'ctrl' and 't'
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])

# Navigate to a website on the new tab
driver.get("https://www.example.com")

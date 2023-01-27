from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)




# Visit the website
driver.get("https://lagranmanzana.com/evento/23008")

button_cookies = driver.find_element("class","btn.btn-lg.btn-outline-warning.gdpr-accept")
print(button_cookies)
button_cookies.click()


#select_number = Select(driver.find_elements_by_class_name("form-control.et-entrada-cantidad.text-center")[0])
#select_number.select_by_value('2')

# Open a new tab by executing JavaScript

# Switch to the new tab



# navigate to the website


# find the dropdown menu element
#dropdown_menu = driver.find_element_by_id('dropdown-menu')
#
## create a Select object for the dropdown menu
#select = Select(dropdown_menu)
#
## select the option by its value
#select.select_by_value('option-value')
#
## submit the form to take the selected option
#form = dropdown_menu.find_element_by_xpath("..")
#form.submit()
#
## close the webdriver
#driver.quit()

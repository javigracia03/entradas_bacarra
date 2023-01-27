from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def comprar_entrada():

    # create a new Firefox browser instance
    driver = webdriver.Firefox()

    # navigate to the website
    num_evento = "23008"
    url = "https://lagranmanzana.com/evento/" + num_evento
    driver.get(url)

    button_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-lg.btn-outline-warning.gdpr-accept")))

    # click the button
    button_cookies.click()

    #Select number of tickets


    id_frame = "etktfrm" + num_evento
    frame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id_frame))
    )

    driver.switch_to.frame(frame)

    #Select the first item of the avaliable tickets
    tickets_number_list = driver.find_elements(By.CLASS_NAME, "list-group-item.et-entrada.false")[0]
    #Select the number of tockets
    tickets_number = tickets_number_list.find_element(By.TAG_NAME, "select")

    select = Select(tickets_number)
    
    select.select_by_value("2")

    continuar_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-continuar")))
    #continuar_btn = driver.find_element(By.ID, "btn-continuar")
    print(continuar_btn.text)
    driver.execute_script("arguments[0].click();", continuar_btn)


comprar_entrada()
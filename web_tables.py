from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



url = ('https://demoqa.com/webtables')

browser = Firefox()
browser.maximize_window()
browser.get(url)


elemento = browser.find_element(By.CSS_SELECTOR, '[title $="e"]')
elemento.click()
    
browser.find_element(By.ID, 'delete-record-2').click()
browser.find_element(By.ID, 'delete-record-3').click()
browser.find_element(By.ID, 'addNewRecordButton').click()


def preenche_label(browser,first_name, last_name, email, age, salary, department):
    browser.find_element(By.ID, 'firstName').send_keys(first_name)
    browser.find_element(By.ID, 'lastName').send_keys(last_name)
    browser.find_element(By.ID, 'userEmail').send_keys(email)
    browser.find_element(By.ID, 'age').send_keys(age)
    browser.find_element(By.ID, 'salary').send_keys(salary)
    browser.find_element(By.ID, 'department').send_keys(department)
    browser.find_element(By.ID, 'submit').click()


dados = {
    'first_name':'Arlison',
    'last_name': 'Marreiro',
    'email': 'arlison.marreiro@gmail.com',
    'age':'22',
    'salary':'999999',
    'department':'##'
}

preenche_label(browser, **dados)







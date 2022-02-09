from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Definir a variavel 'browser' como o navegador firefox e acessar  o site solicitado
browser = Firefox()
browser.maximize_window()
browser.get('https://demoqa.com/text-box')

#Função que encontra os IDS das labels
def preencher_label(navegador, name, email, currentAddress, permanentAddress):
    browser.find_element(By.ID, 'userName').send_keys(name)
    browser.find_element(By.ID, 'userEmail').send_keys(email)
    browser.find_element(By.ID, 'currentAddress').send_keys(currentAddress)
    browser.find_element(By.ID, 'permanentAddress').send_keys(permanentAddress)
    browser.find_element(By.XPATH, '//*[@id="submit"]').click()


#Preencher as labels
preencher_label(browser,
                'Arlison Marreiro',
                'arlison.marreiro@gmail.com',
                'Rua das',
                'Rua do '
)

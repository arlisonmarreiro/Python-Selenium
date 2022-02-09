from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = ("https://selenium.dunossauro.live/aula_05_c.html")
browser = Firefox()
browser.get(url)

def melhor_filme(navegador, filme, email, telefone):
    browser.find_element(By.NAME, 'filme').send_keys(filme)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'enviar').click()

melhor_filme(browser,
            'alice',
            'arlison.marreiro@gmail.com',
            '(092)987654321'
)

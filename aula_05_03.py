from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads


url = ("https://selenium.dunossauro.live/aula_05.html")
browser = Firefox()
browser.get(url)


sleep(2)

def preenche_form(navegador, nome, email, senha, telefone):
    browser.find_element(By.XPATH, '//*[@id="nome"]').send_keys(nome)
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    browser.find_element(By.XPATH, '//*[@id="senha"]').send_keys(senha)
    browser.find_element(By.XPATH, '//*[@id="telefone"]').send_keys(telefone)
    browser.find_element(By.XPATH, '//*[@id="btn"]').click()

estrutura = {
    'nome':'Arlison',
    'email':'arlison.marreiro@gmail.com',
    'senha':'942927',
    'telefone':'987654321'
}
preenche_form(browser, **estrutura)

url_parseada = urlparse(browser.current_url)

sleep(2)

texto_resultado = browser.find_element(By.ID, 'result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_result = loads(resultado_arrumado)

assert dic_result == estrutura

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads

url = ('https://selenium.dunossauro.live/exercicio_04.html')
driver = Firefox()
driver.get(url)
driver.maximize_window()

sleep(2)

def preenche_label(browser, nome, email, senha, telefone):
    driver.find_element(By.XPATH, '//*[@id="nome"]').send_keys(nome)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="senha"]').send_keys(senha)
    driver.find_element(By.XPATH, '//*[@id="telefone"]').send_keys(telefone)
    driver.find_element(By.XPATH, '//*[@id="btn"]').click()

dados = {
    'nome':'Arlison',
    'email':'arlison.marreiro@gmail.com',
    'senha':'40028922',
    'telefone':'987654321'

}

preenche_label(driver, **dados)

url_parseada = urlparse(driver.current_url)

sleep(2)

texto_resultado = driver.find_element(By.XPATH, '/html/body/div/main/textarea').text

resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_result = loads(resultado_arrumado)

assert dic_result == dados

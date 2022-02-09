from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = ("https://selenium.dunossauro.live/aula_05_a.html")
browser = Firefox()
browser.get(url)
div_1 = browser.find_element(By.TAG_NAME , 'div')

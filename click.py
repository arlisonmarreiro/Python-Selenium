from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


browser = Firefox()
browser.get('file:///home/arlison/Python/display_grid.html')

botoes = browser.find_elements(By.CLASS_NAME ,'ui-state-default')

act = ActionChains(browser)

for botao in botoes:
    act.key_down(Keys.CONTROL).click(botao).perform()
    
    





    



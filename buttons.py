from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



url = "https://demoqa.com/buttons"
browser = Firefox()

browser.get(url)
act = ActionChains(browser)


btn_1 = browser.find_element(By.ID, "doubleClickBtn")
btn_2 = browser.find_element(By.ID, "rightClickBtn")
btn_3 = browser.find_element(By.XPATH, "//*[text()='Click Me']")


act.double_click(btn_1) and act.context_click(btn_2) and act.click(btn_3)
act.perform()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#Buat opsi untuk Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Inisialisasi driver
driver = webdriver.Chrome(options=chrome_options)

#Buka URL
driver.get("https://demoqa.com/menu")
driver.maximize_window()
driver.implicitly_wait(10)

#cara1
# menu = driver.find_element(By.LINK_TEXT, "Main Item 2")
# Hover = ActionChains(driver).move_to_element(menu)
# Hover.perform()

#cara2
ActionChains(driver).move_to_element((driver.find_element(By.LINK_TEXT, 'Main Item 2'))).perform()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Buat opsi untuk Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Inisialisasi driver
driver = webdriver.Chrome(options=chrome_options)
#driver2 = webdriver.Chrome()
#driver3= webdriver.Chrome()

#Buka URL
driver.get("https://the-internet.herokuapp.com/windows")
#driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
#driver.get("https://the-internet.herokuapp.com/login")
#driver2.get("https://www.facebook.com/")
#driver3.get("https://www.idejongkok.xyz/")

#Temukan elemen menggunakan By
#driver.find_element(By.ID, "username").send_keys("uno")
#driver.find_element(By.NAME, "username").send_keys("sasa")
#driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Elemental").click()
#driver.find_element(By.CLASS_NAME, "radius").click()
#time.sleep(3)
#driver.find_element(By.CSS_SELECTOR, "button.radius").click()
#driver.find_element(By.CSS_SELECTOR, "#login > button").click()
#driver.find_element(By.CSS_SELECTOR, "#content > div > button").click()

#menggunakan export XPATH
#driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

#cara pindah browser tab otomatis
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])

#Untuk menggunakan Tag Name
#h2 = driver.find_elements(By.TAG_NAME, "h2")
#print(h2)

#link = driver.find_elements(By.TAG_NAME, "a")
#print(len(link))
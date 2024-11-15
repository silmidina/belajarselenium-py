from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Buat opsi untuk Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Inisialisasi driver
driver = webdriver.Chrome(options=chrome_options)

#Buka URL
driver.get("https://demoqa.com/alerts")
time.sleep(3)

#Temukan elemen menggunakan By
#driver.find_element(By.ID, "alertButton").click()
#time.sleep(3)
#driver.switch_to.alert.accept()

driver.find_element(By.ID, "confirmButton").click()
time.sleep(3)
#confirm alert ok
#driver.switch_to.alert.accept()
#confirm alert close
driver.switch_to.alert.dismiss()

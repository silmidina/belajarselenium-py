from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#library yang di import menggunakan Explicitly Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

#Buat opsi untuk Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Inisialisasi driver
driver = webdriver.Chrome(options=chrome_options)

#Buka URL
driver.get("https://demoqa.com/alerts")

#Temukan elemen menggunakan By
driver.find_element(By.ID, "timerAlertButton").click()

try:
  WebDriverWait(driver,10).until(EC.alert_is_present())
  driver.switch_to.alert.accept()
  print("Alert di klik")

except TimeoutException:
  print("Alert tidak muncul")
  pass
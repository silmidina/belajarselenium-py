from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Buat opsi untuk Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Inisialisasi driver
driver = webdriver.Chrome(options=chrome_options)

#kalau menggunakan Charles Proxy
driver.implicitly_wait(10)

#Buka URL
driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")

#Temukan elemen menggunakan By
driver.find_element(By.ID, "login").click()
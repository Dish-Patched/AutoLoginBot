from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def bot(username, password, url):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "user")))

    user = driver.find_element(By.NAME, "user")
    user.clear()
    user.send_keys(username)

    passw = driver.find_element(By.NAME, "password")
    passw.clear()
    passw.send_keys(password)

    submit = driver.find_element(By.CLASS_NAME, "button-primary")
    submit.click()

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "dashboard")))

username = ""
password = ""

url = "https://open.kattis.com/login/email?"
bot(username, password, url)

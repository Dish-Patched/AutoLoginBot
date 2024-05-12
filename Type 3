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

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "email")))

    user = driver.find_element(By.NAME, "email")
    user.clear()
    user.send_keys(username)
    next = driver.find_element(By.ID, "continue")
    next.click()

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "password")))

    passw = driver.find_element(By.NAME, "password")
    passw.clear()
    passw.send_keys(password)
    submit = driver.find_element(By.ID, "signInSubmit")
    submit.click()

    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, "dashboard")))

username = "dishanta.sarma4@gmail.com"
password = "Hagupuku12"

url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

bot(username, password, url)

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

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "username")))

    user = driver.find_element(By.NAME, "username")
    user.clear()
    user.send_keys(username)
    next = driver.find_element(By.ID, "idp-discovery-submit")
    next.click()

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "password")))

    passw = driver.find_element(By.NAME, "password")
    passw.clear()
    passw.send_keys(password)
    submit = driver.find_element(By.ID, "okta-signin-submit")
    submit.click()

    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, "dashboard")))

username = ""
password = ""

url = "https://account.cengage.com/login?SAMLRequest=fZJdS8MwFIb%2FSsn9%2BrnsI6yV4RAGc8icIt6F9KwG25MuJ93cvzd2buiFQq7COc%2F78iSzm4%2BmDg5gSRvMWRLGLABUptRY5expezeYsJtiRrKp01bMO%2FeGG9h3QC6YE4F1fu3WIHUN2EewB63gabPK2ZtzLYkokn4jVICVrCBUpomITNTTotjIdMQnyQ5p%2FcLX1TzjYxYsPFqjdH2dK0Up06H7BapNpZEFd8Yq6HvlbCdrAhYsFznTZZLFw2GWTXkW%2B5AhT%2BJsPBnH0xH3E0QdLJGcRJezNE6Hg9if6TaZiiQVnId8wl9Z8Hzxkn558aaQxFlFzjqLwkjSJFA2QMIp8Ti%2FXwk%2FKlprnFGmZt%2FmRB9ofxL%2BB8iLW1ZcHByPx9C8O3m22Buks%2FCBjzvoEmxE7QHLBlCeTGurvSxPpZtFPytcn3LtM5eLB1NrdfqS2Ej3d6UkTPobXQ52%2FajokFpQeqehZFHxnfH7gxSf&RelayState=%252Foauth2%252Fv1%252Fauthorize%252Fredirect%253Fokta_key%253D3_af4Uj_ZDgzbhEpETBcCiZAReK4PjJlIDttmMw5dT4&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=MM272AGL%2Bqtjrn54nqOnPhOBqK9CpRWyFlDk4zhgX1bY7Yta9s7W2jir6xHpq%2FrY4kuJk5jJIJbhKjh9zwtk7BHRcKq0KJR2WO1JB6KfOe7LutivW%2Bpnc18BX4sBSMUXQHsdYY8UhCaykS45MksYElfsDeETAL%2FigaIJ7wwm0560Elgrv2lqhsid6ZmQgvQ6YQFM5IEbnRIzZHyHRu1nxn%2BzP0Hspbrn4anJ5Gm7XIh5U0gCcHaPYylcB%2F9iw5xz1riRbKX%2BeQwOVAfHPkioEWcPcFYwUUPIdPBSRptwAKs9VrT1BIGdW7Xy2SSeiXJzz9JmkksRFKX7%2BrcsZJ24Uw%3D%3D"

bot(username, password, url)

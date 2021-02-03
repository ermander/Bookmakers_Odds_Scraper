import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


options = Options()
options.headless = False
options.add_argument("--window-size=1500,800")

driver = webdriver.Chrome()

cookieAccettati = 0


quote = []
condition = True

while condition:
    driver.get("https://www.lopoca.it/scommesse-sportive")
    time.sleep(5) ####### cambiare
    if cookieAccettati == 0:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[7]/div[2]/div[3]/div[3]/div/div/button"))).click() #/html/body/form/div[7]/div[2]/div[3]/div[3]/div/div/button
        cookieAccettati = 1

    driver.click("/html/body/form/div[7]/div[2]/div[3]/div[3]/div/div/button")
    nomi = driver.find_elements_by_css_selector("a.ui-corner-all")
    for nome in nomi:
            print(nome.text)
    condition = False

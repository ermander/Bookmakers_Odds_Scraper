import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = False
options.add_argument("--window-size=1500,800")

driver = webdriver.Chrome()

cookieAccettati = False

valori = [1,3,5,7]
quote = []

while True:
    driver.get("https://www.betaland.it/sport/calcio/italia/serie-a-OIA-scommesse-sportive-online")
    time.sleep(1)
    if cookieAccettati == False:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/cloudflare-app/div/div[2]/button"))).click()
        cookieAccettati = True

    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/main/div/iframe'))

    partite = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/a')
    numero_partite = driver.find_elements_by_class_name("date-time-row")
    print(len(numero_partite))

    nextWhileIterations = 0

    while nextWhileIterations
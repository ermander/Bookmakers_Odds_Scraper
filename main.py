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

cookieAccettati = 0

valori = [1,3,5,7]

quote = []
match = {}

condition = True
while condition:
    driver.get("https://www.betaland.it/sport/calcio/italia/serie-a-OIA-scommesse-sportive-online")
    time.sleep(2)
    if cookieAccettati == 0:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/cloudflare-app/div/div[2]/button"))).click()
        cookieAccettati = 1

    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/main/div/iframe'))

    partite = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/a')

    for numero in valori:
        if numero == 1 or numero == 3:
            for x in range(1,4):
                quota = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/table/tbody/tr/td['+str(numero)+']/table/tbody/tr/td['+str(x)+']/a').text
                quote.append(quota)
        elif numero == 5 or numero == 7:
            for x in range(1,3):
                quota = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/table/tbody/tr/td['+str(numero)+']/table/tbody/tr/td['+str(x)+']/a').text
                quote.append(quota)

    # driver.switch_to.default_content()

    print(len(quote), quote)
    condition = False

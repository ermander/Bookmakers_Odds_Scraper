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


def bundesLiga():

    cookiesSetted = False
    condition = True

    while condition:
        driver.get("https://www.betaland.it/sport/calcio/germania/bundesliga-OIA-scommesse-sportive-online")
        time.sleep(0.5)

        #Setting the cookies
        if cookiesSetted == False:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/cloudflare-app/div/div[2]/button"))).click()
            cookiesSetted = True

        #Switching to iframe tag
        driver.switch_to.frame(driver.find_element_by_xpath('/html/body/main/div/iframe'))

        #Finding all odds (1,X,2,1X,12,X2,U2.5,02.5,GG,NG)
        odds = driver.find_elements_by_css_selector("a.prematch-fluid-giocabilita-s")
        for odd in odds:
            print(odd.text)

        #Finding all match names
        calendar = driver.find_elements_by_css_selector("a.match-description-a-tag")
        print(len(calendar))
        for x in calendar:
            print(x.text)

        # driver.switch_to.default_content()
        condition = False

    driver.quit()


bundesLiga()
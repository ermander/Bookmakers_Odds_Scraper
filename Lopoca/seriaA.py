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

        #nomi
        nomi = driver.find_elements_by_css_selector("span.eventName")
        squadre = []
        for nome in nomi:
            nomiL.append(nome.text)

        #partite = [nomiL[i:i+2] for i in range(0, len(nomiL), 2)]
        #Lopoca_serieA["Squadre"] = nomiL



        #odds
        oddsPagina = driver.find_elements_by_css_selector("span.mg-quota-prematch")
        oddsL = []
        for odd in oddsPagina:
            oddsL.append(odd.text)
        oddsList = []
        for item in oddsL:
            try:
                oddsList.append(float(item))
            except ValueError:  # bare exception statements are bad practice too!
                pass
        od1 = [oddsList[i:i+10] for i in range(0, len(oddsList), 10)]
        Lopoca_serieA = pd.DataFrame(od1, columns=["1","X","2","1X","12","X2","U2.5","O2.5","GG","NG"], index=squadre)
        print(Lopoca_serieA)

        #nomi



        #Lopoca_serieA = pd.DataFrame([oddsList])
        #Lopoca_serieA.columns =["1","X","2","1X","12","X2","U2.5","O2.5","GG","NG"]
        condition = False

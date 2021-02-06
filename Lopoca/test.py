import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui as pa
from utils import cercaschermoX5, cercaschermoXquantovuoi

#logo_coppaItalia =
i = 0
box = 0, 0, 600, 2055

condition = True
cookieAccettati = False
driver = webdriver.Chrome()
shortname = "B"
#driver.maximize_window()

while condition:
    driver.maximize_window()
    driver.get("https://www.lopoca.it/scommesse-sportive")
    time.sleep(2) ####### cambiare

    """if cookieAccettati == False:         """"""Non funziona con i cookie non trova il pulsante shortname""""""""
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[7]/div[2]/div[3]/div[3]/div/div/button"))).click() #/html/body/form/div[7]/div[2]/div[3]/div[3]/div/div/button
            cookieAccettati = True
        except:
            cookieAccettati = False
            pass"""



    oddsSn = driver.find_element_by_xpath(f"//li[@data-shortname='{shortname}']")
    oddsSn.click()
    time.sleep(2)


    """pa.moveTo(1950,1100)
    pa.scroll(2000)
    #logo_coppaItalia = None
    #i = 0
    b = "calcio"
    #5 tentativi per trovare il logo
    serieA_box =  cercaschermoX5("SERIEA-primopiano.png",box)
    if serieA_box == None:
        serieA_box =  cercaschermoXquantovuoi(f"serieA-calcio.png",box, 1)
        pa.scroll(2000)
        if serieA_box == None:
                calcio_box = cercaschermoXquantovuoi(f"calcio2.png",box,3)
                if calcio_box == None:
                 raise ValueError(f"calcio.png non trovata")
                else:
                    calcio_center = pa.center(calcio_box)
                    pa.click(calcio_center)
                    time.sleep(1)
                    serieA_box =  cercaschermoX5("SERIEA-primopiano.png",box)
                    if serieA_box == None:
                        serieA_box =  cercaschermoX5("serieA-calcio.png",box)
                        if serieA_box == None:
                            raise ValueError("serieA.png non trovata")


    serieA_center = pa.center(serieA_box)
    pa.click(serieA_center)
    time.sleep(1)
"""

    nomi = driver.find_elements_by_css_selector("span.eventName")
    squadre = []
    for nome in nomi:
        squadre.append(nome.text)

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







"""    while logo_coppaItalia == None:
        logo_coppaItalia = pa.locateOnScreen("coppa_italia.png", region=(0,0, 600, 1900))
        driver.execute_script("window.scrollTo(0,5)")
        i = i + 1
        print("sto cercando logo_coppaItalia, tentativo n:", i, "di 5")
        if i == 5:
            break

    if logo_coppaItalia == None:
        logo_calcio = None
        j = 0
        while logo_calcio == None:
            logo_calcio = pa.locateOnScreen("calcio.png", region=(0,0, 600, 1900))
            driver.execute_script("window.scrollTo(0,5)")
            j = j + 1
            print("sto cercando logo_calcio, tentativo n:", j, "di 5")
            if j == 5:
                break"""







"""    tab_id = driver.current_window_handle
    f = open("tab_id.txt", "w")
    f.write(tab_id)
    f.close()

    tendine = driver.find_elements_by_css_selector("button.search-odds")
    for tendina in tendine:
        driver.execute_script("window.scrollTo(0,100)")
        tendina.click()
        time.wait(3)
        oddspartite = driver.find_elements_by_css_selector("a.ui-corner-all")
        for odd in oddspartite:
            print(odd.text)"""

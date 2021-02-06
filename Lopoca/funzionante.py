import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui as pa
from utils import cercaschermoX5, cercaschermoXquantovuoi
from selenium.webdriver.common.keys import Keys



class Lopoca:

    def __init__(self): #sn può essere anche array
        self.shortnames =  ['A','B','Bun','BND2','L1','L2','Ps','LC','LIG','SPASD','ED','GGV','PORSL','PORD2']
        self.CList = ["1","X","2","1X","12","X2","U2.5","O2.5","GG","NG","squadre"]
        self.switch = False
        self.cookieAccettati = False
        self.DF = pd.DataFrame(data=None, columns=self.CList )
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()     #DF = pd.DataFrame(columns=DF.columns)
        self.driver.get("https://www.lopoca.it/scommesse-sportive")
        time.sleep(4)
        while self.switch == False:
            self.firstTime()
            for sn in self.shortnames:
                time.sleep(1)
                self.openSN(sn)
                a = self.odds()
                self.chiudi()
                print(a)
            self.switch = True


    def firstTime(self):
        """nazioni = ["category-1","eventi-nazione-221","eventi-nazione-218","eventi-nazione-235","eventi-nazione-217","eventi-nazione-225","eventi-nazione-228","eventi-nazione-209"]# logo calcio, ing, ger,spa,fra,ola,port, belg
        for n in nazioni:
            a = self.driver.find_elements_by_xpath(f"//div[@id='{n}']")
            for i in a:
                try:
                    i.click()
                    break                                                   "Non so perchè non worki ma non worka così"
                except:
                    pass
            time.sleep(1)"""

        calcio = self.driver.find_element_by_xpath("//div[@id='category-1']")
        calcio.click()
        time.sleep(1)

        Eng = self.driver.find_element_by_xpath("//li[@id='eventi-nazione-221']") #inghilterra
        Eng.click()
        time.sleep(1)

        Ger = self.driver.find_element_by_xpath("//li[@id='eventi-nazione-218']") #germania
        Ger.click()
        time.sleep(1)

        Esp = self.driver.find_element_by_xpath("//li[@id='eventi-nazione-235']") #spagna
        Esp.click()
        time.sleep(1)

        Fra = self.driver.find_element_by_xpath("//li[@id='eventi-nazione-217']")
        Fra.click()
        time.sleep(1)

        Ola = self.driver.find_element_by_xpath("//li[@id='eventi-nazione-225']") #olanda
        Ola.click()
        time.sleep(1)

        Port = self.driver.find_element_by_xpath("//li[@id='eventi-nazione-228']")
        Port.click()
        time.sleep(1)

        Bel = self.driver.find_element_by_xpath("//li[@id='eventi-nazione-209']") #inghilterra
        Bel.click()
        time.sleep(1)                                                                                                                                                                                                                                                                                                                             #DF.set_index('squadre', inplace=True, drop=True)self.DF.set_index('squadre')

    def chiudi(self):
        chiudi = self.driver.find_elements_by_xpath("//span[@title='Chiudi']")
        for i in chiudi:
            try:
                i.click()
            except:
                pass
        time.sleep(2)



    def openSN(self, sn):
        logoSN = self.driver.find_elements_by_xpath(f"//li[@data-shortname='{sn}']")
        for i in logoSN:
            try:
                i.click()
                break
            except:
                pass
        time.sleep(2)


    def odds(self):
        #nomi
        driver = self.driver
        nomi = self.driver.find_elements_by_css_selector("span.eventName")
        squadre = []
        for nome in nomi:
            squadre.append(nome.text)

        #odds
        oddsPagina = self.driver.find_elements_by_css_selector("span.mg-quota-prematch")
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
        LopocaDF = pd.DataFrame(od1, columns=["1","X","2","1X","12","X2","U2.5","O2.5","GG","NG"])
        LopocaDF["squadre"] = squadre
        self.DF = pd.DataFrame(columns=self.DF.columns)
        self.DF = pd.concat([self.DF, LopocaDF])
        self.DF.set_index('squadre', inplace=True, drop=True)
        return self.DF



Lopoca = Lopoca()

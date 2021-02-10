import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class serie:

    def __init__(self, driver, N):
        self.driver = driver
        self.nat = ""
        self.lega = ""
        self.daiNomi(N)
        self.cookieAccettati = False
        self.calcioAperto = False
        self.natAperta = False
        self.legaAperta = False
        self.aperti = [self.calcioAperto, self.natAperta, self.legaAperta ]
        self.calcioObj = self.driver.find_element_by_xpath("//div[@id='category-1']")
        self.natObj = self.driver.find_element_by_xpath(f"//li[@id='eventi-nazione-{self.nat}']")
        self.legaObj = self.legaObj = self.driver.find_element_by_xpath(f"//li[@data-shortname='{self.lega}']")
        self.CList = ["1","X","2","1X","12","X2","U2.5","O2.5","GG","NG","squadre"]
        self.DF = pd.DataFrame(data=None, columns=self.CList )


    def daiNomi(self,N):
        nats = ["222","222","218","218","217","217","221","221","235","235","225","225","228","228"]
        leghe =  ['A','B','Bun','BND2','L1','L2','Ps','LC','LIG','SPASD','ED','GGV','PORSL','PORD2']
        self.nat = nats[N]
        self.lega = leghe[N]


    def scorrigiu(self):
        self.driver.execute_script("window.scrollTo(0, -100)")


    def scorrisu(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")


    def cerca(self, elemento, aperto):
        giro = 0
        self.scorrisu()
        time.sleep(1)
        trovato = False

        while giro < 6 and trovato == False: #giro = da sopra a sotto
            try:
                elemento.click()
                trovato = True
                time.sleep(2)
                self.aperti[aperto] == True
            except:
                self.scorrigiu()
                time.sleep(1)
                giro = giro + 1


    def openCalcio(self):
        if self.calcioAperto == False:
            giro = 0
            while giro < 6 and self.calcioAperto == False:
                try :
                    self.scorrigiu()
                    time.sleep(1)
                    self.calcioObj.click()
                    time.sleep(2)
                    self.calcioAperto = True
                except:
                    pass
                    self.cerca(self.calcioObj, 0)
                    giro = giro + 1
            if giro == 3 :
                print( "calcio non trovato, aka problemone ")
        else:
            pass


    def openNat(self):
        if self.natAperta == False:
            giro = 0
            while giro < 3 and self.natAperta == False:
                try :
                    self.scorrigiu()
                    time.sleep(1)
                    self.natObj.click()
                    time.sleep(2)
                    self.natAperta = True
                except:
                    pass
                    self.cerca(self.natObj, 1)
                    giro = giro + 1
            if giro == 3 :
                print("nazione: ", self.nat, " non trovata ")
                self.natAperta = False
                self.calcioAperto = False
                self.openCalcio()
        else:
            pass


    def openLega(self):
        if self.legaAperta == False:
            if self.natAperta == True:
                self.chiudi()
                giro = 0
                while giro < 3 and self.legaAperta == False:
                    try :
                        self.scorrigiu()
                        time.sleep(1)
                        self.legaObj.click()
                        time.sleep(2)
                        self.legaAperta = True
                    except:
                        pass
                        self.cerca(self.legaObj, 1)
                        giro = giro + 1
                if giro == 3 :
                    print("lega: ", self.lega, " non trovata ")
                    self.legaAperta = False
                    self.natAperta == False
                    self.openNat()
            else:
                self.openNat()
        else:
            pass


    def chiudi(self):
        chiudis = self.driver.find_elements_by_xpath("//span[@title='Chiudi']")
        for i in chiudis:
            try:
                i.click()
                time.sleep(4)
            except:
                pass
        self.natAperta = True
        self.legaAperta = False


    def odds(self):
        if self.legaAperta == True:
            print("sto cercando:",self.lega)
            nomi = self.driver.find_elements_by_css_selector("span.eventName")
            squadre = []
            for nome in nomi:
                squadre.append(nome.text)
            oddsPagina = self.driver.find_elements_by_css_selector("span.mg-quota-prematch")
            oddsL = []
            for odd in oddsPagina:
                oddsL.append(odd.text)
            oddsList = []
            for item in oddsL:
                try:
                    oddsList.append(float(item))
                except ValueError:
                    pass
            od1 = [oddsList[i:i+10] for i in range(0, len(oddsList), 10)]
            print(od1)
            LopocaDF = pd.DataFrame(od1, columns=["1","X","2","1X","12","X2","U2.5","O2.5","GG","NG"])
            LopocaDF["squadre"] = squadre
            self.DF = pd.DataFrame(columns=self.DF.columns)
            self.DF = pd.concat([self.DF, LopocaDF])
            self.DF.set_index('squadre', inplace=True, drop=True)
            abc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.mg-quota-prematch")))
            self.chiudi()
            return self.DF

def Lopoca():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lopoca.it/scommesse-sportive")
    time.sleep(4)
    leghe =  ['A','B','Bun','BND2','L1','L2','Ps','LC','LIG','SPASD','ED','GGV','PORSL','PORD2']
    DFs = []
    i = 0
    calcioApe = False
    for l in leghe:
        l = serie(driver, i)
        calcioApe = l.calcioAperto
        if calcioApe == False:
            l.openCalcio()
        l.openNat()
        l.openLega()
        a = l.odds()
        print(a)
        DFs.append(a)
        i = + 1
    print(DFs)

Lopoca()

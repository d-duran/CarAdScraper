from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxProfile
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd

Foptions = webdriver.FirefoxOptions()
Foptions.add_argument("--private")
Foptions.add_argument("--disable-blink-features=AutomationControlled")
Foptions.add_argument("--headless")

profile = FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0")
driver = Firefox(executable_path='D:/Users/pablo/OneDrive/Escritorio/PRAC1 CICLO/geckodriver.exe', firefox_profile=profile, options=Foptions)
driver.set_window_size(1920,950)

driver.get('https://www.coches.com/')
#aceptar cookie
time.sleep(3)
driver.find_element_by_id("onetrust-accept-btn-handler").click()
time.sleep(4)
action = ActionChains(driver)
segundaMano=driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[4]/a')
# action.move_to_element_with_offset(segundaMano, -7, -9).perform()
action.move_to_element(segundaMano).perform()

time.sleep(2)
segundaMano_sub=driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[4]/ul/li[1]/a')
action.click(segundaMano_sub).perform()
driver.implicitly_wait(5)
time.sleep(4)

driver.find_element_by_id('search3').send_keys('Volkswagen')

time.sleep(5.2)
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/center/div[2]/form/button").click()

datosCSV=[]
final=False
#recorremos 
while (not final and len(datosCSV)<250):
    time.sleep(7.4)
    for car in driver.find_elements_by_xpath("//div[contains(@class, 'pill car')]"):
        id_coches=car.get_attribute("data-sel")
        info_coches=car.text
        info_coches=info_coches.split(sep='\n')
        #print(len(info_coches))
        if len(info_coches)==8:
            datosCSV.append([id_coches, " ".join(info_coches[4].split(" ")[0:-3]),
                             info_coches[3],
                             info_coches[4].split(" ")[-3],
                             info_coches[4].split(" ")[-2],
                             int(info_coches[-3].split(" ")[0].replace(".","")),
                             info_coches[-2],
                             int(info_coches[-1]),
                             "KM0"])
        elif len(info_coches)==7:
            datosCSV.append([id_coches, " ".join(info_coches[3].split(" ")[0:-3]),
                             info_coches[2],
                             info_coches[3].split(" ")[-3],
                             info_coches[3].split(" ")[-2],
                             int(info_coches[-3].split(" ")[0].replace(".","")),
                             info_coches[-2],
                             int(info_coches[-1]),
                             None])
        else:
            datosCSV.append(None)
    try:    
        driver.find_element_by_xpath("/html/body/div[4]/div[8]/ul/li[13]/a").click()
    except:
        final=True
    
        
driver.close()        

datosCSV=pd.DataFrame(datosCSV, columns=["idAnuncio","Modelo","Precio","Combustible","Potencia","kms","ciudad","antiguedad","KM0"])

datosCSV.to_csv("Coches.csv", index=False)

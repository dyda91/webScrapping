from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())

chrome = webdriver.Chrome(service=servico)

import pandas as pd

options = Options()
options.headless = False

arquivo = "informes.xlsx"

df = pd.read_excel(arquivo)
url_email = "https://outlook.live.com/owa/"



for index, row in df.iterrows():
    options = Options()
    options.headless = False

    chrome.get(url_email)
    time.sleep(3)

    chrome.find_element(By.XPATH, '/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
    time.sleep(2)

    chrome.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys('edjalmasalmeida@outlook.com')
    time.sleep(1)

    chrome.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input').click()
    time.sleep(2)

    chrome.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys('dida1991')
    time.sleep(1)

    chrome.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').click()
    time.sleep(2)

    chrome.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input').click()
    time.sleep(4)


    chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/span/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/span/button[1]/span/span[1]/span').click()
    time.sleep(1)

    chrome.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[1]/div[1]/div/div[3]/div/div/div[1]').send_keys(row["EMAIL"])
    time.sleep(2)

    chrome.find_element(By.XPATH, '//*[@id="editorParent_1"]/div').send_keys(row["TEXTO"])
    time.sleep(1)

    chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/input').send_keys(row["ASSUNTO"])
    time.sleep(1)

    chrome.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[3]/div[1]/div/div/span/button[1]').click()
    time.sleep(10)

    
    chrome.quit()
    


    

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup


options = Options()
options.headless = True

navegador = webdriver.Chrome(options=options)

link = "https://ge.globo.com/futebol/brasileirao-serie-a/"

navegador.get(url=link)
sleep(2)


tabela = navegador.find_element(by=By.CLASS_NAME,value=("tabela__pontos"))
sleep(1)

htmlContent = tabela.get_attribute('outerHTML')

soup = BeautifulSoup(htmlContent, "html.parser")

ticket = soup.find(name='table')

df = pd.read_html(str(ticket))[0]

df.to_excel('pontos.xlsx')

navegador.quit()

print(soup)
while(True):
    pass

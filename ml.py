import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep


base_url = "https://lista.mercadolivre.com.br/"

Todos_os_produtos = []

produto_name = input('qual produto você deseja? ')

response = requests.get(base_url + produto_name)

site = BeautifulSoup(response.text, 'html.parser')



produtos = site.findAll('div', attrs={'class', 'ui-search-result__wrapper shops__result-wrapper'})

# print(produtos)

for produto in produtos:
    titulo = produto.find('h2', attrs={'class', 'ui-search-item__title'})

    link = produto.find('a')

    preco_symbol = produto.find('span', attrs={'class', 'price-tag-symbol'})

    preco_real = produto.find('span', attrs={'class', 'price-tag-fraction'})

    preco_centavos = produto.find('span', attrs={'class', 'price-tag-cents'})

    if(preco_centavos):
        preco = preco_symbol.text + ' ' + preco_real.text + ',' + preco_centavos.text

    else:
        preco = preco_symbol.text + ' ' + preco_real.text

    # print('Titulo do produto ' ,  titulo.text)
    # print('Link do produto ' ,  link['href'])
    # print('Preço do produto ' , preco)
    

    # print('\n\n')   

    Todos_os_produtos.append([titulo.text, preco, link['href']])

    lista_produtos = pd.DataFrame(Todos_os_produtos, columns=['Titulo', 'Preço', 'Link'])


    lista_produtos.to_excel('produtos.xlsx')



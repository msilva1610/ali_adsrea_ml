from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import io
import json
from datetime import datetime
import re

import time
import logging


urls_categorias1 = [
    {
    "url":"https://pt.aliexpress.com/category/201001900/women's-clothing.html",
    "cat":"moda feminina"
    },
    {
    "url":"https://pt.aliexpress.com/category/201001892/men's-clothing.html",
    "cat":"moda masculina",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000054/cellphones-&-telecommunications.html",
    "cat":"telefonia e comunicação",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000006/computer-&-office.html",
    "cat":"Computador e Escritório",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000011/education-&-office-supplies.html",
    "cat":"Material escolar e de escritório",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000014/security-&-protection.html",
    "cat":"Segurança e Proteção",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000020/consumer-electronics.html",
    "cat":"Eletrônicos",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000220/watches.html",
    "cat":"Relógios",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000219/jewelry-&-accessories.html",
    "cat":"Joias e Acessórios",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000008/home-&-garden.html",
    "cat":"Casa e Jardim",
    },
    {
    "url":"https://pt.aliexpress.com/category/201002447/pet-products.html",
    "cat":"Pets e Animais",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000005/home-appliances.html",
    "cat":"Eletrodomésticos",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000224/luggage-&-bags.html",
    "cat":"Bolsas e Malas",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000037/shoes.html",
    "cat":"Calçados",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000013/toys-&-hobbies.html",
    "cat":"Brinquedos e hobbies",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000215/mother-&-kids.html",
    "cat":"Mamãe e Bebê",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000010/sports-&-entertainment.html",
    "cat":"Esporte e Lazer",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000021/beauty-&-health.html",
    "cat":"Beleza e saúde",
    },
    {
    "url":"https://pt.aliexpress.com/category/201004457/hair-extensions-&-wigs.html",
    "cat":"Apliques e perucas",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000015/automobiles-&-motorcycles.html",
    "cat":"Automóveis e motos",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000186/tools.html",
    "cat":"Ferramenta",
    },
    {
    "url":"https://pt.aliexpress.com/category/201000007/home-improvement.html",
    "cat":"Renovação da Casa",
    }
]


urls_categorias = [
    {
    "url":"https://pt.aliexpress.com/category/201001892/men's-clothing.html?g=y",
    "cat":"moda masculina"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000054/cellphones-&-telecommunications.html?g=y",
    "cat":"telefonia e comunicação"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000006/computer-&-office.html?g=y",
    "cat":"Computador e Escritório"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000011/education-&-office-supplies.html?g=y",
    "cat":"Material escolar e de escritório"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000014/security-&-protection.html?g=y",
    "cat":"Segurança e Proteção"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000020/consumer-electronics.html?g=y",
    "cat":"Eletrônicos"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000220/watches.html?g=y",
    "cat":"Relógios"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000219/jewelry-&-accessories.html?g=y",
    "cat":"Joias e Acessórios"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000008/home-&-garden.html?g=y",
    "cat":"Casa e Jardim"
    },
    {
    "url":"https://pt.aliexpress.com/category/201002447/pet-products.html?g=y",
    "cat":"Pets e Animais"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000005/home-appliances.html?g=y",
    "cat":"Eletrodomésticos"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000224/luggage-&-bags.html?g=y",
    "cat":"Bolsas e Malas"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000037/shoes.html?g=y",
    "cat":"Calçados"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000013/toys-&-hobbies.html?g=y",
    "cat":"Brinquedos e hobbies"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000215/mother-&-kids.html?g=y",
    "cat":"Mamãe e Bebê"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000010/sports-&-entertainment.html?g=y",
    "cat":"Esporte e Lazer"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000021/beauty-&-health.html?g=y",
    "cat":"Beleza e saúde"
    },
    {
    "url":"https://pt.aliexpress.com/category/201004457/hair-extensions-&-wigs.html?g=y",
    "cat":"Apliques e perucas"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000015/automobiles-&-motorcycles.html?g=y",
    "cat":"Automóveis e motos"
    },
    {
    "url":"https://pt.aliexpress.com/category/201000007/home-improvement.html?g=y",
    "cat":"Renovação da Casa"
    }
]


logging.basicConfig(filename='./logs/aliexpressv2.log',level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')


options = Options()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# url = 'https://pt.aliexpress.com/category/201000021/beauty-&-health.html?g=y'
# url = 'https://pt.aliexpress.com/category/201000021/beauty-&-health.html?CatId=201000021&g=y&isCategoryBrowse=true&isrefine=y&page=54&trafficChannel=main'

delay = 15
categoria = ''
paginas = 100

def ler_categoria(url):
    cat = ''
    try:
        #ler categoria na url
        logging.info('lendo categoria...')
        cat = parse_qs(url)['catName'][0]
        return cat.strip()
    except Exception as e:
        logging.error(e)
        return cat


def ler_num_paginas(driver):
    paginas = 0
    page = driver.find_elements(By.CLASS_NAME, 'total-page')
    soup = BeautifulSoup(page[0].get_attribute("innerHTML"), "html.parser")
    try:
        logging.info(soup)
        # _paginas = soup.find_all(class_='total-page')
        # logging.info(_paginas)
        # _paginas = re.findall(r'\d+',_paginas[0])
        _paginas = re.findall(r'\d+',str(soup))
        paginas = int(_paginas[0])
        return paginas
    except Exception as e:
        logging.error(e)


def ler_url_produto_id(produto):
    # https://pt.aliexpress.com/item/1005005093482472.html
    produto_id = 0
    try:
        logging.info(produto)
        _url = produto.get('href')
        logging.info(_url) 
        _produto_id = re.findall(r'\d+',_url)[0]
        produto_id = _produto_id
        return int(produto_id)
    except Exception as e:
        logging.error(e)
        return produto_id


def ler_url_produto(produto):
    url_produto = ''
    try:
        _url = produto.a['href']
        logging.info(_url)
        _parsed_url = urlparse(_url)
        _url_produto = f'{_parsed_url.netloc}{_parsed_url.path}'
        url_produto = _url_produto
        return url_produto
    except Exception as e:
        logging.error(e)
        return url_produto


def ler_nomeloja(produto):
    loja = ''
    _loja = ''
    try:
        _nomeloja = produto.find_all(class_='cards--store--A2ezoRc')
        logging.info(_nomeloja)
        _loja = _nomeloja[0].get_text()
        loja = _loja.strip()
        return loja
    except Exception as e:
        logging.error(f'{e} - nome loja: {_nomeloja}')
        print(f'Ocorreu um erro em ler_nomeloja: {e}')


def ler_loja(produto):
    loja = ''
    try:
        _loja = produto.find_all(class_='cards--store--A2ezoRc')
        logging.info(_loja)
        _loja = _loja[0].find_all(class_='cards--storeLink--1_xx4cD')
        _loja = _loja[0].get('href')
        loja = _loja
        return loja
    except Exception as e:
        logging.error(f'{e} - loja: {_loja}')
        print(f'Ocorreu um erro em ler_loja: {e}')


def ler_vendidos(produto):
    vendidos = 0
    try:
        _vendidos = produto.find_all(class_='manhattan--tradeContainer--33O19sx')
        logging.info(_vendidos)
        if len(_vendidos) > 0:
            _vendidos = _vendidos[0].find_all(class_='manhattan--trade--2PeJIEB')[0].get_text()
            _vendidos = re.findall(r'\d+',_vendidos)[0]
            vendidos = int(_vendidos)
        return int(vendidos)
    except Exception as e:
        logging.error(f'{e} - vendidos: {_vendidos}')
        print(f'Ocorreu um exception em ler_vendidos. Error: {e}')
        return vendidos


def ler_preco(produto):
    preco = 0
    try:
        _preco = produto.find_all(class_='manhattan--price-sale--1CCSZfK')
        logging.info(_preco)
        if len(_preco) > 0:
            preco_produto = _preco[0].get_text()
            preco_produto = re.findall(r'\d+[,]?\d+?\d?',preco_produto )[0]
            return float(preco_produto.replace(',','.'),)
    except Exception as e:
        logging.error(f'{e} - preco: {_preco}')
        print(f'Ocorreu um exception em ler_preco. Error: {e}')
        return preco


def ler_titulo(produto):
    titulo = ''
    try:
        _titulo = produto.find_all(class_='manhattan--titleText--WccSjUS')
        logging.info(_titulo)
        if len(_titulo) > 0:
            _titulo = _titulo[0].get_text()
            titulo = _titulo
            return titulo
    except Exception as e:
        logging.error(f'{e} - titulo: {_titulo}')
        print(f'Ocorreu um exception em ler_titulo. Error: {e}')
        return titulo


def lercards(soup, categoria):
    _obj = []
    obj_produto = {}
    produtos = soup.find_all(class_='manhattan--container--1lP57Ag cards--gallery--2o6yJVt')
    print(f'Total de produtos encontrados: {len(produtos)}')
    logging.info(f'Total de produtos encontrados: {len(produtos)}.')
    if len(produtos) < 60:
        logging.warning(f'Total de produtos, {len(produtos)}, na página menor que 60')
    if len(produtos) > 0:
        logging.info(f'Iniciando o loop para um total de: {len(produtos)} produtos.')
        for produto in produtos:
            logging.info(produto)
            obj_produto = {}
            obj_produto['titulo'] = ler_titulo(produto)
            obj_produto['preco'] = ler_preco(produto)
            obj_produto['vendidos'] = ler_vendidos(produto)
            obj_produto['loja'] = ler_loja(produto)
            obj_produto['nomeloja'] = ler_nomeloja(produto)
            obj_produto['produto_id'] = ler_url_produto_id(produto)
            obj_produto['categoria'] = categoria
            obj_produto['DataPesquisa'] = str(datetime.now())

            _obj.append(obj_produto)
    return _obj


def pagereadyv1(driver):
    r = False
    try:

        logging.info('Executando scroll ...')
        print('Executando scroll da página')
        y = 350
        for timer in range(0,delay):
            driver.execute_script(f"window.scrollTo(0,{y})")
            y += 350
            time.sleep(1)

        wait = WebDriverWait(driver, delay, poll_frequency=3, ignored_exceptions=(TimeoutException, NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException))
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pagination--paginationList--2qhuJId')))
        logging.info('Page is ready!')
        print (f"Page is ready!") 
        r = True
        return r
    except Exception as e:
        print (f"Page not is ready! Erro:  {e}") 
        logging.error(f'Página não respondeu! Erro: {e}')
        return r


def seNaoForFim(driver):
    try:
        page = driver.find_elements(By.CLASS_NAME, 'zeroResult--tipContainer--37WGfY4')
        if len(page) > 0:
            logging.info('Pagina final encontrada!')
            return False
        else:
            return True
    except Exception as e:
        logging.error(f'Ocorreu uma exceção: {e}')


def main():
    url = ''

    for url_categoria in urls_categorias:
        url = url_categoria['url']
        categoria = url_categoria['cat']

        cards_de_produtos = []
        obj_produtos = []
        # Sair do loop apenas quando a categoria é lida até o final
        for p in range(1, paginas+1):
            p_url = f'{url}&page={p}'
            driver.get(p_url)
            # driver.refresh()
            if seNaoForFim(driver):
                if pagereadyv1(driver):
                    logging.info(f'Lendo categoria: {categoria} - página: {p}')
                    print(f'Lendo categoria {categoria} página: {p}')
                    page = driver.find_elements(By.CLASS_NAME, 'list--gallery--34TropR')
                    soup = BeautifulSoup(page[0].get_attribute("innerHTML"), "html.parser")
                        
                    # Encontra todos os cards da página
                    cards_de_produtos = lercards(soup, categoria)
                    for produto in cards_de_produtos:
                        obj_produtos.append(produto)
                  
            else:
                print(f'Página não ficou pronta!!!')
                logging.warning(f'Pagina não ficou pronta! Categoria: {categoria} - Página: {p}')
                break
        # Grava um arquivo para cada URL em URLs
        logging.info(f'gravando arquivo! Categoria: {categoria} - Página: {p}')
        arquivo = f"./json/aliexpress/v2/{categoria}.json"

        with io.open(arquivo, 'w', encoding='utf8', errors='ignore') as outfile:  
            json.dump(obj_produtos, outfile, ensure_ascii=False)

    driver.quit()

if __name__ =='__main__':
    main()

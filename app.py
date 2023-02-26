from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random
from time import sleep
import schedule


def buscar_precos():
    # 0 - Abrir o navegador
    print('passei aqui')
    driver = webdriver.Chrome(
        executable_path=os.getcwd() + os.sep + 'chromedriver.exe')
    print('definido chromedriver')
    # 1 - Naveguei até o site(url)
    driver.get('https://www.mercadolivre.com.br')
    # 2 - Pesquisar por produto
    sleep(random.randint(3, 5))
    campo_pesquisa = driver.find_element_by_xpath(
        "//input[@class='nav-search-input']")
    sleep(random.randint(3, 5))
    campo_pesquisa.click()
    sleep(random.randint(3, 5))
    nome_produto = input('Digite o nome do produto que deseja buscar!')
    campo_pesquisa.send_keys(nome_produto)
    sleep(random.randint(3, 5))
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(random.randint(3, 5))
    while True:
        # 4 - Extrair o titulo e preço
        try:
            sleep(random.randint(3, 5))
            titulos = driver.find_elements_by_xpath(
                "//h2[@class='ui-search-item__title ui-search-item__group__element']")
        except:
            print('Não estamos no formato thumbnail')
        try:
            sleep(random.randint(3, 5))
            titulos = driver.find_element_by_xpath(
                "//h2[@class='ui-search-item__title']")
        except:
            print('Não estamos no format listagem')
        sleep(random.randint(3, 5))
        precos = driver.find_elements_by_xpath(
            "//div[@class='ui-search-price ui-search-price--size-medium ui-search-item__group__element']//div[@class='ui-search-price__second-line']//span[@class='price-tag ui-search-price__part']//span[@class='price-tag-fraction']")

        for titulo, preco in zip(titulos, precos):
            with open('celulares.txt', 'a', newline='', encoding='utf-8') as arquivo:
                arquivo.write(titulo.text + ',' + preco.text + os.linesep)
        # 5 - Navegar até o próxima página
        try:
            sleep(random.randint(3, 5))
            driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight);')
            botao_proximo = driver.find_element_by_xpath(
                "//li[@class='andes-pagination__button andes-pagination__button--next']")
            sleep(random.randint(3, 5))
            botao_proximo.click()
        except:
            pass


# 6 - Agendar a execução!
schedule.every().thursday.at('07:00').do(buscar_precos)
while True:
    schedule.run_pending()
    sleep(1)

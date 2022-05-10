from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import randrange

def busca_amazon(item):
    driver.get('https://www.amazon.com.br')
    driver.maximize_window()
    driver.find_element(by=By.ID, value='twotabsearchtextbox').send_keys(item)
    driver.implicitly_wait(3)
    driver.find_element(by=By.ID, value="nav-search-submit-text").click()
    time.sleep(1)

    for i in range(2):
        time.sleep(1)
        produtos = driver.find_elements(by=By.CLASS_NAME, value='a-section.a-spacing-base')
        # print(produtos)
        time.sleep(1)
        if produtos:
            random_number = randrange(5)
            if random_number > len(produtos):
                random_number = randrange(len(produtos))
            print('numero aleatório =', random_number)
            produtos[random_number-1].click()
            time.sleep(2)
            try:
                driver.find_element(by=By.ID, value="add-to-cart-button").click()
            except:
                print('O item não pode ser adicionado ao carrinho')
                return
            driver.execute_script("window.history.go(-2)")
            time.sleep(1)
        else: 
            print('Não foram encontrado produtos')
            return

    driver.find_element(by=By.ID, value="nav-cart-count").click()
    produtos_carrinho = driver.find_elements(by=By.CLASS_NAME, value='a-truncate-cut')

    for produto in produtos_carrinho:
         print('O produto ', produto.text, ' está no carrinho')

item = input("Digite o nome de um produto:")
if not item.strip():
    item = 'caneta'

driver = webdriver.Chrome()
busca_amazon(item) 

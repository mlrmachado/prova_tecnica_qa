# Prova técnica de automação QA com Python e Selenium 

Este é um programa que testa o carrinho de compras de um e-commerce ([Amazon](https://www.amazon.com.br/))

## Instalação

Executar o comando abaixo para verificar se o Python está instalado:

```bash
python -V
```

Caso não retorne nenhum valor, instale a versão mais recente do Python:

[Python Download](https://www.python.org/downloads/)

Com o Python instalado, precisamos executar a instalação da biblioteca do Selenium:

```bash
pip install selenium
```
Em seguida, colocar o arquivo do chromedriver, referente a sua versão do chrome e sistema operacional, na pasta do programa:

[Chromedriver Download](https://chromedriver.chromium.org/downloads)

No meu caso, utilizo o Windows com o Chrome na versão Versão 101, e estou utilizando [este driver](https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_win32.zip).

## Utilização

Executar o comando abaixo no terminal:

```bash
python teste_qa_amazon.py
```
Ao executar o comando acima, o programa perguntará o produto que deseja pesquisar, e caso não for informado nenhum item, o programa vai pesquisar por padrão pelo produto "caneta".

Por fim, o programa mostrará os itens que foram adicionados no carrinho, se não ocorrer nenhuma falha no processo. Quando ocorre falha no processo, um aviso irá aparecer no terminal.

Por padrão, hoje o programa está adicionando 2 itens no carrinho.

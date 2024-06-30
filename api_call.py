# Programa em Phyton para efetuar, com base em um Ticker (código de negociação)
# Os valores dos proventos que serão pagos para um Fundo Imobiliário

# Bibliotecas para acesso a end-point web, matriz de dados e codificador base 64

import requests
import pandas as PD
from base64 import b64encode

def proventos(ticker):

#   Função para buscar os proventos de Fundo Imobiliário.
#   Recebe como input o ticker (4 LETRAS MAIUCULAS DO TICKER DE FUNDOS IMOBILIARIOS)    

#   Prepara a string em base 64 para acesso a API da B3

    parte1 = '{"cnpj":"09072017000129","identifierFund":"'

    parte2 = '","typeFund":7}'

    params = parte1 + ticker + parte2

#   Criptografa a variavel para acessar a API

    cripto = bytes(params,encoding="ascii")

    string = b64encode(cripto)

    string = string.decode()

#   Compoe o end-point para acessar a API

    url = "https://sistemaswebb3-listados.b3.com.br/fundsProxy/fundsCall/GetListedSupplementFunds/" + string

#   Efetua a chamada do End-point da B3
    
    response = requests.get(url)

#   Retorno da função
    return response.json()

def main():
    
#   Captura o Ticker que deseja consultar
    ticker = input("Informe o ticker FII com 4 letras: ")

#   Acessa a função para buscar os proventos
    resultados = proventos(ticker)

#   Obtem a parte das recorrências e coloca em um frame - Array começa em cashDividends

    df = PD.DataFrame(resultados['cashDividends'])

#   Mostra a array com as variáveis com destaque:
#   paymentDate     = Data que será pago provento
#   rate            = valor em reais que será pago por quota
#   lastDatePrior   = Data considerada em posse para receber provento   
    print(df)
    
if __name__ == "__main__":
    main()
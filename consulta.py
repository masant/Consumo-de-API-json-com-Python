import requests #acessar a biblioteca requests
import json #implementa no Python o formato de dados JSON5
import pandas #importa a biblioteca Pandas
import decimal
#request: biblioteca HTTP p/ Python

#link do Fixer.io JSON API p/ acessar a cotação das moedas:
url = "http://data.fixer.io/api/latest?access_key=95b323b205b8583c18bbe28825b1e07f" 
print("Acessando base de dados do Fixer.io...")
resposta = requests.get(url)
print(resposta)

if resposta.status_code == 200:
        print("Acesso realizado com sucesso!")
        print("Buscando informações..")
        dados = resposta.json()
        dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'], 2) #valor de 1 dolar em reais
        euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'], 2) #valor de 1 euro em reais
        bitcoin_real = round(dados['rates']['BRL']/dados['rates']['BTC'], 2) #valor de 1 bitcoin em reais

        print('1 Dolar vale: R$',dolar_real) #Dolar
        print('1 Euro vale: R$',euro_real) #Euro
        print('1 Bitcoin vale: R$',bitcoin_real) #Bitcoin
        print("Exportando resultado em tabela Excel...")
        dados_moedas = {'Moedas':['Dolar','Euro','Bitcoin'],
                        'Valores':[dolar_real,euro_real,bitcoin_real]
                        }
        tela = pandas.DataFrame(dados_moedas)
        tela.to_csv('valores.csv',index=False,sep=";",decimal=",")
        print("Arquivo exportado com sucesso!")
        #print(dados['rates']['BRL']) # Real
else:
    print("Erro na base de dados.")
#Lib utilizada para a requisição
import requests

#Função que utiliza API
def pegar_cotacao(cod_moeda):
    try:
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{cod_moeda}-BRL')
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{cod_moeda}BRL']['bid']
        return cotacao
    except:
        print("Código de Moeda Inválido")
        return None

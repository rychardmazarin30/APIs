# Lib utilizada para a requisição
import requests

# Função que utiliza API
def search_cep(num_cep):
    try:
        requisicao = requests.get(f'https://cep.awesomeapi.com.br/json/{num_cep}')
        requisicao_dic = requisicao.json()
        endereco, bairro, cidade = requisicao_dic['address'], requisicao_dic['district'], requisicao_dic['city']
        return endereco, bairro, cidade
    except:
        cep_invalido = 'CEP Inválido'
        return cep_invalido


# Lib Utlizada e arquivo de requisição da API
import PySimpleGUI as sg
from moeda import pegar_cotacao

# Tema da Interface
sg.theme('DarkAmber')

# Construindo a Interface
layout = [
    [sg.Text("Cotação de Moeda", font="arial 15 bold", background_color='black')],
    [sg.Text("Moeda:", font="arial 15 bold", background_color='black'), sg.InputText(key="nome_cotacao", font="arial 15 bold", background_color='black')],
    [sg.Text("", key="text_cotacao", font="arial 18 bold", background_color='black', text_color='white')],
    [sg.Button("Cotação", font="arial 15 bold"), sg.Button("Sair", font="arial 15 bold"), sg.Text("Desenvolvido por Rychard Mazarin", font="arial 12 bold", background_color='black',text_color='white')]
]

# Janela da aplicação
j = sg.Window("Cotação de Moeda", layout, background_color='black')

# Lista de todos os códigos das moedas
moedas = [
    'USD','EUR','ETH','GBP','BTC','CAD','AED','ARS','AUD',
    'BOB','CHF','CLP','CNY','COP','DKK','DOGE','HKD','ILS',
    'INR','JPY','LTC','MXN','NOK','NZD','PEN','PLN','PYG','RUB',
    'SAR','SEK','SGD','THB','TRY','TWD','UYU','XRP','ZAR'
]

# Controle dos eventos que acontecem e utilização do arquivo de requisição
while True:
    event, values = j.read()
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    if event == "Cotação":
        cod_cotacao = values['nome_cotacao']
        cod_cotacao = cod_cotacao.upper()
        cotacao = pegar_cotacao(cod_cotacao)
        for moeda in moedas:
            if moeda == cod_cotacao:
                if cod_cotacao == "BTC":
                    cotacao = float(cotacao)
                    j['text_cotacao'].update("%s: R$%.3f" % (cod_cotacao,cotacao))
                    break
                else:
                    cotacao = float(cotacao)
                    j['text_cotacao'].update("%s: R$%.2f" % (cod_cotacao,cotacao))
                    break 
            else:
                j['text_cotacao'].update("Código de Moeda Inválido")

j.close()

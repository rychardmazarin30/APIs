#Lib utilizada e arquivo da requisição da API
import PySimpleGUI as sg
from cep import search_cep

#Construindo a Interface Gráfica, nesta parte seja criativo!
layout = [
    [sg.Text("Insira o seu CEP abaixo", font='arial 15 bold',background_color='#781220')],
    [sg.Text('CEP:',font='arial 15 bold',background_color='#781220'), sg.InputText(key='numero_cep',font='arial 15 bold',)],
    [sg.Text('',key='text_cep',font='arial 15 bold',text_color='black', background_color='#781220')],
    [sg.Button('Buscar',font='arial 15 bold'), sg.Button('Cancelar',font='arial 15 bold', ), sg.Text('Desenvolvido por Rychard Mazarin', font='arial 12 bold', background_color='#781220')]
]

#Janela da Aplicação 
j = sg.Window("CEP", layout, background_color='#781220')

#Controle dos eventos que acontecem e utilização do arquivo de requisição
while True:
    event, values = j.read()
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
    if event == "Buscar":
        num_cep = values['numero_cep']
        endereco = search_cep(num_cep)
        if endereco == 'CEP Inválido':
            j['text_cep'].update('CEP Inválido')
        else:
            j['text_cep'].update(f'{endereco[0]}, {endereco[1]} - {endereco[2]}')

j.close()

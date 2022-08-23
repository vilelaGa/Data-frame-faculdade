from PySimpleGUI import PySimpleGUI as sg
import pandas as pd

# pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  

# Layout
sg.theme('LightGray')

layout = [
    [sg.Text('Caminho Arquivo: ', key="mensagemCaminho", size=(50, 3))],
    [sg.FileBrowse('Escolha um arquivo', file_types=(("TXT Files", "*.xlsx"), ("ALL Files", "*.*")), key="arquivo")],
    [sg.Button('Enviar')],
    [sg.Text('', key='valores'), sg.Text('', key='COL1'), sg.Text('', key='COL9')]
    # [sg.Text('', key='valores')]
]

# Janela

janela = sg.Window('Lista de presença', layout)


while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar':
        janela['mensagemCaminho'].update('Caminho Arquivo: ' + valores['arquivo'])
        print(valores['arquivo'])
        x = pd.read_excel(valores['arquivo'])
        # print(x['COL9'])
        # print(x['COL1'])
        
        janela['valores'].update(x[['COL2', 'COL9', 'COL11', 'COL12', 'COL13', 'COL20', 'COL21', 'COL25']])
        # janela['COL1'].update(x['COL1'])
        # janela['COL9'].update(x['COL9'])
        
        

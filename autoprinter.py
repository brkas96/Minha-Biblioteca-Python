#BOOK
import os
import time
import PySimpleGUI as sg
import pyautogui

def main():
    pyautogui.alert('Coloque na tela a ser printada e aperte OK :D')
    n = int(0)
    destino = (fullpath)

    while True:
        c = str(destino + '\pg' + str(n) + '.png')
        img = pyautogui.screenshot()
        time.sleep(5)
        img.save(c)
        pyautogui.press('right')
        n = int(n)
        n = n + 1

layout = [
    [sg.Text('Digite o Nome da pasta onde os prints ficarão: ')],
    [sg.Input('', enable_events=True, key='-INPUT-')],
    [sg.Button('Ok', key='-OK-'), sg.Button('Exit')]
]
janela = sg.Window('AutoPrinter(Feito por Bruno Benvenutti Castro)', layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-OK-':
        pasta = ''
        pasta = values['-INPUT-']
        fullpath = 'C:/AutoPrinter/' + str(pasta)
        janela.close()
        try:
            os.makedirs(fullpath)
            main()
        except:
            pyautogui.alert(':0  OU o diretório já exite OU o programa foi encerrado OU houve algum '
                            'erro que eu não faço idéia de qual seja :P . Vc pode me mandar um email'
                            ' reclamando, mas vai ter que descobrir qual é primeiro :D')

janela.close()

#origem = os.path.dirname(os.path.realpath(__file__)) #pega o caminho atual
#caminho = str(Path.home()) # pega o diretório do usuário ex: C:/User/NomeDoUsuario





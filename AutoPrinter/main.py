# Automação para tirar prints de algo que vc queira e que tenha muitas páginas...o uso indevido é total responsabilidade do usuário e não do desenvolvedor.
import os
import time
import PySimpleGUI as sg
import pyautogui

def printL():
    pyautogui.alert('Coloque na tela a ser printada e aperte OK :D')
    n = int(0)
    destino = (fullpath)

    while n < paginas:
        c = str(destino + '\pg' + str(n) + '.png')
        img = pyautogui.screenshot()
        time.sleep(1)
        img.save(c)
        pyautogui.press('right')
        n = int(n)
        n = n + 1

layout = [
    [sg.Text('Digite o Nome do Livro: ')],
    [sg.Input('', enable_events=True, key='-INPUT-')],
    [sg.Text('Digite a Quantidade de paginas: ')],
    [sg.Input('', enable_events=True, key='-NUM-')],
    [sg.Button('Ok', key='-OK-'), sg.Button('Exit')]
]
janela = sg.Window('AutoPrinter by BBC :D', layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-OK-':
        livro = ''
        livro = values['-INPUT-']
        paginas = values['-NUM-']
        paginas = int(paginas)
        fullpath = 'C:/Livros/' + str(livro)
        janela.close()
        try:
            os.makedirs(fullpath)
            printL()
        except:
            pyautogui.alert('Houve um erro. Tente excluir o diretorio C:/Livros. Não use nomes muito longos para nomear a pasta do'
                            'livro e não use caracteres especiais.')
janela.close()


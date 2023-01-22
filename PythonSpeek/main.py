import gtts
from playsound import playsound
import PySimpleGUI as sg
import os
from time import sleep
from pathlib import Path
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():

    def create_folder():
        directory = "backupfiles"
        user = str(Path.home())
        parent_dir = user
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

    sg.theme('DarkBlue1')
    layout = [
        [sg.LBox([], size=(50, 5), key='-FILESLB-')],
        [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
        [sg.Button('Ler', key='ler'),
         sg.Button('Sair', key='sair'),
         ]

    ]

    window = sg.Window('Leitor de texto', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'sair':
            break
        if event == '-IN-':
            window['-FILESLB-'].Update(values['-IN-'].split(';'))
        if event == 'ler':
            texto = values['-IN-']
            try:
                create_folder()
                sg.popup('Seu audio esta sendo reproduzido, aguarde o término.')
                with open(texto, 'r') as arquivo:
                    for linha in arquivo:
                        frase = gtts.gTTS(linha, lang='pt-br')
                        frase.save('frase.mp3')
                        sleep(2)
                        playsound('frase.mp3')
                        sleep(5)
            except:
                pass

if is_admin():
    main()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)




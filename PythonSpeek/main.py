import gtts
from playsound import playsound
import PySimpleGUI as sg
from time import sleep
import ctypes
import sys
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():

    def falar(texto):

        try:
            # sg.popup('Seu audio esta sendo reproduzido, aguarde o término.')
            with open(texto, 'r') as arquivo:
                for linha in arquivo:
                    try:
                        frase = gtts.gTTS(linha, lang='pt-br')
                        sleep(3)
                        frase.save(os.path.join("temp.mp3"))
                        sleep(2)
                        try:
                            playsound(os.path.join("temp.mp3"))

                        except FileNotFoundError:
                            print("FileNotFoundError")
                            playsound(os.path.abspath("temp.mp3"))
                        except Exception as e:
                            print(f"Erro ao reproduzir temp.mp3: {e}")
                    except:
                        sg.popup('Houve um erro')
            sleep(3)
            #os.remove('temp.mp3')

        except:
            pass

    sg.theme('DarkBlue1')
    layout = [
        [sg.Text("Caminho do .txt: "), sg.Input([], size=(50, 5), key='-FILESLB-'),
         sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
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
            falar(texto)

if is_admin():
    main()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

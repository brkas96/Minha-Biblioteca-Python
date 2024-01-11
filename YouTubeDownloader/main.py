from pytube import YouTube
import PySimpleGUI as sg
import os
from pathlib import Path
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    user = str(Path.home())

    def DownloadMp3(link):
        global destination
        global open

        # url do video
        yt = YouTube(link)

        # extrai apenas o audio
        video = yt.streams.filter(only_audio=True).first()

        destination = user + '\Youtube Downloads'

        # download do arquivo
        out_file = video.download(output_path=destination)

        # salva o arquivo
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        open = user + base

    def DownloadVideo(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()

        try:
            destination = user + '\Youtube Downloads'
            youtubeObject.download(output_path=destination)
        except:
            pass

    def openFolder():
        import subprocess
        subprocess.Popen(r'explorer 'f'{user}' + "\Youtube Downloads")

    sg.theme('DarkRed1')
    tipo = ['video(.mp4)', 'audio(.mp3)']
    layout = [
        [sg.Text('Cole o link aqui: '), sg.InputText('', do_not_clear=False, key='-INPUT-')],
        [sg.Button('Download', key='baixar'),
         sg.Combo(tipo,'Escolha o formato', key='-COMBO-', size=(15,15)),
         sg.Button('Limpar', key='limpar'),
         sg.Button('Abrir Pasta', key='open'),
         sg.Button('Sair', key='sair')]

    ]

    window = sg.Window('Youtube Downloader', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'baixar':
            link = values['-INPUT-']
            if values['-COMBO-'] == 'video(.mp4)':
                sg.popup('Aguarde enquanto o video é baixado. O programa pode parar de responder durante o '
                         'download porque o desenvolvedor tem preguiça de implementar uma barra de progresso.'
                         'Mas fique calmo...seu video está sendo baixado!')
                try:
                    DownloadVideo(link)
                    sg.popup('Download efetuado com sucesso.')
                except Exception as erro:
                    sg.popup(f"Não foi possível efetuar o download devido a um erro: {erro.__cause__}")
                except:
                    pass
            if values['-COMBO-'] == 'audio(.mp3)':
                sg.popup('Aguarde enquanto o audio é baixado. O programa pode parar de responder durante o '
                         'download porque o desenvolvedor tem preguiça de implementar uma barra de progresso.'
                         'Mas fique calmo...seu audio está sendo baixado!')
                try:
                    DownloadMp3(link)
                    sg.popup('Download efetuado com sucesso.')
                    openFolder()
                except Exception as erro:
                    sg.popup(f"Não foi possível efetuar o download devido a um erro: {erro.__cause__}")
                except:
                    pass
        if event == 'open':
            try:
                openFolder()
            except:
                pass
        if event == 'sair':
            break
        if event == 'limpar':
            pass

if is_admin():
    main()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



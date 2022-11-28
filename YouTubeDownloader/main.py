from pytube import YouTube
import PySimpleGUI as sg
import os
import ctypes
from pathlib import Path
import sys
import request

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    def mp3(link):

        # url do video
        yt = YouTube(link)

        # extrai apenas o audio
        video = yt.streams.filter(only_audio=True).first()

        destination = '.'

        # download do arquivo
        out_file = video.download(output_path=destination)

        # salva o arquivo
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    def Download(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()

        try:
            youtubeObject.download()
        except:
            pass
    sg.theme('DarkRed1')
    layout = [
        [sg.Text('Cole o link aqui: '), sg.InputText('', do_not_clear=False, key='-INPUT-')],
        [sg.Button('Baixar video(.mp4)', key='baixarV'),
         sg.Button('Baixar audio(.mp3)', key='baixarM'),
         sg.Button('Limpar', key='limpar'), sg.Button('Sair', key='sair')]

    ]

    window = sg.Window('Youtube Downloader by Bruno Benvenutti', layout)

    while True:
        event, values = window.read()
        user = str(Path.home())

        if event == sg.WIN_CLOSED:
            break
        if event == 'baixarV':
            link = values['-INPUT-']
            sg.popup(
                'Aguarde enquanto o video é baixado. O programa pode parar de responder, apenas aguarde o término do ]'
                'Download.')
            try:
                Download(link)
            except Exception as erro:
                sg.popup(f"Não foi possível efetuar o download devido a um erro: {erro.__cause__}")
            else:
                sg.popup('Download efetuado com sucesso.')
        if event == 'baixarM':
            link = values['-INPUT-']
            sg.popup(
                'Aguarde enquanto o audio é baixado. O programa pode parar de responder, apenas aguarde o término do '
                'Download.')
            try:
                mp3(link)
            except Exception as erro:
                sg.popup(f"Não foi possível efetuar o download devido a um erro: {erro.__cause__}")
            else:
                sg.popup('Download efetuado com sucesso.')
        if event == 'sair':
            break
        if event == 'limpar':
            pass

if is_admin():
    main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
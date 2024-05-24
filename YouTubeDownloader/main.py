from pytube import YouTube
import PySimpleGUI as sg
import os
from pathlib import Path
import ctypes
import sys
import subprocess
import threading # Implementar threads
# implementar barra de progresso

user = str(Path.home())
DOWNLOADS_DIR = user + '\Youtube Downloads'

sg.theme('DarkRed1')
tipo = ['video(.mp4)', 'audio(.mp3)']
layout = [
        [sg.Text('Cole o link aqui: '), sg.InputText('', do_not_clear=False, key='-INPUT-')],
        [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
        [sg.Button('Download', key='baixar'),
         sg.Combo(tipo, 'Escolha o formato', key='-COMBO-', size=(15, 15)),
         sg.Button('Limpar', key='limpar'),
         sg.Button('Abrir Pasta', key='open'),
         sg.Button('Sair', key='sair')]

    ]

window = sg.Window('Youtube Downloader', layout)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def DownloadMp3(link):

    # url do video
    yt = YouTube(link)

    # extrai apenas o audio
    video = yt.streams.filter(only_audio=True).first()

    destination = DOWNLOADS_DIR

    # download do arquivo
    out_file = video.download(output_path=destination)

    # salva o arquivo
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def progress_bar(stream, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    progress_percent = int(bytes_downloaded / total_bytes * 100)
    print(f"progress_percent {progress_percent}")
    window['-PROGRESS-'].update(progress_percent)

def DownloadVideo(link):
    youtubeObject = YouTube(link)
    print(youtubeObject)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    size = youtubeObject.filesize_mb
    print(f'{size}mb')

    try:
        destination = DOWNLOADS_DIR
        youtubeObject.download(output_path=destination)
        window['-PROGRESS-'].update(size)
    except:
        return


def openFolder():
    subprocess.Popen(r'explorer 'f'{user}' + "\Youtube Downloads")


def interface(window):

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'baixar':
            link = values['-INPUT-']
            if values['-COMBO-'] == 'video(.mp4)':
                sg.popup('Aguarde enquanto o video é baixado.')
                try:
                    thread_downvideo = threading.Thread(target=DownloadVideo, daemon=True, args=(link, ))
                    thread_downvideo.start()

                except Exception as erro:
                    sg.popup(f"Não foi possível efetuar o download devido a um erro: {erro.__cause__}")
                except:
                    pass
            if values['-COMBO-'] == 'audio(.mp3)':
                sg.popup('Aguarde enquanto o audio é baixado.')
                try:
                    thread_downmp3 = threading.Thread(target=DownloadMp3, daemon=True, args=(link, ))
                    thread_downmp3.start()
                    openFolder()
                except Exception as erro:
                    sg.popup(f"Não foi possível efetuar o download devido a um erro: {erro.__cause__}")
                except:
                    pass
            elif values['-COMBO-'] == 'Escolha o formato':
                sg.popup('Escolha o formato do arquivo, video ou mp3.')
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

def main():
    if not os.path.exists(DOWNLOADS_DIR):
        try:
            os.makedirs(DOWNLOADS_DIR)
        except Exception as e:
            print(f"Não foi possível criar o diretorio de download: {e}")
            return

    thread_interface = threading.Thread(target=interface, args=(window, ))
    thread_interface.start()
    thread_interface.join()


if is_admin():
    main()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



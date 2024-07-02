from pytube import YouTube
import PySimpleGUI as sg
import os
from pathlib import Path
import ctypes
import sys
import subprocess
import threading
import requests
import shutil
import zipfile

# implementar barra de progresso
# implementar download de playlist
# implementar conversão de video para mp3 da forma correta, com pydub - OK


user = str(Path.home())
DOWNLOADS_DIR = user + '\Youtube Downloads'

sg.theme('Dark Blue 7')
tipo = ['video(.mp4)', 'audio(.mp3)']
layout = [
    [sg.Text('YouTube Link: '), sg.InputText('', do_not_clear=False, key='-INPUT-')],
    #[sg.Text("Download Progress: "), sg.ProgressBar(100, orientation='h', size=(25, 25), key='-PROGRESS-')],
    [sg.Combo(tipo, 'Escolha o formato', key='-COMBO-', size=(15, 15))],
    [sg.Button('Download', key='baixar')],
    [sg.Text('_' * 50)],
    [sg.Button('Limpar', key='limpar'),
     sg.Button('Abrir Pasta', key='open'),
     sg.Button('Sair', key='sair')]

]

window = sg.Window('Youtube Downloader', layout, element_justification='c', margins=(20, 20))


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def download_ffmpeg():
    print(f"Baixando FFmpeg")
    url = f"https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    response = requests.get(url)
    if response.status_code == 200:
        zip_path = os.path.join("ffmpeg-release-essentials.zip")
        with open(zip_path, 'wb') as f:
            f.write(response.content)
        print("FFmpeg baixado com sucesso.")
    else:
        raise Exception("Não foi possível baixar o FFmpeg")


def setup_ffmpeg_path():
    ffmpeg_exe = os.path.join('.', 'ffmpeg.exe')

    if not os.path.exists(ffmpeg_exe):
        download_ffmpeg()
        extract_ffmpeg_bin('ffmpeg-release-essentials.zip')

    if os.path.exists(ffmpeg_exe):
        print(f"FFmpeg encontrado em: {ffmpeg_exe}")
        return ffmpeg_exe

    raise Exception("Não foi possível encontrar o ffmpeg.exe")


def extract_ffmpeg_bin(zip_path):
    temp_dir = "ffmpeg_temp"

    # Garantir que o diretório temporário exista
    os.makedirs(temp_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(temp_dir)
    print("FFmpeg extraído com sucesso.")

    # Encontrar a pasta bin
    bin_path = None
    for root, dirs, files in os.walk(temp_dir):
        if "bin" in dirs:
            bin_path = os.path.join(root, "bin")
            break

    if not bin_path:
        raise Exception("Não foi possível encontrar a pasta bin")

    # Mover os arquivos da pasta bin para o diretório raiz
    final_bin_path = os.path.join(".")
    for file in os.listdir(bin_path):
        shutil.move(os.path.join(bin_path, file), os.path.join(final_bin_path, file))

    ffmpeg_exe = os.path.join(final_bin_path, 'ffmpeg.exe')
    if os.path.exists(ffmpeg_exe):
        return ffmpeg_exe
    else:
        raise Exception("Não foi possível extrair o ffmpeg.exe")


def converter_para_mp3(video_path):
    a = AudioSegment.converter = ffmpeg_path
    print(a)

    output_path = os.path.splitext(video_path)[0] + '.mp3'

    print("Convertendo audio com pydub")
    # Carregar o arquivo de vídeo
    audio = AudioSegment.from_file(video_path, format="mp4")
    try:
        # Exportar como MP3
        audio.export(output_path, format="mp3")
        return True
    except Exception as e:
        print(f"Erro ao converter para mp3: {e}")
        return


def DownloadMp3(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    print(f"video: {video}")
    out_file = video.download(output_path=DOWNLOADS_DIR)
    print(f"out_file: {out_file}")
    c = converter_para_mp3(out_file)
    if c:
        os.remove(out_file)


def progress_bar(stream, chunk, file_handle, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    progress_percent = int(bytes_downloaded / total_bytes * 100)
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
        window['-PROGRESS-'].update(100)
    except:
        return


def openFolder():
    subprocess.Popen(r'explorer 'f'{user}' + "\Youtube Downloads")


def interface(window):
    if not os.path.exists(DOWNLOADS_DIR):
        try:
            os.makedirs(DOWNLOADS_DIR)
            sg.popup(f'Diretorio {DOWNLOADS_DIR} criado com sucesso')
        except Exception as e:
            print()
            sg.popup(f"Não foi possível criar o diretorio de download: {e}")
            return

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'baixar':
            link = values['-INPUT-']
            if values['-COMBO-'] == 'video(.mp4)':
                sg.popup('Aguarde enquanto o video é baixado.')
                try:
                    thread_downvideo = threading.Thread(target=DownloadVideo, daemon=True, args=(link,))
                    thread_downvideo.start()
                except Exception as erro:
                    sg.popup(f"Não foi possível efetuar o download devido a um erro: {erro.__cause__}")
                except:
                    pass
            if values['-COMBO-'] == 'audio(.mp3)':
                sg.popup('Aguarde enquanto o audio é baixado.')
                try:
                    thread_downmp3 = threading.Thread(target=DownloadMp3, daemon=True, args=(link,))
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


if __name__ == "__main__":
    if is_admin():
        ffmpeg_path = setup_ffmpeg_path()

        # Verificar se o ffmpeg foi encontrado e configurar o pydub
        if ffmpeg_path:
            from pydub import AudioSegment

            AudioSegment.converter = ffmpeg_path

            files_to_remove = ['ffmpeg-release-essentials.zip', 'ffmpeg_temp']
            for file in files_to_remove:
                try:
                    if os.path.isdir(file):
                        shutil.rmtree(file)
                        print(f"Diretório {file} removido com sucesso.")
                    else:
                        os.remove(file)
                        print(f"Arquivo {file} removido com sucesso.")
                except FileNotFoundError:
                    print(f"Arquivo ou diretório {file} não encontrado.")
                except PermissionError:
                    print(f"Acesso negado ao remover {file}.")
                except Exception as e:
                    print(f"Erro ao remover o arquivo ou diretório {file}: {e}")

            thread_interface = threading.Thread(target=interface, args=(window,))
            thread_interface.start()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

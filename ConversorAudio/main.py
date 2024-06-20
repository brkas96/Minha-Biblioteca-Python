import time

from pydub import AudioSegment
import os
import stat
import PySimpleGUI as sg

# Verificar permissões de leitura e escrita
def check_permissions(file_path):
    return os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK)

# Ajustar permissões para leitura e escrita para o proprietário
def set_permissions(file_path):
    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR |
                      stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP |
                      stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH)


def convert_audio_to_mp3(input_file, output_file, bitrate):
    try:
        # Carregar o arquivo de áudio
        audio = AudioSegment.from_file(input_file)

        # Exportar para MP3 com ajuste de bitrate (qualidade)
        audio.export(output_file, format="mp3", bitrate=bitrate)
        print(f"Arquivo convertido com sucesso para {output_file} com qualidade {bitrate}")
    except Exception as e:
        print(f"Erro ao converter o arquivo: {e}")

audio_path = input("Selecione a pasta onde estão os audios:")

input_file = os.listdir(audio_path)
print(input_file)

bitrate = "192k"  # Altere para o bitrate desejado
output_file = os.path.abspath(os.path.join('convertidos'))



if not os.path.exists(output_file):
    os.makedirs(output_file)

print(check_permissions(output_file))

print(set_permissions(output_file))

for audio in input_file:
    full_path_audio = os.path.join(audio_path, audio)
    full_path_audio = os.path.abspath(full_path_audio)
    print("full_path_audio: ", full_path_audio)

    convert_audio_to_mp3(full_path_audio, output_file, bitrate)
    time.sleep(3)




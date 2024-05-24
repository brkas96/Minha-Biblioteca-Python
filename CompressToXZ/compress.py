import PySimpleGUI as sg
import shutil
import tarfile
import lzma
import os

# xz = compressão de um único arquivo
# xzt = compressão de multiplos arquivos

# Comprime uma pasta ou arquivo utilizando o algoritmo lzma
def compress(path_orig):
    if os.path.isdir(path_orig):
        print(f'O caminho {path_orig} é um diretório (pasta).')
        file_ext = 'xzt'
        dest_file_name = path_orig + f'.{file_ext}'
        temp_archive_name = 'temp_archive.tar'

        try:
            with tarfile.open(temp_archive_name, 'w') as archive:
                archive.add(path_orig, arcname=os.path.basename(path_orig))

            with lzma.open(dest_file_name, 'w') as compressed_file:
                with open(temp_archive_name, 'rb') as temp_file:
                    shutil.copyfileobj(temp_file, compressed_file)

            os.remove(temp_archive_name)
            print(f'Arquivo comprimido criado com sucesso: {dest_file_name}')
            return True
        except Exception as e:
            print(f'Erro ao comprimir o arquivo: {e}')
            return False

    elif os.path.isfile(path_orig):
        print(f'O caminho {path_orig} é um arquivo único.')
        file_ext = 'xz'
        dir_name = os.path.dirname(path_orig)
        base_name = os.path.basename(path_orig)
        dest_file_name = os.path.join(dir_name, f'{base_name}.{file_ext}')

        try:
            with open(path_orig, 'rb') as file:
                with lzma.open(dest_file_name, 'w') as compressed_file:
                    shutil.copyfileobj(file, compressed_file)

            print(f'Arquivo comprimido criado com sucesso: {dest_file_name}')
            return True
        except Exception as e:
            print(f'Erro ao comprimir o arquivo: {e}')
            return False
    else:
        print(f'O caminho {path_orig} não é um diretório nem um arquivo único.')
        return False

# Descomprime um arquivo xzt
def decompress(file_path):

    if file_path.endswith('.xz'):
        try:
            with lzma.open(file_path, 'rb') as compressed_file:
                decompressed_content = compressed_file.read()
                return decompressed_content
        except Exception as e:
            print(f'Erro ao descomprimir o arquivo {file_path}: {e}')
            return None

    elif file_path.endswith('.xzt'):
        try:
            # Criar um arquivo temporário para extrair o conteúdo
            temp_dir = 'temp_extracted'
            os.makedirs(temp_dir, exist_ok=True)

            # Extrair o conteúdo do arquivo .xzt
            with tarfile.open(file_path, 'r:xz') as archive:
                archive.extractall(temp_dir)

            # Ler o conteúdo do arquivo extraído (pode ser uma lista de arquivos)
            extracted_files = os.listdir(temp_dir)
            extracted_content = {}
            for extracted_file in extracted_files:
                extracted_file_path = os.path.join(temp_dir, extracted_file)
                with open(extracted_file_path, 'rb') as file:
                    extracted_content[extracted_file] = file.read()

            # Limpar o diretório temporário
            shutil.rmtree(temp_dir)

            # Retorna um dicionário com o nome dos arquivos e seus conteúdos
            return extracted_content
        except Exception as e:
            print(f'Erro ao descomprimir o arquivo {file_path}: {e}')
            return None

    else:
        print(f'O arquivo {file_path} não está no formato .xz ou .xzt.')
        return None

def save(file):
    with open(file, 'w') as saved_file:
        saved_file.write()
        return True

def main():
    pass

if __name__ == '__main__':
    file = decompress(r'C:\Users\bruno\OneDrive\Imagens\testes\django-flow.png.xz')
    save(file)

# Essa automação com interface gráfica simples, serve para excluir arquivos com
# determinada extensão como por exemplo .png. Útil para pastas que possuem muitos arquivos
# de vários tipos.
# Feedback: brkas_dev@proton.me
import os
from send2trash import send2trash
import PySimpleGUI as sg

def move_to_trash(folder_path, extension, del_subfolders):
    if not os.path.exists(folder_path):
        print("A pasta não existe.")
        return

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.'+ str(extension)):
                file_path = os.path.join(root, filename)
                print(f"Enviando '{file_path}' para a lixeira.")
                send2trash(file_path)
        if not del_subfolders:
            dirs.clear()


layout = [[sg.Text('Folder Path:'), sg.Input(key='folder',
                                      size=(60, 1))],
          [sg.Text('File Extension:'), sg.Input('ex: png', key='extension',
                                                size=(10, 1)), sg.Checkbox('Include Subfolders'
                                                                           ,key='subfolder')],
          [sg.Button('Start'), sg.Button('Cancel')]
          ]

janela = sg.Window("Auto File Deleter", layout, element_justification='center')

if __name__ == "__main__":
    while True:
        event, values = janela.Read()

        if event == sg.WIN_CLOSED:
            break

        elif event == 'Start':
            path = values['folder']
            file_extension = values['extension']
            subfolders = values['subfolder']
            if subfolders:
                if sg.popup('ATENÇÃO, você marcou para excluir arquivos em subpastas,'
                            'se tem certeza dessa escolha aperte OK do contrario feche '
                            'essa janela de '
                            'aviso e o programa será encerrado.'):
                    pass
                else:
                    break
            move_to_trash(path, file_extension, subfolders)
            sg.popup("Os arquivos com a extensão solicitada foram excluídos com sucesso.")


        elif event == 'Cancel':
            break


    janela.close()




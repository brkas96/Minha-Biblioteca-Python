import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        #layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de email são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes',key='aceitaCartao'),sg.Radio('Não', 'cartoes',key='naoAceitaCartao')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        #janela
        self.janela = sg.Window("Dados de usuário").layout(layout)

    def Iniciar(self):
        #Extrair os dados da tela
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não aceita Cartão: {nao_aceita_cartao}')



tela = TelaPython()
tela.Iniciar()



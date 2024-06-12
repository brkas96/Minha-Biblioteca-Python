# Minha-Biblioteca-Python

Bem-vindo à Minha-Biblioteca-Python! Esta é uma coleção de pequenos programas escritos em Python, criados por mim.

Apoie este projeto: [![Patrocine este projeto](https://img.shields.io/badge/-Sponsor-fafbfc?logo=GitHub%20Sponsors)](https://github.com/sponsors/brkas96)

## Sobre

[Um conjunto de pequenas ferramentas para resolver problemas específicos, que podem ser úteis para você ou não XD]

## Conteúdo

- [AutoPrinter](#auto-printer)
- [DuckDnsUpdater](#duck-dns)
- [Programa 3](#programa-3)

## Auto Printer 
{auto-printer}

[Uma pequena automação para tirar screenshots de livros, documentos ou apps que possuam páginas]

```python
# Exemplo de uso do AutoPrinter
python main.py

'''Ao executar o programa, será aberto uma interface gráfica contruida com a biblioteca PySimpleGUI.

- No primeiro input coloque o "nome do livro". Será criada uma pasta com esse nome, onde os prints seram salvos.

- No segundo input, indique a "quantidade de páginas". A quantidade de páginas, é a quantidade de vezes que
o programa repetirá o processo de clicar para o lado direito pyautogui.press('right') tirará um print da tela
e salvará na pasta cujo nome foi indicado, com uma contagem de páginas no nome de cada print, que foi indicada
em "quantidade de páginas".

- Os screenshots são salvos por padrão em:"C:/Livros/NomeLivro"'''
```

## Duck DNS Updater 
{duck-dns}
[Um programa que atualiza IPV4 e IPV6 no Duck DNS. Usa a API da ipify para adquirir os endereços IPs públicos]

```python
# Exemplo de uso do DuckDNSUpdater
python DuckDnsUpdater.py

'''No código do programa adicione o nome so seu dominio e seu token, adquiridos no site oficial do Duck DNS.
domain = "YOUR-DOMAIN"
token = "YOUR-TOKEN"
Após adicionar os valores as variaveis domain e token, compile o script com Pyinstaller, depois execute o .exe.
O programa entrará em um loop que verifica os IPs públicos da máquina a cada 20 minutos e atualiza no Duck DNS.

'''

```




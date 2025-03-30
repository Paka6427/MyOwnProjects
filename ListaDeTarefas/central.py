from pacotes.menu import *
from pacotes.cores import *
from pacotes.funcoes import *
while True:
    mainmenu()
    opcao = option()
    if titulo(opcao) == 'stop':
        break
    

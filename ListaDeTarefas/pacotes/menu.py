from pacotes.cores import *
from pacotes.funcoes import *
from pacotes.effects00 import *
from time import sleep
def mainmenu():
    print('\033[4;33mOPÇÕES:\033[m')
    selecao = ['Criar nova tarefa', 'Visualizar tarefas', 'Encerrar uma tarefa','Ver tarefas já concluidas','Deletar histórico de tarefas concluidas', 'Encerrar programa']
    for i, selecao in enumerate(selecao):
        print(f'[{azul(i)}] - {verd(selecao)}')
def option():
    opt = -1
    while opt not in ['0','1','2','3', '4', '5']:
        opt = input('Selecione o número correspondente a sua escolha: ')
    return int(opt)
    

def titulo(o):
    opts = ['CRIAR NOVA TAREFA', 'VISUALIZAR TAREFAS','', 'ENCERRAR UMA TAREFA', 'TAREFAS JÁ CONCLUIDAS', 'DELETAR TAREFAS CONCLUIDAS', 'ENCERRAR PROGRAMA']
    linha()
    print(amar(f'OPÇÃO {o}: {opts[o]}'))
    linha()
    return defnum(o)

from time import sleep
def linha():
    print('=-'*15)

def carregar():
    print('Carregando',end='',flush=True)
    
    for i in range(0,2):
        print('.', end='',flush=True)
        sleep(0.5)
    print('.',flush=True)
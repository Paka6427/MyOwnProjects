import mysql.connector
from pacotes.cores import *
from datetime import datetime
from pacotes.effects00 import *

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='27036497'
)
cursor = conn.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS tarefas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
conn.commit()

conn.database = 'tarefas'

cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL, 
    descricao TEXT,
    status VARCHAR(50) NOT NULL,
    prazo DATETIME NOT NULL)
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS concluidas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL, 
    descricao TEXT,
    status VARCHAR(50) NOT NULL,
    prazo DATETIME NOT NULL)
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci''')
conn.commit()

def defnum(o):
    if o == 0:
        nome = input('Insira o nome da tarefa: ')
        desc = input('Descrição da tarefa: ')
        status = 'Não concluida' 

        while True:
            try:
                prazo = input(f'Insira o prazo total da tarefa\nex: {amar("2005-12-03 12:45:00")}\n> ')
                ano = input('Insira o ano do prazo: ')
                dia = input('Insira o dia do prazo: ')
                mes = input('Insira o mês do prazo: ')
                hora = input('Hora do prazo (sem minutos): ')
                minutos = input('Minuto: ')
                segundos = input('Segundos: ')

                prazo_dt = datetime.strptime(prazo, '%Y-%m-%d %H:%M:%S')
                carregar()
                break
            except ValueError:
                print(verm('ERRO: PRAZO INCORRETO. TENTE NOVAMENTE!'))
                

        while True:
            cancelar = input('Deseja criar a tarefa? [S/N]')
            if cancelar.lower() in ['s','n']:
                break
            
        if cancelar == 's':
            cursor.execute('''INSERT INTO tarefas(titulo, descricao, status, prazo)
            VALUES(%s,%s,%s,%s)
            ''', (nome, desc, status, prazo))
            conn.commit()
            print(verd('Nova tarefa criada com sucesso!'))
        else:
            print(verm('Criação de tarefa cancelada'))
    elif o == 1:
        cursor.execute('SELECT * FROM tarefas')
        tarefas = cursor.fetchall()
        if len(tarefas) == 0:
            print(verm('Crie uma tarefa'))
        for tarefa in tarefas:
            print(f'{azul('ID: ')}{tarefa[0]}\n{azul('Tarefa: ')}{tarefa[1]}\n{azul('Descrição: ')}{tarefa[2]}\n{azul('Status: ')}{tarefa[3]}\n{azul('Prazo: ')}{tarefa[4]}')
            print('')
    elif o == 2:
        cursor.execute('SELECT id FROM tarefas')
        ids = cursor.fetchall()
        print('IDs das tarefas: ')
        listaids = list()
        for id_tuple in ids:
            listaids.append(id_tuple[0])
            print(id_tuple[0])
        while True:
            try:
                encerrar = input('Insira o ID da tarefa que deseja encerrar: ')
                int(encerrar)
            except:
                print(verm('ERRO: FORMATO INVALIDO'))
            else:
                if int(encerrar) not in listaids:
                    print(verm('ERRO: O ID INFORMADO NÃO EXISTE'))
                    print(listaids)
                else:
                    cursor.execute('''SELECT * FROM tarefas WHERE id = %s''', (int(encerrar),))
                    tarefa = cursor.fetchone()
                    cursor.execute('''INSERT INTO concluidas(id, titulo, descricao, status, prazo)
                    values (%s, %s, %s, 'Concluida', %s)''', tarefa)
                    conn.commit()
                    cursor.execute('''DELETE FROM tarefas WHERE id = (%s)''', (int(encerrar),))
                    conn.commit()
                    print(verd('Tarefa concluida com sucesso.'))
                    break
    elif o == 3:
        cursor.execute('''SELECT * FROM concluidas''')
        conc = cursor.fetchall()
        if len(conc) == 0:
            print(verm('Não há tarefas concluidas'))

        for c in conc:
            print(f'{azul('ID: ')}{c[0]}\n{azul('Tarefa: ')}{c[1]}\n{azul('Descrição: ')}{c[2]}\n{azul('Status: ')}{c[3]}\n{azul('Prazo: ')}{c[4]}')
            print('')
    
    elif o == 4:
        while True:
            certeza = input('Tem certeza que deseja continuar? [S/N]')
            if certeza.lower() == 's':
                cursor.execute('''DELETE * FROM concluidas''')
                conn.commit()
                print(verd('Histórico deletado com sucesso!'))
                break
            else:
                break

    else:
        carregar()
        return 'stop'
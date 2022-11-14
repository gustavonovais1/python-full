import pymysql.cursors

conection = pymysql.connect(
    host="localhost",
    user="root",
    password="222545",
    port=3306,
    autocommit=True,
    db="python-full",
    charset="utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)

def criaTabela(nomeTabela):
    try:
        with conection.cursor() as cursor:
            cursor.execute(f'create table {nomeTabela} (nome varchar(50)) ')

        print('Tabela criada com sucesso!')

    except Exception as a:
        print(f'Ocorreu um erro de {a} ')

def removeTabela(nomeTabela):
    try:
        with conection.cursor() as cursor:
            cursor.execute(f'drop table {nomeTabela}')

        print('Tabela removida com sucesso!')

    except Exception as a:
        print(f'Ocorreu um erro de {a} ')

def insereTabela(nome):
    try:
        with conection.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values ('{nome}')")

        print('Valor inserido com sucesso!')

    except Exception as a:
        print(f'Ocorreu um erro de {a}')

def consultaTabela():
    try:
        with conection.cursor() as cursor:
            cursor.execute("update teste set nome = 'gustavo' where nome = 'vc'")
        print('Tabela atualizada com sucesso!')

    except Exception as a:
        print(f'Ocorreu um erro de {a}')

def removeColunaTabela():
    try:
        with conection.cursor() as cursor:
            cursor.execute("DELETE FROM teste where nome = 'pedro'")
        print('Remoção realizada com sucesso!')

    except Exception as a:
        print(f'Ocorreu um erro de {a}')

conection.close()   
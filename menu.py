import pymysql.cursors

conexao = pymysql.connect(
     host = 'localhost',
     user = 'root',
     password = '',
     db = 'cinema',
     charset= 'utf8mb4',
     cursorclass= pymysql.cursors.DictCursor
    )

def menuMaster():
    print("CONCORDO!")

def menuUser():
    print("Bem vindo, escolha umas das opções \n")
    escolhaUser = int(input("1 - Filmes em cartaz \n 2 - minhas compras \n 3 - Sair"))
    if escolhaUser == 1:
    
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from filmes')
                resultado = cursor.fetchall()
        except:
            print('erro ao conectar no banco de dados!')
        print("Filmes em cartaz: \n")
        for linha in resultado:
            print(f"Nome: {linha['nome']}")
            print(f"Classificação: {linha['classificacao']}")
            print(f"Valor:{linha['valorIngresso']}\n")

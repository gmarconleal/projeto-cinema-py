import pymysql.cursors
import index

conexao = pymysql.connect(
     host = 'localhost',
     user = 'root',
     password = '',
     db = 'cinema',
     charset= 'utf8mb4',
     cursorclass= pymysql.cursors.DictCursor
    )
try:
    with conexao.cursor() as cursor:
     cursor.execute('select * from filmes')
     resultado = cursor.fetchall()
except:
    print('erro ao conectar no banco de dados!')

def menuMaster():
    print("CONCORDO!")

def menuUser():
    print("Bem vindo, escolha umas das opções \n")
    escolhaUser = int(input("1 - Filmes em cartaz \n 2 - Sair \nopção:"))
    if escolhaUser == 1:
        print("Filmes em cartaz: \n")
        for linha in resultado:
            print(f"Id: {linha['id']}")
            print(f"Nome: {linha['nome']}")
            print(f"Classificação: {linha['classificacao']}")
            print(f"Valor:{linha['valorIngresso']}\n")
        
        compra = int(input("Escolha o id do filme para comprar, ou aperte 0 para voltar para o menu!"))
        while compra != 0:
            if compra == 1:
                print("Escolha seu horário: ")
    else:
        print("Saindo...")
        index.autentico = False
    
    return menuUser(), index.autentico
            
    
import pymysql.cursors
import index, Login

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
    print("Bem vindo! Escolha uma das opções abaixo: \n")
    escolhaMas = int(input("1 - Adicionar novos filmes\n 2 - Filmes em cartaz \n 3 - Adicionar Novos funcionarios\n 4 - Ver quadro de funcionários \n 5 - Sair \n"))
    if escolhaMas == 1:
        print("Cadastro de novos filmes")
    elif escolhaMas == 2:
        print("Filmes em cartaz")
    elif escolhaMas == 3:
        print("Adicionar novos funcionários")
    elif escolhaMas == 4:
        print("Quadro de funcionários")
    elif escolhaMas == 5:
        print("Sair")
    else:
        print("NÃO ESTÁ ENTRE AS OPÇÕES!! TENTE NOVAMENTE")
        menuMaster()


def menuUser():
    print("Bem vindo, escolha umas das opções \n")
    escolhaUser = int(input("1 - Filmes em cartaz \n 2 - Sair \nopção:"))
    if escolhaUser == 1:
        print("Filmes em cartaz: \n")
        for filmes in resultado:
            print(f"Id: {filmes['id']}")
            print(f"Nome: {filmes['nome']}")
            print(f"Classificação: {filmes['classificacao']}")
            print(f"Valor:{filmes['valorIngresso']}\n")
        
        
        compra = int(input("Escolha o id do filme para comprar, ou aperte 0 para voltar para o menu!"))
        while compra != 0:
            if compra == 1:
                print("Escolha seu horário: ")
                break
    else:
        print("Saindo...")
         
    
    return menuUser(), index.autentico
            
    
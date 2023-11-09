import menu,conexao
import pymysql.cursors
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'cinema',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
try:
    with conexao.cursor() as cursor:
     cursor.execute('select * from filmes')
     resultado = cursor.fetchall()
except:
    print('erro ao conectar no banco de dados!')



def cadastroFilmes():
    filme = input("Coloque o nome do filme: ")
    classifica = input("Coloque a classificação: ")
    valorIngress = int(input("Coloque o valor do ingresso: "))

               
    try:
     with conexao.cursor() as cursor:
        cursor.execute('insert into filmes(nome, classificacao, valorIngresso) values (%s, %s, %s)', (filme, classifica.upper(), valorIngress))
        conexao.commit()
        print('Filme cadastrado!')
        menu.menuMaster()
    except:
        print('Erro ao inserir os dados! Tente novamente')

    return cadastroFilmes()

def filmesCartaz():
    print("Filmes em cartaz: \n")
    for filmes in resultado:
            print(f"Id: {filmes['id']}")
            print(f"Nome: {filmes['nome']}")
            print(f"Classificação: {filmes['classificacao']}")
            print(f"Valor:{filmes['valorIngresso']}\n")
        
    escolha = int(input("Caso queira cadastrar outros filmes aperte 1, ou aperte 0 para voltar para o menu!"))
    while escolha != 0:
        if escolha == 1:
         cadastroFilmes()
        
  
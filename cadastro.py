import index,conexao
import pymysql.cursors
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'cinema',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
def Cadastro():
        print('Faca seu cadastro! \n')
        
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
        userEx = 0
        for linha in index.resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                userEx = 1

        if userEx == 1:
            print('Esse usuario já existe!')
            print(userEx)
        elif userEx == 0:
              try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                    conexao.commit()
                    print('Usuario cadastrado com sucesso!')
              except:
                print('Erro ao inserir os dados!')
                print(userEx)
        
     
import pymysql.cursors
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'cinema',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)


nome = str(input('Coloque seu user: '))
senha = input('Coloque sua senha: ')
with conexao.cursor() as cursor: 
    sql = cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
    conexao.commit()
     # Método fetchone(): retorna uma linha da tabela
    print("feito")
    # Acessar o dado retornado pelo nome da coluna
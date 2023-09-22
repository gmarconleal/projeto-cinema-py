import pymysql.cursors
import login, cadastro
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'teste',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

autentico = False
while not autentico:

    decisao =int(input('digite 1 para logar e 2 para cadastrar: '))
    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
    except:
        print('erro ao conectar no banco de dados!')
    if decisao == 1:
        login.entrar()
    elif decisao == 2:
        cadastro.Cadastro()

    


if autentico:
    print('Autenticado')
    if userSup == True:
        decisaoUser = 1
        while decisaoUser !=0:
            decisaoUser = int(input('Digite 0 para sair \nDigite 1 para cadastrar produtos\nDigite 2 para listar produtos cadastrados\nDigite 3 para listar os pedidos\n '))
            if decisaoUser == 1:
                print("Decisão 1")
            elif decisaoUser == 2:
                print("Decisão 2")
            elif decisaoUser == 3:
                print("Decisão 3")

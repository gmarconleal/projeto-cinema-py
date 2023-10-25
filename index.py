import pymysql.cursors
import cadastro,Login

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'cinema',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

autentico = False

while autentico == False:

       decisao = int(input('Digite 1 para logar e 2 para cadastrar: '))
       try:
              with conexao.cursor() as cursor:
                     cursor.execute('select * from cadastros')
                     resultado = cursor.fetchall()
       except:
              print('erro ao conectar no banco de dados!')
       if decisao == 1:
              Login.entra()
       elif decisao == 2:
              cadastro.Cadastro()
      

     
       

    


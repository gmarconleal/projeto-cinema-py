import pymysql.cursors
def conex():
    conexao = pymysql.connect(
     host = 'localhost',
     user = 'root',
     password = '',
     db = 'cinema',
     charset= 'utf8mb4',
     cursorclass= pymysql.cursors.DictCursor
    )

    cursor = conexao.cursor()

    conexao.close()
    cursor.close()
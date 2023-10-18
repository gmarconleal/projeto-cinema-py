import getpass
import index, menu

def entra():
  if index.decisao == 1:
        user =  input("Coloque seu nome de usuario: ")
        senha = input("Coloque sua senha: ")

        if user == "" or senha == "":
          print("Coloque os dados corretamente")
        else:
          for linha in index.resultado:
             if user == linha["nome"] and senha == linha['senha']:
                if linha['nivel'] == 1:
                   userMas = False
                   menu.menuUser()
                elif linha['nivel'] == 2:
                   userMas = True
                   menu.menuMaster()
             else:
                print("Algo deu errado, tente novamente!")
                autenticado = False
          
             
          

  return autenticado




        



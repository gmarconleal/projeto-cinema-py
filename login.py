import getpass
import index

def entrar():
  if index.decisao == 1:
        user =  input("Coloque seu nome de usuario: ")
        senha = getpass.getpass("Coloque sua senha: ")

        if user == "" or senha == "":
          print("Coloque os dados corretamente")
        else:
          for linha in index.resultado:
             if user == linha["nome"] and senha == linha['senha']:
                if linha['nivel'] == 1:
                   userMas = False
                elif linha['nivel'] == 2:
                   userMas = True
                   menuMaster()   
          if not index.autentico:
             print("User ou senha errado!")

          if linha['nivel'] == 1 and index.autentico == True:
             print("Chama MenuUser")
             
          

  return entrar()



        



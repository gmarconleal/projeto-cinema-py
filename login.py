import index, menu,cadastro

def entra():
  if index.decisao == 1:
        print("Faça o login!")
        user =  input("Coloque seu nome de usuario: ")
        senha = input("Coloque sua senha: ")

        if user == "" or senha == "":
          print("Coloque os dados corretamente")
        else:
          for linha in index.resultado:
            if user == linha["nome"] and senha == linha['senha']:
               if linha['nivel'] == 1:
                   userMas = False
                   index.autentico = True
                   menu.menuUser()
                  
               elif linha['nivel'] == 2:
                   userMas = True
                   menu.menuMaster()
               else:
                  print("User não encontrado! Faça seu cadastro!")
                  cadastro.Cadastro()
         
             
          
             
          

  return index.autentico,user




        



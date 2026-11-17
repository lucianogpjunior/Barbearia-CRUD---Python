import Dto
import os

class Layout:
    def __init__(self):
        pass
    def loginModule(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        dto = Dto()
        print("==================================")
        print("             BARBEARIA            ")
        print("==================================\n")
        status = True
        layoutClass = Layout()

        print("Digite o seu usuário:\n")
        nomeInput = input(str("Nome: \n"))
        senhaInput = input(str("Senha: \n"))

        dto.loginUser(nomeInput, senhaInput)


        if (nomeInput, senhaInput):
            layoutClass.mainModule()
        else:
            return
        
    def mainModule(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==================================")
        print("             BARBEARIA            ")
        print("==================================\n")
        status = True

        if status == True:
            print("Sistema. Escolha uma das opçoes abaixo:\n")
            print("[1] - Gerenciar Clientes\n")
            print("[2] - Gerenciar Dependentes\n")
            print("[3] - Gerenciar Agenda\n")
            print("[0] - Logout\n")
            value = input("Escolho a opção: ")

            match value:
                case 1:
                    print('')
                case 2:
                    print('')
                case 3:
                    print('')
                case 0:
                    status = False

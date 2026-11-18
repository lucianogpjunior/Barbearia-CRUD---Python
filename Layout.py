from Dto import Dto
import os
from ClienteEntity import ClienteEntity
import UserEntity
import DependenteEntity
import AgendamentoEntity

class Layout:
    def __init__(self):
        pass
    def loginModule(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        dto = Dto(False)
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
        layoutClass = Layout()
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
            value = int(input("Escolho a opção: "))

            match value:
                case 1:
                    layoutClass.clienteModule()
                case 2:
                    print('')
                case 3:
                    print('')
                case 0:
                    status = False

    def clienteModule(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        layoutClass = Layout()
        print("==================================")
        print("             BARBEARIA            ")
        print("==================================\n")
        status = True

        if status == True:
            print("Sistema. Escolha uma das opçoes abaixo:\n")
            print("[1] - Cadastrar Cliente\n")
            print("[2] - Alterar Cliente\n")
            print("[3] - Listar Clientes\n")
            print("[4] - Excluir Cliente\n")
            print("[<] - Voltar\n")
            value = int(input("Escolho a opção: "))

            match value:
                case 1:
                    layoutClass.cadastrarClienteModule()
                case 2:
                    print('')
                case 3:
                    print('')
                case 4:
                    print('')
                case 5:
                    print('')

    def cadastrarClienteModule(self):
        dto = Dto(False)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==================================")
        print("             BARBEARIA            ")
        print("==================================\n")
        
        print("Cadastre o seu cliente:\n")
        nomeInput = input(str("Nome: \n"))
        cpfInput = input(str("Cpf: \n"))
        telefoneInput = input(str("Telefone: \n"))
        emailInput = input(str("Email: \n"))

        cliente = ClienteEntity(None, nomeInput, cpfInput, telefoneInput, emailInput)

        cliente.setCpf(cpfInput)
        dto.cadastrarCliente(cliente)

        


            


from Database import Database
from UserEntity import UserEntity
from ClienteEntity import ClienteEntity
import DependenteEntity
import AgendamentoEntity
import mariadb
from datetime import datetime, timedelta

class Dto:
    def __init__(self, sessao_ativa):
        self.sessao_ativa = {
            "id": None,
            "nome": None,
            "expira_em": None
        }
    
    #User Login DTO + Sessão

    def loginUser(self, nomeInput, senhaInput):
        databaseClass = Database()
        databaseConnect = databaseClass.conectar_banco()

        cursor = databaseConnect.cursor(dictionary = True)

        while True:

            query = "SELECT id, nome, email, senha FROM usuario WHERE nome = %s"
            cursor.execute(query, (nomeInput,))
            user = cursor.fetchone()

            if user:
                try:
                    userClass = UserEntity(
                        user['id'],
                        user['nome'],
                        user['email'],
                        user['senha']
                    )
                    senhaValidate = userClass.verificarSenha(senhaInput)

                except ValueError:
                    senhaValidate = False
                if senhaValidate:
                    self.sessao_ativa["id"] = user["id"]
                    self.sessao_ativa["nome"] = user["nome"]
                    self.sessao_ativa["expira_em"] = datetime.now() + timedelta(minutes=10)
                    
                    print(f"\n[SUCESSO] Autenticação realizada. Bem-vindo, {user['nome']}!")
                    
                    break
                else:
                    print("[ERRO] Senha incorreta. Tente novamente.")
            else:
                print("[ERRO] Nome não encontrado. Tente novamente.")
        cursor.close()
        databaseConnect.close()

    def verificarSessao(self):
        if not self.sessao_ativa.get("id"):
            print("Acesso negado. Faça login primeiro.")
            return False

        if datetime.now() > self.sessao_ativa["expira_em"]:
            print("\n[AVISO] Sua sessão expirou. Por favor, faça login novamente.")
            self.sessao_ativa["id"] = None
            self.sessao_ativa["nome"] = None
            self.sessao_ativa["expira_em"] = None
            
            return True

    #ClienteEntity

    def cadastrarCliente(self, cliente ):
        databaseClass = Database()
        databaseConnect = databaseClass.conectar_banco()
        try:
            cursor = databaseConnect.cursor(dictionary = True)

            query = "INSERT INTO cliente(nome, cpf, telefone, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (
                cliente.nome,
                cliente.cpf,
                cliente.telefone,
                cliente.email
            ))


            databaseConnect.commit()

            print("Cliente cadastrado com sucesso!")

        except mariadb.Error as err:
            databaseConnect.rollback()
            print(f"Erro ao cadastrar cliente: {err}")

        finally:
            cursor.close()
            databaseConnect.close()
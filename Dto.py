import Database
import UserEntity
import ClienteEntity
import DependenteEntity
import AgendamentoEntity
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
        userClass = UserEntity()
        databaseConnect = databaseClass.conectar_banco

        cursor = databaseConnect.cursor(dictionary = True)

        while True:

            query = "SELECT id, email, senha FROM WHERE nome = %s"
            cursor.execute(query, (nomeInput))
            user = cursor.fetchone()

            if user:
                try:
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

    #
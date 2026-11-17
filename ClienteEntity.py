import base64
class ClienteEntity:
    def __init__(self, id, nome: str, cpf: str, telefone: str, email: str):
        self.id= id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def getId(self):
        return self.id
    
    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf
    
    def getTelefone(self) -> str:
        return self.senha

    def getEmail(self) -> str:
        return self.email

    def setCpf(self, cpfInput: str) -> None:
        cpf = cpfInput.encode('utf-8').decode('ascii')
        cpfCript = base64.b64decode(cpf)

        self.cpf = cpfCript.decode('utf-8')

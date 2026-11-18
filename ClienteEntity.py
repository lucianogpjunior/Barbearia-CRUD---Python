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
        return self.telefone

    def getEmail(self) -> str:
        return self.email

    def setCpf(self, cpfInput: str) -> None:
        cpfCript = base64.b64encode(cpfInput.encode('utf-8'))

        self.cpf = cpfCript.decode('utf-8')

    def verificarCpf(self, cpfInput: str) -> bool:
        cpfDecode = base64.b64decode(self.cpf).decode('utf-8')
        cpfInput = cpfInput.replace('.', '').replace('-', '')
        if cpfDecode == cpfInput:
            return True
        else:
            return False

import bcrypt;

class UserEntity:
    def __init__(self, id: int, nome: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    #getters
    def getId(self):
        return self.id
    
    def getNome(self) -> str:
        return self.nome

    def getEmail(self) -> str:
        return self.email

    def getSenha(self) -> str:
        return self.senha

    def setSenha(self, senhaInput: str) -> None:
        psw = senhaInput.encode('utf-8')
        salt = bcrypt.gensalt(rounds=12)
        hashed_psw = bcrypt.hashpw(psw, salt)

        self.senha = hashed_psw.decode('utf-8')

    def verificarSenha(self, senhaInput: str) -> bool:
        checkPw = bcrypt.checkpw(
            senhaInput.encode('utf-8'), 
            self.senha.encode('utf-8')
        )

        return checkPw

        

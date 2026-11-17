class DependenteEntity:
    def __init__(self, id: int, nome: str, parentesco: str, observacao: str, dataNascimento: str, idDependente: int ):
        self.id = id
        self.nome = nome
        self.parentesco = parentesco
        self.observacao = observacao
        self.dataNascimento = dataNascimento
        self.idDependente = idDependente

    def getId(self):
        return self.id
    
    def getNome(self) -> str:
        return self.nome

    def getParentesco(self) -> str:
        return self.cpf
    
    def getObservacao(self) -> str:
        return self.senha

    def getDataNascimento(self) -> str:
        return self.email

    def getIdDependente(self) -> int:
        return self.idDependente
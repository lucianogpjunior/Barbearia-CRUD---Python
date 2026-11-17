class AgendamentoEntity:
    def __init__(self, id: int, dataAgendamento: str, motivoServico: str, idDependente: int):
        self. id = id
        self.dataAgendamento = dataAgendamento
        self.motivoServico = motivoServico
        self.idDependente = idDependente

    def getId(self) -> int:
        return self.id

    def getDataAgedamento(self) -> str:
        return self.dataAgendamento

    def getMotivoServico(self) -> str:
        return self.motivoServico

    def getIdDependente(self) -> int:
        return self.idDependente

    
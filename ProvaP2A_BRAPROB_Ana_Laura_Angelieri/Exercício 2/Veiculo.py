class Veiculo:
    def __init__(self, placa, combustivel):
        self.placa = placa
        self.combustivel = combustivel

class Caminhao(Veiculo):
    def __init__(self, capacidadeCarga, placa, combustivel):
        super().__init__( placa, combustivel)
        self.capacidadeCarga = capacidadeCarga



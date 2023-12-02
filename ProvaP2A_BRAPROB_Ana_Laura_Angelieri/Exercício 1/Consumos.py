class ConsumoCombustivel:
    def __init__(self, modeloVeiculo,  KmInicial, KmFinal, consumoKmPorLitro):
        self.modeloVeiculo = modeloVeiculo
        self.tipoCombustivel = ['Gasolina', 'Etanol']
        self.consumoKmPorLitro = consumoKmPorLitro
        self.quantidadeCombustivelGasto = 0
        self.KmInicial = KmInicial
        self.KmFinal = KmFinal

#metodo onde é informado o valor da km inicial e do km final e calcula a quant de combustível usado
    def calculaQuantidadeCombustivelGasto(self):
        self.quantidadeCombustivelGasto = (self.KmFinal - self.KmInicial)/self.consumoKmPorLitro
        print(f'A quantidade de combustível gasto foi: {self.quantidadeCombustivelGasto} litros')

    # consumo em km  por litro de gasolina
    def consumoPorLitroGasolina(self, litroGasolina):
        if self.tipoCombustivel == 'Gasolina':
            self.consumoKmPorLitro = litroGasolina
            #self.consumoKmPorLitro = self.quantidadeCombustivelGasto / (self.KmFinal - self.KmInicial)
            print(f'O consumo em km por litro de gasolina gasta foi de {self.consumoKmPorLitro}')
        else:
            print('O tipo estabelecido não foi gasolina')

    # consumo em km  por litro de etanol
    def consumoPorLitroEtanol(self, litroEtanol):
        if self.tipoCombustivel == 'Etanol':
            self.consumoKmPorLitro = litroEtanol
            print(f'O consumo em km por litro de etanol gasto foi de: {self.consumoKmPorLitro}')
        else:
            print('O tipo estabelecido não foi etanol')

#estabelece o tipo de combustivel
    def setTipoCombustivel(self):
        tipoCombustivel = str(input('Digite o tipo de combustível: '))
        if tipoCombustivel in self.tipoCombustivel:
            self.tipoCombustivel = tipoCombustivel
            print(f'O tipo de combusível estabelecido foi:', tipoCombustivel)

#comparar etanol (R$ 3.29 o litro) e gasolina(R$5.29 o litro)
    def comparaCombustivel(self):
        custoKmEtanol = (3.29 * self.quantidadeCombustivelGasto) / 1.3
        custoKmGasolina = 5.29 * self.quantidadeCombustivelGasto

        if custoKmEtanol < custoKmGasolina:
            print('É mais econômico usar Etanol.')
            print('O custo em etanol vai ser de R$', custoKmEtanol)
        else:
            print('É mais econômico usar Gasolina.')
            print('O custo em gasolina vai ser de R$', custoKmGasolina)

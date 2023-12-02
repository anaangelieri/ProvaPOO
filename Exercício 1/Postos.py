from Consumos import ConsumoCombustivel
#veiculo1 é o objeto de acesso a classe
veiculo1 = ConsumoCombustivel('Fusca', 40, 57, 10)
veiculo1.setTipoCombustivel()
veiculo1.consumoPorLitroEtanol(10)
veiculo1.consumoPorLitroGasolina(5)

veiculo1.calculaQuantidadeCombustivelGasto()
veiculo1.comparaCombustivel()

print('\n*******Relatório de dados*******\n')
print('Modelo : ', veiculo1.modeloVeiculo)
print('Km Inicial: ', veiculo1.KmInicial)
print('Km Final: ', veiculo1.KmFinal)
print('Consumo por litro: ', veiculo1.consumoKmPorLitro)
print('Quantidade combustível gasto: ', veiculo1.quantidadeCombustivelGasto)
print('Tipo Combustível: ',veiculo1.tipoCombustivel)
veiculo1.comparaCombustivel()


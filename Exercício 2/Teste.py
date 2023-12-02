from Veiculo import Veiculo, Caminhao

carro = Veiculo(placa="CRD156", combustivel="Gasolina")
print(f"Veiculo\n Placa: {carro.placa}\n Combustível: {carro.combustivel}")


caminhao = Caminhao(capacidadeCarga=5000, placa="ATF895", combustivel="Diesel")
print(f"Caminhão \nPlaca: {caminhao.placa} \nCombustível: {caminhao.combustivel} \nCapacidade de Carga: {caminhao.capacidadeCarga} Kg")

class Agencia:
    def __init__(self, nome, nConta):
        self.nome = nome
        self.nConta = nConta
        self.saldo = 0
        self.transacoes = []

    def transferencia(self, valor, conta_destino):
#primeiro erro: a conta destino estava nomeada como conta2
        self.saldo -= valor
#segundo erro: o saldo estava com um underline na frente, mas não deve, pq o saldo irá mudar
        self.transacoes.append((-valor, self.saldo))
#terceiro erro: o append estava sendo usado para passar dois valores, mas não consegue, então é preciso colocar mais um parênteses para transformar em tupla
#quarto e quinto erro: o nome transacao estava errado, deve ser transacoes e não deve ter o underline antes de transacoes
        conta_destino.saldo += valor
#sexto erro: o saldo estava com um underline na frente, mas não deve, pq o saldo irá mudar
        conta_destino._transacoes.append((valor, conta_destino.saldo))
#sétimo erro: o append estava sendo usado para passar dois valores, mas não consegue, então é preciso colocar mais um parênteses para transformar em tupla
#oitavo erro: o saldo estava com um underline na frente, mas não pode, pq o saldo irá mudar
#nono erro: o underline na frente de transacoes deve ser retirado, porque seu valor irá mudar
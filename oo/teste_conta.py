'''
Módulo de caixa eletrônico.

funções

Cria a conta do usuário
cria_conta(numero, titular, saldo, limite)

Deposita na conta que foi passado como parâmetro
deposita(conta, valor)

Saca da conta que foi passada como parâmetro
saca(conta, valor)

Mostra o número da conta e o saldo da conta passada como parâmetro
extrato(conta)
'''

def cria_conta(numero, titular, saldo, limite):
	conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
	return conta

def deposita(conta, valor):
	conta['saldo'] += valor

def saca(conta, valor):
	conta['saldo'] -= valor

def extrato(conta):
	print("Número da conta: {} \nSaldo: {}".format(conta['numero'], conta['saldo']))
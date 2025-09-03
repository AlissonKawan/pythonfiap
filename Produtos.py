prodt1 =  int(input('Digite o valor do produto 1: '))
prodt2 =  int(input('Digite o valor do produto 2: '))
prodt3 =  int(input('Digite o valor do produto 3: '))
prodt4 =  int(input('Digite o valor do produto 4: '))
prodt5 =  int(input('Digite o valor do produto 5: '))

total = (prodt1 + prodt2 + prodt3 + prodt4 + prodt5)

print (f'O valor total dos produtos é: R${total}')

cliente = int(input('qual o dinheiro que sera aplicado?'))

troco = (cliente - total)

print (f'o troco é de R${troco}')
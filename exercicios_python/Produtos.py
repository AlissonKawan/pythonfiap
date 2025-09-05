prodt1 =  float(input('Digite o valor do produto 1: '))
prodt2 =  float(input('Digite o valor do produto 2: '))
prodt3 =  float(input('Digite o valor do produto 3: '))
prodt4 =  float(input('Digite o valor do produto 4: '))
prodt5 =  float(input('Digite o valor do produto 5: '))

total = (prodt1 + prodt2 + prodt3 + prodt4 + prodt5)

print (f'O valor total dos produtos é: R${total:.2f}')

cliente = float(input('qual o dinheiro que sera aplicado?'))

troco = (cliente - total)

print (f'o troco é de R${troco:.2f}')
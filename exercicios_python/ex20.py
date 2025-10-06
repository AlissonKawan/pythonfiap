n1 = int(input('Digite um valor positivo para a tabuada: '))

while n1 <= 0:
    print('Não pode ser 0 e nem negativo meu camarada!')
    print('Tente novamente!')
    n1 = int(input('Digite um valor positivo para a tabuada: '))

i = 1

while i < 11:
    r = n1 * i
    print(f'{n1} x {i} = {r}')
    i = i + 1

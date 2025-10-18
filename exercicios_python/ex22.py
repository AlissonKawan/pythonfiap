qtd = int(input('Digite quantos numeros serão digitados: '))
soma = 0
media = 0
pos = 0
neg = 0
n = 1

while (qtd<= 0 or qtd >20):
   print('Somente valores maiores que 0 e menores ou iguais a 20!')
   qtd = int(input('Digite quantos numeros serão digitados: '))

while n <= qtd :
    num = int(input("Digite um valor: "))
    if (n == 1):
        maior = num
        menor = num
    if(num > maior):
       maior = num
    if(num < menor):
       menor = num

    n += 1

    soma += num
    media = soma / num
    if (num >= 0):
     pos += 1
    else:
     neg += 1
    
per_neg = (neg * 100) / num
per_pos = (pos * 100) / num
print(f"O maior numero é?: {maior}")
print(f"O menor numero é?: {menor}")
print(f'A soma de todos eles é: {soma}')
print(f'A media é : {media:.2f}')
print(f'Quantidade de positivos: {pos}')
print(f'Quantidade de negativos: {neg}')
print(f'Percentual de positovs: {per_pos:.1f}')
print(f'Percentual de negativos: {per_neg:.1f}')



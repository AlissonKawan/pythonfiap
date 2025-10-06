
peso = float(input('Digite o peso: '))
excesso = (peso - 50)
tarifa = (excesso * 4)

if peso > 50:
    print (f'O peso foi: {peso}kg e o excesso: {excesso}kg com isso a tarifa a ser paga é: {tarifa}R$')

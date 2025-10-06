import random
print('Bem vindo ao RPG')

vidamonstro = 10
velocidademonstro = 4


acao = int (input('Tem um monstro digite 1 se voce quer bater, e 2 se voce quer fugir: '))

if (acao == 1):
    bate = random.randint(1, 10)
    resultado = vidamonstro - bate
    if(bate == vidamonstro):
        print('Voce matou o monstro')
    else:
        print(f'O monstro ta vivo e esta com: {resultado} de vida')

if (acao == 2):
    corre = random.randint(1, 10)
    if(corre >= velocidademonstro):
        print('Voce fugiu')
    else:
        print(f'O monstro ta vivo e vai te comer!')
  
  

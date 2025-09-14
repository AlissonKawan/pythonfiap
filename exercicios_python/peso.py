alt = float(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))

imc = (peso/alt**2)

if(imc<20):
    print("Abaixo do peso")
elif (imc<25):
    print("Voce esta no peso ideal")

else : print("Voce esta acima do peso")

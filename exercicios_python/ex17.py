valor_aceleracao = float(input("Digite o valor da aceleração em m/s²: "))
valor_velocidade_inicial = float(input("Digite o valor da velocidade inicial em m/s: "))
valor_tempo = float(input("Digite o valor do tempo em segundos: "))
# V = Vo + a.t

velocidade = valor_velocidade_inicial + (valor_aceleracao * valor_tempo)
print("O valor da velocidade é: ", velocidade , "km/h")

if(velocidade > 0 and velocidade <= 40):
    print("Veículo muito lento")
elif(velocidade == 0):
    print("Veículo parado")
elif(velocidade > 40 and velocidade <= 60):
    print("Velocidade permitida")
elif(velocidade > 60 and velocidade <= 80):
    print("Velocidade de cruzeiro")
elif(velocidade > 80 and velocidade <= 120):
    print("Veículo rápido")
elif(velocidade < 0):
    print("Veiculo esta dando ré")
else:
    print("Veículo muito rápido")



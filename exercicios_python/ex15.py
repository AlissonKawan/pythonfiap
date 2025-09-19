v1 = int(input("Digite um valor: "))
v2 = int(input("Digite mais um valor: "))
v3 = int(input("Digite o ultimo valor: "))

#es = (v1 != v2 != v3)

#iso = (v1 != v2 == v3 )

#equ = (v1 == v2 == v3)
 
 #aqui estou verificando se é um triangulo
if (v1 < v2 + v3) or (v2 < v1 + v3) or (v3 < v1 + v2):
        #aqui estou verificando se é isoceles, escaleno ou equilatero
    if (v1 != v2 != v3):
        print("Escaleno")
    elif (v1 == v2 == v3):
        print("Equilatero")
    else:
        print("Isoceles")
else:
    print("Nao forma um triangulo")


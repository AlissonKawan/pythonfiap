va = int(input("Digite a  valor: "))
vb = int(input("Digite outro valor: "))
vc = int(input("Digite mais um valor: "))

#hipotenusa = soma dos quadrados dos catetos

#teorema de pitágoras se 
# a² = b² + c²
#ou b² = a² + c²
#ou c² = a² + b²
if(va**2 == (vb**2) + (vc**2)) or (vb**2 == (va**2) + (vc**2)) or (vc**2 == (va**2) + (vb**2)):
    print("É um triângulo retângulo")
else:
    print("Não é um triângulo retângulo")
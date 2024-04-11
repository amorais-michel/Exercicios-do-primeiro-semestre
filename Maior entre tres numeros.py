lista_numero = []

lista_numero.append(float(input("Digite um numero")))
lista_numero.append(float(input("Digite mais um numero:")))
lista_numero.append(float(input("Digite outro numero:")))

if lista_numero[0] > lista_numero[1] and lista_numero[2]:
    print("O primeiro é maior")

elif lista_numero[1] > lista_numero[2] and lista_numero[0]:
    print("O segundo é maior")

elif lista_numero[2] > lista_numero[1] and lista_numero[0]:
    print("O terceiro é maior")

else:
    print("Todos sao iguais")
lado1 = float(input("Valor 1:"))
lado2 = float(input("Valor 2:"))
lado3 = float(input("Valor 3:"))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print("Não é um triangulo")

elif lado1 == lado2 == lado3:
    print("Equilátero")

elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
    print("Isosceles")

elif (lado1 != lado2 != lado3) or (lado2 != lado3 != lado1) or (lado3 != lado1):
    print("Escaleno")


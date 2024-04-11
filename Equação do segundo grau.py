import math

a = float(input("Coeficiente A:"))
b = float (input("Coeficiente B:"))
c = float(input(("Coeficiente c")))

if a <= 0:
    print("Não é equação do segundo grau")

delta = math.pow(b,2) - 4 * a *c
if delta <= 0:
    print("Não tem raiz")

elif delta > 0:
    print("Valor de delta é :", delta)
    x1 = (-b + math.sqrt(delta)) / (2 *a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print("X1:" , x1)
    print("X2:", x2)

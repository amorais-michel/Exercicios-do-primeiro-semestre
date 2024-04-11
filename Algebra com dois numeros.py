import math

n1 = int(input("Digite um numero inteiro:"))
n2 = int(input("Digite outro numero inteiro:"))
n3 = float(input("Digite um numero real qualquer:"))

p1 = ((n1*2) * (n2 / 2)) # resolvendo o problema 1 do exercicio
p2 = ((n1 * 3) + n3) # resolvendo o problema 2 do exercicio
p3 = math.pow(n3,3) #resolvendo o problema 3 do exercicio

print ("O produto do dobro do primeiro numero com metade do segundo, é:," , p1)
print("A soma do triplo do primeiro com o terceiro é:", p2)
print ("O terceiro elevado ao cubo é: ", p3)


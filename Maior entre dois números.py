numero = float(input("Digite um número"))

numero2 = float(input("Digite outro número:"))

if numero > numero2:
	print("O primeiro número digitado ", numero , "é maior que o segundo ", numero2)

elif numero2 > numero:
	print("O  segundo número ", numero2, "é maior que o primeiro números", numero)
	
elif numero == numero2:
	print("Sao números iguais")

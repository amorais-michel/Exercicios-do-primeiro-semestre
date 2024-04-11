letras = ["M", "F"] #lista que armazena tamanhos

tecla = input("Digite uma tecla: ")

if tecla in letras[0]: #se tiver oque o usuario.digitou na liista imprime masculino
	print("Masculino")
	
elif tecla in letras[1]:
	print("Feminino")

else:
	print("Sexo invalido")

	
	
	
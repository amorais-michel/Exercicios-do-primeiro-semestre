vogal = ["a", "e", "i", "o", "u"]
consoante = ["b", "c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

letra = input("Digite uma letra:")

if letra in vogal:
	print ("Vogal")

elif letra in consoante:
	print("Consoante")

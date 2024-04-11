print('Informe a tua altura em metros. Ex: 1.60 ')

altura = float(input("\n Altura:"))

peso_ideal_homens = (72.7 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7

print("O peso ideal para um homem da sua altura é: %.2f" %(peso_ideal_homens) , "e o peso ideal para uma mulher da sua altura é de: %.2f" %(peso_ideal_mulheres))

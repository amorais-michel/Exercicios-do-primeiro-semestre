peso_peixe_pescado = float(input("Informe a quantidade de quilos de peixe que tu tem:"))

peso_peixe_permitido = 50

excesso = peso_peixe_pescado - peso_peixe_permitido# o excesso é calculado pela diferença da quantidade de peixes sobre o peso permitido

if peso_peixe_pescado >= 50:
    multa = excesso * 4 # o excesso é calculado pela multiplicação do excesso pelo valor da multa
    print("Voce foi multado! Pague:", multa, "reais de multa. Seu excesso foi de ", excesso, "kg")

else:
    print("Tu não precisa pagar multa")

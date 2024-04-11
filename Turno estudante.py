turno = input ("Qual seu turno? Insira uma letra correspondente a ele:")

if turno == 'M' or 'm':
    print("Turno matutino. Bom dia!")

elif turno == 'V' or 'v':
    print("Turno vespertino. Boa tarde!")

elif turno == 'N' or  'n':
    print("Turno noturno. Boa noite!")

else:
    print("Valor invalido")

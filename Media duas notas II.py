nota1 = float(input("Entre com a nota 1:"))
nota2 = float(input("Digite outra nota:"))

media = (nota1 + nota2) / 2

if media == 7:
    print("Aprovado")

elif media < 7:
    print("Reprovado")

elif media >= 10:
    print("Aprovado com distinção")




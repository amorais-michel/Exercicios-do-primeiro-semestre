p1 = float(input("Informe o preço do primeiro produto:"))
p2 = float(input("Informe o preço do segundo produto:"))
p3 = float((input("Informe o preço do segundo produto:")))

if p1 < p2 and p3:
    print("Compre o primeiro produto, ele é o mais barato")

elif p2 < p3 and p1:
    print("Compre o segundo produto, ele é mais barato")

elif p3 < p1 and p2:
    print("Compre o terceiro produto, ele é o mais barato")

else:
    print("Valores iguais")
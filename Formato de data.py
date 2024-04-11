dia = int(input("Dia:"))
mes = int(input("Mes:"))
ano = int(input("Ano:"))

if dia == 1 or dia <= 31:
    if mes == 1 or mes <= 12:
        if ano == 0 or ano <= 10000:
            print("Data valida")
            print("", dia ,'/', mes , "/" , ano)

else:
    print("Digite uma data valida")
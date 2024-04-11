horas_trabalhadas = float(input('Trabalhou quantas horas:'))

valor_hora = float(input("Qual o valor da hora:"))

salario_bruto = valor_hora * horas_trabalhadas # calculando o salario bruto
desconto_inss = salario_bruto * 0.10
desconto_IR = 0
FGTS = salario_bruto * 0.11


if salario_bruto <= 900.00:

    desconto_IR = 0
    total_descontos = desconto_inss + desconto_IR
    salario_liquido = salario_bruto - desconto_IR - desconto_inss
    print("\nSeu salario bruto é de:", salario_bruto)
    print("Valor do desconto do IR é de 0%, o mesmo que:" , desconto_IR)
    print("Seu desconto do INSS =", desconto_inss)
    print("FGTS (11%) = ", FGTS )
    print("Total de descontos = ",  total_descontos)
    print("Salario liquido = ", salario_liquido )


elif salario_bruto == 900.01 or salario_bruto <= 1500.00:

    desconto_IR = salario_bruto * 0.05
    total_descontos = desconto_inss + desconto_IR
    salario_liquido = salario_bruto - desconto_IR - desconto_inss
    print("\nSeu salario bruto é de:", salario_bruto)
    print("Valor do desconto do IR é de 5%, o mesmo que:" , desconto_IR)
    print("Seu desconto do INSS =", desconto_inss)
    print("FGTS = ", FGTS )
    print("Total de descontos = ",  total_descontos)
    print("Salario liquido = ", salario_liquido )

elif salario_bruto == 1500.01 or salario_bruto <= 2500.00:

    desconto_IR = salario_bruto * 0.10
    total_descontos = desconto_inss + desconto_IR
    salario_liquido = salario_bruto - desconto_IR - desconto_inss
    print("\nSeu salario bruto é de:", salario_bruto)
    print("Valor do desconto do IR é de 15%, o mesmo que:" , desconto_IR)
    print("Seu desconto do INSS =", desconto_inss)
    print("FGTS = ", FGTS )
    print("Total de descontos = ",  total_descontos)
    print("Salario liquido = ", salario_liquido )

elif salario_bruto >= 2500.01:

    desconto_IR = salario_bruto * 0.20
    total_descontos = desconto_inss + desconto_IR
    salario_liquido = salario_bruto - desconto_IR - desconto_inss
    print("\nSeu salario bruto é de:", salario_bruto)
    print("Valor do desconto do IR é de 20%, o mesmo que:" , desconto_IR)
    print("Seu desconto do INSS =", desconto_inss)
    print("FGTS = ", FGTS )
    print("Total de descontos = ",  total_descontos)
    print("Salario liquido = ", salario_liquido )




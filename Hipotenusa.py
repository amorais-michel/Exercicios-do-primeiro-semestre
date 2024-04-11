import math

cateto1 = float(input("Digite um valor para o cateto oposto:"))

cateto2 = float (input("Digite outro valor para o cateto adjascente:"))

hipotenusa = math.sqrt((math.pow(cateto1,2)) + (math.pow(cateto2,2)))

print ("A hipotenusa é: %.2f" %(hipotenusa))
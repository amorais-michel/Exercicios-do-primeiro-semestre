e1 = float(input("Elemento 1: "))
e2 = float (input("Elemento 2:"))
e3 = float (input("Elemento 3:"))
e4 = float (input("Elemento 4:"))

p1 = float (input("\nPeso 1:"))
p2 = float (input("Peso 2:"))
p3 = float (input("Peso 3:"))
p4 = float (input("Peso 4:"))

media_ponderada = ((e1 * p1) + (e2 * p2) + (e3 * p3) + (e4 * p4)) / (p1 + p2 + p3 + p4)

print ("A media ponderada é : %.2f" %(media_ponderada))


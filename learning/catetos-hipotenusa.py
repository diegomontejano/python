from math import hypot
co=float(input("Insira o cateto oposto: "))
ca=float(input("Insira o cateto adjacente: "))
hip=hypot(co, ca)
print("A hipotenusa de {} e {} é {:.2f}.".format(co, ca, hip))
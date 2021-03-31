#Método 1:
dist=int(input("Qual a distância da viagem em Km? "))
if dist<=200:
    print("Sua passagem custará R${}.".format(dist*0.5))
else:
    print("Sua passagem custará R${}.".format(dist*0.45))

#Método 2:
dist=int(input("Qual a distância da viagem em Km? "))
if dist<=200:
    valor=dist*0.5
else:
    valor=dist*0.45
print("Sua passagem custará R${}.".format(valor))
    
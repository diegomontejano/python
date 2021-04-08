dias=int(input("O carro será usado por quantos dias? "))
km=float(input("Quantos quilometros o carro percorrerá? "))
custodias=dias*60
custokm=km*0.15
soma=custodias+custokm
print("Você gastará R${:.2f} ao percorrer {}Km por {} dias.".format(soma, km, dias))

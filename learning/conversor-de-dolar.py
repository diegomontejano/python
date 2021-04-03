real=float(input("Quantos reais você gostaria de converter? "))
dolar=float(real/5.50)
print("Você pode comprar ${:.2f} com R${}.".format(dolar, real))

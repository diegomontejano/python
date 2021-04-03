speed=int(input("Insira a velocidade que você atingiu em Km: "))
multa=(speed-80)*7
if speed>80:
    print("Você foi multado e pagará uma multa de R${:.2f}.".format(multa))
else:
    print("Você não foi multado.")
num=int((input("Insira um número entre 0 e 9999: ")))
uni=num // 1 % 10
dez=num // 10 % 10
cen=num // 100 % 10
mil=num // 1000 % 10
print("Milhar: {} \nCentena: {} \nDezena: {} \nUnidade: {}".format(mil, cen, dez, uni))

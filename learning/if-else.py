nome=str(input("Qual o seu nome? "))
print("Bom dia {}!".format(nome))
if nome=="Diego":
    print("Que nome lindo você tem!")

n1=float(input("Insira sua primeira nota: "))
n2=float(input("Insira sua segunda nota: "))
m=(n1+n2) / 2
print("Sua média é {:.1f}.".format(m))
if m>=7:
    print("Você passou, parabéns!")
else:
    print("Você reprovou, estude mais!")

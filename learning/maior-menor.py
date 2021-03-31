n1=int(input("Insira o número 1: ").strip())
n2=int(input("Insira o número 2: ").strip())
n3=int(input("Insira o número 3: ").strip())

if n1 and n2>n3:
    print("{} é MAIOR.".format(n1))
else:
    print("{} é MENOR.".format(n1))
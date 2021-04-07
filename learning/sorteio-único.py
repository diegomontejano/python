a1=str(input("Aluno 1: "))
a2=str(input("Aluno 2: "))
a3=str(input("Aluno 3: "))
from random import choice
lista=[a1, a2, a3]
escolhido=choice(lista)
print("O aluno escolhido foi... {}.".format(escolhido))

a1=str(input("Aluno 1: "))
a2=str(input("Aluno 2: "))
a3=str(input("Aluno 3: "))
import random
lista=[a1, a2, a3]
random.shuffle(lista)
print("O aluno escolhido foi... {}.".format(lista))

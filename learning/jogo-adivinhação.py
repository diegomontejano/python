import random
num=[1,2,3,4,5]
result=random.choice(num)
answer=int(input("Escolhi um número entre 1 e 5. Qual número eu escolhi? "))
if result == answer:
    print("Parabéns, você acertou!")
else:
    print("Você errou, tente novamente!")
    
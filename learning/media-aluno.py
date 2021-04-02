s1 = float(input("Type your score to subject 1: "))
s2 = float(input("Type your score to subject 2: "))
s3 = float(input("Type your score to subject 3: "))
final = ((s1 + s2 + s3) / 3)
if (s1 >= 7 and s2 >=7 and s3 >= 7.00):
    print("You final score is {:.2f}! Congrats, you passed!".format(final))
else:
    print("You final score is {:.2f}! Sorry, you reproved!".format(final))
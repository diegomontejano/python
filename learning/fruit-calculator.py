apple = int(input("How many APPLES do you want? "))
applePrice = apple*2.30
orange = int(input("How many ORANGES do you want? "))
orangePrice = orange*3.60
banana = int(input("How many BANANAS do you want? "))
bananaPrice = banana*1.85
bill = applePrice + orangePrice + bananaPrice
print("You bought {} apples, {} oranges and {} bananas. Your bill is ${:.2f}.".format(apple, orange, banana, bill))
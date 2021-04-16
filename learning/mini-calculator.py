n1 = int(input("Type a firth number: "))
n2 = int(input("Type a second number: "))
op = str(input("type the sign of the operation to calculate: (+), (-), (*), (/)"))
if (op == "+"):
    print(n1 + n2)
if (op == "-"):
    print(n1 - n2)
if (op == "*"):
    print(n1 * n2)
if (op == "/"):
    print(n1 / n2)
if (op != "+" or "-" or "*" or "/"):
    print("ERROR! Check your values and try")

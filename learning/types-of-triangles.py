a = int(input("Type triangle side 1: "))
b = int(input("Type triangle side 2: "))
c = int(input("Type triangle side 3: "))

if ((a or b or c == 0) and (a > b+c or b > a+c or c > a+b)):
    print("ERROR! We can't make a triangle with these values!")
else:
    if (a == b and a == c):
        print("Equilateral Triangle")
    if (a == b and a != c):
        print("Isosceles Triangle")
    if (a != b and a != c):
        print("Right-angled Triangle")

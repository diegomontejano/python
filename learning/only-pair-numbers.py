start = int(input("Type one number to start the count: "))
end = int(input("Type one number to end the count: "))
while(start <= end):
    if(start % 2 == 0):
        print(start)
    start = start + 1
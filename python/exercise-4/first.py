inputData = int(input("Enter the number: "))
c = 1

while inputData >= c:
    if inputData == c:
        print(c)
        break
    print(c, end=",")
    c = c + 1

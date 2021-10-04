inputData = int(input("Enter the number: "))
c = 1

while inputData >= c:
    if inputData == c:
        print(c)
        break

    if inputData % 3 == 0:
        print(-inputData, end=",")
    else:
        print(inputData, end=",")
    inputData = inputData - 1

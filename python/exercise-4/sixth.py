inputData = int(input("Enter the number: "))

count = 0
num = inputData

while num >= 1:
    if inputData % num == 0:
        count = count + 1

    num = num - 1

if count > 2:
    print("Sade deyil")
else:
    print("Sadedir")

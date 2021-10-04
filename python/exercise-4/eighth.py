inputData = [1, 6, -3, 45, 11, 20, -67, 332, 885, 11, 120, 4, 77, -5]

flag = 0
sumEls = 0

while len(inputData) > flag:
    if inputData[flag] % 5 == 0:
        sumEls = sumEls + inputData[flag]
    flag = flag + 1

print(sumEls)

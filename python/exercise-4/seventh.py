inputData = [1, 6, -3, 45, 11, -67, 332, 885, 11, 4, 77, -5]

# with builtin min() methos
print(min(inputData))

# with only while loop
flag = 0
minEl = inputData[0]

while len(inputData) > flag:
    if minEl > inputData[flag]:
        minEl = inputData[flag]
    flag = flag + 1

print(minEl)

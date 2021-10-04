inputData = [-2, 356, 3, 5, 7, -3, 6, -9, 5, 2, 5, 7, 22, 80, 0, 4, 3, -2]

non_unique_list = []

flag1 = 0
flag2 = 0

while len(inputData) > flag1:
    while len(inputData) > flag2 + 1:
        if inputData[flag1] == inputData[flag2]:
            non_unique_list.append(inputData[flag1])
        flag2 = flag2 + 1
    flag1 = flag1 + 1

print(non_unique_list)

A = 12
B = 20

result = []
index = A

while index <= B:
    if index % 2 == 0:
        result.append(index)
    index = index + 1

print(result)

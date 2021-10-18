num = int(input("Enter the number for factorial calculation: "))

result = 1
index = 1

while index <= num:
    result = result * index
    index = index + 1

print(result)

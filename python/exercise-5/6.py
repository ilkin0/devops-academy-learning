# inum = int(input("Enter the size of Christmas Tree: "))
inum = 15

index = 1

while index <= inum:
    while index <= inum / 2:
        print("*" * index)
        print("*" * index)
        index = index + 1

print("||")
print("____")

input_data = [1, 2, 3, 3, 3, 3, 4, 5]

index = 0

u_list = []

while index < len(input_data):
    if input_data[index] not in u_list:
        u_list.append(input_data[index])
    index = index + 1

print(u_list)

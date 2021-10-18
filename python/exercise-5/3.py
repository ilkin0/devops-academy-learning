input_data = "This is Python"

ilen = len(input_data)
result = ""

while ilen > 0:
    result = result + input_data[ilen - 1]
    ilen = ilen - 1

print(result)

listVar = [["Ali", 22, 180],
           ["Jeyhun", 24, 178],
           ["Rufat", 17, 170],
           ["Hasan", 21, 182],
           ["Farid", 22, 178],
           ["Arif", 21, 180],
           ["Rauf", 18, 188]]


def custom_sort(el):
    return el[1]


listVar.sort(key=custom_sort)

print(listVar)

list_varr = ["hello", 23, -45.6, False, "This is a text", None]

new_list = list_varr.copy()
del new_list[-2]

print("Original list:  ", list_varr)
print("New list: ", new_list)

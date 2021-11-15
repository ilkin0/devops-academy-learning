listA = [1, 2, 3, 45, 65]
listB = [-11, 2, 7, 45, 90]


def common_list(a_list, b_list):
    common = []

    for i in a_list:
        for j in b_list:
            if i == j:
                common.append(i)

    return common


print(common_list(listA, listB))

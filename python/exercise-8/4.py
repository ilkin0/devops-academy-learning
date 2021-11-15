def sum_of_pow_singulars(begin, end):
    result = 0
    for i in range(begin, end):
        if i % 2 != 0:
            i *= i
            result += i
    return result


print(sum_of_pow_singulars(10, 100))

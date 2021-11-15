import random
import string


def random_generation(random_len):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    condition = lower + upper + numbers

    int_password = random.sample(condition, random_len)
    return "".join(int_password)


print(random_generation(10))

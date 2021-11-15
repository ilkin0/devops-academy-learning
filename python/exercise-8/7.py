input_text = 'Python is the best programming language'


def replace_with_comma(input_data):
    new_string = ''
    for c in input_data:
        if c == ' ':
            new_string += ','
            continue
        new_string += c

    return new_string


print(replace_with_comma(input_text))

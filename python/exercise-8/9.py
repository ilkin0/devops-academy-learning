dictionary = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
              "seven": 7, "eight": 8, "nine": 9}

input_data = 'I have bought five apples, three onions, four bananas and six kiwis'


def string_to_number(text, num_dict):
    # for c in text:
    for (key, value) in num_dict.items():
        text.replace(key, str(value))


string_to_number(input_data, dictionary)
print(input_data)

# Why didnt work?TODO

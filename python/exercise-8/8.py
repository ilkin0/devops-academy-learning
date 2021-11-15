input_data = 'Python is the best programming language'
input_data.upper()


def first_letter_upper(text):
    new_text = ''
    for c in text:
        if c == '\n':
            text[text.index(c) + 1] = text[text.index(c) + 1].upper()
        new_text += c


first_letter_upper(input_data)
print(input_data)

# TODO

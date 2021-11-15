text = "Hi everybody.Welcome to our python class"

char = 'e'


def find_most_used(text_str, char_str):
    count = 0

    for c in text_str:
        if c == 'e':
            count += 1
    return count


print(find_most_used(text, char))

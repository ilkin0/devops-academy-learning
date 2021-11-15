text = """ Hi everybody 
Welcome to our python class. 
We will learn python in this class"""

stringList = []


def convert_to_list(string):
    new_line = ''
    for c in string:
        if c == '\n':
            stringList.append(new_line)
            new_line = ''
            continue
        new_line = new_line + c


convert_to_list(text)
print(stringList)

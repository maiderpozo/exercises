import re


def remove_repeated_words(string):
    return re.sub(r'([a-zA-Z]+)( \1)+', r'\1', string)

print(remove_repeated_words('aa'))
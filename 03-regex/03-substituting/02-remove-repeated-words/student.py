# Write your code here
import re


def remove_repeated_words(string):
    return re.sub(r'(.)', r'\1\1', string)

print(remove_repeated_words('aa'))
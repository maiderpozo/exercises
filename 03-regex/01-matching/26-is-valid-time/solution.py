import re


def is_valid_time(string):
    return re.fullmatch(r'[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{3})?', string)
    #return re.fullmatch(r'([01][0-9]|[2][0-3])\:([0-5][0-9])\:([0-5][0-9])(\.[0-9]{3})?', string) is more correct, limiting the minutes and seconds to 59

print(is_valid_time('10:00:00'))
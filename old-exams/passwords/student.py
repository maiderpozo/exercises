import itertools
import re
letters ="QWERTYUIOP"

passwords = list(itertools.product(letters,repeat=6))
passwords = list("".joins(x) for x in itertools.product(letters,repeat=6))


for password in passwords:
    if re.search(r"([AEIOU])\1", password)and re.search(r'([QWRTYP])\1', password) and len(set(password)) == 4:
        print(password)


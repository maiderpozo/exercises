import sys
import re


data = sys.stdin.read()
with open('output.txt', 'w') as out:
    for id, sec, title in re.findall(r'\[#(.*?)\]\s*(=+) (.*)', data):
        depth = len(sec)
        bullets = "*" * depth
        link = f'<<{id},{title}>>'
        print(f'{bullets} {link}',out)
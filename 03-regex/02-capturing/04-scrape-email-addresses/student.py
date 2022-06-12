import re
 # Write your code here
def collect_string(string):
    return re.findall(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})', string)

print(collect_string('maidorchin@ma.com'))
print(collect_string('maidorchin@ma.com'))
# Write your code here
# Creas una var porque hay como un for por lista
def all_greater(ns, ms):
    return all( [ n >= m for m in ms for n in ns ])

print(all_greater([5, 7, 8], [4, 2, 1]))
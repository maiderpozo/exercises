# Write your code here
def includes(xs, ys):
    return all(y in xs for y in ys)

print(includes([1, 2, 3, 4], [1, 2]))

def includes2(xs,ys):
    result =  all(elem in xs for elem in ys)
    return result
   
print(includes2([1, 2, 3, 4], [1, 2]))
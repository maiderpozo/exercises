# Write your code here
def dropFirst(xs):
    xs2 = [x for x in xs if x != xs[0]]
    return xs2


a=[1,2,3,4,5]
print(dropFirst(a));
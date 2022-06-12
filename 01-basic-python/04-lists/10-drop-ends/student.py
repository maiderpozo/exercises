def dropFirst(xs):
    xs2 = [x for x in xs if x != xs[0]]
    
    xs3=[x for x in xs if x != xs[len(xs2)]]
    return xs3


a=[1,2,3,4,5]
print(dropFirst(a));# Write your code here

# Write your code here
def targetSum(xs,target):
    for  x in xs:
        for y in xs:
            if x + y == target:
                return True;
    return False;

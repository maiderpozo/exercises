# Write your code here
def containsDuplicates(xs):
    for i in range (len(xs)):
        for j in range(i + 1, len(xs)):
             if xs[i] == xs[j]:
                return True

    return False



print(containsDuplicates([3,3,3,1]));
# Write your code here
def is_increasing(ns):
    isAscending = True
    isDescending = True
    for i in range(1,len(ns)):
        if(ns[i] >= ns[i-1]):
            isDescending = False
        elif(ns[i] <= ns[i-1]):
            isAscending = False
        if((not isAscending) and (not isDescending)):
            print("The list is not sorted in either order.")
            break
    if(isAscending):
        print("The list is sorted in ascending order.")
    if(isDescending):
        print("The list is sorted in descending order.")

is_increasing([1, 6, 3, 8])
       # testcase([1, 3, 6, 8])